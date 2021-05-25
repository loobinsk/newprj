# -*- coding: utf-8 -*-
from django.views.generic import View, TemplateView, FormView
from main.models import Town, ReferralPayment, News
from gutils.views import BreadcrumbMixin, AjaxableResponseMixin
from vashdom.forms import PaymentOrderForm, FeedbackForm, RegisterForm, PaymentAlertForm
from vashdom.models import Tariff, Payment, VashdomAdvert, VashdomVKAdvert
from mail_templated import send_mail
from django.conf import settings
from django.utils.decorators import method_decorator
from annoying.decorators import ajax_request
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import login, logout
from main.form import AuthForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from registration.backends.default.views import RegistrationView
from django.core.urlresolvers import reverse
from datetime import datetime, timedelta


class LoginView(View):
    def get(self, *args, **kwargs):
        return login(self.request, authentication_form=AuthForm, template_name='registration/login.html')

    def post(self, *args, **kwargs):
        return login(self.request, authentication_form=AuthForm, template_name='registration/login.html')


class AjaxLoginView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AjaxLoginView, self).dispatch(request, *args, **kwargs)

    @method_decorator(ajax_request)
    def post(self, *args, **kwargs):
        context = {}
        form = AuthForm(self.request, data=self.request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    auth_login(self.request, user)
                    context['success'] = True
                    context['message'] = 'Добро пожаловать'
                    context['username'] = user.get_full_name()
                else:
                    context['success'] = False
                    context['message'] = 'Аккаунт заблокирован'
            else:
                # Return an 'invalid login' error message.
                context['success'] = False
                context['message'] = 'Неправильные имя пользователя или пароль'
        else:
            context['success'] = False
            a = []
            for error in form.errors:
                for e in form.errors[error]:
                    a.append(e)
            context['message'] = '<br>'.join(a)
        return context


class LogoutView(LoginView):
    def get(self, *args, **kwargs):
        return logout(self.request, next_page='/login/', template_name='registration/login.html')

    def post(self, *args, **kwargs):
        return logout(self.request, next_page='/login/', template_name='registration/login.html')


class RegisterView(AjaxableResponseMixin, BreadcrumbMixin, RegistrationView):
    template_name = 'registration/registration_form.html'
    form_class = RegisterForm

    def __init__(self, *argc, **kwargs):
        super(RegisterView, self).__init__(*argc, **kwargs)

    def get_form_kwargs(self, request=None, form_class=None):
        kwargs = super(RegisterView, self).get_form_kwargs(request, form_class)
        kwargs['town'] = self.request.current_town
        return kwargs

    def form_valid(self, request, form):
        response = super(AjaxableResponseMixin, self).form_valid(request, form)
        if self.request.is_ajax():
            data = {
                'id': self.object.pk if hasattr(self, 'object') else None,
                'object': self.get_model_dict(),
                }
            return self.render_to_json_response(data)
        else:
            return response

    def register(self, request, form):
        form.cleaned_data['email'] = form.cleaned_data['username']
        new_user = super(RegisterView, self).register(request, form)
        new_user.tel = form.cleaned_data['tel']
        new_user.gen_access_code()
        new_user.save()

        # формируем платеж
        tariff = Tariff.objects.get(id=form.cleaned_data['tariff'])
        payment = Payment(user=new_user,
                          tariff=tariff,
                          town_id=form.cleaned_data['town'],
                          tel=new_user.tel)
        payment.total = tariff.price
        payment.description = u'Оплата доступа по тарифу: %s' % tariff.title
        payment.save()

        if tariff.price == 0:
            payment.change_status(Payment.STATUS_CONFIRMED)
            payment.success()

        # реферрал
        if self.request.referral:
            refPayment = ReferralPayment(referral=self.request.referral, payment=payment)
            refPayment.save()

        request.session['registration_email'] = form.cleaned_data['username']
        request.session['payment_id'] = payment.id
        request.session.modified = True
        return new_user

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context['tariff_list'] = Tariff.objects.filter(hidden=False).order_by('order')
        return context

    def get_breadcrumbs(self):
        return [('Регистрация', reverse('registration_register'))]

    def get_model_dict(self):
        return {
            'message': u'Регистрация завершена',
            'url': reverse('registration_complete')
        }


class RegisterCompleteView(TemplateView):
    template_name= 'registration/registration_complete.html'

    def get_context_data(self, **kwargs):
        context = super(RegisterCompleteView, self).get_context_data(**kwargs)
        if self.request.session.get('payment_id'):
            try:
                payment = Payment.objects.get(id=self.request.session.get('payment_id'))
                context['payment'] = payment
            except:
                pass


        mail_servers = [
            ("mail.ru","Почта Mail.Ru","https://e.mail.ru/"),
            ("bk.ru","Почта Mail.Ru (bk.ru)","https://e.mail.ru/"),
            ("list.ru","Почта Mail.Ru (list.ru)","https://e.mail.ru/"),
            ("inbox.ru","Почта Mail.Ru (inbox.ru)","https://e.mail.ru/"),
            ("yandex.ru","Яндекс.Почта","https://mail.yandex.ru/"),
            ("ya.ru","Яндекс.Почта","https://mail.yandex.ru/"),
            ("yandex.ua","Яндекс.Почта","https://mail.yandex.ua/"),
            ("yandex.by","Яндекс.Почта","https://mail.yandex.by/"),
            ("yandex.kz","Яндекс.Почта","https://mail.yandex.kz/"),
            ("yandex.com","Yandex.Mail","https://mail.yandex.com/"),
            ("gmail.com","Почта Gmail","https://mail.google.com/"),
            ("googlemail.com","Почта Gmail","https://mail.google.com/"),
            ("outlook.com","Почта Outlook.com","https://mail.live.com/"),
            ("hotmail.com","Почта Outlook.com (Hotmail)","https://mail.live.com/"),
            ("live.ru","Почта Outlook.com (live.ru)","https://mail.live.com/"),
            ("live.com","Почта Outlook.com (live.com)","https://mail.live.com/"),
            ("me.com","Почта iCloud Mail","https://www.icloud.com/"),
            ("icloud.com","Почта iCloud Mail","https://www.icloud.com/"),
            ("rambler.ru","Рамблер-Почта","https://mail.rambler.ru/"),
            ("yahoo.com","Почта Yahoo! Mail","https://mail.yahoo.com/"),
            ("ukr.net","Почта ukr.net","https://mail.ukr.net/"),
            ("i.ua","Почта I.UA","http://mail.i.ua/"),
            ("bigmir.net","Почта Bigmir.net","http://mail.bigmir.net/"),
            ("tut.by","Почта tut.by","https://mail.tut.by/"),
            ("inbox.lv","Inbox.lv","https://www.inbox.lv/"),
            ("mail.kz","Почта mail.kz","http://mail.kz/"),
        ]

        email = self.request.session.get('registration_email')
        if email:
            for server in mail_servers:
                if server[0].lower() in email.lower():
                    context['mail_server'] = server
        return context


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['advert_count'] = VashdomAdvert.objects.filter(VashdomAdvert.get_advert_query(self.request.current_town)).\
            filter(date_vashdom__gte=datetime.now()-timedelta(days=1), town=self.request.current_town).count()
        context['vkadvert_count'] = VashdomVKAdvert.objects.\
            filter(date_vashdom__gte=datetime.now()-timedelta(days=1),
                   status=VashdomVKAdvert.STATUS_VIEW,
                   town=self.request.current_town).count()
        context['news_list'] = News.objects.filter(site_id=settings.SITE_ID).order_by('-date').select_related()[:2]
        return context


class TariffView(BreadcrumbMixin, TemplateView):
    template_name = 'tariff.html'

    def get_context_data(self, **kwargs):
        context = super(TariffView, self).get_context_data(**kwargs)
        context['form'] = PaymentOrderForm(town=self.request.current_town)
        context['tariff_list'] = Tariff.objects.filter(hidden=False).order_by('order')
        return context

    def get_breadcrumbs(self):
        return super(TariffView, self).get_breadcrumbs() + [
            ('Оплата', reverse('tariff'))
        ]


class FreeAccessView(TemplateView):
    template_name = 'free-access.html'

    def get_context_data(self, **kwargs):
        context = super(FreeAccessView, self).get_context_data(**kwargs)
        need_auth = True
        if self.request.user.is_authenticated():
            for ua in self.request.user.social_auth.all():
                if ua.provider == 'vk-oauth':
                    need_auth = False
        context['need_auth'] = need_auth

        #free access
        if self.request.user.is_authenticated():
            services = ConnectedService.objects.filter(user=self.request.user,
                                                           tariff__code='freevk',
                                                           base=ConnectedService.BASE_VK).order_by('-end_date')[:1]
            context['free_access'] = services[0] if services else None
        else:
            context['free_access'] = None
        return context


class MentionsView(TemplateView):
    template_name = 'mentions.html'


class ContactsView(AjaxableResponseMixin, BreadcrumbMixin, FormView):
    form_class = FeedbackForm
    template_name = 'contacts.html'
    success_url = '/contact'

    def get_form_kwargs(self):
        kwargs = super(ContactsView, self).get_form_kwargs()
        kwargs['town'] = self.request.current_town
        return kwargs

    def form_valid(self, form):
        town = Town.objects.get(id=form.cleaned_data['town'])
        send_mail('vashdom/email/feedback.html',{
                'town': town,
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'tel': form.cleaned_data['tel'],
                'body': form.cleaned_data['body'],
                'subject': u'Новый вопрос с сайта BAZAVASHDOM.RU'
                },
                recipient_list=settings.NOTICE_FEEDBACK_EMAIL,
                fail_silently=True)
        return super(ContactsView, self).form_valid(form)

    def get_model_dict(self):
        return {
            'message': 'Ваш вопрос был отправлен менеджеру сайта.В ближайшее время он вам ответит'
        }

    def get_breadcrumbs(self):
        return super(ContactsView, self).get_breadcrumbs() + [
            ('Контакты', reverse('contacts')),
        ]


class PaymentAlertView(AjaxableResponseMixin, FormView):
    form_class = PaymentAlertForm
    template_name = 'payment-alert.html'
    success_url = '/buy_alert'

    def get_form_kwargs(self):
        kwargs = super(PaymentAlertView, self).get_form_kwargs()
        kwargs['town'] = self.request.current_town
        return kwargs

    def form_valid(self, form):
        town = Town.objects.get(id=form.cleaned_data['town'])
        send_mail('vashdom/email/payment-alert.html',{
                'town': town,
                'data': form.cleaned_data,
                'subject': u'Новое уведомление о платеже с BAZAVASHDOM.RU'
                },
                recipient_list=settings.NOTICE_FEEDBACK_EMAIL,
                fail_silently=True)
        return super(PaymentAlertView, self).form_valid(form)

    def get_model_dict(self):
        return {
            'message': 'Ваш уведомление получено'
        }


class PartnerView(TemplateView):
    template_name = 'partner.html'


def page_not_found(request, template_name='404.html'):
    from django.views.defaults import page_not_found
    return page_not_found(request, template_name)