# coding=utf8

from django.db import models
from datetime import datetime, timedelta
from uimg.models import UserImage, get_user_image_path
from uvideo.models import UserVideo
from uprofile.models import User
from ckeditor.fields import RichTextField
import re
import urllib2
import urllib
from django.core.files.base import ContentFile
from paysto.models import BasePayment
from main.models.promocode import Promocode
from django.db.models import Q, Sum, Count
from gutils.views import delete_template_fragment_cache
from pytils.translit import slugify
from django.shortcuts import get_object_or_404
from robokassa.signals import result_received, fail_page_visited
from mail_templated import send_mail
import string
import random
from django.utils.safestring import mark_safe
from django.conf import settings
from django.utils.functional import cached_property
from django.core.urlresolvers import reverse
from django.db.models.signals import post_delete, post_save
from django.contrib.sites.models import Site
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from decimal import Decimal
import collections
from jsonfield import JSONField
from caching.base import CachingManager, CachingMixin


def get_tel_list(tel_string):
    """
    Список телефонов из строки
    """
    join = []
    tel_list = re.split('[,;\+]|<br>', tel_string)

    if len(tel_list) == 1 and len(tel_string) > 20:
        tel_list = re.split('[\ ]', tel_string)

    for tel in tel_list:
        tel = re.sub('\D', '', tel)
        if len(tel) >= 5:
            join.append(tel)
    return join


def clear_tel_list(tel_string):
    """
    Удаление лишних символов из списка телефонов
    """
    join = get_tel_list(tel_string)
    return ', '.join(join)


def clear_tel(tel_string):
    tel = re.sub('\D', '', tel_string)
    return tel


def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class TownManager(CachingManager):
    def get_queryset(self):
        return super(TownManager, self).get_queryset().filter(site=settings.SITE_ID)


class Town(CachingMixin, models.Model):
    """
    Город
    """
    title = models.CharField('Название', max_length=255)
    title_d = models.CharField('Название (дат. падеж)', max_length=255, default='')
    latitude = models.FloatField('Широта', blank=True, null=True)
    longitude = models.FloatField('Долгота', blank=True, null=True)
    zoom = models.IntegerField('Масштаб', default=13, blank=True, null=True)
    slug = models.SlugField(default='', blank=True)
    vkid = models.IntegerField(default=0)
    site = models.ManyToManyField(Site, verbose_name='Сайты', blank=True, null=True)
    main_base = models.BooleanField('Основная база', default=True)
    vk_base = models.BooleanField('База Вконтакте', default=True)
    order = models.IntegerField('Сортировка', default=100)


    objects = TownManager()
    admin_objects = CachingManager()

    class Meta:
        verbose_name = u'Город'
        verbose_name_plural = u'Города'
        ordering = ['title']
        permissions = (
            ('view_town', 'Просмотр списка городов'),
        )

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('client:town:detail', [self.id])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Town, self).save(*args, **kwargs)

    @cached_property
    def get_metro_count(slf):
        return slf.metro_set.all().count()


class District(CachingMixin, models.Model):
    """
    Район
    """
    title = models.CharField('Название', max_length=255)
    town = models.ForeignKey('Town', verbose_name='Город')
    slug = models.SlugField(default='', blank=True)

    objects = CachingManager()

    class Meta:
        verbose_name = u'Район'
        verbose_name_plural = u'Районы'
        ordering = ['title']
        permissions = (
            ('view_district', 'Просмотр районов'),
        )

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(District, self).save(*args, **kwargs)

    @property
    def vashdom_main_url(self):
        return '/%s/rayon-%s/' % (self.town.slug, self.slug)

    @property
    def vashdom_vk_url(self):
        return '/vk/%s/rayon-%s/' % (self.town.slug, self.slug)


class Metro(CachingMixin, models.Model):
    """
    Metro
    """
    title = models.CharField('Название', max_length=255, db_index=True)
    town = models.ForeignKey(Town, verbose_name='Город')
    slug = models.SlugField(default='', blank=True)
    centr = models.BooleanField(verbose_name='Центр', default=False, blank=True)
    x = models.IntegerField(default=0, blank=True, null=True)
    y = models.IntegerField(default=0, blank=True, null=True)
    x1 = models.IntegerField(default=0, blank=True, null=True)
    y1 = models.IntegerField(default=0, blank=True, null=True)
    x2 = models.IntegerField(default=0, blank=True, null=True)
    y2 = models.IntegerField(default=0, blank=True, null=True)
    x3 = models.IntegerField(default=0, blank=True, null=True)
    y3 = models.IntegerField(default=0, blank=True, null=True)
    color = models.CharField(max_length=20, default='', blank=True, null=True, db_index=True)

    objects = CachingManager()

    class Meta:
        verbose_name = u'Метро'
        verbose_name_plural = u'Метро'
        ordering = ['title']
        permissions = (
            ('view_metro', 'Просмотр списка метро'),
        )

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Metro, self).save(*args, **kwargs)

    @staticmethod
    def from_title(town, title):
        for metro in Metro.objects.filter(town=town):
            if metro.title.lower() in title.lower():
                return metro
        return None

    @property
    def vashdom_main_url(self):
        return '/%s/metro-%s/' % (self.town.slug, self.slug)

    @property
    def vashdom_vk_url(self):
        return '/vk/%s/metro-%s/' % (self.town.slug, self.slug)


class Complain(CachingMixin, models.Model):
    """
    Жалобы пользователей
    """
    REASONS = {
        '1': u'Объявление не актуально',
        '2': u'Вымышленный объект',
        '3': u'Спам или реклама',
        '4': u'Неверная информация',
        '5': u'Неверный адрес',
        '6': u'Не дозвониться',
        '7': u'Это агент',
        '8': u'Это не объявление',
        '9': u'Неверная цена',
    }

    user = models.ForeignKey(User, verbose_name='Пользователь')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content = GenericForeignKey('content_type', 'object_id')
    reason = models.CharField('Причина', max_length=5, choices=REASONS.items(), default='')
    date = models.DateTimeField('Дата', default=datetime.now())

    objects = CachingManager()

    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы пользователей'

    def __unicode__(self):
        return unicode(self.id)

    @property
    def reason_text(self):
        if self.reason in self.REASONS:
            return self.REASONS[self.reason]
        else:
            return ''


class Advert(CachingMixin, models.Model):
    """
    Объявление
    """

    TYPE_LEASE = 'L'
    TYPE_SALE = 'S'
    TYPES = {
        TYPE_LEASE: u'Аренда',
        TYPE_SALE: u'Продажа'
    }
    TYPES_SLUG = {
        TYPE_LEASE: 'sdam',
        TYPE_SALE: 'prodam'
    }

    ESTATE_LIVE = 'F'
    ESTATE_COUNTRY = 'H'
    ESTATE_TERRITORY = 'T'
    ESTATE_COMMERCIAL = 'C'
    ESTATES = {
        ESTATE_LIVE: u'Жилая',
        ESTATE_COUNTRY: u'Загородная',
        ESTATE_TERRITORY: u'Земля',
        ESTATE_COMMERCIAL: u'Коммерческая'
    }
    ESTATES_SLUG = {
        ESTATE_LIVE: 'zhilaya_nedvizhimost',
        ESTATE_COUNTRY: 'doma_dachi_kottedzhi',
        ESTATE_TERRITORY: 'zemelnye_uchastki',
        ESTATE_COMMERCIAL: 'kommercheskaya_nedvizhimost'
    }

    NEED_SALE = 's'
    NEED_DEMAND = 'd'
    NEEDS = {
        NEED_SALE: u'Предложение',
        NEED_DEMAND: u'Спрос'
    }

    LIMIT_DAY = 'd'
    LIMIT_LONG = 'l'
    LIMITS = {
        LIMIT_DAY: u'посуточно',
        LIMIT_LONG: u'на длительный срок'
    }

    LIVE_FLAT = 'F'
    LIVE_ROOM = 'R'
    LIVES = {
        LIVE_FLAT: u'Квартира',
        LIVE_ROOM: u'Комната'
    }

    COUNTRY_HOUSE = 'H'
    COUNTRY_DACHA = 'D'
    COUNTRY_COTTAGE = 'C'
    COUNTRY_TOWNHOUSE = 'T'
    COUNTRIES = {
        COUNTRY_HOUSE: u'Дом',
        COUNTRY_DACHA: u'Дача',
        COUNTRY_COTTAGE: u'Коттедж',
        COUNTRY_TOWNHOUSE: u'Таунхаус',
    }
    COUNTRIES_SLUG = {
        COUNTRY_HOUSE: u'dom',
        COUNTRY_DACHA: u'dacha',
        COUNTRY_COTTAGE: u'kottedg',
        COUNTRY_TOWNHOUSE: u'taunhaus',
    }

    COMMERCIAL_OFFICE = 'O'
    COMMERCIAL_TRADE = 'T'
    COMMERCIAL_STORAGE = 'S'
    COMMERCIAL_PRODUCTION = 'P'
    COMMERCIAL_FREE = 'F'
    COMMERCIAL_SERVICE = 'E'
    COMMERCIALS = {
        COMMERCIAL_OFFICE: u'Офисное',
        COMMERCIAL_TRADE: u'Торговое',
        COMMERCIAL_STORAGE: u'Склад',
        COMMERCIAL_PRODUCTION: u'Производственное',
        COMMERCIAL_FREE: u'Свободное назначение',
        COMMERCIAL_SERVICE: u'Сфера услуг'
    }
    COMMERCIALS_SLUG = {
        COMMERCIAL_OFFICE: u'ofis',
        COMMERCIAL_TRADE: u'torgovoe',
        COMMERCIAL_STORAGE: u'sklad',
        COMMERCIAL_PRODUCTION: u'proizvodstvennoe',
        COMMERCIAL_FREE: u'svobodnoe',
        COMMERCIAL_SERVICE: u'sfera-uslug'
    }

    TERR_BUILD = 'B'
    TERR_FARM = 'F'
    TERR_INDUSTRIAL = 'I'
    TERRITORIES = {
        TERR_BUILD: u'Поселение ИЖС',
        TERR_FARM: u'Сельскохозяйственное',
        TERR_INDUSTRIAL: u'Промышленное',
    }
    TERRITORIES_SLUG = {
        TERR_BUILD: u'poselenie-izhs',
        TERR_FARM: u'selskohozyaistvennoe',
        TERR_INDUSTRIAL: u'promishlennoe',
    }


    STATUS_VIEW = 'v'
    STATUS_MODERATE = 'm'
    STATUS_BLOCKED = 'b'
    STATUSES = {
        STATUS_VIEW: 'Размещено',
        STATUS_MODERATE: 'На модерации',
        STATUS_BLOCKED: 'Неактуально',
    }

    ARCHIVE_YES = 'y'
    ARCHIVE_NO = 'n'
    ARCHIVE_AUTO = 'a'
    ARCHIVES = {
        ARCHIVE_YES: 'В архиве',
        ARCHIVE_NO: 'В каталоге',
        ARCHIVE_AUTO: 'Автоматически'
    }
    ARCHIVE_YES_QUERY = (Q(archive=ARCHIVE_YES) |
                      (Q(archive=ARCHIVE_AUTO) & (Q(adtype=TYPE_LEASE, date__lte=datetime.now()-timedelta(days=settings.ARCHIVE_LEASE_DAYS)) | Q(adtype=TYPE_SALE, date__lte=datetime.now()-timedelta(days=settings.ARCHIVE_SALE_DAYS)))))
    ARCHIVE_NO_QUERY = (Q(archive=ARCHIVE_NO) |
                      (Q(archive=ARCHIVE_AUTO) & (Q(adtype=TYPE_LEASE, date__gte=datetime.now()-timedelta(days=settings.ARCHIVE_LEASE_DAYS)) | Q(adtype=TYPE_SALE, date__gte=datetime.now()-timedelta(days=settings.ARCHIVE_SALE_DAYS)))))

    CHECK_SPAM_LOW = 'low'
    CHECK_SPAM_STRONG = 'strong'


    date = models.DateTimeField('Дата подачи', default=datetime.now, db_index=True)
    date_vashdom = models.DateTimeField('Дата подачи', default=datetime.now, db_index=True)
    date_smart = models.DateTimeField('Дата подачи', default=datetime.now, db_index=True)
    date_roomas = models.DateTimeField('Дата подачи', default=datetime.now, db_index=True)
    date_stopagent = models.DateTimeField('Дата подачи', default=datetime.now, db_index=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', null=True, blank=True, on_delete=models.SET_NULL)
    company = models.ForeignKey('Company', verbose_name='Агенство', null=True, blank=True)
    body = models.TextField('Описание', blank=True, null=True, default='')
    images = models.ManyToManyField(UserImage, verbose_name='Изображения', blank=True)
    adtype = models.CharField('Тип объявления', max_length=1, default=TYPE_LEASE, choices=TYPES.items(), db_index=True)
    need = models.CharField('Спрос/предложение', max_length=1, default=NEED_SALE, choices=NEEDS.items(), db_index=True)
    estate = models.CharField('Тип недвижимости', max_length=1, default=ESTATE_LIVE, choices=ESTATES.items(), db_index=True)
    live = models.CharField('Тип жилой недвижимости', max_length=1, default=LIVE_FLAT, choices=LIVES.items(), db_index=True)
    live_flat1 = models.BooleanField('1к', default=False, blank=True)
    live_flat2 = models.BooleanField('2к', default=False, blank=True)
    live_flat3 = models.BooleanField('3к', default=False, blank=True)
    live_flat4 = models.BooleanField('4к+', default=False, blank=True)
    country = models.CharField('Тип загородной недвижимости', max_length=1, default=COUNTRY_HOUSE, choices=COUNTRIES.items())
    commercial = models.CharField('Тип коммерческой недвижимости', max_length=1, default=COMMERCIAL_OFFICE, choices=COMMERCIALS.items())
    territory = models.CharField('Тип земли', max_length=1, default=TERR_BUILD, choices=TERRITORIES.items())
    limit = models.CharField('Срок', max_length=1, default=LIMIT_LONG, choices=LIMITS.items(), db_index=True)
    address = models.TextField('Адрес', max_length=255, blank=True, null=True, default='')
    town = models.ForeignKey(Town, verbose_name='Город', db_index=True)
    district = models.ForeignKey(District, verbose_name='Район', blank=True, null=True)
    metro = models.ForeignKey(Metro, verbose_name='Метро', blank=True, null=True)
    square = models.FloatField('Общая площадь', default=None, blank=True, null=True)
    square_max = models.FloatField('Общая площадь, макс', default=None, blank=True, null=True)
    living_square = models.CharField('Жилая площадь', max_length=30, blank=True, null=True)
    living_square_max = models.CharField('Жилая площадь, макс', max_length=30, blank=True, null=True)
    kitchen_square = models.FloatField('Площадь кухни', blank=True, null=True)
    kitchen_square_max = models.FloatField('Площадь кухни, макс', blank=True, null=True)
    rooms = models.IntegerField('Количество комнат', blank=True, null=True)
    price = models.FloatField('Цена', blank=True, null=True)
    min_price = models.FloatField('Цена от', blank=True, null=True)

    # удобства -----------------

    # интерьер
    refrigerator = models.BooleanField(u'Холодильник', default=False, blank=True)
    tv = models.BooleanField(u'Телевизор', default=False, blank=True)
    washer = models.BooleanField(u'Стиральная машина', default=False, blank=True)
    phone = models.BooleanField(u'Телефон', default=False, blank=True)
    internet = models.BooleanField(u'Интернет', default=False, blank=True)
    conditioner = models.BooleanField(u'Кондиционер', default=False, blank=True)
    furniture = models.BooleanField(u'Мебель', default=False, blank=True)
    separate_wc = models.BooleanField(u'Раздельный санузел', default=False, blank=True)
    balcony = models.BooleanField(u'Балкон', default=False, blank=True)
    # ремонт
    euroremont = models.BooleanField(u'Евроремонт', default=False, blank=True)
    redecoration = models.BooleanField(u'Косметический ремонт', default=False, blank=True)
    no_remont = models.BooleanField(u'Без ремонта', default=False, blank=True)
    need_remont = models.BooleanField(u'Требуется ремонт', default=False, blank=True)
    # коммуникации
    electric = models.BooleanField(u'Электричество', default=False, blank=True)
    gas = models.BooleanField(u'Газ', default=False, blank=True)
    water = models.BooleanField(u'Вода', default=False, blank=True)
    sewage = models.BooleanField(u'Канализация', default=False, blank=True)
    brick_building = models.BooleanField(u'Кирпичная постройка', default=False, blank=True)
    wood_building = models.BooleanField(u'Деревянная постройка', default=False, blank=True)
    # проживание
    live_one = models.BooleanField(u'Одному чел.', default=False, blank=True)
    live_two = models.BooleanField(u'2-м людям', default=False, blank=True)
    live_pare = models.BooleanField(u'Семейной паре', default=False, blank=True)
    live_more = models.BooleanField(u'Более 2-х чел.', default=False, blank=True)
    live_child = models.BooleanField(u'Можно с детьми', default=False, blank=True)
    live_animal = models.BooleanField(u'Можно с животными', default=False, blank=True)
    live_girl = models.BooleanField(u'Для девушек', default=False, blank=True)
    live_man = models.BooleanField(u'Для мужчин', default=False, blank=True)
    # разное
    parking = models.BooleanField(u'Парковка', default=False, blank=True)
    lift = models.BooleanField(u'Лифт', default=False, blank=True)
    concierge = models.BooleanField(u'Консьерж', default=False, blank=True)
    guard = models.BooleanField(u'Охрана', default=False, blank=True)
    garage = models.BooleanField(u'Гараж', default=False, blank=True)

    latitude = models.FloatField('Широта', blank=True, null=True)
    longitude = models.FloatField('Долгота', blank=True, null=True)

    floor = models.PositiveIntegerField('Этаж', default=None, blank=True, null=True)
    count_floor = models.PositiveIntegerField('Всего этажей', default=None, blank=True, null=True)
    floor_max = models.PositiveIntegerField('Этаж до', default=None, blank=True, null=True)

    extnum = models.CharField('Внешний код', max_length=50, default=None, null=True, blank=True, db_index=True)

    owner_name = models.CharField('ФИО собственника', max_length=250, null=True, blank=True)
    owner_tel = models.CharField('Телефон собственника', max_length=50, null=True, blank=True, db_index=True)
    owner_email = models.EmailField('E-mail собственника', null=True, blank=True)

    status = models.CharField('Статус объявления', max_length=1, default=STATUS_VIEW, choices=STATUSES.items(), db_index=True)
    archive = models.CharField('Статус архива', max_length=1, default=ARCHIVE_AUTO, choices=ARCHIVES.items(), db_index=True)
    views = models.IntegerField('Просмотры', default=0, blank=True)
    views_tel = models.IntegerField('Просмотры телефона', default=0, blank=True)

    #пользователи добавившие в избранного
    favorites = models.ManyToManyField(User, blank=True, related_name='favorites')
    #пользователи свернувшие объявление
    folded = models.ManyToManyField(User, blank=True, related_name='folded')
    #пользователи просмотревшие телефон
    viewed = models.ManyToManyField(User, blank=True, related_name='viewed', through='RegViewed', through_fields=('advert', 'user'))
    # пользователи пожаловашиеся на объявление
    complained = GenericRelation(Complain)

    #выкуп
    buy_date = models.DateTimeField(verbose_name='Дата окончания выкупа', null=True, blank=True, default=None)
    buy_users = models.ManyToManyField(User, blank=True, related_name='buy_adverts')
    buy_company = models.ManyToManyField('Company', blank=True, related_name='buy_adverts')

    #возможные клиенты объявления
    clients = models.ManyToManyField('self', blank=True)
    last_viewed_count = models.IntegerField(default=0, null=True, blank=True)

    # параметры блокировки
    blocked = models.BooleanField('Заблокировано', default=False, blank=True)
    block_date = models.DateTimeField('Время блокировки', null=True, blank=True, default=None)
    block_user = models.ForeignKey(User, verbose_name='Заблокировавший пользователь', null=True, blank=True,
                                   on_delete=models.SET_NULL, default=None, related_name='blocked_adverts')

    #модерация объявления
    moderator = models.ForeignKey(User, verbose_name='Модератор', null=True, blank=True, default=None,
                                  on_delete=models.SET_NULL, related_name='moderated')
    moderate_date = models.DateTimeField('Дата модерации', null=True, blank=True, default=None)
    not_answer = models.BooleanField('Не берет трубку', blank=True, default=False)

    # доп метро для раздела СНИМУ
    need_metro = models.ManyToManyField('Metro', blank=True, related_name='need_adverts')

    parser = models.ForeignKey('Parser', verbose_name='Парсер', null=True, blank=True, default=None, on_delete=models.SET_NULL)
    vk_imported = models.BooleanField('Импортировано VK', default=False, blank=True)
    vk_imported_bvd = models.BooleanField('Импортировано VK БазаВашДом', default=False, blank=True)
    vk_imported_stopagent = models.BooleanField('Импортировано VK Стопагент', default=False, blank=True)
    vk_imported_smart = models.BooleanField('Импортировано VK Smart', default=False, blank=True)
    user_noticed = models.ManyToManyField(User, verbose_name='Уведомления об объявлении', blank=True, related_name='advert_noticed')

    properties = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict}, default={}, blank=True, null=True)

    objects = CachingManager()

    class Meta:
        verbose_name = u'Объявление'
        verbose_name_plural = u'Объявления'
        ordering = ['-date']
        permissions = (
            ('view_all_advert', 'Просмотр всех объявлений в панели модераторов'),
            ('view_advert_moderate', 'Просмотр объявлений на модерации'),
            ('change_advert_status', 'Смена статуса объявления'),
        )

    def __unicode__(self):
        return self.title

    @property
    def title(self):
        result = ''
        if self.need == self.NEED_SALE:
            if self.estate == self.ESTATE_LIVE:
                if self.live == self.LIVE_ROOM:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сдам комнату%s' % (u' в %s-комнатной квартире' % self.rooms if self.rooms else '') + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u' на длительный срок')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Продам комнату%s' % (u' в %s-комнатной квартире' % self.rooms if self.rooms else '')
                elif self.live == self.LIVE_FLAT:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сдам %s квартиру' % (u'%s-комнатную' % self.rooms if self.rooms else '') + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u' на длительный срок')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Продам %s квартиру' % (u'%s-комнатную' % self.rooms if self.rooms else '')

            elif self.estate == self.ESTATE_TERRITORY:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Аренда земельного участка' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Продам земельный участок'

            elif self.estate == self.ESTATE_COUNTRY:
                if self.adtype == self.TYPE_LEASE:
                    if self.count_floor:
                        result = u'Сдам %s этаж. дом в аренду' % self.count_floor + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u' на длительный срок')
                    else:
                        result = u'Сдам дом в аренду' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u' на длительный срок')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Продам дом'

            elif self.estate == self.ESTATE_COMMERCIAL:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Сдам помещение в аренду' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u' на длительный срок')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Продам помещение'
        elif self.need == self.NEED_DEMAND:
            if self.estate == self.ESTATE_LIVE:
                if self.live == Advert.LIVE_ROOM:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сниму комнату' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u' на длительный срок')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Куплю комнату'
                elif self.live == Advert.LIVE_FLAT:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сниму квартиру' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u' на длительный срок')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Куплю квартиру'

                    flat_array = []
                    if self.live_flat1:
                        flat_array.append('1')
                    if self.live_flat2:
                        flat_array.append('2')
                    if self.live_flat3:
                        flat_array.append('3')
                    if self.live_flat4:
                        flat_array.append('4')
                    result += u' (%s комн.)' % u','.join(flat_array)

            elif self.estate == self.ESTATE_TERRITORY:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Арендую земельный участок'
                elif self.adtype == self.TYPE_SALE:
                    result = u'Куплю земельный участок'

            elif self.estate == self.ESTATE_COUNTRY:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Возьму дом в аренду' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Куплю дом'

            elif self.estate == self.ESTATE_COMMERCIAL:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Возьму помещение в аренду' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Куплю помещение'

        return result

    @property
    def short_title(self):
        result = ''
        if self.need == self.NEED_SALE:
            if self.estate == self.ESTATE_LIVE:
                if self.live == self.LIVE_ROOM:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сдам комн.' + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Продам комн.'
                elif self.live == self.LIVE_FLAT:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сдам' + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Продам'
                    if self.rooms:
                        result += u' %s комн.кв.' % self.rooms
                    else:
                        result += u' кв.'

            elif self.estate == self.ESTATE_TERRITORY:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Сдам зем.участок' + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Продам зем.участок'

            elif self.estate == self.ESTATE_COUNTRY:
                if self.adtype == self.TYPE_LEASE:
                    if self.count_floor:
                        result = u'Сдам %s этаж. дом' % self.count_floor + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                    else:
                        result = u'Сдам дом' + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Продам дом'

            elif self.estate == self.ESTATE_COMMERCIAL:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Сдам помещение' + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Продам помещение'
        elif self.need == self.NEED_DEMAND:
            if self.estate == self.ESTATE_LIVE:
                if self.live == Advert.LIVE_ROOM:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сниму комн.' + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Куплю комн.'
                elif self.live == Advert.LIVE_FLAT:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сниму кв.' + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Куплю кв.'
                    flat_array = []
                    if self.live_flat1:
                        flat_array.append('1')
                    if self.live_flat2:
                        flat_array.append('2')
                    if self.live_flat3:
                        flat_array.append('3')
                    if self.live_flat4:
                        flat_array.append('4')
                    result += u' (%s комн.)' % u','.join(flat_array)

            elif self.estate == self.ESTATE_TERRITORY:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Арендую участок'
                elif self.adtype == self.TYPE_SALE:
                    result = u'Куплю участок'

            elif self.estate == self.ESTATE_COUNTRY:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Возьму дом в аренду' + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Куплю дом'

            elif self.estate == self.ESTATE_COMMERCIAL:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Возьму помещение в аренду' + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Куплю помещение'

        return result

    @property
    def page_title(self):

        def action():
            """
            Операция с недвижимостью
            """
            result = u''
            if self.need == self.NEED_SALE:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Сдам'
                elif self.adtype == self.TYPE_SALE:
                    result = u'Продам'

            elif self.need == self.NEED_DEMAND:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Снять'
                elif self.adtype == self.TYPE_SALE:
                    result = u'Купить'
            return result

        def obj():
            result = u''
            if self.estate == Advert.ESTATE_LIVE:
                if self.live == Advert.LIVE_ROOM:
                    result = u'комнату'
                else:
                    result = u'квартиру'
            elif self.estate == Advert.ESTATE_COUNTRY:
                result = Advert.COUNTRIES[self.country].lower()
            elif self.estate == Advert.ESTATE_COMMERCIAL:
                result = Advert.COMMERCIALS[self.commercial].lower() + u' помещение'
            elif self.estate == Advert.ESTATE_TERRITORY:
                result = Advert.TERRITORIES[self.territory].lower()
            return result

        def town_name():
            return self.town.title

        def metro_name():
            if self.metro:
                return u'метро ' + self.metro.title
            else:
                return u''

        def address_text():
            if self.address:
                return self.address.strip().replace(u'.', u'').replace(u',', u'')
            else:
                return ''

        def limit_text():
            if self.estate in [Advert.ESTATE_LIVE, Advert.ESTATE_COUNTRY] and self.adtype == Advert.TYPE_LEASE:
                if self.limit == Advert.LIMIT_DAY:
                    return u'посуточно'
                else:
                    return u'на длительный срок'
            return u''

        def room_text():
            if (self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT):
                if self.rooms:
                    return u'%s комнатную' % self.rooms
            elif self.estate == Advert.ESTATE_COUNTRY:
                if self.rooms:
                    return u'%s комнатный' % self.rooms
            return u''

        def floor_text():
            if self.estate == Advert.ESTATE_COUNTRY and self.count_floor:
                return u'%s этаж' % self.count_floor
            return u''

        def square_text():
            if self.estate in [Advert.ESTATE_COMMERCIAL, Advert.ESTATE_TERRITORY]:
                if self.square:
                    return u'%.0f м2' % self.square
            return u''

        result = u' '.join([action(), room_text(), floor_text(), obj(), limit_text(), square_text(), town_name(), metro_name(), address_text()])
        return result

    @property
    def metatag(self):

        def action():
            """
            Операция с недвижимостью
            """
            result = u''
            if self.need == self.NEED_SALE:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Сдать'
                elif self.adtype == self.TYPE_SALE:
                    result = u'Продать'

            elif self.need == self.NEED_DEMAND:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Снять'
                elif self.adtype == self.TYPE_SALE:
                    result = u'Купить'
            return result

        def obj():
            result = u''
            if self.estate == Advert.ESTATE_LIVE:
                result = Advert.LIVES[self.live].lower()
            elif self.estate == Advert.ESTATE_COUNTRY:
                result = Advert.COUNTRIES[self.country].lower()
            elif self.estate == Advert.ESTATE_COMMERCIAL:
                result = Advert.COMMERCIALS[self.commercial].lower() + u' помещение'
            elif self.estate == Advert.ESTATE_TERRITORY:
                result = Advert.TERRITORIES[self.territory].lower()
            return result

        def room_text():
            if (self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT) or \
                    (self.estate == Advert.ESTATE_COUNTRY):
                if self.need == Advert.NEED_SALE:
                    if self.rooms:
                        return u'%s комнатная' % self.rooms
                elif self.need == Advert.NEED_DEMAND:
                    flat_array = []
                    if self.live_flat1:
                        flat_array.append(1)
                    if self.live_flat2:
                        flat_array.append(2)
                    if self.live_flat3:
                        flat_array.append(3)
                    if self.live_flat4:
                        flat_array.append(4)
                    return u'%s комнатная' % ','.join(flat_array)
            return u''

        def metro_name():
            if self.metro:
                return u'метро ' + self.metro.title
            else:
                return u''

        def town_name():
            t = u''
            if self.town_id == 1:
                t = u'москве'
            elif self.town_id == 1:
                t = u'санкт-петербурге'
            return u'в %s' % t

        def limit_text():
            if self.estate in [Advert.ESTATE_LIVE, Advert.ESTATE_COUNTRY] and self.adtype == Advert.TYPE_LEASE:
                if self.limit == Advert.LIMIT_DAY:
                    return u'посуточно'
                else:
                    return u'длительно'
            return u''

        def address_text():
            if self.address:
                return self.address.strip().replace(u',', '')
            else:
                return ''

        def company_text():
            if self.company:
                return self.company.title
            return ''

        def owner_tags():
            return u'Собственник, от собстенника, Без комиссии, Без агентов, База собственников'

        def company_tags():
            return u'Комиссия, Агентство недвижимости'

        def flat_tags():
            return u'База квартир'

        def sale_tags():
            return u'объявления продажа, объявления продаю'

        def lease_tags():
            return u'объявления аренда, объявления сдам'

        result = [
            u' '.join([action(), obj()]),
            u' '.join([action(), obj(), town_name()]),
            (u' '.join([action(), obj(), limit_text()]) if self.estate in [Advert.ESTATE_LIVE, Advert.ESTATE_COUNTRY] and self.adtype == Advert.TYPE_LEASE else u''),
            (u' '.join([room_text(), obj()]) if self.estate == Advert.ESTATE_LIVE and self.live==Advert.LIVE_FLAT else u''),
            metro_name(),
            address_text(),
            company_text(),
            (company_tags() if self.company else owner_tags()),
            (flat_tags() if self.estate==Advert.ESTATE_LIVE and self.live==Advert.LIVE_FLAT else u''),
            (sale_tags() if self.adtype==Advert.TYPE_SALE else u''),
            (lease_tags() if self.adtype==Advert.TYPE_LEASE else u''),
            u'База недвижимость, Объявления, бесплатные объявления, частные объявления, доска объявлений, бесплатные доски, дать объявление, бесплатные доски объявлений, сайт объявления',
        ]
        return u', '.join(result)

    def get_absolute_url(self):
        url = [self.town.slug]
        if self.estate:
            url.append(Advert.ESTATES_SLUG[self.estate])
        url.append(Advert.TYPES_SLUG[self.adtype])
        prefix = []
        if self.estate == Advert.ESTATE_LIVE:
            if self.live == Advert.LIVE_ROOM:
                prefix.append('komnata')
            elif self.live == Advert.LIVE_FLAT:
                if self.rooms:
                    prefix.append('%s_komnatnaya_kvartira' % self.rooms)
                else:
                    prefix.append('kvartira')
        elif self.estate == Advert.ESTATE_COUNTRY:
            if self.country:
                prefix.append(Advert.COUNTRIES_SLUG[self.country])
            else:
                prefix.append(Advert.ESTATES_SLUG[self.estate])
        elif self.estate == Advert.ESTATE_TERRITORY:
            if self.territory:
                prefix.append(Advert.TERRITORIES_SLUG[self.territory])
            else:
                prefix.append(Advert.ESTATES_SLUG[self.estate])
        elif self.estate == Advert.ESTATE_COMMERCIAL:
            if self.commercial:
                prefix.append(Advert.COMMERCIALS_SLUG[self.commercial])
            else:
                prefix.append(Advert.ESTATES_SLUG[self.estate])
        return '/%s/%s/id%s' % ('/'.join(url), '_'.join(prefix), self.id)

    @property
    def comfort_list(self):
        result = []
        for field in ['refrigerator',
                      'washer',
                      'tv',
                      'phone',
                      'internet',
                      'conditioner',
                      'furniture',
                      'euroremont',
                      'separate_wc',
                      'balcony',
                      'lift',
                      'parking',
                      'redecoration',
                      'no_remont',
                      'need_remont',
                      'electric',
                      'gas',
                      'water',
                      'sewage',
                      'brick_building',
                      'wood_building',
                      'live_one',
                      'live_two',
                      'live_pare',
                      'live_more',
                      'live_child',
                      'live_animal',
                      'live_girl',
                      'live_man',
                      'concierge',
                      'guard',
                      'garage']:
            result.append((field,
                           getattr(self, field),
                           self._meta.get_field(field).verbose_name
            ))
        return result

    @property
    def is_buyed(self):
        if self.buy_date:
            return datetime.now() < self.buy_date
        else:
            return False

    def find_clients(self):
        query = Q(town=self.town,
                  estate=self.estate,
                  adtype=self.adtype,
                  date__gte=datetime.now() - timedelta(days=7),
                  status=Advert.STATUS_VIEW)
        query &= Advert.ARCHIVE_NO_QUERY
        if self.estate == Advert.ESTATE_LIVE:
            query &= Q(live=self.live, limit=self.limit)
        elif self.estate == Advert.ESTATE_COUNTRY:
            query &= Q(country=self.country, limit=self.limit)
        elif self.estate == Advert.ESTATE_COMMERCIAL:
            query &= Q(commercial=self.commercial)
        elif self.estate == Advert.ESTATE_TERRITORY:
            query &= Q(territory=self.territory)

        if self.metro:
            query &= Q(metro__in=[self.metro] + [metro for metro in self.need_metro.all()]) | Q(need_metro__id=self.metro.id)
        if self.district:
            query &= (Q(district=self.district) | Q(district__isnull=True))
        # if self.price and self.min_price:
        #     query &= Q(price__gte=self.min_price, price__lte=self.price)
        # elif self.price:
        #     query &= Q(price__gte=self.price-1000, price__lte=self.price+1000)

        if self.need == Advert.NEED_DEMAND:
            if self.price:
                query &= Q(price__lte=self.price)
            if self.min_price:
                query &= Q(price__gte=self.min_price)
            if self.floor:
                query &= Q(floor__gte=self.floor)
            if self.floor_max:
                query &= Q(floor__lte=self.floor_max)
            if self.square:
                query &= Q(square__gte=self.square)
            if self.square_max:
                query &= Q(square__lte=self.square_max)
            if self.kitchen_square:
                query &= Q(kitchen_square__gte=self.kitchen_square)
            if self.kitchen_square_max:
                query &= Q(kitchen_square__lte=self.kitchen_square_max)
            if self.estate == Advert.ESTATE_LIVE:
                if self.live == Advert.LIVE_FLAT:
                    flat_array = []
                    if self.live_flat1:
                        flat_array.append(1)
                    if self.live_flat2:
                        flat_array.append(2)
                    if self.live_flat3:
                        flat_array.append(3)
                    if self.live_flat4:
                        flat_array.append(4)
                        flat_array.append(5)
                        flat_array.append(6)
                    if flat_array:
                        query &= Q(rooms__in=flat_array)
        elif self.need == Advert.NEED_SALE:
            if self.price:
                query &= (Q(min_price__lte=self.price) | Q(min_price__isnull=True))
                query &= (Q(price__gte=self.price) | Q(price__isnull=True))
            if self.floor:
                query &= (Q(floor__lte=self.floor) | Q(floor__isnull=True))
                query &= (Q(floor_max__gte=self.floor) | Q(floor_max__isnull=True))
            if self.square:
                query &= (Q(square__lte=self.square) | Q(square__isnull=True))
                query &= (Q(square_max__gte=self.square) | Q(square_max__isnull=True))
            if self.kitchen_square:
                query &= (Q(kitchen_square__lte=self.kitchen_square) | Q(kitchen_square__isnull=True))
                query &= (Q(kitchen_square_max__gte=self.kitchen_square) | Q(kitchen_square_max__isnull=True))
            if self.estate == Advert.ESTATE_LIVE:
                if self.live == Advert.LIVE_FLAT and self.rooms:
                    rooms_query = Q()
                    if self.rooms == 1:
                        rooms_query = Q(live_flat1=True)
                    if self.rooms == 2:
                        rooms_query = Q(live_flat2=True)
                    if self.rooms == 3:
                        rooms_query = Q(live_flat3=True)
                    if self.rooms >= 4:
                        rooms_query = Q(live_flat4=True)
                    rooms_query |= Q(live_flat1=False, live_flat2=False, live_flat3=False, live_flat4=False)
                    query &= rooms_query

        exists_clients_id = [advert.id for advert in self.clients.all()]
        self.clients.clear()

        if self.need == Advert.NEED_SALE:
            client_list = Advert.objects.filter(query & Q(need=Advert.NEED_DEMAND)).order_by('-date')
        else:
            client_list = Advert.objects.filter(query & Q(need=Advert.NEED_SALE)).order_by('-date')
        for advert in client_list:
            self.clients.add(advert)
            advert.clear_cache()
        self.save()
        self.clear_cache()

        # if not settings.DEBUG:
        #     self.send_client_notice()

        self.find_search_request()
        return len(client_list)

    def find_search_request(self):
        if self.status == Advert.STATUS_VIEW:
            query = Q(town=self.town,
                      estate=self.estate,
                      adtype=self.adtype,
                      active=True,
                      )
            query &= ~Q(user__status=User.STATUS_BLOCK)

            delta = datetime.now() - self.date
            query &= Q(period__gte=delta.days)

            if self.estate == Advert.ESTATE_LIVE:
                query &= Q(live=self.live, limit=self.limit)
                if self.live == Advert.LIVE_FLAT:
                    if self.rooms == 1:
                        query &= Q(live_flat1=True)
                    if self.rooms == 2:
                        query &= Q(live_flat2=True)
                    if self.rooms == 3:
                        query &= Q(live_flat3=True)
                    if self.rooms >= 4:
                        query &= Q(live_flat4=True)

            elif self.estate == Advert.ESTATE_COUNTRY:
                query &= Q(country=self.country, limit=self.limit)
            elif self.estate == Advert.ESTATE_COMMERCIAL:
                query &= Q(commercial=self.commercial)
            elif self.estate == Advert.ESTATE_TERRITORY:
                query &= Q(territory=self.territory)

            if self.metro:
                query &= (Q(metro=self.metro) | Q(metro__isnull=True))
            else:
                query &= Q(metro__isnull=True)

            if self.district:
                query &= (Q(district=self.district) | Q(district__isnull=True))
            else:
                query &= Q(district__isnull=True)

            if self.price:
                query &= (Q(price__gte=self.price) | Q(price__isnull=True))
                query &= (Q(min_price__lte=self.price) | Q(min_price__isnull=True))
            else:
                query &= Q(price__isnull=True)
                query &= Q(min_price__isnull=True)

            if self.need == Advert.NEED_SALE:
                query &= Q(need=Advert.NEED_DEMAND)
            else:
                query &= Q(need=Advert.NEED_SALE)

            if self.floor:
                query &= (Q(floor__lte=self.floor) | Q(floor__isnull=True))
                query &= (Q(floor_max__gte=self.floor) | Q(floor_max__isnull=True))
            else:
                query &= Q(floor__isnull=True, floor_max__isnull=True)

            if self.square:
                query &= (Q(square__lte=self.square) | Q(square__isnull=True))
                query &= (Q(square_max__gte=self.square) | Q(square_max__isnull=True))
            else:
                query &= Q(square__isnull=True, square_max__isnull=True)

            # if self.living_square:
            #     query &= (Q(living_square__lte=self.living_square) | Q())
            #     query &= (Q(living_square_max__gte=self.living_square) | Q())
            # else:
            #     query &= Q(living_square__isnull=True, living_square_max__isnull=True)

            if self.kitchen_square:
                query &= (Q(kitchen_square__lte=self.kitchen_square) | Q(kitchen_square__isnull=True))
                query &= (Q(kitchen_square_max__gte=self.kitchen_square) | Q(kitchen_square_max__isnull=True))
            else:
                query &= Q(kitchen_square__isnull=True, kitchen_square_max__isnull=True)

            if self.company:
                query &= Q(from_agent=True)
            else:
                query &= Q(from_owner=True)

            for comfort in self.comfort_list:
                kwargs = {comfort[0]: comfort[1]}
                kwargs1 = {comfort[0]: False}
                query &= (Q(**kwargs) | Q(**kwargs1))

            if self.town.slug == 'moskva':
                if self.live == Advert.LIVE_ROOM and (self.price < 12000 or self.price >= 35000):
                    query &= ~Q(site__domain='bazavashdom.ru')
                if self.live == Advert.LIVE_FLAT and self.rooms == 1 and (self.price < 25000 or self.price >= 45000):
                    query &= ~Q(site__domain='bazavashdom.ru')
                if self.live == Advert.LIVE_FLAT and self.rooms == 2 and (self.price < 30000 or self.price >= 82000):
                    query &= ~Q(site__domain='bazavashdom.ru')
                if self.live == Advert.LIVE_FLAT and self.rooms == 3 and (self.price < 40000 or self.price >= 92000):
                    query &= ~Q(site__domain='bazavashdom.ru')
                if self.live == Advert.LIVE_FLAT and self.rooms >= 4 and (self.price < 45000 or self.price >= 100000):
                    query &= ~Q(site__domain='bazavashdom.ru')
            elif self.town.slug == 'sankt-peterburg':
                if self.live == Advert.LIVE_ROOM and (self.price < 7000 or self.price >= 20000):
                    query &= ~Q(site__domain='bazavashdom.ru')
                if self.live == Advert.LIVE_FLAT and self.rooms == 1 and (self.price < 14000 or self.price >= 39000):
                    query &= ~Q(site__domain='bazavashdom.ru')
                if self.live == Advert.LIVE_FLAT and self.rooms == 2 and (self.price < 18000 or self.price >= 45000):
                    query &= ~Q(site__domain='bazavashdom.ru')
                if self.live == Advert.LIVE_FLAT and self.rooms == 3 and (self.price < 18000 or self.price >= 49000):
                    query &= ~Q(site__domain='bazavashdom.ru')
                if self.live == Advert.LIVE_FLAT and self.rooms >= 4 and (self.price < 20000 or self.price >= 80000):
                    query &= ~Q(site__domain='bazavashdom.ru')
            elif self.town.slug == 'novosibirsk':
                if self.live == Advert.LIVE_ROOM and (self.price < 7000 or self.price >= 11000):
                    query &= ~Q(site__domain='bazavashdom.ru')
                if self.live == Advert.LIVE_FLAT and self.rooms == 1 and (self.price < 12000 or self.price >= 21000):
                    query &= ~Q(site__domain='bazavashdom.ru')
                if self.live == Advert.LIVE_FLAT and self.rooms == 2 and (self.price < 15000 or self.price >= 25000):
                    query &= ~Q(site__domain='bazavashdom.ru')
                if self.live == Advert.LIVE_FLAT and self.rooms == 3 and (self.price < 17000 or self.price >= 33000):
                    query &= ~Q(site__domain='bazavashdom.ru')
                if self.live == Advert.LIVE_FLAT and self.rooms >= 4 and (self.price < 18000 or self.price >= 35000):
                    query &= ~Q(site__domain='bazavashdom.ru')
            elif self.town.slug == 'ekaterinburg':
                if self.live == Advert.LIVE_ROOM and (self.price < 7000 or self.price >= 11000):
                    query &= ~Q(site__domain='bazavashdom.ru')
                if self.live == Advert.LIVE_FLAT and self.rooms == 1 and (self.price < 9000 or self.price >= 21000):
                    query &= ~Q(site__domain='bazavashdom.ru')
                if self.live == Advert.LIVE_FLAT and self.rooms == 2 and (self.price < 12000 or self.price >= 25000):
                    query &= ~Q(site__domain='bazavashdom.ru')
                if self.live == Advert.LIVE_FLAT and self.rooms == 3 and (self.price < 17000 or self.price >= 33000):
                    query &= ~Q(site__domain='bazavashdom.ru')
                if self.live == Advert.LIVE_FLAT and self.rooms >= 4 and (self.price < 18000 or self.price >= 35000):
                    query &= ~Q(site__domain='bazavashdom.ru')

            self.searchrequest_set.clear()
            request_list = SearchRequest.objects.filter(query)
            for sr in request_list:
                if sr.clients.filter(date__gte=datetime.now()-timedelta(days=1)).count() <= settings.SEARCH_REQUEST_COUNT_LIMIT:
                    self.searchrequest_set.add(sr)
                    sr.clear_cache()
                    if not settings.DEBUG:
                        notice_func = SearchRequest.get_site_notice_func()[sr.site_id]
                        notice_func.apply_async(kwargs={'id': sr.id}, countdown=900)
            return len(request_list)

    # def send_client_notice(self):
    #     from django.core import mail
    #     connection = mail.get_connection(host=settings.SECONDARY_EMAIL_HOST,
    #                                          port=settings.SECONDARY_EMAIL_PORT,
    #                                          username=settings.SECONDARY_EMAIL_USERNAME,
    #                                          password=settings.SECONDARY_EMAIL_PASSWORD,
    #                                          use_tls=True)
    #     subscribe = Subscribe.objects.get(code='clients')
    #     advert_list = self.clients.all()
    #     for advert in advert_list:
    #         if advert.company:
    #             if advert.user.status != User.STATUS_BLOCK:
    #                 if advert.user.email or advert.user.agent_email:
    #                     if (not self.user_noticed.filter(id=advert.user_id).count()) and (subscribe.unsubscribed.filter(id=advert.user_id).count()==0):
    #                         send_mail('main/email/advert-notice.html', {
    #                             'client_user': advert.user,
    #                             'advert': advert,
    #                             'client_advert': self,
    #                             'subject': 'У вашего объявления №%s на сайте появился потенциальный клиент' % self.id,
    #                             'unsubscribe_code': Subscribe.get_unsubscribe_code('clients', advert.user)
    #                             },
    #                                   recipient_list=[advert.user.email if advert.user.email else advert.user.agent_email],
    #                                   fail_silently=True,
    #                                   from_email='<noreply@bazavashdom.ru>',
    #                                   connection=connection)
    #                         self.user_noticed.add(advert.user)

    @cached_property
    def count_clients(self):
        return self.clients.count()

    @cached_property
    def count_clients_owner(self):
        return self.clients.filter(company=None).count()

    @cached_property
    def count_clients_company(self):
        return self.clients.exclude(company=None).count()

    @cached_property
    def count_complains(self):
        return self.complained.all().count()

    @property
    def last_add_client_count(self):
        return self.count_clients - self.last_viewed_count

    def clear_cache(self):
        delete_template_fragment_cache('catalog_preview', unicode(self.id))
        delete_template_fragment_cache('catalog_preview_vert', unicode(self.id))
        delete_template_fragment_cache('catalog_preview_client', unicode(self.id), unicode(False))
        delete_template_fragment_cache('catalog_preview_client', unicode(self.id), unicode(True))
        delete_template_fragment_cache('catalog_preview_agent24', unicode(self.id))
        delete_template_fragment_cache('catalog_preview_client_clients_count', unicode(self.id))

        delete_template_fragment_cache('vashdom_catalog_preview', unicode(self.id))
        delete_template_fragment_cache('vashdom_vkcatalog_preview', unicode(self.id))
        delete_template_fragment_cache('vashdom_catalog_detail', unicode(self.id))
        delete_template_fragment_cache('vashdom_vkcatalog_detail', unicode(self.id))

    def clear_user_cache(self, user):
        delete_template_fragment_cache('catalog_preview_tel', unicode(self.id), unicode(user.id))

    @staticmethod
    def get_catalog_url(args=[]):
        params = args.copy()
        parts = []
        if 'town' in params:
            town = get_object_or_404(Town, id=params['town'])
            parts.append(town.slug)
            del params['town']

            if params.get('estate', '') in Advert.ESTATES_SLUG:
                parts.append(Advert.ESTATES_SLUG[params['estate']])

                exists_type = False
                if params.get('type', '') in Advert.TYPES:
                    parts.append(Advert.TYPES_SLUG[params['type']])
                    del params['type']
                    exists_type = True

                if params.get('type', '') == 'LP':
                    parts.append('sdam-posutochno')
                    del params['type']
                    exists_type = True

                if exists_type:
                    if params['estate'] == Advert.ESTATE_LIVE:
                        if 'rooms' in params:
                            if len(params['rooms']) == 1:
                                if params['rooms'] == 'R':
                                    parts.append('komnata')
                                else:
                                    parts.append('%s-komnatnaya-kvartira' % params['rooms'])
                                del params['rooms']
                    elif params['estate'] == Advert.ESTATE_COUNTRY:
                        if 'country' in params:
                            if len(params['country']) == 1:
                                if params['country'] in Advert.COUNTRIES:
                                    parts.append(Advert.COUNTRIES_SLUG[params['country']])
                                    del params['country']
                    elif params['estate'] == Advert.ESTATE_COMMERCIAL:
                        if 'commercial' in params:
                            if len(params['commercial']) == 1:
                                if params['commercial'] in Advert.COMMERCIALS:
                                    parts.append(Advert.COMMERCIALS_SLUG[params['commercial']])
                                    del params['commercial']
                    elif params['estate'] == Advert.ESTATE_TERRITORY:
                        if 'territory' in params:
                            if len(params['territory']) == 1:
                                if params['territory'] in Advert.TERRITORIES:
                                    parts.append(Advert.TERRITORIES_SLUG[params['territory']])
                                    del params['territory']

                if exists_type:
                    if ('metro' in params) and (not isinstance(params.get('metro'), list)) and params['estate'] in [Advert.ESTATE_LIVE, Advert.ESTATE_TERRITORY, Advert.ESTATE_COMMERCIAL]:
                        metro_list = Metro.objects.filter(id=params['metro'])
                        if metro_list:
                            parts.append('metro-' + metro_list[0].slug)
                            del params['metro']
                    if 'district' in params and params['estate'] in [Advert.ESTATE_COUNTRY]:
                        district_list = District.objects.filter(id=params['district'])
                        if district_list:
                            parts.append('rayon-' + district_list[0].slug)
                            del params['district']

                del params['estate']


        if len(parts) <= 2:
            parts.append('nedvizhimost')

        get_params = []
        for key, value in params.iteritems():
            if isinstance(value, list):
                for v in value:
                    get_params.append((key, v))
            else:
                get_params.append((key, value))

        return '/' + ('/'.join(parts)) + '/' + ('?' if len(get_params) else '') + urllib.urlencode(get_params)

    @staticmethod
    def get_catalog_title(args, request):
        def action():
            """
            Операция с недвижимостью
            """
            result = u''
            if 'type' in args:
                if args['type'] == Advert.TYPE_LEASE:
                    result = u'Аренда'
                elif args['type'] == Advert.TYPE_SALE:
                    result = u'Продажа'
                elif args['type'] == 'LP':
                    result = u'Аренда'
            else:
                return u'Объявления'
            return result

        def limit():
            """
            Срок
            """
            result = u''
            if 'type' in args:
                if args['type'] == Advert.TYPE_LEASE:
                    result = u' длительно'
                elif args['type'] == Advert.TYPE_SALE:
                    result = u''
                elif args['type'] == 'LP':
                    result = u' посуточно'
            else:
                return u''
            return result

        def obj():
            result = u' недвижимости'
            if 'estate' in args:
                if args['estate'] == Advert.ESTATE_LIVE:
                    if 'rooms' in args:
                        if args['rooms'] == 'R':
                            result = u'комната'
                        else:
                            result = u'%s комнатная квартира' % args['rooms']
                    else:
                        result = Advert.ESTATES[args['estate']].lower() + u' недвижимость'
                elif args['estate'] == Advert.ESTATE_COUNTRY:
                    if 'country' in args:
                        result = Advert.COUNTRIES[args['country']]
                    else:
                        result = Advert.ESTATES[args['estate']].lower() + u' недвижимость'
                elif args['estate'] == Advert.ESTATE_COMMERCIAL:
                    if 'commercial' in args:
                        result = Advert.COMMERCIALS[args['commercial']].lower() + u' нежилое помещение'
                    else:
                        result = Advert.ESTATES[args['estate']].lower() + u' недвижимость'
                elif args['estate'] == Advert.ESTATE_TERRITORY:
                    if 'territory' in args:
                        result = Advert.TERRITORIES[args['territory']].lower()
                    else:
                        result = Advert.ESTATES[args['estate']].lower()
            return result

        def town_name():
            if 'town' in args:
                town = Town.objects.get(id=args['town'])
                return u'в г ' + town.title
            return ''

        def metro_name():
            metro_id = None
            if 'metro' in args:
                metro_id = args['metro']
            if request.GET.get('metro', None):
                metro_id = request.GET.get('metro')
            if metro_id:
                metro_list = Metro.objects.filter(id=metro_id)
                if metro_list:
                    return u'у метро %s' % metro_list[0].title
            return ''

        def district_name():
            district_id = None
            if 'district' in args:
                district_id = args['district']
            if request.GET.get('district', None):
                district_id = request.GET.get('district')
            if district_id:
                try:
                    district_list = District.objects.filter(id=district_id)
                    if district_list:
                        return u'в районе %s' % district_list[0].title
                except:
                    pass
            return ''

        result = u' '.join([action(), obj(), limit(), town_name(), metro_name(), district_name()])
        return result

    def dict2xml(self, doc, parent, d):
        for key, value in d.iteritems():
            node = doc.createElement(key)
            if isinstance(value, dict):
                self.dict2xml(doc, node, value)
            elif isinstance(value, list):
                for el in value:
                    nodeList = doc.createElement('element')
                    textnode = doc.createTextNode(unicode(el))
                    nodeList.appendChild(textnode)
                    node.appendChild(nodeList)
            else:
                textnode = doc.createTextNode(unicode(value))
                node.appendChild(textnode)
            parent.appendChild(node)

    def to_xml(self):
        from xml.dom import minidom

        impl = minidom.getDOMImplementation()
        doc = impl.createDocument(None, 'advert', None)

        self.dict2xml(doc, doc.documentElement, self.to_dict())

        return doc.toxml(encoding='utf8')

    def to_dict(self):
        fields = ['id',
                'date',
                  'body',
                  'live',
                  'rooms',
                  'address',
                  'town',
                  'district',
                  'metro',
                  'square',
                  'living_square',
                  'kitchen_square',
                  'price',
                  'refrigerator',
                  'tv',
                  'washer',
                  'furniture',
                  'latitude',
                  'longitude',
                  'floor',
                  'count_floor',
                  'owner_name',
                  'owner_tel',
                  ]

        result = {}
        for field in fields:
            if not getattr(self, field) is None:
                result[field] = getattr(self, field)
        result['live'] = u'room' if self.live == Advert.LIVE_ROOM else u'flat'
        result['date'] = self.date.strftime("%d-%m-%Y %H:%M")
        result['body'] = self.generate_client_description()
        result['base'] = u'main'
        result['images'] = []
        site = Site.objects.get_current()
        for image in self.images.all():
            result['images'].append(u'http://%s%s' % (site.domain, image.image.url))
        return result

    def publish(self):
        pass

    def delete(self, using=None):
        if self.extnum:
            Advert.objects.filter(extnum=self.extnum).exclude(id=self.id).delete()
        return super(Advert, self).delete(using=using)

    def __setattr__(self, key, value):
        super(Advert, self).__setattr__(key, value)
        if key == 'date':
            self.date_vashdom = self.date + timedelta(minutes=random.randrange(5, 30), seconds=random.randrange(1, 50))
            self.date_smart = self.date + timedelta(minutes=random.randrange(5, 30), seconds=random.randrange(1, 50))
            self.date_roomas = self.date + timedelta(minutes=random.randrange(5, 30), seconds=random.randrange(1, 50))
            self.date_stopagent = self.date + timedelta(minutes=random.randrange(5, 60), seconds=random.randrange(1, 50))

    @staticmethod
    def get_duplicates(adtype, estate, need, exclude_id=None, metro=None, tel=None, level=CHECK_SPAM_LOW):
        """
        Поиск дубликатов среди опубликованных объявлений
        """
        query = Q(owner_tel=tel)
        if level == Advert.CHECK_SPAM_LOW:
            query &= Q(date__gte=datetime.now() - timedelta(days=2))
        elif level == Advert.CHECK_SPAM_STRONG:
            query &= Q(date__gte=datetime.now() - timedelta(days=30))
        query &= ~Q(status=Advert.STATUS_BLOCKED)
        return Advert.objects.filter(query)\
            .exclude(id=exclude_id if exclude_id else 0)

    @staticmethod
    def get_owner_live_spam(adtype, estate, need, exclude_id=None, metro=None, tel=None, exclude_live=None):
        """
        Поиск повторения объявления от собственника
        """
        return Advert.objects.filter(owner_tel=tel,
                                     estate=estate,
                                     adtype=adtype,
                                     need=need,
                                     date__gte=datetime.now() - timedelta(days=1)) \
            .exclude(id=exclude_id if exclude_id else 0)\
            .exclude(live=exclude_live)\
            .exclude(metro=metro)

    def check_spam(self, actions=False, level=CHECK_SPAM_LOW):
        # проверка по черному списку
        result = Blacklist.check_tel(self.owner_tel)
        if result:
            return result

        # проверка на мошеннический спам
        spam_query = Q(owner_tel=self.owner_tel,
                       estate=self.estate,
                       adtype=self.adtype,
                       need=self.need,
                       )

        if (level == Advert.CHECK_SPAM_LOW):
            spam_query &= Q(date__gte=datetime.now() - timedelta(days=2))
        elif (level == Advert.CHECK_SPAM_STRONG):
            spam_query &= Q(date__gte=datetime.now() - timedelta(days=30))

        spam_query &= ~Q(metro=self.metro)
        if self.id:
            spam_query &= ~Q(id=self.id)
        if (self.estate == Advert.ESTATE_LIVE) and (self.live == Advert.LIVE_FLAT):
            spam_query &= (~Q(live=self.live) | ~Q(rooms=self.rooms))
        if (self.estate == Advert.ESTATE_LIVE) and (self.live == Advert.LIVE_ROOM):
            spam_query &= ~Q(live=self.live)

        spam_list = Advert.objects.filter(spam_query)
        if spam_list:
            msg = [u'найден спам от собственника №%s тел %s' % (spam_list[0].id, spam_list[0].owner_tel)]
            if actions:
                ids = [str(advert.id) for advert in spam_list]
                Blacklist.add_tel(self.owner_tel, 'Определен как спамер объявлений ' + (', '.join(ids)))
                msg.append(u'Телефон %s добавлен в черный список' % self.owner_tel)
                Advert.objects.filter(owner_tel=self.owner_tel).update(status=Advert.STATUS_BLOCKED)
                msg.append(u'Объявления с номером %s заблокированы' % self.owner_tel)
            return u'\n'.join(msg)

        # проверка на дубликаты
        duplicate_list = Advert.get_duplicates(self.adtype, self.estate, self.need,
                                               tel=self.owner_tel, exclude_id=self.id, level=level)
        if duplicate_list:
            return u'найден дубликат №%s тел %s' % (duplicate_list[0].id, duplicate_list[0].owner_tel)

        return False

    def check_owner(self):
        """
        Проверка собственника на размещенные объявления
        """
        if self.need == Advert.NEED_SALE and self.company is None and \
                        self.estate == Advert.ESTATE_LIVE and \
                        self.adtype == Advert.TYPE_LEASE and \
                        self.status == Advert.STATUS_MODERATE and \
                        self.owner_tel:
            count = Advert.objects.filter(status=Advert.STATUS_VIEW,
                                                need=Advert.NEED_SALE,
                                                company=None,
                                                town=self.town,
                                                estate=Advert.ESTATE_LIVE,
                                                adtype=Advert.TYPE_LEASE,
                                                owner_tel=self.owner_tel,
                                                live=self.live,
                                                rooms=self.rooms,
                                                metro=self.metro,
                                                limit=self.limit,
                                                date__lte=self.date-timedelta(days=14),
                                                date__gte=self.date-timedelta(days=547))\
                        .exclude(id=self.id).count()
            if count > 0:
                self.status = Advert.STATUS_VIEW
                self.moderate_date = datetime.now()
                self.moderator = User.admin_objects.get(username='automoder_owner')
                return True

            if self.town.id in [1, 2]:
                from .stopagent import StopAgentAdvert

                def check_pattern(options):
                    metro_list = [self.metro] + [d.metro for d in self.metrodistance_set.all()]
                    query = Q(town=self.town,
                                    live=self.live,
                                    date__gte=self.date-timedelta(days=7),
                                    owner_tel=options['pattern']) & \
                            (Q(metro__in=metro_list) | Q(owner_name__iexact=self.owner_name))
                    if self.live == Advert.LIVE_FLAT:
                        query &= Q(rooms=self.rooms)
                    advert_list = StopAgentAdvert.objects.filter(query)
                    if advert_list:
                        self.status = Advert.STATUS_VIEW
                        self.moderate_date = datetime.now()
                        self.moderator = User.admin_objects.get(username=options['moderator'])
                        return True
                    return False

                for tel in get_tel_list(self.owner_tel):
                    pattern = tel
                    if pattern.startswith(u'7') or pattern.startswith(u'8'):
                        pattern = pattern[1:]
                    options = [
                        {
                            'pattern': u'%sXXX%sX' % (pattern[0:3], pattern[6:9]),
                            'moderator': 'automoder_stopagent'
                        },
                        {
                            'pattern': u'%sXXXX' % pattern[0:6],
                            'moderator': 'automoder_kvarnado'
                        },
                        {
                            'pattern': u'%sXXX%s' % (pattern[0:3], pattern[6:]),
                            'moderator': 'automoder_baza812'
                        },
                    ]
                    for option in options:
                        if check_pattern(option):
                            return True

        return False

    @staticmethod
    def block_by_tel(tel):
        return Advert.objects.filter(owner_tel=tel).exclude(status=Advert.STATUS_BLOCKED).update(status=Advert.STATUS_BLOCKED)

    def find_metro_distance(self):

        def getDistance(lat1, lon1, lat2, lon2):
            from math import sin, cos, pi, atan2, sqrt, pow
            lat1 *= pi / 180
            lat2 *= pi / 180
            lon1 *= pi / 180
            lon2 *= pi / 180

            d_lon = lon1 - lon2

            slat1 = sin(lat1)
            slat2 = sin(lat2)
            clat1 = cos(lat1)
            clat2 = cos(lat2)
            sdelt = sin(d_lon)
            cdelt = cos(d_lon)

            y = pow(clat2 * sdelt, 2) + pow(clat1 * slat2 - slat1 * clat2 * cdelt, 2)
            x = slat1 * slat2 + clat1 * clat2 * cdelt

            return atan2(sqrt(y), x) * 6372795

        try:
            if self.longitude and self.latitude:
                from lxml.html.soupparser import fromstring
                import requests
                import json
                proxies = {
                    "http": "http://127.0.0.1:8118",
                }
                self.metrodistance_set.all().delete()
                r = requests.get(u'http://geocode-maps.yandex.ru/1.x/?results=5&kind=metro&geocode=%s,%s' % (self.longitude, self.latitude), proxies=proxies)
                r.encoding = 'utf8'
                doc_metro = fromstring(r.text)
                for element in doc_metro.xpath('//featuremember/geoobject'):
                    try:
                        md = MetroDistance(advert=self)
                        metro_name = element.xpath('.//name')
                        if metro_name:
                            md.metro = Metro.from_title(self.town, metro_name[0].text_content())
                            if not md.metro:
                                continue
                        metro_coords = element.xpath('.//point/pos')
                        if metro_coords:
                            coords = metro_coords[0].text_content().split(' ')
                            md.latitude = float(coords[1])
                            md.longitude = float(coords[0])
                            if not md.latitude or not md.longitude:
                                continue

                        try:
                            # doc_distance = requests.get(u'https://api-maps.yandex.ru/services/route/2.0/?lang=ru_RU&token=18a4c9102dbd0892e7c8a03a93cff2b1&rtext=%s,%s~%s,%s' % (self.latitude, self.longitude, coords[1], coords[0]), proxies=proxies)
                            # # m = re.search(u'<script id="vpage" type="application/json">(.+)</script>', doc_distance.text)
                            # print doc_distance.text
                            # data = json.loads(doc_distance.text)
                            # md.duration_driving = float(data['data']['features'][0]['properties']['RouteMetaData']['Duration']['value'])
                            # md.distance_driving = float(data['data']['features'][0]['properties']['RouteMetaData']['Distance']['value'])

                            md.distance_driving = getDistance(self.latitude, self.longitude, float(coords[1]), float(coords[0]))
                            md.duration_driving = md.distance_driving / 1000.0 / 40.0 * 3600
                        except:
                            pass

                        try:
                            # print u'https://api-maps.yandex.ru/services/route/2.0/?lang=ru_RU&token=18a4c9102dbd0892e7c8a03a93cff2b1&rtext=%s,%s~%s,%s&rtt=mt' % (self.latitude, self.longitude, coords[1], coords[0])
                            # doc_distance = requests.get(u'http://maps.yandex.ru/?rtext=%s,%s~%s,%s&rtt=mt' % (self.latitude, self.longitude, coords[1], coords[0]), proxies=proxies)
                            # # m = re.search(u'<script id="vpage" type="application/json">(.+)</script>', doc_distance.text)
                            # data = json.loads(doc_distance.text)
                            # md.duration_transport = float(data['data']['features'][0]['properties']['RouteMetaData']['Duration']['value'])
                            # md.distance_transport = float(data['data']['features'][0]['properties']['RouteMetaData']['Distance']['value'])

                            md.distance_transport = getDistance(self.latitude, self.longitude, float(coords[1]), float(coords[0]))
                            md.duration_transport = md.distance_driving / 1000.0 / 5.0 * 3600
                        except:
                            pass

                        md.save()
                        # print md.metro
                        # print md.advert
                        # print md.duration_transport
                        # print md.distance_transport
                        # print md.duration_driving
                        # print md.distance_driving
                    except:
                        pass
        except:
            pass

    def find_surrounding_objects(self):
        if self.latitude and self.longitude:
            import requests
            import json
            search_url = 'https://psearch-maps.yandex.ru/1.x/?text=%s&ll=%s,%s&spn=0.003,0.003&results=10&format=json'
            headers = {'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"}
            proxies = {
                "http": "http://127.0.0.1:8118",
            }

            def find_objects(search, lat, lon, span):
                count = 0
                objects = []
                for text in search:
                    r = requests.get(search_url % (text, lon, lat), headers=headers, proxies=proxies)
                    data = json.loads(r.text)
                    try:
                        for item in data['response']['GeoObjectCollection']['featureMember']:
                            coords = item['GeoObject']['Point']['pos'].split(' ')
                            latitude = float(coords[1])
                            longitude = float(coords[0])
                            if abs(self.latitude-latitude) <= span and abs(self.longitude-longitude) <= span:
                                count += 1
                                objects.append({
                                    'title': item['GeoObject']['metaDataProperty']['PSearchObjectMetaData']['name'],
                                    'address': item['GeoObject']['metaDataProperty']['PSearchObjectMetaData']['address'],
                                    'category': item['GeoObject']['metaDataProperty']['PSearchObjectMetaData']['category'],
                                    'lat': latitude,
                                    'lon': longitude
                                })
                    except:
                        pass
                return {
                    'count': count,
                    'obj': objects
                }

            if 'surround' not in self.properties:
                self.properties['surround'] = {}

            self.properties['surround']['school'] = find_objects(['школа'], self.latitude, self.longitude, 0.003)
            self.properties['surround']['stop'] = find_objects(['остановка'], self.latitude, self.longitude, 0.004)
            self.properties['surround']['shop'] = find_objects(['продуктовый магазин'], self.latitude, self.longitude, 0.003)
            self.properties['surround']['sport'] = find_objects(['тренажер'], self.latitude, self.longitude, 0.003)
            self.properties['surround']['cafe'] = find_objects(['кафе', 'ресторан'], self.latitude, self.longitude, 0.003)
            self.properties['surround']['medic'] = find_objects(['аптека', 'больница'], self.latitude, self.longitude, 0.003)
            self.save()

    @property
    def is_archive(self):
        """
        Флаг, в архиве или нет объявление
        """
        if self.archive == Advert.ARCHIVE_AUTO:
            if self.adtype == Advert.TYPE_LEASE:
                td = datetime.now() - timedelta(days=settings.ARCHIVE_LEASE_DAYS)
                return td > self.date
            else:
                td = datetime.now() - timedelta(days=settings.ARCHIVE_SALE_DAYS)
                return td > self.date
        elif self.archive == Advert.ARCHIVE_YES:
            return True
        elif self.archive == Advert.ARCHIVE_NO:
            return False

    def parse(self, text):
        text_lower = text.lower()
        if re.findall(u'(мебель|меблирован|мебелирован)', text_lower, re.IGNORECASE | re.UNICODE):
            self.furniture = True
        if re.findall(u'(парковк|парковоч|паркинг|стоянка|мест.{1,10}машин|мест.{1,10}авто|машиноместо)', text_lower, re.IGNORECASE | re.UNICODE):
            self.parking = True
        if re.findall(u'(гараж)', text_lower, re.IGNORECASE | re.UNICODE):
            self.garage = True
        if u'консьерж' in text_lower:
            self.concierge = True
        if re.findall(u'(евро[\ |\-]*ремонт|хорош.{0,5}ремонт|качественн.{0,5}ремонт|нов.{0,5}ремонт|посл{0,5}ремонт|свеж{0,5}ремонт)', text_lower, re.IGNORECASE | re.UNICODE):
            self.euroremont = True
        if re.findall(u'(косм.{1,20}ремонт|небольш{0,5}ремонт|легк{0,5}ремонт|необх{0,10}ремонт)', text_lower, re.IGNORECASE | re.UNICODE):
            self.redecoration = True
        if re.findall(u'(треб.{1,10}ремонт|нужен.{1,10}ремонт)', text_lower, re.IGNORECASE | re.UNICODE):
            self.need_remont = True
        if re.findall(u'(нет.{1,10}ремонт|без.{1,10}ремонт)', text_lower, re.IGNORECASE | re.UNICODE):
            self.no_remont = True
        if re.findall(u'(охрана|охр\.)', text_lower, re.IGNORECASE | re.UNICODE):
            self.guard = True
        if re.findall(u'(tv|телевизор|кабельное|[\ |\.|\,|\-|\!|\t|\n]тв[\ |\.|\,|\-|\!|\t|\n])', text_lower, re.IGNORECASE | re.UNICODE):
            self.tv = True
        if re.findall(u'(стиральн.{0,5}машин|машинка|стиралка|СМА)', text_lower, re.IGNORECASE | re.UNICODE):
            self.washer = True
        if re.findall(u'(wi[\ |\-]*fi|интернет|вай|фай|ви-фи)', text_lower, re.IGNORECASE | re.UNICODE):
            self.internet = True
        if re.findall(u'(телефон)', text_lower, re.IGNORECASE | re.UNICODE):
            self.phone = True
        if re.findall(u'(балкон[\ |\.|\,|\-|\!|\t|\n]|балконом|лоджия)', text_lower, re.IGNORECASE | re.UNICODE):
            self.balcony = True
        if u'холодильник' in text_lower:
            self.refrigerator = True
        if re.findall(u'(быт.{0,6}техника|нов.{0,6}техника)', text_lower, re.IGNORECASE | re.UNICODE):
            self.refrigerator = True
            self.washer = True
        if u'посуточно' in text_lower:
            self.limit = self.LIMIT_DAY
        if re.findall(u'(сан[\ |\.]*узел раздел|раздел[ь|ён]ный сан[\ |\.]*узел|с/у разд|туал.{0,10}раздел[ь|ён]н|ванн.{0,10}раздел)', text_lower, re.IGNORECASE | re.UNICODE):
            self.separate_wc = True
        if re.findall(u'(с детьми|с реб[е|ё]нк)', text_lower, re.IGNORECASE | re.UNICODE):
            self.live_child = True
        if re.findall(u'(семьи|семье)', text_lower, re.IGNORECASE | re.UNICODE):
            self.live_pare = True
        if re.findall(u'(дв.{0,10}челов|дв.{0,10}жильц|двоих)', text_lower, re.IGNORECASE | re.UNICODE):
            self.live_two = True
        if re.findall(u'(женщин|девушк)', text_lower, re.IGNORECASE | re.UNICODE):
            self.live_girl = True
        if re.findall(u'(мужчин|парня|парней)', text_lower, re.IGNORECASE | re.UNICODE):
            self.live_man = True
        if re.findall(u'(с животн|с домашними животными|с кошк|с котом|с соба|мален.{0,5}соба)', text_lower, re.IGNORECASE | re.UNICODE):
            self.live_animal = True
        if re.findall(u'(лифт)', text_lower, re.IGNORECASE | re.UNICODE):
            self.lift = True
        self.parse_tags(text)

    def parse_tags(self, text):
        from main.models.adverttags import AdvertTags
        self.properties['tags'] = AdvertTags.parse(text)

    def generate_description(self, variant=''):
        def start_sentence():
            words = []
            if self.need == self.NEED_SALE:
                if self.adtype == self.TYPE_LEASE:
                    words.append(random.choice([u'Сдается', u'Сдается в аренду', u'Сдается без посредников']))
                elif self.adtype == self.TYPE_SALE:
                    words.append(u'Продается')

            elif self.need == self.NEED_DEMAND:
                if self.adtype == self.TYPE_LEASE:
                    words.append(u'Сниму')
                elif self.adtype == self.TYPE_SALE:
                    words.append(u'Куплю')

            if self.estate == Advert.ESTATE_LIVE:
                if self.live == Advert.LIVE_ROOM:
                    if self.need == Advert.NEED_SALE:
                        words.append(u'комната')
                        if self.rooms:
                            words.append(random.choice([u'в %s-комнатной квартире%s' % (self.rooms, self.get_tag('studia', 'p')),
                                                        u', в квартире %s комн.,' % self.rooms]))
                    elif self.need == Advert.NEED_DEMAND:
                        words.append(u'комнату')
                        rooms = []
                        if self.live_flat1:
                            rooms.append(u'1')
                        if self.live_flat2:
                            rooms.append(u'2')
                        if self.live_flat3:
                            rooms.append(u'3')
                        if self.live_flat4:
                            rooms.append(u'4')
                        if rooms:
                            words.append(u'в %s-комнатной квартире%s' % (u', '.join(rooms), self.get_tag('studia', 'p')))

                elif self.live == Advert.LIVE_FLAT:
                    if self.need == Advert.NEED_SALE:
                        if self.rooms:
                            words.append(u'%s-комнатная' % self.rooms)
                        if random.choice([1, 2, 3]) == 3 and self.furniture:
                            words.append(u'мебелированная')
                        words.append(u'квартира%s' % self.get_tag('studia'))
                    elif self.need == Advert.NEED_DEMAND:
                        rooms = []
                        if self.live_flat1:
                            rooms.append(u'1')
                        if self.live_flat2:
                            rooms.append(u'2')
                        if self.live_flat3:
                            rooms.append(u'3')
                        if self.live_flat4:
                            rooms.append(u'4')
                        if rooms:
                            words.append(u'%s-комнатную' % u', '.join(rooms))
                        if random.choice([1, 2, 3]) == 3 and self.furniture:
                            words.append(u'мебелированную')
                        words.append(u'квартиру%s' % self.get_tag('studia'))

                if self.get_tag('lasthostel'):
                    words.append(self.get_tag('lasthostel'))
                elif self.get_tag('hostel'):
                    words.append(self.get_tag('hostel'))
                elif self.get_tag('small family'):
                    words.append(self.get_tag('small family'))
                if self.get_tag('newhouse'):
                    words.append(self.get_tag('newhouse', 'p'))
            elif self.estate == Advert.ESTATE_COUNTRY:
                words.append(Advert.COUNTRIES[self.country].lower())
            elif self.estate == Advert.ESTATE_COMMERCIAL:
                words.append(Advert.COMMERCIALS[self.commercial].lower() + u' помещение')
            elif self.estate == Advert.ESTATE_TERRITORY:
                words.append(Advert.TERRITORIES[self.territory].lower())
            random_words = []
            if self.adtype == Advert.TYPE_LEASE:
                if self.limit == Advert.LIMIT_DAY:
                    random_words.append(u'посуточно')
                else:
                    random_words.append(random.choice([u'на длительный срок',u'длительно',u'на продолжительное время',u'надолго']))

            if self.metro:
                random_words.append(random.choice([u'в районе метро', u'вблизи метро', u'рядом с метро', u'недалеко от метро', u'в пешей доступности от метро'])+
                             u' ' + self.metro.title)
            if self.get_tag('centr'):
                random_words.append(self.get_tag('centrs'))
            if random_words:
                words.append(u' '.join(random_words))
            return u' '.join(words)

        def sentence2():
            words = []
            if self.refrigerator:
                words.append(u'холодильник')
            if self.tv:
                words.append(u'телевизор')
            if self.washer:
                words.append(u'стиральная машина')
            if self.phone:
                words.append(u'телефон')
            if self.internet:
                words.append(u'интернет')
            if self.conditioner:
                words.append(u'кондиционер')
            if self.furniture:
                if self.need == Advert.NEED_SALE:
                    words.append(random.choice([u'мебель', u'необходимая мебель']))
                else:
                    words.append(u'мебель')
            if self.get_tag('newfurniture'):
                words.append(self.get_tag('newfurniture'))
            if self.get_tag('in kitchen'):
                words.append(self.get_tag('in kitchen'))
            if self.get_tag('micro'):
                words.append(self.get_tag('micro'))
            if self.get_tag('bedroom set'):
                words.append(self.get_tag('bedroom set'))
            if self.get_tag('sofa'):
                words.append(self.get_tag('sofa'))
            if self.get_tag('bed'):
                words.append(self.get_tag('bed'))
            if self.get_tag('cupboard'):
                words.append(self.get_tag('cupboard'))
            if self.get_tag('table'):
                words.append(self.get_tag('table'))
            if self.get_tag('clockery'):
                words.append(self.get_tag('clockery')),
            if self.get_tag('teapot'):
                words.append(self.get_tag('teapot'))
            if self.get_tag('appliances'):
                words.append(self.get_tag('appliances'))
            if self.get_tag('multivar'):
                words.append(self.get_tag('multivar'))
            if self.get_tag('pmm'):
                words.append(self.get_tag('pmm'))


            words.sort(key=lambda v: random.random())

            if self.need == Advert.NEED_SALE:
                return (random.choice([u'Имеется ', u'Есть ']) + u', '.join(words)) if words else u''
            else:
                return (random.choice([u'Нужны ', u'Необходимы ']) + u', '.join(words)) if words else u''

        def sentence3():
            enter = u''
            if self.estate == Advert.ESTATE_LIVE:
                # if self.live == Advert.LIVE_ROOM:
                #     enter = u'В комнате'
                # elif self.live == Advert.LIVE_FLAT:
                enter = u'В квартире'
            elif self.estate == Advert.ESTATE_COUNTRY:
                enter = u'В помещении'
            elif self.estate == Advert.ESTATE_COMMERCIAL:
                enter = u'В помещении'
            elif self.estate == Advert.ESTATE_TERRITORY:
                enter = u'В территории'

            if self.need == Advert.NEED_DEMAND:
                enter += u' нужны'

            words = []
            if self.euroremont:
                if self.need == Advert.NEED_SALE:
                    words.append(random.choice([u'сделан евроремонт', u'сделан ремонт', u'сделан хороший ремонт', u'сделан качественный ремонт', u'хороший ремонт']))
                else:
                    words.append(random.choice([u'евроремонт', u'хороший ремонт']))
            if self.need_remont:
                words.append(u'нужен ремонт' if self.need == Advert.NEED_SALE else u'(можно без ремонта)')
            if self.no_remont:
                words.append(u'нет ремонта' if self.need == Advert.NEED_SALE else u'(можно без ремонта)')
            if self.redecoration:
                words.append(u'сделан косметический ремонт' if self.need == Advert.NEED_SALE else u'косметический ремонт')
            if self.separate_wc:
                words.append(random.choice([u'имеется раздельный санузел', u'раздельный санузел', u'санузел раздельный', u'ванна и туалет раздельные']) if self.need == Advert.NEED_SALE else u'раздельный санузел')
            if self.get_tag('bathtoilet'):
                words.append(self.get_tag('bathtoilet'))
            if self.get_tag('glassbalcony'):
                words.append(self.get_tag('glassbalcony'))
            elif self.balcony:
                words.append(random.choice([u'есть балкон', u'балкон']) if self.need == Advert.NEED_SALE else u'балкон')
            elif self.get_tag('glassloggia'):
                words.append(self.get_tag('glassloggia'))
            elif self.get_tag('loggia'):
                words.append(self.get_tag('loggia'))
            if self.electric:
                words.append(u'электричество')
            if self.gas:
                words.append(u'проведен газ')
            if self.water:
                words.append(u'проведена вода')
            if self.sewage:
                words.append(u'есть канализация' if self.need == Advert.NEED_SALE else u'канализация')
            if self.get_tag('panoram window'):
                words.append(self.get_tag('panoram window'))

            words.sort(key=lambda v: random.random())
            return (enter + u' ' + u', '.join(words)) if words else u''

        def sentence4():
            words = []
            if self.live_one:
               words.append(random.choice([u'для одного человека', u'для одного жильца', u'одному жильцу']))
            if self.live_two:
               words.append(random.choice([u'для двух человек', u'для двух жильцов', u'двум жильцам']))
            if self.live_pare:
                words.append(random.choice([u'для семейной пары', u'для семьи', u'для пары']))
            if self.live_child:
                if words:
                    words.append(random.choice([u'с ребенком', u'с детьми']))
                else:
                    words.append(random.choice([u'для мужчины или женщины c ребенком', u'для пары с ребенком', u'для семьи с детьми', u'для пары с детьми']))
            if self.live_girl:
                words.append(random.choice([u'для девушек', u'для женщин', u'женщинам']))
            if self.live_man:
                words.append(random.choice([u'для парней', u'для мужчин', u'мужчинам']))
            if self.live_animal:
                words.append(random.choice([u'можно с животными', u'можно с домашними питомцами', u'можно с домашними животными']))
            elif self.get_tag('no animal'):
                 words.append(self.get_tag('no animal'))
            if self.adtype == Advert.TYPE_LEASE and self.need == Advert.NEED_SALE:
                return (random.choice([u'Сдается ', u'Сдаю ', u'Сдам ']) + u', '.join(words)) if words else u''
            if self.adtype == Advert.TYPE_SALE and self.need == Advert.NEED_SALE:
                return (u'Продается ' + u', '.join(words)) if words else u''
            if self.adtype == Advert.TYPE_LEASE and self.need == Advert.NEED_DEMAND:
                return (u'Сниму ' + u', '.join(words)) if words else u''
            if self.adtype == Advert.TYPE_SALE and self.need == Advert.NEED_DEMAND:
                return (u'Куплю ' + u', '.join(words)) if words else u''

        def sentence5():
            words = []
            if self.brick_building:
                words.append(u'Кирпичная построка')
            if self.wood_building:
                words.append(u'Деревянная постройка')
            if self.get_tag('newhouse'):
                words.append(self.get_tag('newhouse'))
            return u', '.join(words) if words else u''

        def sentence6():
            words = []
            if self.parking:
                words.append(u'парковка')
            if self.lift:
                words.append(u'лифт')
            if self.concierge:
                words.append(random.choice([u'консьерж', u'в подъезде консьерж']))
            if self.guard:
                words.append(random.choice([u'охрана', u'охраняемый двор', u'двор с охраной', u'закрытый двор']))
            if self.garage:
                words.append(u'гараж')
            if self.get_tag('video'):
                words.append(self.get_tag('video'))
            if self.get_tag('domofon'):
                words.append(self.get_tag('domofon'))
            if self.get_tag('steeldoor'):
                words.append(self.get_tag('steeldoor'))
            words.sort(key=lambda v: random.random())

            if self.need == Advert.NEED_SALE:
                return (random.choice([u'Имеется ', u'Есть ']) + u', '.join(words)) if words else u''
            else:
                return (random.choice([u'Нужны ', u'Должны быть ']) + u', '.join(words)) if words else u''

        def sentence7():
            words = []
            if self.get_tag('no furniture'):
                words.append(self.get_tag('no furniture'))

            if self.adtype == Advert.TYPE_LEASE:
                return (random.choice([u'На данный момент ', u'Сейчас ']) + u', '.join(words)) if words else u''

        def sentence8():
            words = []
            if self.get_tag('cleanflat'):
                words.append(self.get_tag('cleanflat'))
            if self.get_tag('firsttime'):
                words.append(self.get_tag('firsttime'))

            if self.adtype == Advert.TYPE_LEASE:
                return (u'Квартира ' + u', '.join(words)) if words else u''

        def sentence9():
            words = []
            if self.get_tag('asap'):
                words.append(self.get_tag('asap'))

            if self.adtype == Advert.TYPE_LEASE:
                return u' '.join(words)

        def sentence10():
            words = []
            if self.get_tag('sosedi'):
                words.append(self.get_tag('sosedi'))

            if self.adtype == Advert.TYPE_LEASE:
                return u' '.join(words)

        def sentence11():
            words = []
            if self.get_tag('alone'):
                words.append(self.get_tag('alone'))

            if self.adtype == Advert.TYPE_LEASE:
                return u' '.join(words)

        def sentence12():
            words = []
            if self.get_tag('yard'):
                words.append(self.get_tag('yard'))
            if self.get_tag('infrastructure'):
                words.append(self.get_tag('infrastructure'))
            if self.get_tag('transport'):
                words.append(self.get_tag('transport'))

            if self.adtype == Advert.TYPE_LEASE:
                return u' '.join(words)

        def pay_sentence():
            words = []
            if self.price:
                if self.adtype == Advert.TYPE_LEASE:
                    words = [u'Оплата %d руб.' % self.price] if self.need == Advert.NEED_SALE else [u'Оплата до %d руб.' % self.price]
                elif self.adtype == Advert.TYPE_SALE:
                    words = [u'Стоимость %d руб.' % self.price] if self.need == Advert.NEED_SALE else [u'Стоимость до %d руб.' % self.price]
                if self.adtype == Advert.TYPE_LEASE:
                    if self.limit == Advert.LIMIT_DAY:
                        words.append(random.choice([u'в сутки', u'за сутки', u'/ сутки']))
                    else:
                        words.append(random.choice([u'в месяц', u'за месяц', u'/ месяц']))
                if self.get_tag('no ku'):
                    words.append(self.get_tag('no ku'))
                elif self.get_tag('ku'):
                    words.append(self.get_tag('ku'))
                if self.get_tag('zalog'):
                    words.append(self.get_tag('zalog'))
                elif self.get_tag('no zalog'):
                    words.append(self.get_tag('no zalog'))
                return u''.join(words)
            else:
                return u''

        def square_sentence():
            words = []
            if self.square:
                if self.estate == Advert.ESTATE_LIVE:
                    words.append(random.choice([u'Площадь', u'Жилая площадь'])+
                        u' ' + unicode(self.square) + random.choice([u' м2', u' метров', u'кв. метров']))
                else:
                    words.append(u', '.join([
                        u'Площадь %d ' % self.square + random.choice([u'м2', u'метров']),
                        (u'жилая - %s ' % self.living_square + random.choice([u'м2', u'метров', u'кв. метров'])) if self.living_square else '',
                        (u'кухни - %d ' % self.kitchen_square + random.choice([u'м2', u'метров', u'кв. метров'])) if self.kitchen_square else '',
                    ]))
            return u' '.join(words)

        def end_sentence():
            if self.need == Advert.NEED_SALE and not variant == 'gsn':
                words = []
                if self.need == self.NEED_SALE:
                    if self.adtype == self.TYPE_LEASE:
                        words.append(random.choice([u'Сдается', u'Сдам', u'Сдам лично', u'Сдаю самостоятельно', u'Сдаю']))
                    elif self.adtype == self.TYPE_SALE:
                        words.append(u'Продажа')
                else:
                    if self.adtype == self.TYPE_LEASE:
                        words.append(u'Снимается')
                    elif self.adtype == self.TYPE_SALE:
                        words.append(u'Покупается')
                if self.adtype == Advert.TYPE_LEASE:
                    if self.limit == Advert.LIMIT_DAY:
                        words.append(u'посуточно')
                    else:
                        words.append(random.choice([u'на длительный срок', u'длительно']))
                if not self.company:
                    words.append(random.choice([u'без посредников', u'от хозяина', u'от владельца', u'от собственника', u'без агентов', u'без комиссии', u'напрямую от собственника']))
                return u' '.join(words) if words else u''
            else:
                return u' '

        random_func = [sentence2, sentence3, sentence4, sentence5, sentence6, sentence7, sentence8, sentence9, sentence10, sentence11, sentence12, pay_sentence, square_sentence]
        random_func.sort(key=lambda v: random.random())
        random_func = [start_sentence] + random_func + [end_sentence]

        sentences = [func() for func in random_func]
        while u'' in sentences:
            sentences.remove(u'')
        result = u'. '.join(sentences)
        return result

    def generate_client_description(self):
        from main.templatetags.main_tags import fmt_price

        def start_sentence():
            words = []

            if self.need == self.NEED_SALE:
                if self.adtype == self.TYPE_LEASE:
                    words.append(u'Сдается')
                elif self.adtype == self.TYPE_SALE:
                    words.append(u'Продается')

            elif self.need == self.NEED_DEMAND:
                if self.adtype == self.TYPE_LEASE:
                    words.append(u'Сниму')
                elif self.adtype == self.TYPE_SALE:
                    words.append(u'Куплю')

            if self.estate == Advert.ESTATE_LIVE:
                if self.live == Advert.LIVE_ROOM:
                    words.append(u'комната')
                    if self.rooms:
                        words.append(u'в %s-к.кв.%s' % (self.rooms, self.get_tag('studia', 'p')))
                elif self.live == Advert.LIVE_FLAT:
                    if self.rooms:
                        words.append(u'%s-к.кв.' % self.rooms)
                    else:
                        words.append(u'квартира%s' % self.get_tag('studia'))

                if self.get_tag('lasthostel'):
                    words.append(self.get_tag('lasthostel'))
                elif self.get_tag('hostel'):
                    words.append(self.get_tag('hostel'))
                elif self.get_tag('small family'):
                    words.append(self.get_tag('small family'))
                if self.get_tag('newhouse'):
                    words.append(self.get_tag('newhouse', 'p'))
            elif self.estate == Advert.ESTATE_COUNTRY:
                words.append(Advert.COUNTRIES[self.country].lower())
            elif self.estate == Advert.ESTATE_COMMERCIAL:
                words.append(Advert.COMMERCIALS[self.commercial].lower() + u' помещение')
            elif self.estate == Advert.ESTATE_TERRITORY:
                words.append(Advert.TERRITORIES[self.territory].lower())
            random_words = []
            if self.adtype == Advert.TYPE_LEASE:
                if self.limit == Advert.LIMIT_DAY:
                    random_words.append(u'посуточно')

            if self.metro:
                random_words.append(u'у метро ' + self.metro.title)

            if self.address:
                random_words.append(u'по адресу ' + self.address)

            if self.get_tag('centr'):
                random_words.append(self.get_tag('centrs'))
            if random_words:
                words.append(u' '.join(random_words))
            return u' '.join(words)

        def sentence2():
            words = []
            if self.refrigerator:
                words.append(u'холодильник')
            if self.tv:
                words.append(u'телевизор')
            if self.washer:
                words.append(u'стиральная машина')
            if self.phone:
                words.append(u'телефон')
            if self.internet:
                words.append(u'интернет')
            if self.conditioner:
                words.append(u'кондиционер')
            if self.furniture:
                words.append(u'мебель')
            if self.get_tag('newfurniture'):
                words.append(self.get_tag('newfurniture'))
            if self.get_tag('in kitchen'):
                words.append(self.get_tag('in kitchen'))
            if self.get_tag('bedroom set'):
                words.append(self.get_tag('bedroom set'))
            if self.get_tag('sofa'):
                words.append(self.get_tag('sofa'))
            if self.get_tag('bed'):
                words.append(self.get_tag('bed'))
            if self.get_tag('cupboard'):
                words.append(self.get_tag('cupboard'))
            if self.get_tag('table'):
                words.append(self.get_tag('table'))
            if self.get_tag('no furniture'):
                words.append(self.get_tag('no furniture'))
            if self.get_tag('clockery'):
                words.append(self.get_tag('clockery')),
            if self.get_tag('teapot'):
                words.append(self.get_tag('teapot'))
            if self.get_tag('appliances'):
                words.append(self.get_tag('appliances'))


            words.sort(key=lambda v: random.random())

            return (u'Есть ' + u', '.join(words)) if words else u''

        def sentence3():
            enter = u''
            if self.estate == Advert.ESTATE_LIVE:
                # if self.live == Advert.LIVE_ROOM:
                #     enter = u'В комнате'
                # elif self.live == Advert.LIVE_FLAT:
                enter = u'В квартире'
            elif self.estate == Advert.ESTATE_COUNTRY:
                enter = u'В помещении'
            elif self.estate == Advert.ESTATE_COMMERCIAL:
                enter = u'В помещении'
            elif self.estate == Advert.ESTATE_TERRITORY:
                enter = u'В территории'

            words = []
            if self.euroremont:
                words.append(u'сделан евроремонт')
            if self.need_remont:
                words.append(u'нужен ремонт')
            if self.no_remont:
                words.append(u'нет ремонта')
            if self.redecoration:
                words.append(u'сделан косметический ремонт')
            if self.separate_wc:
                words.append(u'раздельный санузел')
            if self.get_tag('bathtoilet'):
                words.append(self.get_tag('bathtoilet'))
            if self.get_tag('glassbalcony'):
                words.append(self.get_tag('glassbalcony'))
            elif self.balcony:
                words.append(u'балкон')
            if self.electric:
                words.append(u'электричество')
            if self.gas:
                words.append(u'проведен газ')
            if self.water:
                words.append(u'проведена вода')
            if self.sewage:
                words.append(u'есть канализация')
            if self.get_tag('panoram window'):
                words.append(self.get_tag('panoram window'))
            if self.get_tag('glassloggia'):
                words.append(self.get_tag('glassloggia'))
            elif self.get_tag('loggia'):
                words.append(self.get_tag('loggia'))

            words.sort(key=lambda v: random.random())
            return (enter + u' ' + u', '.join(words)) if words else u''

        def sentence5():
            words = []
            if self.brick_building:
                words.append(u'Кирпичная построка')
            if self.wood_building:
                words.append(u'Деревянная постройка')
            if self.get_tag('newhouse'):
                words.append(self.get_tag('newhouse'))
            return u', '.join(words) if words else u''

        def sentence6():
            words = []
            if self.parking:
                words.append(u'парковка')
            if self.lift:
                words.append(u'лифт')
            if self.concierge:
                words.append(random.choice([u'консьерж', u'в подъезде консьерж']))
            if self.guard:
                words.append(random.choice([u'охрана', u'охраняемый двор', u'двор с охраной', u'закрытый двор']))
            if self.garage:
                words.append(u'гараж')
            if self.get_tag('video'):
                words.append(self.get_tag('video'))
            if self.get_tag('domofon'):
                words.append(self.get_tag('domofon'))
            if self.get_tag('steeldoor'):
                words.append(self.get_tag('steeldoor'))
            words.sort(key=lambda v: random.random())

            return (random.choice([u'Имеется ', u'Есть ']) + u', '.join(words)) if words else u''

        def pay_sentence():
            words = []
            if self.price:
                if self.adtype == Advert.TYPE_LEASE:
                    words = [u'Оплата %d руб.' % self.price] if self.need == Advert.NEED_SALE else [u'Оплата до %d руб.' % self.price]
                elif self.adtype == Advert.TYPE_SALE:
                    words = [u'Стоимость %d руб.' % self.price] if self.need == Advert.NEED_SALE else [u'Стоимость до %d руб.' % self.price]
                if self.adtype == Advert.TYPE_LEASE:
                    if self.limit == Advert.LIMIT_DAY:
                        words.append(random.choice([u'в сутки', u'за сутки', u'/ сутки']))
                    else:
                        words.append(random.choice([u'в месяц', u'за месяц', u'/ месяц']))
                if self.get_tag('no ku'):
                    words.append(self.get_tag('no ku'))
                elif self.get_tag('ku'):
                    words.append(self.get_tag('ku'))
                return u' '.join(words)
            else:
                return u''

        def square_sentence():
            words = []
            if self.square:
                if self.estate == Advert.ESTATE_LIVE:
                    words.append(u'Площадь' + \
                        u' ' + unicode(self.square) +u' м2')
                else:
                    words.append(u', '.join([
                        u'Площадь %d ' % self.square + u' м2',
                        (u'жилая - %s ' % self.living_square + u' м2') if self.living_square else '',
                        (u'кухни - %d ' % self.kitchen_square + u' м2') if self.kitchen_square else '',
                    ]))
            return u' '.join(words)

        def limit_sentence():
            if self.need == Advert.NEED_SALE:
                words = []
                if self.need == self.NEED_SALE:
                    if self.adtype == self.TYPE_LEASE:
                        words.append(u'Сдается')
                    elif self.adtype == self.TYPE_SALE:
                        words.append(u'Продажа')
                else:
                    if self.adtype == self.TYPE_LEASE:
                        words.append(u'Снимается')
                    elif self.adtype == self.TYPE_SALE:
                        words.append(u'Покупается')
                if self.adtype == Advert.TYPE_LEASE:
                    if self.limit == Advert.LIMIT_DAY:
                        words.append(u'посуточно')
                    else:
                        words.append(random.choice([u'на длительный срок', u'длительно']))
                return u' '.join(words) if words else u''
            else:
                return u' '

        def company_sentence():
            if not self.company:
                return u'Без посредников'
            else:
                return u''

        random_func = [sentence2, sentence3, pay_sentence, limit_sentence]
        random_func.sort(key=lambda v: random.random())
        random_func = [start_sentence] + random_func + [company_sentence]

        sentences = [func() for func in random_func]
        while u'' in sentences:
            sentences.remove(u'')
        result = u'. '.join(sentences)
        return result

    @property
    def description(self):
        if not self.company_id:
            text = self.properties.get('desc.gsn', '')
            if not text:
                text = self.generate_description('gsn')
                self.properties['desc.gsn'] = text
                self.save()
            return text
        else:
            return self.body

    def clear_description(self):
        self.properties['desc.gsn'] = ''
        self.properties['desc.vashdom'] = ''


    def get_tag(self, tag, padeg=None):
        from main.models.adverttags import AdvertTags
        title_tag = ('title-' + padeg) if padeg else 'title'
        if tag in self.properties.get('tags', []):
            if title_tag in AdvertTags.TAGS[tag]:
                return random.choice(AdvertTags.TAGS[tag][title_tag])
            else:
                return random.choice(AdvertTags.TAGS[tag]['title'])
        else:
            return u''

    # вспомогательные методы

    @staticmethod
    def reset_last_viewed():
        advert_list = Advert.objects.filter(clients__id__isnull=False).distinct()
        for advert in advert_list:
            print '%s - %s' % (advert.id, advert.clients.count())
            advert.last_viewed_count = advert.clients.count()
            advert.save()
            advert.clear_cache()

    @staticmethod
    def reset_demand_rooms():
        advert_list = Advert.objects.filter(need=Advert.NEED_DEMAND, live_flat1=False, live_flat2=False, live_flat3=False, live_flat4=False)
        for advert in advert_list:
            print advert.id
            advert.live_flat1 = advert.rooms == 1
            advert.live_flat2 = advert.rooms == 2
            advert.live_flat3 = advert.rooms == 3
            advert.live_flat4 = advert.rooms >= 4
            advert.save()

    @staticmethod
    def reset_date():
        offset = 0
        while True:
            advert_list = Advert.objects.filter(id__lte=500000).order_by('-id')[offset:offset+100]
            for advert in advert_list:
                advert.date = advert.date
                advert.save()
                print '%s' % advert.id
            if not advert_list:
                break
            offset += 100


class RegViewed(models.Model):
    advert = models.ForeignKey(Advert, default=0)
    date = models.DateTimeField('Дата', default=datetime.now)
    user = models.ForeignKey(User, default=0)

    class Meta:
        verbose_name = u'Просмотренные объявления'
        verbose_name_plural = u'Регистр просмотренных объявлений'
        ordering = ['-date']
        unique_together = ('advert', 'user')

    def __unicode__(self):
        return unicode(self.id)

    @staticmethod
    def add(advert, user):
        reg = RegViewed(advert=advert, user=user)
        reg.save()
        return reg

    @staticmethod
    def day_count_user(user, query=Q()):
        today = datetime.now().date()
        query &= Q(user=user, date__gte=today)
        count = RegViewed.objects.filter(query).count()
        return count

    @staticmethod
    def day_count_company(company, query=Q()):
        today = datetime.now().date()
        query &= Q(user__company=company, date__gte=today)
        count = RegViewed.objects.filter(query).count()
        return count


class News(models.Model):
    """
    Новости
    """

    title = models.CharField(verbose_name='Заголовок', max_length=250, default='')
    date = models.DateTimeField(verbose_name='Дата', default=datetime.now())
    body = RichTextField(verbose_name='Содержимое', blank=True, null=True, default='')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    images = models.ManyToManyField(UserImage, blank=True)
    video = models.ForeignKey(UserVideo, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    moder = models.BooleanField('Для модераторов', blank=True, default=False)
    client = models.BooleanField('Для клиентов', blank=True, default=False)
    site = models.ForeignKey(Site, blank=True)

    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'
        ordering = ['-date']
        permissions = (
            ('view_news', 'Просмотр новостей'),
        )

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('news:detail', [self.id])

    @models.permalink
    def get_client_url(self):
        return ('client:news:detail', [self.id])

    def save(self, *args, **kwargs):
        if not self.site_id:
            self.site = Site.objects.get_current()
        return super(News, self).save(*args, **kwargs)


class Vacancy(models.Model):
    """
    Вакансии
    """
    title = models.CharField(verbose_name='Заголовок', max_length=250, default='')
    body = models.TextField(verbose_name='Содержимое', blank=True, null=True, default='')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='Дата', default=datetime.now())

    class Meta:
        verbose_name = u'Вакансия'
        verbose_name_plural = u'Вакансии'
        ordering = ['-date']
        permissions = (
            ('view_vacancy', 'Просмотр вакансий'),
        )

    def __unicode__(self):
        return self.title


class Question(models.Model):
    """
    Вакансии
    """
    body = models.TextField(verbose_name='Вопрос', default='')
    answer = models.TextField(verbose_name='Содержимое', blank=True, null=True, default='')
    date = models.DateTimeField(verbose_name='Дата', default=datetime.now())

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'
        ordering = ['-date']
        permissions = (
            ('view_question', 'Просмотр вопросов'),
        )


class Blacklist(CachingMixin, models.Model):
    """
    Черный список телефонов
    """
    tel = models.CharField(verbose_name='Телефон', max_length=250, default='')
    body = models.TextField(verbose_name='Описание', default='', blank=True, null=True)
    tag = models.CharField(verbose_name='Тег', max_length=50, default=None, blank=True, null=True)
    town = models.ForeignKey(Town, verbose_name='Город', default=None, blank=True, null=True)

    objects = CachingManager()

    class Meta:
        verbose_name = u'Элемент черного списка'
        verbose_name_plural = u'Черный список'
        ordering = ['tel']
        permissions = (
            ('view_blacklist', 'Просмотр черного списка'),
        )

    def __unicode__(self):
        return self.tel

    @staticmethod
    def add_tel(tel, desc='', tag=None, town=None):
        tel_list = get_tel_list(tel)
        for t in tel_list:
            t = t.strip()
            if len(t) >= 5:
                blacklist = Blacklist(tel=t, body=desc, tag=tag, town=town)
                blacklist.save()

    @staticmethod
    def check_tel(tel):
        t = clear_tel(tel)
        blacklist = Blacklist.objects.filter(tel__icontains=t)
        if blacklist:
            return  u'Телефон %s есть в черном списке как %s' % (t, blacklist[0].tel)
        mask_blacklist = Blacklist.objects.filter(tel__icontains='X')
        for mask_tel in mask_blacklist:
            if re.search(mask_tel.tel.replace('X', '(.)'), t):
                return  u'Телефон %s есть в черном списке как %s' % (tel, mask_tel.tel)
        company = Company.objects.filter(tel__icontains=t)
        if company:
            return u'Телефон %s принадлежит агентству' % t
        user = User.objects.filter(tel__icontains=t)
        if user:
            return u'Телефон %s принадлежит пользователю' % t
        return False

    @staticmethod
    def check_list(tel_list):
        tels = get_tel_list(tel_list)
        for tel in tels:
            result = Blacklist.check_tel(tel)
            if result:
                return result
        return False


class Company(CachingMixin, models.Model):
    """
    Агенство
    """

    STATUS_ACTIVE = 'a'
    STATUS_MODERATE = 'm'
    STATUS_BLOCK = 'b'
    STATUSES = {
        STATUS_ACTIVE: 'Активна',
        STATUS_MODERATE: 'На модерации',
        STATUS_BLOCK: 'Заблокирована',
    }

    title = models.CharField(verbose_name='Заголовок', max_length=250, default='')
    body = models.TextField('Описание', blank=True, null=True, default='')
    image = models.ImageField('Фото', upload_to=get_user_image_path, null=True, blank=True)
    address = models.CharField('Адрес', max_length=250, null=True, blank=True)
    fact_address = models.CharField('Адрес', max_length=250, null=True, blank=True)
    town = models.ForeignKey(Town, verbose_name='Город', default=1)
    tel = models.CharField('Телефон', max_length=50, null=True, blank=True)
    inn = models.CharField('ИНН', max_length=50, null=True, blank=True)
    ogrn = models.CharField('ОГРН', max_length=50, null=True, blank=True)
    email = models.EmailField('Email', max_length=50, null=True, blank=True)
    desc = models.TextField('Описание', null=True, blank=True)
    person = models.CharField('Контактное лицо', max_length=250, default='')
    owner = models.ForeignKey(User, verbose_name='Владелец', null=True, blank=True, related_name='owner', on_delete=models.SET_NULL)
    status = models.CharField('Статус', max_length=1, default=STATUS_MODERATE, choices=STATUSES.items())
    extnum = models.CharField('Внешний код', max_length=50, default=None, null=True, blank=True)
    buys = models.PositiveIntegerField(verbose_name='Выкупы', default=0, blank=True)
    slug = models.SlugField(default='', blank=True, max_length=100)
    rating = models.FloatField('Рейтинг агентства', default=5, blank=True, db_index=True)

    # реальное ли агентсво
    is_real = models.BooleanField('Реальное агентство', default=True, blank=True)
    hidden = models.BooleanField('Скрытое', default=False, blank=True)

    objects = CachingManager()

    class Meta:
        verbose_name = u'Агенство'
        verbose_name_plural = u'Агенства'
        ordering = ['title']
        permissions = (
            ('view_company', 'Просмотр агенств'),
        )

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = 'default'
        self.title = self.title.strip()
        return super(Company, self).save(*args, **kwargs)

    def load_logo(self, href):
        img = urllib2.urlopen(href)
        self.image.save(get_user_image_path(self, href), ContentFile(img.read()), save=True)

    @models.permalink
    def get_absolute_url(self):
        return ('company:detail', [self.slug if self.slug else 'default', self.id])

    @staticmethod
    def get_catalog_url(args=[]):
        params = args.copy()
        parts = ['company']
        if 'town' in params:
            town = get_object_or_404(Town, id=params['town'])
            parts.append(town.slug)
            del params['town']

        get_params = []
        for key, value in params.iteritems():
            if isinstance(value, list):
                for v in value:
                    get_params.append((key, v))
            else:
                get_params.append((key, value.encode('utf8')))

        return '/' + ('/'.join(parts)) + '/' + ('?' if len(get_params) else '') + urllib.urlencode(get_params)

    def get_access_query(self, user=None, base='main'):
        query = Q(id=None)
        service_list = ConnectedService.objects.filter(company=self, active=True,  start_date__lte=datetime.now(), end_date__gte=datetime.now()).select_related('perm')
        enable_perms = []
        if user:
            enable_perms = user.enable_perms.all()
        for service in service_list:
            if (service.perm in enable_perms) or (user == self.owner):
                query |= service.perm.get_query(base=base, company=self)
        return query

    @cached_property
    def agents_count(self):
        return self.user_set.all().count()

    @cached_property
    def adverts_count(self):
        return self.advert_set.all().count()

    def title_crop(self):
        m = re.search(u'^Агентство Недвижимости «(.+)»$', self.title)
        if m:
            if m.group(1):
                self.title = m.group(1)

    def clear_cache(self):
        delete_template_fragment_cache('company_preview', unicode(self.id))

    def update_rating(self):
        self.rating = 5
        weights = {
            'adverts': 0.25,
            'perms_company': 1.5,
            'perms_users': 1,
            'agents': 0.25,
            'real': 1,
            'buys': 0.5
        }

        # заполненность реквизитов
        if self.image:
            self.rating += 0.1
        if self.tel:
            self.rating += 0.1
        if self.email:
            self.rating += 0.1
        if self.inn:
            self.rating += 0.1
        if self.address:
            self.rating += 0.1
        if self.body:
            self.rating += 0.1

        # Количество объявлений
        try:
            max_count = Company.objects.filter(advert__date__gte=datetime.now()-timedelta(days=30)).annotate(num_adverts=Count('advert')).order_by('-num_adverts')[:1]
            rate = float(Advert.objects.filter(company=self, status=Advert.STATUS_VIEW, date__gte=datetime.now()-timedelta(days=30)).count()) / \
                   float(max_count[0].num_adverts)
            self.rating += rate * weights['adverts']
        except:
            pass

        # Количество оплаченных разделов агентства
        try:
            rate = ConnectedService.objects.filter(company=self, end_date__gte=datetime.now(), active=True).count() / 10.0
            self.rating += rate * weights['perms_company']
        except:
            pass

        # Количество оплаченных разделов независимых агентов
        try:
            ind_users = [user.id for user in self.user_set.filter(independent=True, status=User.STATUS_ACTIVE)]
            rate = float(ConnectedService.objects.filter(user_id__in=ind_users, end_date__gte=datetime.now(), active=True).count()) / float(len(ind_users)) / 10.0
            self.rating += rate * weights['perms_users']
        except:
            pass

        # Количество агентов
        try:
            max_agents = Company.objects.annotate(num_agents=Count('user')).order_by('-num_agents')[:1]
            rate = float(User.objects.filter(company=self, status=User.STATUS_ACTIVE, is_active=True).count()) / \
                   float(max_agents[0].num_agents)
            self.rating += rate * weights['agents']
        except:
            pass

        # Подключенное
        if self.is_real:
            self.rating += 1 * weights['real']

        # Выкупы
        try:
            buys_users = User.objects.filter(company=self).aggregate(Sum('buys'))
            buys_all = User.objects.all().aggregate(Sum('buys'))
            rate = float(buys_users['buys_sum']) / float(buys_all['buys_sum'])
            self.rating += rate * weights['buys']
        except:
            pass

        self.save()

    def activate_freevk(self):
        perm = Perm.objects.get(code='freevk')
        list = ConnectedService.objects.filter(company=self, perm=perm)
        if not list:
            service = ConnectedService(company=self, perm=perm,
                                       start_date=datetime.now(), end_date=datetime.now() + timedelta(days=30),
                                       active=True)
            service.save()
            for user in self.user_set.all():
                print user.username
                user.activate_freevk()

    @staticmethod
    def activate_freevk_all():
        company_list = Company.objects.filter(is_real=True, hidden=False).exclude(status=Company.STATUS_BLOCK)
        for company in company_list:
            print company.title
            company.activate_freevk()

    def get_tel_list(self):
        return get_tel_list(self.tel)


class Perm(models.Model):
    """
    Элементарное право просмотра объявлений
    """
    title = models.CharField('Заголовок', max_length=250, default='')
    adtype = models.CharField('Тип объявления', max_length=1, default=None, choices=Advert.TYPES.items(), null=True, blank=True)
    need = models.CharField('Спрос/предложение', max_length=1, default=None, choices=Advert.NEEDS.items(), null=True, blank=True)
    estate = models.CharField('Тип недвижимости', max_length=1, default=None, choices=Advert.ESTATES.items(), null=True, blank=True)
    live = models.CharField('Тип жилой недвижимости', max_length=1, default=None, choices=Advert.LIVES.items(), null=True, blank=True)
    country = models.CharField('Тип загородной недвижимости', max_length=1, default=None, choices=Advert.COUNTRIES.items(), null=True, blank=True)
    commercial = models.CharField('Тип коммерческой недвижимости', max_length=1, default=None, choices=Advert.COMMERCIALS.items(), null=True, blank=True)
    territory = models.CharField('Тип земли', max_length=1, default=None, choices=Advert.TERRITORIES.items(), null=True, blank=True)
    day_limit = models.PositiveIntegerField('Кол-во объявлений в день', default=0)
    base_main = models.BooleanField('Основная база', default=True)
    base_vk = models.BooleanField('База Вконтакте', default=False)
    order = models.IntegerField('Cортировка', default=10, blank=True)
    code = models.CharField('Символьный код', max_length=50, default='', null=True, blank=True)

    class Meta:
        verbose_name = u'Право просмотра объявлений'
        verbose_name_plural = u'Права просмотра объявлений'
        ordering = ['title']

    def __unicode__(self):
        return self.title

    def get_query(self, base='main', user=None, company=None):
        query = Q()
        query_limit = Q(advert__company=None)
        if base == 'main' and self.base_main:
            if self.adtype:
                query &= Q(adtype=self.adtype)
                query_limit &= Q(advert__adtype=self.adtype)
            if self.need:
                query &= Q(need=self.need)
                query_limit &= Q(advert__need=self.need)
            if self.estate:
                query &= Q(estate=self.estate)
                query_limit &= Q(advert__estate=self.estate)
            if self.live:
                query &= Q(live=self.live)
                query_limit &= Q(advert__live=self.live)
            if self.country:
                query &= Q(country=self.country)
                query_limit &= Q(advert__country=self.country)
            if self.commercial:
                query &= Q(commercial=self.commercial)
                query_limit &= Q(advert__commercial=self.commercial)
            if self.territory:
                query &= Q(territory=self.territory)
                query_limit &= Q(advert__territory=self.territory)
            if user and self.day_limit:
                count = RegViewed.day_count_user(user, query=query_limit)
                if self.day_limit <= count:
                    query &= Q(id=None)
            if company and self.day_limit:
                count = RegViewed.day_count_company(company, query=query_limit)
                if self.day_limit <= count:
                    query &= Q(id=None)
        elif base == 'vk' and self.base_vk:
            query &= Q(id__isnull=False)
        return query


class WeekPerm(models.Model):
    """
    Ограничения для пользователей
    """
    DAYS = [
        (1, 'Понедельник'),
        (2, 'Вторник'),
        (3, 'Среда'),
        (4, 'Четверг'),
        (5, 'Пятница'),
        (6, 'Суббота'),
        (7, 'Воскресенье'),
    ]

    user = models.ForeignKey(User)
    day = models.IntegerField(choices=DAYS, default=1)
    min_hour = models.IntegerField(default=0, null=True, blank=True)
    max_hour = models.IntegerField(default=24, null=True, blank=True)
    active = models.BooleanField(default=True, blank=True)

    class Meta:
        verbose_name = u'Ограничения для пользователей по дням'

    def __unicode__(self):
        return self.title


class Tariff(models.Model):
    """
    Тариф
    """
    title = models.CharField(verbose_name='Название', max_length=250, default='')
    desc = models.TextField('Описание', null=True, blank=True)
    price = models.FloatField('Цена', default=100)
    perms = models.ManyToManyField(Perm, verbose_name='Права тарифа', blank=True, related_name='tariffs')
    order = models.IntegerField('Сортировка', blank=True, default=500)
    town = models.ManyToManyField(Town, verbose_name='Города', blank=True)
    code = models.CharField('Символьный код', max_length=30, default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'
        ordering = ['title']

    def __unicode__(self):
        return self.title


class PaymentItem(models.Model):
    """
    Элемент заказа
    """
    TYPE_TARIFF = 'T'
    TYPE_BUY = 'B'
    TYPES = {
        TYPE_TARIFF: 'Тариф',
        TYPE_BUY: 'Выкуп'
    }

    paytype = models.CharField(verbose_name='Тип платежа', max_length=1, default=TYPE_TARIFF, choices=TYPES.items())
    tariff = models.ForeignKey(Tariff, null=True, blank=True, default=None)
    quantity = models.PositiveIntegerField(verbose_name='Количество месяцев', default=1)
    total = models.FloatField(verbose_name='Сумма', default=0)
    price = models.FloatField(verbose_name='Цена', default=0)

    class Meta:
        verbose_name = 'Элемент заказ'
        verbose_name_plural = 'Элементы заказа'

    def __unicode__(self):
        if self.paytype == self.TYPE_TARIFF:
            return self.tariff.title
        else:
            return u'%s выкупов' % self.quantity

    def apply(self, user):
        if self.paytype == self.TYPE_TARIFF:
            self.apply_tariff(user)
        elif self.paytype == self.TYPE_BUY:
            self.apply_buy(user)

    def apply_tariff(self, user):
        use_company = user.company.owner == user
        for perm in self.tariff.perms.all():
            service_list = ConnectedService.objects.filter(user=user, perm=perm, end_date__gte=datetime.now()).order_by('-end_date')
            if service_list:
                service = ConnectedService(
                    company=user.company if use_company else None,
                    user=user,
                    tariff=self.tariff,
                    perm=perm,
                    months=self.quantity,
                    start_date=service_list[0].end_date,
                    end_date=service_list[0].end_date + timedelta(days=30 * self.quantity)
                )
                service.save()
            else:
                service = ConnectedService(
                    company=user.company if use_company else None,
                    user=user,
                    tariff=self.tariff,
                    perm=perm,
                    months=self.quantity,
                    start_date=datetime.now(),
                    end_date=datetime.now() + timedelta(days=30 * self.quantity)
                )
                service.save()

    def apply_buy(self, user):
        user.buys += self.quantity
        user.save()


class Payment(BasePayment):
    """
    Оплата
    """

    user = models.ForeignKey(User, verbose_name='Пользователь')
    items = models.ManyToManyField(PaymentItem, blank=True)
    discount = models.DecimalField(max_digits=9, decimal_places=2, default='0.0')
    promocode = models.ForeignKey(Promocode, verbose_name=u'Промокод', default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created']

    def success(self):
        item_list = self.items.all()
        for item in item_list:
            item.apply(self.user)

    def fail(self):
        pass

    def recalc_total(self):
        self.total = Decimal(self.sum) - Decimal(self.discount)
        if self.promocode:
            self.total -= self.promocode.get_discount(self.sum)

    @property
    def total_discount(self):
        result = self.discount
        if self.promocode:
            result += self.promocode.get_discount(self.sum)
        return result


def payment_received(sender, **kwargs):
    payment = Payment.objects.get(id=kwargs['InvId'])
    if payment.status != Payment.STATUS_CONFIRMED:
        payment.change_status(Payment.STATUS_CONFIRMED)
        payment.success()


def payment_fail(sender, **kwargs):
    payment = Payment.objects.get(id=kwargs['InvId'])
    payment.change_status(Payment.STATUS_REJECTED)
    payment.fail()

if settings.SITE_ID == 1:
    result_received.connect(payment_received)
    fail_page_visited.connect(payment_fail)


class ConnectedService(models.Model):
    """
    Подключенные услуги
    """
    company = models.ForeignKey(Company, verbose_name='Агентство', blank=True, null=True, default=None)
    user = models.ForeignKey(User, verbose_name='Агент', blank=True, null=True, default=None)
    tariff = models.ForeignKey(Tariff, verbose_name='Тариф', blank=True, null=True, default=None)
    perm = models.ForeignKey(Perm, verbose_name='Права', related_name='connectedservice')
    months = models.PositiveIntegerField('Количество месяцев', default=1)
    start_date = models.DateTimeField('Дата начала действия', default=datetime.now())
    end_date = models.DateTimeField('Дата конца действия', default=datetime.now())
    active = models.BooleanField('Активная', default=True, blank=True)

    class Meta:
        verbose_name = 'Подключенная услуга'
        verbose_name_plural = 'Подключенные услуги'
        ordering = ['start_date', 'end_date']

    @property
    def elapsed_time(self):
        if self.end_date < datetime.now():
            return 'Подписка истекла'
        else:
            delta = self.end_date - datetime.now()
            return mark_safe("%s&nbsp;д. %s&nbsp;ч. %s&nbsp;мин." % (delta.days, delta.seconds // 3600, delta.seconds % 3600 // 60))


class Abbr(models.Model):
    """
    Сокращения в описании
    """
    title = models.CharField('Сокращение', max_length=50)
    desc = models.CharField('Описание', max_length=250)

    class Meta:
        verbose_name = 'Сокращение'
        verbose_name_plural = 'Сокращения'
        ordering = ['title']

    def __unicode__(self):
        return self.title

    @staticmethod
    def abbry(txt):
        result = txt
        abbr_list = Abbr.objects.all()
        for abbr in abbr_list:
            result = result.replace(abbr.title, abbr.desc)
        return result


class Parser(models.Model):
    """
    парсеры
    """
    title = models.CharField('Название', max_length=50)
    desc = models.CharField('Описание', max_length=250, default='', blank=True, null=True)
    priority = models.IntegerField('Приоритет', default=10, blank=True)

    class Meta:
        verbose_name = 'Парсер'
        verbose_name_plural = 'Парсеры'

    def __unicode__(self):
        return self.title


class Subscribe(models.Model):
    """
    Подписка
    """
    title = models.CharField('Название', max_length=250)
    code = models.CharField('Код', max_length=50)
    subscribed = models.ManyToManyField(User, verbose_name='Подписанные', blank=True, related_name='subscribed')
    unsubscribed = models.ManyToManyField(User, verbose_name='Отписанные', blank=True, related_name='unsubscribed')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Почтовые рассылки'

    def __unicode__(self):
        return self.title

    @staticmethod
    def get_subscribe_code(code, user):
        subscribe = Subscribe.objects.get(code=code)
        code, created = SubscribeCode.objects.get_or_create(user=user, subscribe=subscribe, active=True)
        if created:
            code.code = id_generator(30)
            code.save()
        return code.code

    @staticmethod
    def get_unsubscribe_code(code, user):
        subscribe = Subscribe.objects.get(code=code)
        code, created = SubscribeCode.objects.get_or_create(user=user, subscribe=subscribe, active=False)
        if created:
            code.code = id_generator(30)
            code.save()
        return code.code


class SubscribeCode(models.Model):
    """
    Коды активации/деактивации подписки
    """
    subscribe = models.ForeignKey(Subscribe)
    user = models.ForeignKey(User)
    code = models.CharField('Код', max_length=30, default=id_generator(30))
    active = models.BooleanField('Вкл.', default=False, blank=True)

    class Meta:
        verbose_name = 'Код подписки'
        verbose_name_plural = 'Коды подписки'

    def __unicode__(self):
        return self.code


class SearchRequest(CachingMixin, models.Model):
    """
    Заявка на автопоиск
    """

    PERIODS = [
        (1, '1 день'),
        (3, '3 дня'),
        (7, '7 дней'),
    ]

    date = models.DateTimeField('Дата подачи', default=datetime.now(), db_index=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', null=True, blank=True, on_delete=models.SET_NULL)
    company = models.ForeignKey('Company', verbose_name='Агенство', null=True, blank=True)
    body = models.TextField('Описание', max_length=255, blank=True, null=True, default='')
    adtype = models.CharField('Тип объявления', max_length=1, default=Advert.TYPE_LEASE, choices=Advert.TYPES.items(), db_index=True)
    need = models.CharField('Спрос/предложение', max_length=1, default=Advert.NEED_SALE, choices=Advert.NEEDS.items(), db_index=True)
    estate = models.CharField('Тип недвижимости', max_length=1, default=Advert.ESTATE_LIVE, choices=Advert.ESTATES.items(), db_index=True)
    live = models.CharField('Тип жилой недвижимости', max_length=1, default=Advert.LIVE_FLAT, choices=Advert.LIVES.items())
    # live_room = models.BooleanField('Комната', default=False, blank=True)
    live_flat1 = models.BooleanField('1-к.', default=True, blank=True)
    live_flat2 = models.BooleanField('2-к.', default=False, blank=True)
    live_flat3 = models.BooleanField('3-к.', default=False, blank=True)
    live_flat4 = models.BooleanField('4+-к.', default=False, blank=True)
    country = models.CharField('Тип загородной недвижимости', max_length=1, default=Advert.COUNTRY_HOUSE, choices=Advert.COUNTRIES.items())
    commercial = models.CharField('Тип коммерческой недвижимости', max_length=1, default=Advert.COMMERCIAL_OFFICE, choices=Advert.COMMERCIALS.items())
    territory = models.CharField('Тип земли', max_length=1, default=Advert.TERR_BUILD, choices=Advert.TERRITORIES.items())
    limit = models.CharField('Срок', max_length=1, default=Advert.LIMIT_LONG, choices=Advert.LIMITS.items())
    town = models.ForeignKey(Town, verbose_name='Город')
    district = models.ManyToManyField('District', verbose_name='Район', blank=True)
    metro = models.ManyToManyField('Metro', verbose_name='Метро', blank=True)
    square = models.FloatField('Общая площадь, мин', default=None, blank=True, null=True)
    square_max = models.FloatField('Общая площадь, макс', default=None, blank=True, null=True)
    living_square = models.CharField('Жилая площадь, мин', max_length=30, blank=True, null=True)
    living_square_max = models.CharField('Жилая площадь, макс', max_length=30, blank=True, null=True)
    kitchen_square = models.FloatField('Площадь кухни, мин', blank=True, null=True)
    kitchen_square_max = models.FloatField('Площадь кухни, макс', blank=True, null=True)
    # rooms = models.IntegerField('Количество комнат', blank=True, null=True)
    price = models.FloatField('Цена', blank=True, null=True)
    min_price = models.FloatField('Цена от', blank=True, null=True)

    # удобства -----------------

    # интерьер
    refrigerator = models.BooleanField('Холодильник', default=False, blank=True)
    tv = models.BooleanField('Телевизор', default=False, blank=True)
    washer = models.BooleanField('Стиральная машина', default=False, blank=True)
    phone = models.BooleanField('Телефон', default=False, blank=True)
    internet = models.BooleanField('Интернет', default=False, blank=True)
    conditioner = models.BooleanField('Кондиционер', default=False, blank=True)
    furniture = models.BooleanField('Мебель', default=False, blank=True)
    separate_wc = models.BooleanField('Раздельный санузел', default=False, blank=True)
    balcony = models.BooleanField('Балкон', default=False, blank=True)
    # ремонт
    euroremont = models.BooleanField('Евроремонт', default=False, blank=True)
    redecoration = models.BooleanField('Косметический ремонт', default=False, blank=True)
    no_remont = models.BooleanField('Без ремонта', default=False, blank=True)
    need_remont = models.BooleanField('Требуется ремонт', default=False, blank=True)
    # коммуникации
    electric = models.BooleanField('Электричество', default=False, blank=True)
    gas = models.BooleanField('Газ', default=False, blank=True)
    water = models.BooleanField('Вода', default=False, blank=True)
    sewage = models.BooleanField('Канализация', default=False, blank=True)
    brick_building = models.BooleanField('Кирпичная постройка', default=False, blank=True)
    wood_building = models.BooleanField('Деревянная постройка', default=False, blank=True)
    # проживание
    live_one = models.BooleanField('Одному чел.', default=False, blank=True)
    live_two = models.BooleanField('2-м людям', default=False, blank=True)
    live_pare = models.BooleanField('Семейной паре', default=False, blank=True)
    live_more = models.BooleanField('Более 2-х чел.', default=False, blank=True)
    live_child = models.BooleanField('Можно с детьми', default=False, blank=True)
    live_animal = models.BooleanField('Можно с животными', default=False, blank=True)
    live_girl = models.BooleanField('Для девушек', default=False, blank=True)
    live_man = models.BooleanField('Для мужчин', default=False, blank=True)
    # разное
    parking = models.BooleanField('Парковка', default=False, blank=True)
    lift = models.BooleanField('Лифт', default=False, blank=True)
    concierge = models.BooleanField('Консьерж', default=False, blank=True)
    guard = models.BooleanField('Охрана', default=False, blank=True)
    garage = models.BooleanField('Гараж', default=False, blank=True)

    floor = models.PositiveIntegerField('Этаж от', default=None, blank=True, null=True)
    floor_max = models.PositiveIntegerField('Этаж до', default=None, blank=True, null=True)

    active = models.BooleanField('Активность заявки', default=False, db_index=True)

    owner_name = models.CharField('ФИО клиента', max_length=250, null=True, blank=True)
    owner_tel = models.CharField('Телефон клиента', max_length=50, null=True, blank=True)
    owner_email = models.EmailField('E-mail клиента', null=True, blank=True)

    period = models.PositiveIntegerField('Период', default=1, choices=PERIODS)
    from_agent = models.BooleanField('От агентов', default=False, blank=True)
    from_owner = models.BooleanField('От собственников', default=True, blank=True)

    #возможные клиенты объявления
    clients = models.ManyToManyField('Advert', blank=True)
    last_viewed_count = models.IntegerField(default=0, null=True, blank=True)

    advert_noticed = models.ManyToManyField('Advert', verbose_name='Уведомления об заявке', blank=True, related_name='search_request_noticed')
    advert_not_send = models.ManyToManyField('Advert', blank=True, related_name='search_request_not_send')

    site = models.ForeignKey(Site, verbose_name='Сайт', blank=True, null=True)

    objects = CachingManager()

    class Meta:
        verbose_name = u'Заявка на автопоиск'
        verbose_name_plural = u'Заявки на автопоиск'
        ordering = ['-date']

    def __unicode__(self):
        return self.title

    @staticmethod
    def get_site_notice_func():
        from main.task import send_search_request_notice as main_sr_notice
        from vashdom.tasks import send_search_request_notice as vashdom_sr_notice

        SITE_NOTICE_FUNC = {
            1: main_sr_notice,
            5: vashdom_sr_notice,
        }
        return SITE_NOTICE_FUNC

    def save(self, *args, **kwargs):
        if not self.site:
            self.site = Site.objects.get_current()
        return super(SearchRequest, self).save(*args, **kwargs)

    @property
    def comfort_list(self):
        result = []
        for field in ['refrigerator',
                      'washer',
                      'tv',
                      'phone',
                      'internet',
                      'conditioner',
                      'furniture',
                      'euroremont',
                      'separate_wc',
                      'balcony',
                      'lift',
                      'parking',
                      'redecoration',
                      'no_remont',
                      'need_remont',
                      'electric',
                      'gas',
                      'water',
                      'sewage',
                      'brick_building',
                      'wood_building',
                      'live_one',
                      'live_two',
                      'live_pare',
                      'live_more',
                      'live_child',
                      'live_animal',
                      'live_girl',
                      'live_man',
                      'concierge',
                      'guard',
                      'garage']:
            result.append((field,
                           getattr(self, field),
                           self._meta.get_field(field).verbose_name
            ))
        return result

    def find_clients(self):

        query = Q(town=self.town,
                  estate=self.estate,
                  adtype=self.adtype,
                  date__gte=datetime.now() - timedelta(days=self.period),
                  status=Advert.STATUS_VIEW)
        if self.estate == Advert.ESTATE_LIVE:
            query &= Q(live=self.live, limit=self.limit)
            if self.live == Advert.LIVE_FLAT:
                live_query = Q(rooms=0)
                if self.live_flat1:
                    live_query |= Q(rooms=1)
                if self.live_flat2:
                    live_query |= Q(rooms=2)
                if self.live_flat3:
                    live_query |= Q(rooms=3)
                if self.live_flat4:
                    live_query |= Q(rooms__gte=4)
                query &= live_query
        elif self.estate == Advert.ESTATE_COUNTRY:
            query &= Q(country=self.country, limit=self.limit)
        elif self.estate == Advert.ESTATE_COMMERCIAL:
            query &= Q(commercial=self.commercial)
        elif self.estate == Advert.ESTATE_TERRITORY:
            query &= Q(territory=self.territory)

        metro_list = self.metro.all()
        if metro_list:
            query &= Q(metro__in=[metro for metro in metro_list])
        district_list = self.district.all()
        if district_list:
            query &= Q(district__in=[district for district in district_list])
        if self.price:
            query &= Q(price__lte=self.price)
        if self.min_price:
            query &= Q(price__gte=self.min_price)
        if self.floor:
            query &= Q(floor__gte=self.floor)
        if self.floor_max:
            query &= Q(floor__lte=self.floor_max)
        if self.square:
            query &= Q(square__gte=self.square)
        if self.square_max:
            query &= Q(square__lte=self.square_max)
        if self.living_square:
            query &= Q(living_square__gte=self.living_square)
        if self.living_square_max:
            query &= Q(living_square__lte=self.living_square_max)
        if self.kitchen_square:
            query &= Q(kitchen_square__gte=self.kitchen_square)
        if self.kitchen_square_max:
            query &= Q(kitchen_square__lte=self.kitchen_square_max)
        if self.need == Advert.NEED_SALE:
            query &= Q(need=Advert.NEED_DEMAND)
        else:
            query &= Q(need=Advert.NEED_SALE)

        from_query = Q()
        if self.from_agent:
            from_query |= Q(company__isnull=False)
        if self.from_owner:
            from_query |= Q(company__isnull=True)
        query &= from_query

        for comfort in self.comfort_list:
            if comfort[1]:
                kwargs = {comfort[0]: comfort[1]}
                query &= Q(**kwargs)

        if self.site.domain == 'bazavashdom.ru':
            price_query = Q()
            if self.town.slug == 'moskva':
                price_query |= (Q(live=Advert.LIVE_ROOM, price__gte=12000, price__lte=35000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=1, price__gte=25000, price__lte=45000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=2, price__gte=30000, price__lte=82000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=3, price__gte=40000, price__lte=92000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms__gte=4, price__gte=45000, price__lte=100000))
            elif self.town.slug == 'sankt-peterburg':
                price_query |= (Q(live=Advert.LIVE_ROOM, price__gte=7000, price__lte=15000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=1, price__gte=15000, price__lte=35000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=2, price__gte=18000, price__lte=40000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=3, price__gte=18000, price__lte=45000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms__gte=4, price__gte=20000, price__lte=55000))
            elif self.town.slug == 'novosibirsk':
                price_query |= (Q(live=Advert.LIVE_ROOM, price__gte=7000, price__lte=11000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=1, price__gte=12000, price__lte=21000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=2, price__gte=15000, price__lte=25000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=3, price__gte=17000, price__lte=33000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms__gte=4, price__gte=18000, price__lte=35000))
            elif self.town.slug == 'ekaterinburg':
                price_query |= (Q(live=Advert.LIVE_ROOM, price__gte=7000, price__lte=11000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=1, price__gte=9000, price__lte=21000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=2, price__gte=12000, price__lte=25000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=3, price__gte=17000, price__lte=33000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms__gte=4, price__gte=18000, price__lte=35000))
            query &= price_query

        clear_list = self.clients.exclude(id__in=[a.id for a in self.advert_noticed.all()])
        self.clients.remove(*clear_list)

        client_list = Advert.objects.filter(query).order_by('-date')
        for advert in client_list[:settings.SEARCH_REQUEST_COUNT_LIMIT]:
            self.clients.add(advert)
        self.clear_cache()
        if not settings.DEBUG:
            if self.active:
                notice_func = self.get_site_notice_func()[self.site_id]
                notice_func.apply_async(kwargs={'id': self.id}, countdown=900)
        return len(client_list)

    def send_client_notice(self):
        from django.core import mail
        from main.task import send_search_request_notice
        if self.active:
            connection = mail.get_connection(host=settings.SECONDARY_EMAIL_HOST,
                                             port=settings.SECONDARY_EMAIL_PORT,
                                             username=settings.SECONDARY_EMAIL_USERNAME,
                                             password=settings.SECONDARY_EMAIL_PASSWORD,
                                             use_tls=True)
            advert_exclude = [advert.id for advert in self.advert_noticed.all()] + \
                                  [advert.id for advert in self.advert_not_send.all()]
            advert_list = self.clients.all().exclude(id__in=advert_exclude)
            count_adverts = advert_list.count()
            al = advert_list[:settings.SEARCH_REQUEST_NOTICE_LIMIT]
            if count_adverts > 0:
                send_mail('main/email/search-request-notice.html', {
                    'client_name': self.owner_name,
                    'advert_list': al,
                    'search_request': self,
                    'agent_tel': self.user.tel,
                    'agent_email': self.user.email,
                    'subject': 'По вашему запросу были найдены несколько объявлений',
                    },
                          recipient_list=[self.owner_email],
                          fail_silently=True,
                          from_email=settings.SECONDARY_EMAIL_FROM,
                          connection=connection)
                self.advert_noticed.add(*[a.id for a in al])

            if len(al) < count_adverts:
                send_search_request_notice.apply_async(kwargs={'id': self.id}, countdown=900)

    def send_vashdom_notice(self):
        from vashdom.tasks import send_search_request_notice
        if self.active:
            advert_exclude = [advert.id for advert in self.advert_noticed.all()] + \
                                  [advert.id for advert in self.advert_not_send.all()]
            advert_list = self.clients.all().exclude(id__in=advert_exclude)
            count_adverts = advert_list.count()
            al = advert_list[:settings.SEARCH_REQUEST_NOTICE_LIMIT]
            if count_adverts > 0:
                send_mail('vashdom/email/search-request-notice.html', {
                    'client_name': self.owner_name,
                    'advert_list': al,
                    'search_request': self,
                    'subject': 'По вашему запросу были найдены несколько объявлений',
                    },
                          recipient_list=[self.owner_email],
                          fail_silently=True)
                self.advert_noticed.add(*[a.id for a in al])

            if len(al) < count_adverts:
                send_search_request_notice.apply_async(kwargs={'id': self.id}, countdown=900)


    @cached_property
    def count_clients(self):
        return self.clients.count()

    def clear_cache(self):
        delete_template_fragment_cache('search_request_preview', unicode(self.id))
        if self.user:
            self.user.clear_cache()

    @property
    def title(self):
        result = ''
        if self.need == Advert.NEED_SALE:
            if self.estate == Advert.ESTATE_LIVE:
                if self.live == Advert.LIVE_ROOM:
                    if self.adtype == Advert.TYPE_LEASE:
                        result = u'Сдам комнату' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                    elif self.adtype == Advert.TYPE_SALE:
                        result = u'Продам комнату'
                elif self.live == Advert.LIVE_FLAT:
                    if self.adtype == Advert.TYPE_LEASE:
                        result = u'Сдам квартиру' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                    elif self.adtype == Advert.TYPE_SALE:
                        result = u'Продам квартиру'

                    flat_array = []
                    if self.live_flat1:
                        flat_array.append('1')
                    if self.live_flat2:
                        flat_array.append('2')
                    if self.live_flat3:
                        flat_array.append('3')
                    if self.live_flat4:
                        flat_array.append('4')
                    result += u' (%s комн.)' % u','.join(flat_array)

            elif self.estate == Advert.ESTATE_TERRITORY:
                if self.adtype == Advert.TYPE_LEASE:
                    result = u'Аренда земельного участка' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == Advert.TYPE_SALE:
                    result = u'Продам земельный участок'

            elif self.estate == Advert.ESTATE_COUNTRY:
                if self.adtype == Advert.TYPE_LEASE:
                    if self.count_floor:
                        result = u'Сдам %s этаж. дом в аренду' % self.count_floor + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                    else:
                        result = u'Сдам дом в аренду' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == Advert.TYPE_SALE:
                    result = u'Продам дом'

            elif self.estate == Advert.ESTATE_COMMERCIAL:
                if self.adtype == Advert.TYPE_LEASE:
                    result = u'Сдам помещение в аренду' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == Advert.TYPE_SALE:
                    result = u'Продам помещение'
        elif self.need == Advert.NEED_DEMAND:
            if self.estate == Advert.ESTATE_LIVE:
                if self.live == Advert.LIVE_ROOM:
                    if self.adtype == Advert.TYPE_LEASE:
                        result = u'Сниму комнату' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                    elif self.adtype == Advert.TYPE_SALE:
                        result = u'Куплю комнату'
                elif self.live == Advert.LIVE_FLAT:
                    if self.adtype == Advert.TYPE_LEASE:
                        result = u'Сниму квартиру' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                    elif self.adtype == Advert.TYPE_SALE:
                        result = u'Куплю квартиру'
                    flat_array = []
                    if self.live_flat1:
                        flat_array.append('1')
                    if self.live_flat2:
                        flat_array.append('2')
                    if self.live_flat3:
                        flat_array.append('3')
                    if self.live_flat4:
                        flat_array.append('4')
                    result += u' (%s комн.)' % u','.join(flat_array)

            elif self.estate == Advert.ESTATE_TERRITORY:
                if self.adtype == Advert.TYPE_LEASE:
                    result = u'Арендую земельный участок'
                elif self.adtype == Advert.TYPE_SALE:
                    result = u'Куплю земельный участок'

            elif self.estate == Advert.ESTATE_COUNTRY:
                if self.adtype == Advert.TYPE_LEASE:
                    result = u'Возьму дом в аренду' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == Advert.TYPE_SALE:
                    result = u'Куплю дом'

            elif self.estate == Advert.ESTATE_COMMERCIAL:
                if self.adtype == Advert.TYPE_LEASE:
                    result = u'Возьму помещение в аренду' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == Advert.TYPE_SALE:
                    result = u'Куплю помещение'

        return result

    @property
    def short_title(self):
        result = ''
        if self.need == Advert.NEED_SALE:
            if self.estate == Advert.ESTATE_LIVE:
                if self.live == Advert.LIVE_ROOM:
                    if self.adtype == Advert.TYPE_LEASE:
                        result = u'Сдам комн.' + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                    elif self.adtype == Advert.TYPE_SALE:
                        result = u'Продам комн.'
                elif self.live == Advert.LIVE_FLAT:
                    if self.adtype == Advert.TYPE_LEASE:
                        result = u'Сдам' + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                    elif self.adtype == Advert.TYPE_SALE:
                        result = u'Продам'

                    flat_array = []
                    if self.live_flat1:
                        flat_array.append('1')
                    if self.live_flat2:
                        flat_array.append('2')
                    if self.live_flat3:
                        flat_array.append('3')
                    if self.live_flat4:
                        flat_array.append('4')
                    result += u' (%s комн.)' % u','.join(flat_array)

            elif self.estate == Advert.ESTATE_TERRITORY:
                if self.adtype == Advert.TYPE_LEASE:
                    result = u'Сдам зем.участок' + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == Advert.TYPE_SALE:
                    result = u'Продам зем.участок'

            elif self.estate == Advert.ESTATE_COUNTRY:
                if self.adtype == Advert.TYPE_LEASE:
                    if self.count_floor:
                        result = u'Сдам %s этаж. дом' % self.count_floor + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                    else:
                        result = u'Сдам дом' + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == Advert.TYPE_SALE:
                    result = u'Продам дом'

            elif self.estate == Advert.ESTATE_COMMERCIAL:
                if self.adtype == Advert.TYPE_LEASE:
                    result = u'Сдам помещение' + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == Advert.TYPE_SALE:
                    result = u'Продам помещение'
        elif self.need == Advert.NEED_DEMAND:
            if self.estate == Advert.ESTATE_LIVE:
                if self.live == Advert.LIVE_ROOM:
                    if self.adtype == Advert.TYPE_LEASE:
                        result = u'Сниму комн.' + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                    elif self.adtype == Advert.TYPE_SALE:
                        result = u'Куплю комн.'
                elif self.live == Advert.LIVE_FLAT:
                    if self.adtype == Advert.TYPE_LEASE:
                        result = u'Сниму кв.' + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                    elif self.adtype == Advert.TYPE_SALE:
                        result = u'Куплю кв.'
                    flat_array = []
                    if self.live_flat1:
                        flat_array.append('1')
                    if self.live_flat2:
                        flat_array.append('2')
                    if self.live_flat3:
                        flat_array.append('3')
                    if self.live_flat4:
                        flat_array.append('4')
                    result += u' (%s комн.)' % u','.join(flat_array)

            elif self.estate == Advert.ESTATE_TERRITORY:
                if self.adtype == Advert.TYPE_LEASE:
                    result = u'Арендую участок'
                elif self.adtype == Advert.TYPE_SALE:
                    result = u'Куплю участок'

            elif self.estate == Advert.ESTATE_COUNTRY:
                if self.adtype == Advert.TYPE_LEASE:
                    result = u'Возьму дом в аренду' + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == Advert.TYPE_SALE:
                    result = u'Куплю дом'

            elif self.estate == Advert.ESTATE_COMMERCIAL:
                if self.adtype == Advert.TYPE_LEASE:
                    result = u'Возьму помещение в аренду' + (u' посут.' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == Advert.TYPE_SALE:
                    result = u'Куплю помещение'

        return result

    @property
    def last_add_client_count(self):
        return self.count_clients - self.last_viewed_count


def sr_clear_user_cache(sender, instance, *args, **kwargs):
    if instance.user:
        instance.user.clear_cache()

post_save.connect(sr_clear_user_cache, sender=SearchRequest)
post_delete.connect(sr_clear_user_cache, sender=SearchRequest)


class ClientRequest(CachingMixin, models.Model):
    """
    Заявка от клиента
    """
    date = models.DateTimeField('Дата подачи', default=datetime.now(), db_index=True)
    user = models.ForeignKey(User, verbose_name='Агент', null=True, blank=True)
    body = models.TextField('Комментарий к заявке', max_length=255, blank=True, null=True, default='')
    name = models.CharField('Ваше имя', max_length=250, null=True, blank=True)
    tel = models.CharField('Телефон', max_length=50, null=True, blank=True)
    email = models.EmailField('E-mail', null=True, blank=True)
    adverts = models.ManyToManyField('Advert', blank=True)
    is_viewed = models.BooleanField('Просмотрена пользователем', default=True, db_index=True)

    objects = CachingManager()

    class Meta:
        verbose_name = u'Заявка от клиента'
        verbose_name_plural = u'Заявки от клиентов'
        ordering = ['-date']

    def __unicode__(self):
        return self.title

    @cached_property
    def count_adverts(self):
        return self.adverts.all().count()


def cr_clear_user_cache(sender, instance, *args, **kwargs):
    instance.user.clear_cache()

post_save.connect(cr_clear_user_cache, sender=ClientRequest)
post_delete.connect(cr_clear_user_cache, sender=ClientRequest)


class MetroDistance(CachingMixin, models.Model):
    """
    Расстояние до метро
    """
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE)
    metro = models.ForeignKey(Metro, on_delete=models.CASCADE)
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')
    duration_transport = models.FloatField('Время на автобусе', null=True, blank=True)
    distance_transport = models.FloatField('Расстояние на автобусе', null=True, blank=True)
    duration_driving = models.FloatField('Время на машине', null=True, blank=True)
    distance_driving = models.FloatField('Расстояние на машине', null=True, blank=True)

    objects = CachingManager()

    class Meta:
        verbose_name = u'Расстояние до метро'
