# -*- coding: utf-8 -*-
from django.views.generic import View, TemplateView, FormView, ListView, CreateView
from main.models import Referral, ReferralUser, ReferralReferer, ReferralPayment
from vashdom.views.private import ClientPermMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from annoying.decorators import ajax_request
from gutils.views import AjaxableResponseMixin
from django.contrib.sites.models import Site
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import get_object_or_404


class ReferralView(ClientPermMixin, ListView):
    model = Referral
    template_name = 'vashdom/referral/page.html'

    def get_queryset(self):
        return super(ReferralView, self).get_queryset().filter(user=self.request.user)


class ReferralCreateView(ClientPermMixin, AjaxableResponseMixin, View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ReferralCreateView, self).dispatch(request, *args, **kwargs)

    @method_decorator(ajax_request)
    def post(self, request, *args, **kwargs):
        if Referral.objects.filter(user=self.request.user).count()<5:
            ref = Referral(user_id=self.request.user.id, site=Site.objects.get_current())
            ref.save()
            tpl = get_template('vashdom/referral/preview.html')
        else:
            raise Exception(u'У вас 5 реферальных ссылок. Чтобы создать больше, обратитесь к администратору сайта')
        return {
            'preview': tpl.render(Context({'referral': ref}))
        }


class ReferralUserListView(ClientPermMixin, ListView):
    model = ReferralUser
    template_name = 'vashdom/referral/user.html'
    context_object_name = 'user_list'
    referral = None
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        self.referral = get_object_or_404(Referral, id=kwargs['pk'], user=request.user)
        return super(ReferralUserListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return ReferralUser.objects.filter(referral=self.referral).select_related('user').order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(ReferralUserListView, self).get_context_data(**kwargs)
        context['referral'] = self.referral
        return context


class ReferralPaymentListView(ClientPermMixin, ListView):
    model = ReferralPayment
    template_name = 'vashdom/referral/payment.html'
    context_object_name = 'payment_list'
    referral = None
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        self.referral = get_object_or_404(Referral, id=kwargs['pk'], user=request.user)
        return super(ReferralPaymentListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return ReferralPayment.objects.filter(referral=self.referral).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(ReferralPaymentListView, self).get_context_data(**kwargs)
        context['referral'] = self.referral
        return context


class ReferralRefererListView(ClientPermMixin, ListView):
    model = ReferralPayment
    template_name = 'vashdom/referral/referer.html'
    context_object_name = 'referer_list'
    referral = None
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        self.referral = get_object_or_404(Referral, id=kwargs['pk'], user=request.user)
        return super(ReferralRefererListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return ReferralReferer.objects.filter(referral=self.referral).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(ReferralRefererListView, self).get_context_data(**kwargs)
        context['referral'] = self.referral
        return context
