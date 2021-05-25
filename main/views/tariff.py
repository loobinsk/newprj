#-*- coding: utf-8 -*-
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView, FormView
from main.models import Town, Tariff, Payment, PaymentItem
from gutils.views import BreadcrumbMixin, AjaxPageMixin, AjaxableResponseMixin
from django.core.urlresolvers import reverse
from gutils.views import class_view_decorator
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import get_object_or_404
from main.form import TariffForm


class TariffListView(BreadcrumbMixin, ListView):
    model = Tariff
    template_name = 'main/tariff/page.html'

    def get_breadcrumbs(self):
        return [(u'Тарифы', reverse('tariff:list'))]


@class_view_decorator(permission_required('main.view_tariff'))
class TariffListView_Client(BreadcrumbMixin, ListView):
    model = Tariff
    template_name = 'main/client/tariff/page.html'

    def get_breadcrumbs(self):
        return [(u'Тарифы', reverse('client:tariff:list'))]

    def get_context_data(self, **kwargs):
        context = super(TariffListView_Client, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_tariff')
        return context


@class_view_decorator(permission_required('main.view_tariff'))
class TariffPreviewView(DetailView):
    model = Tariff
    template_name = 'main/client/tariff/preview.html'
    context_object_name = 'tariff'

    def get_context_data(self, **kwargs):
        context = super(TariffPreviewView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_tariff')
        return context


@class_view_decorator(permission_required('main.add_tariff'))
class TariffCreateView(AjaxableResponseMixin, CreateView):
    model = Tariff
    form_class = TariffForm
    template_name = 'main/client/tariff/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(TariffCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:tariff:create')
        return context

    def get_model_dict(self):
        return {
        }


@class_view_decorator(permission_required('main.change_tariff'))
class TariffUpdateView(AjaxableResponseMixin, UpdateView):
    model = Tariff
    form_class = TariffForm
    template_name = 'main/client/tariff/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(TariffUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:tariff:edit', kwargs={'pk': self.object.id})
        return context

    def get_model_dict(self):
        return {
        }


@class_view_decorator(permission_required('main.delete_tariff'))
class TariffDeleteView(AjaxableResponseMixin, DeleteView):
    model = Tariff
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super(TariffDeleteView, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return {
        }