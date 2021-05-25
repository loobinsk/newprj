# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, View, FormView
from main.models import Advert, Metro, District, Company, clear_tel_list, Blacklist, Town, clear_tel, Parser, SearchRequest
from uprofile.models import User
from django.contrib.sites.models import Site
from gutils.views import BreadcrumbMixin, AjaxableResponseMixin, AjaxPageMixin, AdminRequiredMixin
from django.core.urlresolvers import reverse
from django.db.models import Q
from main.form import FeedbackAdvertForm, RequestRemoveForm, AdvertForm, AdvertForm_Client, RequestForm, \
    SearchRequestForm_Client, DeliveryFilterForm
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden, HttpResponsePermanentRedirect, Http404
from django.utils.decorators import method_decorator
from annoying.decorators import ajax_request
from mail_templated import send_mail_admins, send_mail
from django.db.transaction import atomic
from django.views.decorators.csrf import csrf_exempt
from main.task import find_search_request_clients, send_search_request_notice
from main.views.private import ClientPermMixin, ModerPermMixin
from django.conf import settings


# ПРОВЕРКА ПРАВ
class SearchRequestUpdatePermMixin(object):
    """
    Проверка прав на редактирование заявки
    """
    def dispatch(self, request, *args, **kwargs):
        sr = self.get_object()
        if sr.user == request.user or request.user.is_staff:
            return super(SearchRequestUpdatePermMixin, self).dispatch(request, *args, **kwargs)
        return HttpResponseForbidden()


class SearchRequestDeletePermMixin(object):
    """
    Проверка прав на удаление заявки
    """
    def dispatch(self, request, *args, **kwargs):
        sr = self.get_object()
        if sr.user == request.user:
            return super(SearchRequestDeletePermMixin, self).dispatch(request, *args, **kwargs)
        return HttpResponseForbidden()


class SearchRequestPreviewView_Client(ClientPermMixin, SearchRequestUpdatePermMixin, DetailView):
    model = SearchRequest
    context_object_name = 'sr'
    template_name = 'main/client/search_request/preview.html'

    def get_queryset(self):
        return super(SearchRequestPreviewView_Client, self).get_queryset()


class MySearchRequestView_Client(ClientPermMixin, BreadcrumbMixin, ListView):
    template_name = 'main/client/search_request/my-page.html'
    model = SearchRequest
    context_object_name = 'request_list'
    paginate_by = 15

    def get_breadcrumbs(self):
        return super(MySearchRequestView_Client, self).get_breadcrumbs() + [('Мои заявки', reverse('client:search-request:my'))]

    def get_queryset(self):
        return SearchRequest.objects.filter(user=self.request.user).order_by('-active', '-date')

    def get_context_data(self, **kwargs):
        context = super(MySearchRequestView_Client, self).get_context_data(**kwargs)
        return context


class SearchRequestCreateView_Client(ClientPermMixin, BreadcrumbMixin, AjaxableResponseMixin, CreateView):
    model = SearchRequest
    form_class = SearchRequestForm_Client
    template_name = 'main/client/search_request/create.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(SearchRequestCreateView_Client, self).get_context_data(**kwargs)
        context['action'] = reverse('client:search-request:create')
        context['map_town'] = self.request.current_town
        return context

    def get_form_kwargs(self):
        kwargs = super(SearchRequestCreateView_Client, self).get_form_kwargs()
        kwargs['filter_town'] = self.request.current_town
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.company = self.request.user.company

        if form.cleaned_data['type2'] == 'LS':
            form.instance.adtype = Advert.TYPE_LEASE
            form.instance.need = Advert.NEED_SALE
        elif form.cleaned_data['type2'] == 'SS':
            form.instance.adtype = Advert.TYPE_SALE
            form.instance.need = Advert.NEED_SALE
        elif form.cleaned_data['type2'] == 'LD':
            form.instance.adtype = Advert.TYPE_LEASE
            form.instance.need = Advert.NEED_DEMAND
        elif form.cleaned_data['type2'] == 'SD':
            form.instance.adtype = Advert.TYPE_SALE
            form.instance.need = Advert.NEED_DEMAND

        form.instance.date = datetime.now()
        form.instance.town = self.request.current_town

        result = super(SearchRequestCreateView_Client, self).form_valid(form)
        form.instance.find_clients()
        return result

    def get_model_dict(self):
        url = reverse('client:search-request:my')
        message = '<div class="success-advert"><img src="/static/img/ok.png"><p>Ваша заявка добавлена</p></div>'
        return {
            'url': url,
            'message': message
        }

    def get_breadcrumbs(self):
        return [('Создать заявку', reverse('client:search-request:create'))]


class SearchRequestUpdateView_Client(ClientPermMixin, SearchRequestUpdatePermMixin, AjaxableResponseMixin, UpdateView):
    model = SearchRequest
    form_class = SearchRequestForm_Client
    template_name = 'main/client/search_request/edit.html'
    context_object_name = 'advert'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(SearchRequestUpdateView_Client, self).get_context_data(**kwargs)
        context['action'] = reverse('client:search-request:edit', kwargs={'pk': self.object.id})
        context['map_town'] = self.object.town
        return context

    def form_valid(self, form):
        if form.cleaned_data['type2'] == 'LS':
            form.instance.adtype = Advert.TYPE_LEASE
            form.instance.need = Advert.NEED_SALE
        elif form.cleaned_data['type2'] == 'SS':
            form.instance.adtype = Advert.TYPE_SALE
            form.instance.need = Advert.NEED_SALE
        elif form.cleaned_data['type2'] == 'LD':
            form.instance.adtype = Advert.TYPE_LEASE
            form.instance.need = Advert.NEED_DEMAND
        elif form.cleaned_data['type2'] == 'SD':
            form.instance.adtype = Advert.TYPE_SALE
            form.instance.need = Advert.NEED_DEMAND

        form.instance.date = datetime.now()

        result = super(SearchRequestUpdateView_Client, self).form_valid(form)
        form.instance.find_clients()
        form.instance.clear_cache()
        return result

    def get_model_dict(self):
        if self.request.is_moder:
            url = reverse('client:search-request:delivery')
        else:
            url = reverse('client:search-request:url')
        message = '<div class="success-advert"><img src="/static/img/ok.png"><p>Ваша заявка сохранена</p></div>'
        return {
            'url': url,
            'message': message
        }

    def get_form_kwargs(self):
        kwargs = super(SearchRequestUpdateView_Client, self).get_form_kwargs()
        kwargs['filter_town'] = self.object.town
        if kwargs['instance'].adtype == Advert.TYPE_LEASE and kwargs['instance'].need == Advert.NEED_SALE:
            kwargs['initial']['type2'] = 'LS'
        elif kwargs['instance'].adtype == Advert.TYPE_SALE and kwargs['instance'].need == Advert.NEED_SALE:
            kwargs['initial']['type2'] = 'SS'
        elif kwargs['instance'].adtype == Advert.TYPE_LEASE and kwargs['instance'].need == Advert.NEED_DEMAND:
            kwargs['initial']['type2'] = 'LD'
        elif kwargs['instance'].adtype == Advert.TYPE_SALE and kwargs['instance'].need == Advert.NEED_DEMAND:
            kwargs['initial']['type2'] = 'SD'
        return kwargs


class SearchRequestDeleteView_Client(ClientPermMixin, SearchRequestDeletePermMixin, AjaxableResponseMixin, DeleteView):
    model = SearchRequest
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super(SearchRequestDeleteView_Client, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return {
            'url': reverse('client:search-request:my')
        }


class SearchRequestStartView_Client(ClientPermMixin, View):
    @method_decorator(ajax_request)
    def post(self, request, *args, **kwargs):
        try:
            sr = get_object_or_404(SearchRequest, id=kwargs['pk'])
            if sr.user != request.user:
                raise Exception(u'Нет прав')
            sr.active = True
            sr.save()
            sr.clear_cache()

            send_search_request_notice.delay(sr.id)

            return {
                'result': True,
                'id': sr.id,
                'message': u'Поиск по заявке запущен'
            }
        except Exception as ex:
            return {
                'result': False,
                'message': unicode(ex)
            }


class SearchRequestStopView_Client(ClientPermMixin, View):
    @method_decorator(ajax_request)
    def post(self, request, *args, **kwargs):
        try:
            sr = get_object_or_404(SearchRequest, id=kwargs['pk'])
            if sr.user != request.user:
                raise Exception(u'Нет прав')

            sr.active = False
            sr.save()
            sr.clear_cache()

            return {
                'result': True,
                'id': sr.id,
                'message': u'Поиск по заявке остановлен'
            }
        except Exception as ex:
            return {
                'result': False,
                'message': unicode(ex)
            }


class SearchRequestClientsView_Client(SearchRequestPreviewView_Client):
    template_name = 'main/client/search_request/advert-list.html'

    def get_context_data(self, **kwargs):
        context = super(SearchRequestClientsView_Client, self).get_context_data(**kwargs)
        context['advert_list'] = self.object.clients.all()
        self.object.last_viewed_count = len(context['advert_list'])
        self.object.save()
        context['advert_noticed'] = [advert.id for advert in self.object.advert_noticed.all()]
        context['advert_not_send'] = [advert.id for advert in self.object.advert_not_send.all()]
        return context


class SearchRequestNotSendView_Client(ClientPermMixin, View):
    @method_decorator(ajax_request)
    def post(self, request, *args, **kwargs):
        try:
            sr = get_object_or_404(SearchRequest, id=kwargs['pk'])
            if sr.user != request.user:
                raise Exception(u'Нет прав')

            advert = get_object_or_404(Advert, id=request.POST.get('id'))

            sr.advert_not_send.add(advert)

            return {
                'result': True,
                'id': sr.id,
                'advert': advert.id
            }
        except Exception as ex:
            return {
                'result': False,
                'message': unicode(ex)
            }


class SearchRequestDoSendView_Client(ClientPermMixin, View):
    @method_decorator(ajax_request)
    def post(self, request, *args, **kwargs):
        try:
            sr = get_object_or_404(SearchRequest, id=kwargs['pk'])
            if sr.user != request.user:
                raise Exception(u'Нет прав')

            advert = get_object_or_404(Advert, id=request.POST.get('id'))

            sr.advert_not_send.remove(advert)
            if sr.active:
                send_search_request_notice.apply_async(kwargs={'id': sr.id}, countdown=900)

            return {
                'result': True,
                'id': sr.id,
                'advert': advert.id
            }
        except Exception as ex:
            return {
                'result': False,
                'message': unicode(ex)
            }


class DeliveryListView_Client(AdminRequiredMixin, BreadcrumbMixin, ListView):
    template_name = 'main/client/search_request/delivery-page.html'
    model = SearchRequest
    context_object_name = 'sr_list'
    paginate_by = 50

    def get_breadcrumbs(self):
        return super(DeliveryListView_Client, self).get_breadcrumbs() + [('Подписки', reverse('client:search-request:delivery'))]

    def get_queryset(self):
        query = Q()
        if self.request.REQUEST.get('username'):
            query &= Q(user__username__icontains=self.request.REQUEST.get('username'))
        if self.request.REQUEST.get('email'):
            query &= (Q(owner_email__icontains=self.request.REQUEST.get('email')))
        if self.request.REQUEST.get('site'):
            site_list = Site.objects.filter(id=self.request.REQUEST.get('site'))
            if site_list:
                query &= Q(site=site_list[0])
        return SearchRequest.objects.filter(query).select_related('user', 'site').order_by('-active', '-date')

    def get_context_data(self, **kwargs):
        context = super(DeliveryListView_Client, self).get_context_data(**kwargs)
        context['filter_form'] = DeliveryFilterForm(self.request.GET)
        return context