#-*- coding: utf-8 -*-
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from main.models import Referral, ReferralUser, ReferralPayment, ReferralReferer
from gutils.views import BreadcrumbMixin, AjaxableResponseMixin, AdminRequiredMixin
from django.core.urlresolvers import reverse
from gutils.views import class_view_decorator
from django.contrib.auth.decorators import permission_required
from main.form import ReferralForm, ReferralFilterForm
from django.shortcuts import get_object_or_404
from django.db.models import Q, Count
from datetime import datetime


@class_view_decorator(permission_required('main.view_referral'))
class ReferralListView(AdminRequiredMixin, BreadcrumbMixin, ListView):
    model = Referral
    context_object_name = 'referral_list'
    paginate_by = 50
    template_name = 'main/client/referral/page.html'

    def get_queryset(self):
        return super(ReferralListView, self).get_queryset()

    def get_context_data(self, **kwargs):
        context = super(ReferralListView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_referral')
        return context

    def get_breadcrumbs(self):
        return [('Реферральные ссылки', reverse('client:referral:list'))]


@class_view_decorator(permission_required('main.view_referral'))
class ReferralPreviewView(AdminRequiredMixin, DetailView):
    model = Referral
    template_name = 'main/client/referral/preview.html'
    context_object_name = 'referral'

    def get_context_data(self, **kwargs):
        context = super(ReferralPreviewView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_referral')
        return context


@class_view_decorator(permission_required('main.add_referral'))
class ReferralCreateView(AdminRequiredMixin, AjaxableResponseMixin, CreateView):
    model = Referral
    form_class = ReferralForm
    template_name = 'main/client/referral/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ReferralCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:referral:create')
        return context

    def form_valid(self, form):
        return super(ReferralCreateView, self).form_valid(form)

    def get_model_dict(self):
        return { }


@class_view_decorator(permission_required('main.change_referral'))
class ReferralUpdateView(AdminRequiredMixin, AjaxableResponseMixin, UpdateView):
    model = Referral
    form_class = ReferralForm
    template_name = 'main/client/referral/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ReferralUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:referral:edit', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        return super(ReferralUpdateView, self).form_valid(form)

    def get_model_dict(self):
        return { }


@class_view_decorator(permission_required('main.delete_referral'))
class ReferralDeleteView(AdminRequiredMixin, AjaxableResponseMixin, DeleteView):
    model = Referral
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super(ReferralDeleteView, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return { }


@class_view_decorator(permission_required('main.view_referral'))
class ReferralUserListView_Client(AdminRequiredMixin, BreadcrumbMixin, ListView):
    model = ReferralUser
    template_name = 'main/client/referral/user.html'
    context_object_name = 'user_list'
    referral = None
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        self.referral = get_object_or_404(Referral, id=kwargs['pk'])
        return super(ReferralUserListView_Client, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return ReferralUser.objects.filter(referral=self.referral).select_related('user').order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(ReferralUserListView_Client, self).get_context_data(**kwargs)
        context['referral'] = self.referral
        context['can_edit'] = self.request.user.has_perm('uprofile.change_user')
        return context

    def get_breadcrumbs(self):
        return super(ReferralUserListView_Client, self).get_breadcrumbs() + [
            ('Реферральные ссылки', reverse('client:referral:list')),
            ('Привлеченные пользователи', reverse('client:referral:user', kwargs={'pk': self.referral.id})),
            ]
    
@class_view_decorator(permission_required('main.view_referral'))
class ReferralPaymentListView_Client(AdminRequiredMixin, BreadcrumbMixin, ListView):
    model = ReferralPayment
    template_name = 'main/client/referral/payment.html'
    context_object_name = 'payment_list'
    referral = None
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        self.referral = get_object_or_404(Referral, id=kwargs['pk'])
        return super(ReferralPaymentListView_Client, self).get(request, *args, **kwargs)

    def get_queryset(self):
        query = Q(referral=self.referral)
        start_date = '0001-01-01'
        if self.request.GET.get('start_date'):
            start_date = datetime.strptime(self.request.GET.get('start_date'), '%d.%m.%Y').strftime('%Y-%m-%d')
            query &= Q(date__gte=start_date)
        end_date = '9999-01-01'
        if self.request.GET.get('end_date'):
            end_date = datetime.strptime(self.request.GET.get('end_date'), '%d.%m.%Y').strftime('%Y-%m-%d')
            query &= Q(date__lte=end_date)
        return ReferralPayment.objects.filter(query).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(ReferralPaymentListView_Client, self).get_context_data(**kwargs)
        context['referral'] = self.referral
        context['form'] = ReferralFilterForm(data=self.request.GET)
        return context

    def get_breadcrumbs(self):
        return super(ReferralPaymentListView_Client, self).get_breadcrumbs() + [
            ('Реферральные ссылки', reverse('client:referral:list')),
            ('Привлеченные пользователи', reverse('client:referral:payment', kwargs={'pk': self.referral.id})),
            ]

@class_view_decorator(permission_required('main.view_referral'))
class ReferralRefererListView_Client(AdminRequiredMixin, BreadcrumbMixin, ListView):
    model = ReferralPayment
    template_name = 'main/client/referral/referer.html'
    context_object_name = 'referer_list'
    referral = None
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        self.referral = get_object_or_404(Referral, id=kwargs['pk'])
        return super(ReferralRefererListView_Client, self).get(request, *args, **kwargs)

    def get_queryset(self):
        query = Q(referral=self.referral)
        start_date = '0001-01-01'
        if self.request.GET.get('start_date'):
            start_date = datetime.strptime(self.request.GET.get('start_date'), '%d.%m.%Y').strftime('%Y-%m-%d')
            query &= Q(date__gte=start_date)
        end_date = '9999-01-01'
        if self.request.GET.get('end_date'):
            end_date = datetime.strptime(self.request.GET.get('end_date'), '%d.%m.%Y').strftime('%Y-%m-%d')
            query &= Q(date__lte=end_date)
        return ReferralReferer.objects.filter(query).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(ReferralRefererListView_Client, self).get_context_data(**kwargs)
        context['referral'] = self.referral
        context['form'] = ReferralFilterForm(data=self.request.GET)
        return context

    def get_breadcrumbs(self):
        return super(ReferralRefererListView_Client, self).get_breadcrumbs() + [
            ('Реферральные ссылки', reverse('client:referral:list')),
            ('Referer', reverse('client:referral:referer', kwargs={'pk': self.referral.id})),
            ]
