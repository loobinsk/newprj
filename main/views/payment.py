#-*- coding: utf-8 -*-
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView, FormView, View
from django.core.urlresolvers import reverse
from main.models import Payment, PaymentItem, Tariff, Promocode
from vashdom.models import Payment as VashdomPayment
from gutils.views import AjaxableResponseMixin, BreadcrumbMixin
from datetime import datetime
from main.form import PaymentOrderForm, BuyOrderForm, PromoForm
from main.views.private import ClientPermMixin
from django.http import HttpResponseNotFound
from gutils.views import AdminRequiredMixin
from django.shortcuts import get_object_or_404


class PaymentViewPermMixin(object):

    def dispatch(self, request, *args, **kwargs):
        payment = self.get_object()
        if (payment.user == request.user) or (request.user.is_superuser):
            return super(PaymentViewPermMixin, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseNotFound()


class PaymentDetailView(PaymentViewPermMixin, ClientPermMixin, BreadcrumbMixin, DetailView):
    model = Payment
    template_name = 'main/client/payment/detail.html'
    context_object_name = 'payment'

    def get_breadcrumbs(self):
        return [('Настройки', reverse('client:company:my')),
            ('История платежей', reverse('client:payment:history')),
            ('Заказ %s' % self.object.id, reverse('client:payment:detail', kwargs={'pk':self.object.id}))
        ]


class PaymentOrderView(AjaxableResponseMixin, ClientPermMixin, FormView):
    form_class = PaymentOrderForm

    def get_form_kwargs(self):
        kwargs = super(PaymentOrderView, self).get_form_kwargs()
        kwargs['town'] = self.request.current_town
        return kwargs

    def form_valid(self, form):
        self.payment = Payment(
            total=0,
            user=self.request.user
        )
        self.payment.save()
        total_sum = 0
        discount = 0
        months = form.cleaned_data['months']
        if months == 2:
            discount = 0.10
        elif months == 3:
            discount = 0.15
        elif months == 6:
            discount = 0.20
        elif months == 9:
            discount = 0.25
        elif months == 12:
            discount = 0.30
        desc = []
        tariff = Tariff.objects.get(id=form.cleaned_data['tariff'])
        item = PaymentItem(
            tariff=tariff,
            total=tariff.price * months,
            quantity=months,
            price=tariff.price
        )
        item.save()
        total_sum += item.total
        self.payment.items.add(item)
        desc.append(u'%s (%s мес.)' % (tariff.title, months))

        total_discount = total_sum * discount
        self.payment.discount = total_discount
        self.payment.sum = total_sum
        self.payment.recalc_total()
        self.payment.description = u', '.join(desc)
        self.payment.save()
        return super(PaymentOrderView, self).form_valid(form)

    def get_success_url(self):
        return reverse('client:payment:detail', kwargs={'pk': self.payment.id})

    def get_model_dict(self):
        return {
            'id': self.payment.id,
            'url': reverse('client:payment:detail', kwargs={'pk': self.payment.id})
        }


class BuyOrderView(ClientPermMixin, AjaxableResponseMixin, FormView):
    form_class = BuyOrderForm

    def form_valid(self, form):
        self.payment = Payment(
            total=0,
            user=self.request.user
        )
        self.payment.save()
        total_sum = 0
        price = 150
        count = int(form.cleaned_data['count'])
        if count == 10:
            price = 130
        elif count == 20:
            price = 100
        elif count == 50:
            price = 80

        item = PaymentItem(
            paytype=PaymentItem.TYPE_BUY,
            total=price * count,
            quantity=count,
            price=price
        )
        item.save()
        total_sum += item.total
        self.payment.items.add(item)

        self.payment.sum = total_sum
        self.payment.recalc_total()
        self.payment.description = u'Выкупы (%s шт.)' % count
        self.payment.save()
        return super(BuyOrderView, self).form_valid(form)

    def get_success_url(self):
        return reverse('client:payment:detail', kwargs={'pk': self.payment.id})

    def get_model_dict(self):
        return {
            'id': self.payment.id,
            'url': reverse('client:payment:detail', kwargs={'pk': self.payment.id})
        }


class PaymentHistoryView(ClientPermMixin, BreadcrumbMixin, ListView):
    model = Payment
    paginate_by = 20
    template_name = 'main/client/payment/page.html'
    context_object_name = 'payment_list'

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)

    def get_breadcrumbs(self):
        return [('Настройки', reverse('client:company:my')),
            ('История платежей', reverse('client:payment:history'))]


class AllPaymentListView(AdminRequiredMixin, BreadcrumbMixin, ListView):
    model = Payment
    paginate_by = 20
    template_name = 'main/client/payment/all.html'
    context_object_name = 'payment_list'

    def get_queryset(self):
        return Payment.objects.all().select_related('user').order_by('-created')

    def get_breadcrumbs(self):
        return [('Платежи', reverse('client:payment:all'))]


class AllVashdomPaymentListView(AdminRequiredMixin, BreadcrumbMixin, ListView):
    model = VashdomPayment
    paginate_by = 20
    template_name = 'main/client/payment/vashdom/all.html'
    context_object_name = 'payment_list'

    def get_queryset(self):
        return VashdomPayment.objects.all().select_related('user', 'tariff', 'town').order_by('-created')

    def get_breadcrumbs(self):
        return [('Платежи БазаВашДом', reverse('client:payment:all-vashdom'))]


class PromocodeActivateView(ClientPermMixin, AjaxableResponseMixin, FormView):
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