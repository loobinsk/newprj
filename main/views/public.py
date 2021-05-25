#-*- coding: utf-8 -*-
from registration.backends.default.views import RegistrationView
from main.form import RegisterForm, AuthForm, FeedbackForm, ReclameForm
from django.views.generic import View, TemplateView, FormView
from django.contrib.auth.views import login, logout
from main.models import Company, Advert, Tariff, Town
from uprofile.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from annoying.decorators import ajax_request
from django.views.decorators.csrf import csrf_exempt
from sorl.thumbnail import get_thumbnail
from gutils.views import BreadcrumbMixin, AjaxableResponseMixin
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from mail_templated import send_mail_admins, send_mail
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from datetime import datetime, timedelta
from ucomment.signals import comment_create
import re
from django.db.models import Count
from cache_utils.decorators import cached
from django.contrib.sites.models import Site


def user_check_sessions(sender, user, request, **kwargs):
    """
    Проверка сессий пользователя и закрытие остальных сессий
    """
    from user_sessions.models import Session

    Session.objects.filter(user=user).exclude(session_key=request.session.session_key).delete()


user_logged_in.connect(user_check_sessions)


def comment_send_notice(sender, user, **kwargs):
    """
    Отправка уведомления о комментарии
    """
    m = re.search('^company_(\d+)$', sender.key)
    if m:
        company_list = Company.objects.filter(id=m.group(1))
        if company_list:
            if company_list[0].owner:
                if company_list[0].owner != user:
                    send_mail('main/email/comment-notice.html', context={
                        'subject': 'У вашего агентства появился новый отзыв',
                        'comment': sender,
                        'company': company_list[0]
                    },
                          recipient_list=[company_list[0].owner.email],
                          fail_silently=True)

if settings.SITE_ID == 1:
    comment_create.connect(comment_send_notice)


class RegisterView(AjaxableResponseMixin, BreadcrumbMixin, RegistrationView):
    def __init__(self, *argc, **kwargs):
        super(RegisterView, self).__init__(*argc, **kwargs)
        self.form_class = RegisterForm

    def get_initial(self, request=None):
        initial = super(RegisterView, self).get_initial(request)
        initial['company_town'] = self.request.current_town.id
        return initial

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
        if form.cleaned_data['agent_status'] == RegisterForm.REGISTER_STATUS_COMPANY:
            town = get_object_or_404(Town, id=form.cleaned_data['company_town'])
            company = Company(
                owner=new_user,
                title=form.cleaned_data['company_name'],
                tel=form.cleaned_data['company_tel'],
                email=form.cleaned_data['username'],
                address=form.cleaned_data['company_address'],
                fact_address=form.cleaned_data['company_fact_address'],
                ogrn=form.cleaned_data['company_ogrn'],
                inn=form.cleaned_data['company_inn'],
                person=form.cleaned_data['company_person'],
                town=town
            )
            company.save()
            new_user.company = company
            new_user.tel =form.cleaned_data['company_tel']
            new_user.gen_access_code()
            new_user.save()

            send_mail('main/email/reg-notice.html',
                  {'company': company, 'subject': u'Поступила новая заявка на регистрацию от %s' % company.title},
                  recipient_list=settings.NOTICE_REGISTER_EMAIL)

        elif form.cleaned_data['agent_status'] == RegisterForm.REGISTER_STATUS_AGENT:
            if form.cleaned_data['company_town'] == '1':
                company = Company.objects.get(id=form.cleaned_data['agent_company_msk'])
            elif form.cleaned_data['company_town'] == '2':
                company = Company.objects.get(id=form.cleaned_data['agent_company_spb'])
            if not company.is_real:
                company.is_real = True
                company.status = Company.STATUS_MODERATE
                # company.owner = new_user
                if not company.tel:
                    company.tel = form.cleaned_data['company_tel']
                if not company.email:
                    company.email = new_user.email
            if not company.owner:
                company.owner = new_user
            company.save()

            new_user.company = company
            new_user.tel = form.cleaned_data['company_tel']
            new_user.first_name = form.cleaned_data['agent_name']
            new_user.gen_access_code()
            new_user.status = User.STATUS_MODERATE
            new_user.save()
            exist_users = company.user_set.filter(agent_email=new_user.email)
            if exist_users:
                new_user.extnum = exist_users[0].extnum
                new_user.save()
                exist_users[0].advert_set.all().update(user=new_user)
                exist_users[0].delete()

            send_mail('main/email/reg-agent-notice.html', {
                    'user': new_user,
                    'subject': u'Поступила новая заявка на регистрацию от агента %s' % new_user.username
                },
                recipient_list=settings.NOTICE_REGISTER_EMAIL)

        request.session['registration_email'] = form.cleaned_data['username']
        request.session.modified = True
        return new_user

    def get_breadcrumbs(self):
        return [('Агентствам недвижимости', reverse('registration_register'))]

    def get_model_dict(self):
        return {
            'message': u'Регистрация завершена',
            'url': reverse('registration_complete')
        }


class RegisterCompleteView(TemplateView):
    template_name='registration/registration_complete.html'

    def get_context_data(self, **kwargs):
        context = super(RegisterCompleteView, self).get_context_data(**kwargs)

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


class LoginView(View):
    def get(self, *args, **kwargs):
        return login(self.request, authentication_form=AuthForm)

    def post(self, *args, **kwargs):
        return login(self.request, authentication_form=AuthForm)


class LoginView_Moder(LoginView):
    def get(self, *args, **kwargs):
        return login(self.request, authentication_form=AuthForm, template_name='registration/moder/login.html')

    def post(self, *args, **kwargs):
        return login(self.request, authentication_form=AuthForm, template_name='registration/moder/login.html')


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
                    if user.image:
                        try:
                            thumb = get_thumbnail(user.image, '100x100', crop='center', quality=99)
                            context['image'] = thumb.url
                        except:
                            context['image'] = ''
                    else:
                        context['image'] = ''
                    company = user.company
                    if company:
                        context['activated'] = company.status == Company.STATUS_ACTIVE
                        context['company'] = company.title
                    else:
                        context['activated'] = True
                        context['company'] = ''
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


class LogoutView_Moder(LoginView):
    def get(self, *args, **kwargs):
        return logout(self.request, next_page='/', template_name='registration/moder/login.html')

    def post(self, *args, **kwargs):
        return logout(self.request, next_page='/', template_name='registration/moder/login.html')


class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        town = self.request.current_town

        # статистика
        context['count_adverts'] = self.get_count_adverts()
        context['count_companies'] = self.get_count_companies()

        # последние объявления

        context['vip_list'] = Advert.objects.filter(company=None,
                                                    town=town,
                                                    need=Advert.NEED_SALE,
                                                    status=Advert.STATUS_VIEW,
                                                    date__gte=datetime.now() - timedelta(days=30))\
            .filter(Advert.ARCHIVE_NO_QUERY)\
            .annotate(image_count=Count('images'))\
            .exclude(image_count=0)\
            .order_by('?')[:5]

        context['last_advert_list'] = Advert.objects.filter(town=town, need=Advert.NEED_SALE, status=Advert.STATUS_VIEW).order_by('-date')[:5]
        context['arenda_advert_list'] = Advert.objects\
            .filter(adtype=Advert.TYPE_LEASE, town=town, need=Advert.NEED_SALE)\
            .filter(estate=Advert.ESTATE_LIVE, status=Advert.STATUS_VIEW)\
            .order_by('-date')[:4]

        context['sale_advert_list'] = Advert.objects \
                                            .filter(adtype=Advert.TYPE_SALE, town=town, need=Advert.NEED_SALE) \
                                            .filter(estate=Advert.ESTATE_LIVE, status=Advert.STATUS_VIEW) \
                                            .order_by('-date')[:4]

        return context

    @cached(3600)
    def get_count_adverts(self):
        return Advert.objects.filter(status=Advert.STATUS_VIEW).count()

    @cached(3600)
    def get_count_companies(self):
        return Company.objects.all().count()


def page_not_found(request, template_name='404.html'):
    from django.views.defaults import page_not_found
    return page_not_found(request, template_name)


def page_not_found_moder(request, template_name='404.html'):
    from django.views.defaults import page_not_found
    return page_not_found(request, template_name='404-moder.html')
