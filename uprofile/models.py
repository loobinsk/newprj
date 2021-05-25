# coding=utf8

from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, UserManager as BaseUserManager
import string
import random
import os
from django.db import models
import urllib2
from django.core.files.base import ContentFile
from datetime import datetime, timedelta
from django.db.models import Q, Sum, Count
from wsgi_jsonrpc.json_tools import ServerProxy
import uuid, json
from cache_utils.decorators import cached
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.core.mail import send_mail
from mail_templated import send_mail as mailto
from django.conf import settings
from jsonfield import JSONField
import collections
from registration.signals import user_registered


def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def get_user_avatar_path(instance, filename):
    fname, ext = os.path.splitext(filename)
    return os.path.join('user', str(instance.id), id_generator(10) + ext)


class UserManager(BaseUserManager):
    def get_queryset(self):
        return super(UserManager, self).get_queryset().filter(site=settings.SITE_ID)


class UserAdminManager(BaseUserManager):
    pass


class User(AbstractBaseUser, PermissionsMixin):
    """
    Пользователь
    """
    STATUS_ACTIVE = 'a'
    STATUS_MODERATE = 'm'
    STATUS_BLOCK = 'b'
    STATUSES = {
        STATUS_ACTIVE: 'Активен',
        STATUS_MODERATE: 'На модерации',
        STATUS_BLOCK: 'Заблокирован',
    }

    SEX_MALE = 'm'
    SEX_FEMALE = 'f'
    SEX = {
        SEX_MALE: 'Мужской',
        SEX_FEMALE: 'Женский'
    }

    username = models.CharField(_('username'), max_length=30,
        help_text=_('Required. 30 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$',
                                      _('Enter a valid username. '
                                        'This value may contain only letters, numbers '
                                        'and @/./+/-/_ characters.'), 'invalid'),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        })
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=datetime.now)

    objects = UserManager()
    admin_objects = UserAdminManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    image = models.ImageField(u'Фото', upload_to=get_user_avatar_path, null=True, blank=True)
    tel = models.CharField(u'Телефон', max_length=50, null=True, blank=True)
    extnum = models.CharField(u'Внешний код', max_length=50, default=None, null=True, blank=True)
    town = models.ForeignKey('main.Town', verbose_name='Город', null=True, blank=True, default=None)
    company = models.ForeignKey('main.Company', verbose_name='Агентство', null=True, blank=True, default=None)
    agent24_code = models.CharField(u'Код доступа', max_length='15', default=None, null=True, blank=True, unique=True)
    buys = models.PositiveIntegerField(verbose_name=u'Выкупы', default=0, blank=True)
    agent_email = models.EmailField(verbose_name=u'Агентский email', null=True, blank=True, default='')
    status = models.CharField(u'Статус', max_length=1, default=STATUS_ACTIVE, choices=STATUSES.items())
    independent = models.BooleanField(u'Независимый агент', default=True, blank=True)
    enable_perms = models.ManyToManyField('main.Perm', verbose_name='Подключенные разделы доступа', blank=True)
    sex = models.CharField(u'Пол', max_length=1, default=SEX_MALE, blank=True)
    uuid = models.CharField(u'UUID', max_length=250, default='', blank=True)
    site = models.ForeignKey(Site, verbose_name='Сайт', null=True, blank=True, default=None)

    # настройки ГСН24
    agent24_view_owner = models.BooleanField(u'Объявления от собственников', default=True, blank=True)
    agent24_view_company = models.BooleanField(u'Объявления от агентств', default=True, blank=True)
    AGENT24_SECTIONS = collections.OrderedDict([
        ('lease', u'Аренда'),
        ('sale', u'Продажа'),
        ('house', u'Дома'),
        ('territory', u'Земля'),
        ('commercial', u'Коммерческая недвижимость')
    ])
    # agent24_view_perms = models.ManyToManyField('main.Perm', verbose_name='Подключенные разделы ГСН24', blank=True, related_name='agent24_view')
    properties = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict}, default={}, blank=True, null=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        permissions = (
            ('view_client', 'Просмотр клиентской части'),
            ('view_moderate', 'Просмотр модераторской части'),
            ('view_user', 'Просмотр списка агентов'),
        )
        unique_together = ('username', 'site',)

    def __unicode__(self):
        return unicode(self.id)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.uuid:
            self.uuid = uuid.uuid4()
        if not self.site:
            self.site = Site.objects.get_current()

        result = super(User, self).save(force_insert, force_update, using, update_fields)
        if (not update_fields or 'image' in update_fields) and self.image.name:
            from main.models import SyncFiles
            SyncFiles.syncfiles([self.image.name])
        return result


    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        if not full_name.strip():
            full_name = self.username
        return full_name

    def get_short_name(self):
        short_name = self.first_name
        if not short_name:
            short_name = self.username
        return short_name

    def get_company_name(self):
        if self.company:
            return self.company.title
        else:
            return self.get_full_name()

    def gen_password(self):
        self.set_password(id_generator(8))

    def gen_username(self, prefix=''):
        self.username = prefix + id_generator(8)

    def load_photo(self, href):
        from main.models import SyncFiles
        img = urllib2.urlopen(href)
        self.image.save(get_user_avatar_path(self, href), ContentFile(img.read()), save=True)
        SyncFiles.syncfiles([self.image.name])

    def get_tel_list(self):
        from main.models import get_tel_list
        return get_tel_list(self.tel)

    def gen_access_code(self):
        while True:
            agent24_code = id_generator(6, chars=string.digits)
            if User.objects.filter(agent24_code=agent24_code).count() == 0:
                self.agent24_code = agent24_code
                break

    def has_access(self):
        hour = datetime.now().hour
        if self.is_active:
            if self.company.owner == self:
                return True
            perm = self.get_active_week_perm()
            if perm:
                if perm.active and (perm.min_hour<=hour) and (hour<=perm.max_hour):
                    return True
            else:
                return True
        return False

    def get_active_week_perm(self):
        week_day = datetime.now().weekday()+1
        perm_list = self.weekperm_set.filter(day=week_day)
        if perm_list:
            return perm_list[0]
        return None

    def get_access_query(self, base='main'):
        if self.independent:
            from main.models import ConnectedService
            query = Q(id=None)
            service_list = ConnectedService.objects.filter(user=self, active=True, start_date__lte=datetime.now(), end_date__gte=datetime.now()).select_related('perm')
            for service in service_list:
                query |= service.perm.get_query(base=base, user=self)
            return query
        else:
            return self.company.get_access_query(user=self, base=base)

    def get_perms(self):
        """
        Получить список подключенных разделов
        """
        from main.models import Perm, ConnectedService, Company
        if self.independent:
            return Perm.objects.filter(connectedservice__user__id=self.id, connectedservice__start_date__lte=datetime.now(), connectedservice__end_date__gte=datetime.now()).distinct()
        else:
            return Perm.objects.filter(connectedservice__company__id=self.company_id, connectedservice__start_date__lte=datetime.now(), connectedservice__end_date__gte=datetime.now()).distinct()

    def get_active_perms(self):
        """
        получить список активных подключенных разделов
        """
        if self.independent or (self == self.company.owner):
            return self.get_perms()
        else:
            return self.get_perms().filter(id__in=[perm.id for perm in self.enable_perms.all()]).order_by('order')

    def get_agent24_perms(self):
        return User.AGENT24_SECTIONS.copy()

    def get_agent24_active_perms(self):
        perms = self.get_agent24_perms()
        if 'agent24_disabled' in self.properties:
            for item in self.properties['agent24_disabled']:
                del(perms[item])
        return perms

    @models.permalink
    def get_absolute_url(self):
        return ('user:detail', [self.id])

    def brokers_filter(self):
        from main.models import Company, Advert
        if self.company:
            if self.first_name == self.company.title and not self.company.is_real:
                old_company = self.company
                if self.company.town_id == 1:
                    new_company = Company.objects.get(extnum='msk_brokers')
                elif self.company.town_id == 2:
                    new_company = Company.objects.get(extnum='spb_brokers')
                self.advert_set.all().update(company=new_company)
                self.company = new_company
                self.save()
                old_company.delete()

    def is_online(self):
        from online.middleware import online
        return online.exists(self)

    @cached(3600)
    def get_client_request_count(slf):
        from main.models import ClientRequest
        return ClientRequest.objects.filter(user=slf).count()

    @cached(3600)
    def get_new_client_request_count(slf):
        from main.models import ClientRequest
        return ClientRequest.objects.filter(user=slf, is_viewed=False).count()

    @cached(3600)
    def get_search_request_count(slf):
        from main.models import SearchRequest
        return SearchRequest.objects.filter(user=slf).count()

    @cached(3600)
    def get_new_search_request_count(slf):
        from main.models import SearchRequest, Advert
        last = SearchRequest.objects.filter(user=slf).aggregate(Sum('last_viewed_count'))['last_viewed_count__sum']
        return SearchRequest.objects.filter(user=slf).aggregate(Count('clients'))['clients__count'] - (last if last else 0)

    @cached(3600)
    def get_request_count(slf):
        from main.models import Advert
        return Advert.objects.filter(user=slf).count()

    @cached(3600)
    def get_new_request_count(slf):
        from main.models import Advert
        last = Advert.objects.filter(user=slf).aggregate(Sum('last_viewed_count'))['last_viewed_count__sum']
        return Advert.objects.filter(user=slf).aggregate(Count('clients'))['clients__count'] - (last if last else 0)

    def clear_cache(self):
        cached(3600)(self.get_client_request_count).invalidate(self)
        cached(3600)(self.get_new_client_request_count).invalidate(self)
        cached(3600)(self.get_search_request_count).invalidate(self)
        cached(3600)(self.get_new_search_request_count).invalidate(self)
        cached(3600)(self.get_request_count).invalidate(self)
        cached(3600)(self.get_new_request_count).invalidate(self)

    @cached(3600)
    def get_vkontakte_link(slf):
        from social_auth.db.django_models import UserSocialAuth
        ua = UserSocialAuth.objects.filter(user=slf, provider='vk-oauth')
        if ua:
            return 'https://vk.com/id%s' % ua[0].uid
        else:
            return None

    def update_photo_vkontakte(self):
        import requests
        from social_auth.db.django_models import UserSocialAuth

        if not self.image:
            print self.username
            ua = UserSocialAuth.objects.filter(user=self, provider='vk-oauth')
            if ua:
                r = requests.get('https://api.vk.com/method/users.get?user_ids=%s&fields=photo_200' % ua[0].uid)
                response_data = json.loads(r.text)
                user_data = response_data['response'][0]
                if 'photo_200' in user_data:
                    image_url = user_data['photo_200']
                    print image_url
                    self.load_photo(image_url)

    def activate_freevk(self):
        from main.models import ConnectedService, Perm

        perm = Perm.objects.get(code='freevk')
        list = ConnectedService.objects.filter(user=self, perm=perm)
        if not list:
            service = ConnectedService(user=self, perm=perm,
                                       start_date=datetime.now(), end_date=datetime.now() + timedelta(days=7),
                                       active=True)
            service.save()
            if self.email:
                print self.email
                mailto('main/email/freevk-notice.html', context={'user': self, 'subject': 'Вам предоставлен бесплатный доступ к базе недвижимости ВКонтакте'},
                       recipient_list=[self.email], fail_silently=True)
            elif self.agent_email:
                print self.agent_email
                mailto('main/email/freevk-notice.html', context={'user': self, 'subject': 'Вам предоставлен бесплатный доступ к базе недвижимости ВКонтакте'},
                       recipient_list=[self.agent_email], fail_silently=True)


class GlobalUser(User):
    class Meta:
        proxy = True

    objects = BaseUserManager()


def load_user_image(backend, user, response, is_new, *args, **kwargs):
    import requests
    if is_new:
        try:
            image_url = None
            if backend.name == 'vk-oauth':
                # получаю информацию о пользователе для определения города
                r = requests.get('https://api.vk.com/method/users.get?user_ids=%s&fields=photo_200' % response['uid'])
                response_data = json.loads(r.text)
                user_data = response_data['response'][0]
                if 'photo_200' in user_data:
                    image_url = user_data['photo_200']
            elif backend.name == 'twitter':
                image_url = response['profile_image_url']
            elif backend.name == 'google-oauth2':
                image_url = response['picture']

            if image_url:
                user.load_photo(image_url)
        except Exception:
            pass


def social_user_referral(backend, user, is_new, request, *args, **kwargs):
    if is_new:
        user_referral(backend, user, request)


def user_referral(sender, user, request, **kwargs):
    """
    Сохранение реферрала пользователя
    """
    from main.models import ReferralUser
    if request:
        if hasattr(request, 'referral'):
            if request.referral:
                refUser = ReferralUser(referral=request.referral, user_id=user.id)
                refUser.save()

user_registered.connect(user_referral)

