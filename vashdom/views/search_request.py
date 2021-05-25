# -*- coding: utf-8 -*-
from django.views.generic import View, TemplateView, FormView, ListView, CreateView, DetailView
from main.models import SearchRequest
from gutils.views import AjaxableResponseMixin, BreadcrumbMixin
from vashdom.forms import SearchRequestForm, SearchRequestSimpleForm
from django.core.urlresolvers import reverse
from main.models import Advert
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.contrib.sites.models import Site


class SearchRequestCreateView(BreadcrumbMixin, AjaxableResponseMixin, CreateView):
    model = SearchRequest
    form_class = SearchRequestForm
    template_name = 'vashdom/searchrequest/create.html'
    success_url = '/'
    advert = None

    def get(self, request, *args, **kwargs):
        if request.GET.get('catalog'):
            self.advert = get_object_or_404(Advert, id=request.GET.get('catalog'))
        return super(SearchRequestCreateView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SearchRequestCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('search-request:create')
        context['advert'] = self.advert
        return context

    def get_form_kwargs(self):
        kwargs = super(SearchRequestCreateView, self).get_form_kwargs()
        kwargs['filter_town'] = self.request.current_town
        return kwargs

    def get_initial(self):
        initial = super(SearchRequestCreateView, self).get_initial()
        if self.advert:
            if self.advert.square:
                initial['square'] = self.advert.square
            initial['price'] = self.advert.price
            if self.advert.live == Advert.LIVE_ROOM:
                initial['live'] = Advert.LIVE_ROOM
            if self.advert.live == Advert.LIVE_FLAT:
                initial['live'] = Advert.LIVE_FLAT
                if self.advert.rooms == 1:
                    initial['live_flat1'] = True
                elif self.advert.rooms == 2:
                    initial['live_flat2'] = True
                elif self.advert.rooms == 3:
                    initial['live_flat3'] = True
                elif self.advert.rooms >= 4:
                    initial['live_flat4'] = True
            if self.request.user.is_authenticated():
                initial['owner_tel'] = self.request.user.tel
                initial['owner_email'] = self.request.user.email
            if self.advert.metro:
                initial['metro'] = [str(self.advert.metro_id)]
            if self.advert.district:
                initial['district'] = [str(self.advert.district_id)]
            if self.advert.refrigerator:
                initial['refrigerator'] = True
            if self.advert.internet:
                initial['internet'] = True
            if self.advert.balcony:
                initial['balcony'] = True
            if self.advert.tv:
                initial['tv'] = True
            if self.advert.conditioner:
                initial['conditioner'] = True
            if self.advert.euroremont:
                initial['euroremont'] = True
            if self.advert.washer:
                initial['washer'] = True
            if self.advert.furniture:
                initial['furniture'] = True
            if self.advert.parking:
                initial['parking'] = True
            if self.advert.phone:
                initial['phone'] = True
            if self.advert.separate_wc:
                initial['separate_wc'] = True
            if self.advert.lift:
                initial['lift'] = True
        return initial

    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user

        form.instance.adtype = Advert.TYPE_LEASE
        form.instance.need = Advert.NEED_DEMAND
        form.instance.date = datetime.now()
        form.instance.town = self.request.current_town
        form.instance.active = True

        result = super(SearchRequestCreateView, self).form_valid(form)
        form.instance.find_clients()
        return result

    def get_model_dict(self):
        message = '<div class="success-advert"><img src="/static/img/ok.png"><p>Ваша подписка оформлена.</p><p>Для существенного ускорения поиска рекомендуем услугу подбора.</p><p><a href="/poisk/" title="Поиск жилья под Ваши требования">Подробнее..</a></p></div>'
        return {
            'message': message,
            'url': '/%s/' % self.request.current_town.slug
        }

    def get_breadcrumbs(self):
        return [('Подписаться на объявления', reverse('search-request:create'))]


class SearchRequestSimpleCreateView(AjaxableResponseMixin, FormView):
    model = SearchRequest
    form_class = SearchRequestSimpleForm
    template_name = 'vashdom/searchrequest/simple.html'
    success_url = '/'
    advert = None

    def get(self, request, *args, **kwargs):
        if request.GET.get('id'):
            self.advert = get_object_or_404(Advert, id=request.GET.get('id'))
        return super(SearchRequestSimpleCreateView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SearchRequestSimpleCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('search-request:simple')
        context['advert'] = self.advert
        return context

    def get_initial(self):
        initial = super(SearchRequestSimpleCreateView, self).get_initial()
        if self.advert:
            initial['catalog_id'] = self.advert.id
        if self.request.user.is_authenticated():
            initial['email'] = self.request.user.email
        return initial

    def form_valid(self, form):
        advert = get_object_or_404(Advert, id=form.cleaned_data['catalog_id'])
        
        sr = SearchRequest(adtype=Advert.TYPE_LEASE,
                           need=Advert.NEED_DEMAND,
                           date=datetime.now(),
                           town=advert.town,
                           active=True,
                           owner_email=form.cleaned_data['email'])
        
        if advert.square:
            sr.square = advert.square
        sr.price = advert.price
        if advert.live == Advert.LIVE_ROOM:
            sr.live = Advert.LIVE_ROOM
        if advert.live == Advert.LIVE_FLAT:
            sr.live = Advert.LIVE_FLAT
            if advert.rooms == 1:
                sr.live_flat1 = True
            elif advert.rooms == 2:
                sr.live_flat2 = True
            elif advert.rooms == 3:
                sr.live_flat3 = True
            elif advert.rooms >= 4:
                sr.live_flat4 = True
        if self.request.user.is_authenticated():
            sr.owner_tel = self.request.user.tel
            sr.user = self.request.user
        if advert.refrigerator:
            sr.refrigerator = True
        if advert.internet:
            sr.internet = True
        if advert.balcony:
            sr.balcony = True
        if advert.tv:
            sr.tv = True
        if advert.conditioner:
            sr.conditioner = True
        if advert.euroremont:
            sr.euroremont = True
        if advert.washer:
            sr.washer = True
        if advert.furniture:
            sr.furniture = True
        if advert.parking:
            sr.parking = True
        if advert.phone:
            sr.phone = True
        if advert.separate_wc:
            sr.separate_wc = True
        if advert.lift:
            sr.lift = True

        sr.save()
        if advert.metro:
            sr.metro.add(advert.metro)

        result = super(SearchRequestSimpleCreateView, self).form_valid(form)
        sr.find_clients()
        return result

    def get_model_dict(self):
        message = '<div class="success-advert"><img src="/static/img/ok.png"><p>Ваша подписка оформлена</p></div>'
        return {
            'message': message,
        }


class SearchRequestUnsubsribeView(DetailView):
    model = SearchRequest
    template_name = 'vashdom/searchrequest/unsubscribe.html'

    def get_queryset(self):
        return super(SearchRequestUnsubsribeView, self).get_queryset().filter(site=Site.objects.get_current())

    def get_context_data(self, **kwargs):
        context = super(SearchRequestUnsubsribeView, self).get_context_data(**kwargs)
        context['object'].delete()
        return context