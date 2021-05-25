#-*- coding: utf-8 -*-
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView, FormView, View
from django.core.urlresolvers import reverse
from vashdom.models import Payment, Tariff
from main.models import Advert, VKAdvert, Promocode, ReferralPayment
from gutils.views import AjaxableResponseMixin, BreadcrumbMixin
from datetime import datetime
from django.http import HttpResponseNotFound
from vashdom.forms import PaymentOrderForm
from django.shortcuts import get_object_or_404
from django.db.models import Q
from main.form import PromoForm
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class PaymentViewPermMixin(object):

    def dispatch(self, request, *args, **kwargs):
        payment = self.get_object()
        if (payment.user == request.user and request.user.is_authenticated()) or (request.user.is_anonymous() and payment.session_key==request.session.session_key) or (request.user.is_superuser):
            return super(PaymentViewPermMixin, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(redirect_to='/login/?next=%s' % request.path)


class PaymentDetailView(PaymentViewPermMixin, BreadcrumbMixin, DetailView):
    model = Payment
    template_name = 'vashdom/payment/detail.html'
    context_object_name = 'payment'

    def get_breadcrumbs(self):
        return [
            ('Платеж %s' % self.object.id, reverse('payment:detail', kwargs={'pk':self.object.id}))
        ]


class PaymentOrderView(AjaxableResponseMixin, FormView):
    form_class = PaymentOrderForm
    payment = None

    def form_valid(self, form):
        tariff = get_object_or_404(Tariff, id=form.cleaned_data['tariff'])
        if unicode(tariff.town_id) != form.cleaned_data['town']:
            raise Exception(u'Выберите тариф для вашего города')
        if not self.request.session.session_key:
            self.request.session.save()
        self.payment = Payment(
            tariff=tariff,
            town_id=form.cleaned_data['town'],
            tel=form.cleaned_data['tel'],
            email=form.cleaned_data['email'],
            session_key=self.request.session.session_key
        )
        if self.request.user.is_authenticated():
            self.payment.user = self.request.user
        else:
            if tariff.price == 0:
                raise Exception(u'Для того чтобы получить бесплатный доступ необходимо <a href="/register" class="btn btn-primary btn-sm">зарегистрироваться</a>')
        self.payment.sum = tariff.price
        self.payment.recalc_total()
        self.payment.description = u'Оплата доступа по тарифу: %s' % tariff.title
        self.payment.save()
        if self.payment.tariff.price == 0:
            self.payment.change_status(Payment.STATUS_CONFIRMED)
            self.payment.success()

        # реферрал
        if self.request.referral:
            refPayment = ReferralPayment(referral=self.request.referral, payment=self.payment)
            refPayment.save()
        return super(PaymentOrderView, self).form_valid(form)

    def get_success_url(self):
        return reverse('payment:detail', kwargs={'pk': self.payment.id})

    def get_model_dict(self):
        if self.payment.tariff.price > 0:
            return {
                'id': self.payment.id,
                'url': reverse('payment:detail', kwargs={'pk': self.payment.id}),
                'type': 'payment'
            }
        else:
            return {
                'id': self.payment.id,
                'type': 'free',
                'message': u'<div class="text-center">Вам предоставлен бесплатный доступ.<br>Спасибо за использование.'
                            u'<hr>'
                            u'<p>Расскажите друзьям о нашем сервисе</p>'
                            u'<span id="share_vkontakte" style="display:inline-block;"></span>'
                            u'<script type="text/javascript"><!-- '
                            u'jQuery("#share_vkontakte").html(VK.Share.button({url: "https://bazavashdom.ru/"},{type: "round", text: "Рассказать друзьям"}));'
                            u'--></script></div>'

            }


class PaymentSuccessView(TemplateView):
    template_name = 'vashdom/payment/success.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PaymentSuccessView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PaymentSuccessView, self).get_context_data(**kwargs)
        context['PAYMENT_ID'] = self.request.GET.get('PAYMENT_NO')
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class PaymentFailView(TemplateView):
    template_name = 'vashdom/payment/fail.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PaymentFailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PaymentFailView, self).get_context_data(**kwargs)
        context['PAYMENT_ID'] = self.request.GET.get('PAYMENT_NO')
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class PromocodeActivateView(AjaxableResponseMixin, FormView):
    form_class = PromoForm
    success_url = '/'
    promocode = None
    payment = None

    def form_valid(self, form):
        promocode_list = Promocode.objects.filter(code=self.request.POST.get('code').upper())
        if promocode_list:
            self.promocode = promocode_list[0]
        else:
            raise Exception(u'Неверный промокод')
        self.payment = get_object_or_404(Payment, id=self.request.POST.get('payment'))
        if self.payment.promocode:
            raise Exception(u'Уже активирован один промокод для этого платежа')
        if self.promocode.user:
            if self.request.user != self.promocode.user:
                raise Exception(u'Неверный промокод')
        if self.promocode.activate():
            self.payment.promocode = self.promocode
            self.payment.recalc_total()
            self.payment.save()
        return super(PromocodeActivateView, self).form_valid(form)

    def get_model_dict(self):
        return {
            'result': True,
            'promocode': self.promocode.id,
            'payment': self.payment.id
        }