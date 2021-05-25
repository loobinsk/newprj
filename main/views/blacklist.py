#-*- coding: utf-8 -*-
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView, FormView, View
from main.models import Blacklist, clear_tel_list, get_tel_list, Company
from uprofile.models import User
from gutils.views import BreadcrumbMixin, AjaxPageMixin, AjaxableResponseMixin, UpdateAccessMixin
from django.core.urlresolvers import reverse
from gutils.views import class_view_decorator
from django.contrib.auth.decorators import permission_required
from main.form import BlacklistForm, BlacklistMultiForm, BlacklistFilterForm
from datetime import datetime
from django.utils.decorators import method_decorator
from annoying.decorators import ajax_request
from django.contrib import messages
import re


@class_view_decorator(permission_required('main.view_blacklist'))
class BlacklistListView(BreadcrumbMixin, ListView):
    """
    Список городов
    """
    model = Blacklist
    context_object_name = 'blacklist_list'
    paginate_by = 50
    template_name = 'main/client/blacklist/page.html'

    def get_queryset(self):
        qs = super(BlacklistListView, self).get_queryset()
        if self.request.GET.get('tel'):
            qs = qs.filter(tel__icontains=self.request.GET.get('tel'))
        return qs

    def get_breadcrumbs(self):
        return super(BlacklistListView, self).get_breadcrumbs() + [('Черный список', reverse('client:blacklist:list'))]

    def get_context_data(self, **kwargs):
        context = super(BlacklistListView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_blacklist')
        context['filter_form'] = BlacklistFilterForm(data=self.request.GET)
        return context


@class_view_decorator(permission_required('main.view_blacklist'))
class BlacklistDetailView(BreadcrumbMixin, AjaxPageMixin, DetailView):
    model = Blacklist
    template_name = 'main/client/blacklist/detail.html'
    template_name_ajax = 'main/client/blacklist/detail-ajax.html'
    context_object_name = 'blacklist'

    def get_context_data(self, **kwargs):
        context = super(BlacklistDetailView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_blacklist')
        return context

    def get_breadcrumbs(self):
        return [(u'Вакансии', reverse('client:blacklist:list')),
                (self.object.title, reverse('client:blacklist:detail', kwargs={'pk':self.object.id}))]


@class_view_decorator(permission_required('main.view_blacklist'))
class BlacklistPreviewView(DetailView):
    model = Blacklist
    template_name = 'main/client/blacklist/preview.html'
    context_object_name = 'blacklist'

    def get_context_data(self, **kwargs):
        context = super(BlacklistPreviewView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_blacklist')
        return context


@class_view_decorator(permission_required('main.add_blacklist'))
class BlacklistCreateView(AjaxableResponseMixin, CreateView):
    model = Blacklist
    form_class = BlacklistForm
    template_name = 'main/client/blacklist/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(BlacklistCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:blacklist:create')
        return context

    def get_model_dict(self):
        return {}


@class_view_decorator(permission_required('main.change_blacklist'))
class BlacklistUpdateView(AjaxableResponseMixin, UpdateView):
    model = Blacklist
    form_class = BlacklistForm
    template_name = 'main/client/blacklist/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(BlacklistUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:blacklist:edit', kwargs={'pk': self.object.id})
        return context

    def get_model_dict(self):
        return { }


@class_view_decorator(permission_required('main.delete_blacklist'))
class BlacklistDeleteView(AjaxableResponseMixin, DeleteView):
    model = Blacklist
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super(BlacklistDeleteView, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return {
            'url': reverse('client:blacklist:list')
        }

@class_view_decorator(permission_required('main.add_blacklist'))
class BlacklistCreateMultiView(AjaxableResponseMixin, FormView):
    form_class = BlacklistMultiForm
    template_name = 'main/client/blacklist/multi-create-form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(BlacklistCreateMultiView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:blacklist:multi-create')
        return context

    def form_valid(self, form):
        tel_list = form.cleaned_data['tel'].split('\n')
        n = 0
        for tel in tel_list:
            tel = clear_tel_list(tel)
            if tel:
                Blacklist.add_tel(tel)
                n += 1
        messages.info(self.request, 'Импортировано %s телефонов' % n)
        return super(BlacklistCreateMultiView, self).form_valid(form)

    def get_model_dict(self):
        return {
            'url': reverse('client:blacklist:list')
        }


@class_view_decorator(permission_required('main.view_blacklist'))
class BlacklistCheckView(View):

    @method_decorator(ajax_request)
    def get(self, request, *args, **kwargs):
        message = u''
        tel_list = get_tel_list(request.GET.get('tel'))
        result = False
        for tel in tel_list:
            if tel:
                exists = False
                blacklist = Blacklist.objects.filter(tel__icontains=tel)
                if blacklist:
                    message += u'Телефон %s есть в черном списке как %s<br>' % (tel, blacklist[0].tel)
                    result = exists = True
                else:
                    mask_blacklist = Blacklist.objects.filter(tel__icontains='X')
                    for mask_tel in mask_blacklist:
                        if re.search(mask_tel.tel.replace('X', '(.)'), tel):
                            message += u'Телефон %s есть в черном списке как %s' % (tel, mask_tel.tel)
                            result = exists = True
                            break
                    if not exists:
                        company = Company.objects.filter(tel__icontains=tel)
                        if company:
                            message += u'Телефон %s принадлежит агентству <br>'
                            result = exists = True
                        else:
                            user = User.objects.filter(tel__icontains=tel)
                            if user:
                                message += u'Телефон %s принадлежит агентству <br>'
                                result = exists = True
                if not exists:
                    message += u'Телефона %s нет в черном списке<br>' % tel
            else:
                message += u'Телефон пустой<br>'

        if result:
            message = u'<div class="modal-icon"><img src="/static/img/agent.png"><p>' + message + u'</p>'
        else:
            message = u'<div class="modal-icon"><img src="/static/img/ok.png"><p>' + message + u'</p>'

        return {
            'message': message,
            'result': result
        }


@class_view_decorator(permission_required('main.add_blacklist'))
class BlacklistAddTelView(View):

    @method_decorator(ajax_request)
    def post(self, request, *args, **kwargs):
        message = u''
        tel_list = get_tel_list(request.POST.get('tel'))
        for tel in tel_list:
            if len(tel)>=5:
                blacklist = Blacklist.objects.filter(tel__icontains=tel)
                if blacklist:
                    message += u'Есть совпадения с телефоном %s, который уже в черном списке<br>' % blacklist[0].tel
                else:
                    Blacklist.add_tel(tel)
                    message += u'Телефон %s добавлен в черный список<br>' % tel
            else:
                message += u'Телефон %s меньше 5 цифр<br>' % tel
        return {
            'message': message
        }