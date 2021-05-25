# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime, timedelta
from uimg.models import UserImage, get_user_image_path
from uprofile.models import User
import urllib
from django.db.models import Q
from gutils.views import delete_template_fragment_cache
from django.shortcuts import get_object_or_404
from mail_templated import send_mail
from django.conf import settings
from django.utils.functional import cached_property
from django.core.urlresolvers import reverse
from main.models.general import Town, District, Metro, Complain
from django.contrib.contenttypes.fields import GenericRelation
import random
from django.contrib.sites.models import Site
from caching.base import CachingManager, CachingMixin


class VKAdvert(CachingMixin, models.Model):
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

    ARCHIVE_YES_QUERY = (Q(adtype=TYPE_LEASE, date__lte=datetime.now()-timedelta(days=settings.ARCHIVE_LEASE_DAYS)) | Q(adtype=TYPE_SALE, date__lte=datetime.now()-timedelta(days=settings.ARCHIVE_SALE_DAYS)))
    ARCHIVE_NO_QUERY = (Q(adtype=TYPE_LEASE, date__gte=datetime.now()-timedelta(days=settings.ARCHIVE_LEASE_DAYS)) | Q(adtype=TYPE_SALE, date__gte=datetime.now()-timedelta(days=settings.ARCHIVE_SALE_DAYS)))

    date = models.DateTimeField(u'Дата подачи', default=datetime.now(), db_index=True)
    date_vashdom = models.DateTimeField(u'Дата подачи', default=datetime.now, db_index=True)
    date_smart = models.DateTimeField(u'Дата подачи', default=datetime.now, db_index=True)
    date_roomas = models.DateTimeField(u'Дата подачи', default=datetime.now, db_index=True)
    date_stopagent = models.DateTimeField(u'Дата подачи', default=datetime.now, db_index=True)
    body = models.TextField(u'Описание', blank=True, null=True, default='')
    body_hash = models.CharField(u'Хеш описания', max_length=50, blank=True, null=True, default='')
    images = models.ManyToManyField(UserImage, verbose_name=u'Изображения', blank=True, related_name='vkadverts')
    adtype = models.CharField(u'Тип объявления', max_length=1, default=TYPE_LEASE, choices=TYPES.items(), db_index=True)
    need = models.CharField(u'Спрос/предложение', max_length=1, default=NEED_SALE, choices=NEEDS.items(), db_index=True)
    estate = models.CharField(u'Тип недвижимости', max_length=1, default=ESTATE_LIVE, choices=ESTATES.items(), db_index=True)
    live = models.CharField(u'Тип жилой недвижимости', max_length=1, default=LIVE_FLAT, choices=LIVES.items(), db_index=True)
    # live_flat1 = models.BooleanField('1к', default=False, blank=True)
    # live_flat2 = models.BooleanField('2к', default=False, blank=True)
    # live_flat3 = models.BooleanField('3к', default=False, blank=True)
    # live_flat4 = models.BooleanField('4к+', default=False, blank=True)
    country = models.CharField(u'Тип загородной недвижимости', max_length=1, default=COUNTRY_HOUSE, choices=COUNTRIES.items())
    commercial = models.CharField(u'Тип коммерческой недвижимости', max_length=1, default=COMMERCIAL_OFFICE, choices=COMMERCIALS.items())
    territory = models.CharField(u'Тип земли', max_length=1, default=TERR_BUILD, choices=TERRITORIES.items())
    limit = models.CharField(u'Срок', max_length=1, default=LIMIT_LONG, choices=LIMITS.items(), db_index=True)
    address = models.TextField(u'Адрес', max_length=255, blank=True, null=True, default='')
    town = models.ForeignKey(Town, verbose_name=u'Город', db_index=True)
    district = models.ForeignKey(District, verbose_name=u'Район', blank=True, null=True)
    metro = models.ForeignKey(Metro, verbose_name=u'Метро', blank=True, null=True)
    square = models.FloatField(u'Общая площадь', default=None, blank=True, null=True)
    living_square = models.CharField(u'Жилая площадь', max_length=30, blank=True, null=True)
    kitchen_square = models.FloatField(u'Площадь кухни', blank=True, null=True)
    rooms = models.IntegerField(u'Количество комнат', blank=True, null=True)
    price = models.FloatField(u'Цена', blank=True, null=True)

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

    latitude = models.FloatField(u'Широта', blank=True, null=True)
    longitude = models.FloatField(u'Долгота', blank=True, null=True)

    floor = models.PositiveIntegerField(u'Этаж', default=None, blank=True, null=True)
    count_floor = models.PositiveIntegerField(u'Всего этажей', default=None, blank=True, null=True)

    extnum = models.CharField(u'Внешний код', max_length=50, default=None, null=True, blank=True)

    owner_name = models.CharField(u'ФИО собственника', max_length=250, null=True, blank=True)
    owner_vkid = models.CharField(u'ID собственника', max_length=50, null=True, blank=True)
    owner_tel = models.CharField(u'Телефон', max_length=50, null=True, blank=True, default='')
    owner_photo = models.ForeignKey(UserImage, blank=True, null=True)

    status = models.CharField(u'Статус объявления', max_length=1, default=STATUS_VIEW, choices=STATUSES.items(), db_index=True)
    views = models.IntegerField(u'Просмотры', default=0, blank=True)
    views_tel = models.IntegerField(u'Просмотры контактов', default=0, blank=True)

    #пользователи просмотревшие телефон
    viewed = models.ManyToManyField(User, blank=True, related_name='vkviewed')
    complained = GenericRelation(Complain)

    objects = CachingManager()

    class Meta:
        verbose_name = u'Объявление Вконтакте'
        verbose_name_plural = u'Объявления Вконтакте'
        ordering = ['-date']

    def __unicode__(self):
        return self.title

    @property
    def title(self):
        result = ''
        if self.need == self.NEED_SALE:
            if self.estate == self.ESTATE_LIVE:
                if self.live == self.LIVE_ROOM:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сдам комнату' + (u' посуточно' if self.limit == VKAdvert.LIMIT_DAY else u'')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Продам комнату'
                elif self.live == self.LIVE_FLAT:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сдам квартиру' + (u' посуточно' if self.limit == VKAdvert.LIMIT_DAY else u'')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Продам квартиру'
                    if self.rooms:
                        result += u' (%s комн.)' % self.rooms
    
            elif self.estate == self.ESTATE_TERRITORY:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Аренда земельного участка' + (u' посуточно' if self.limit == VKAdvert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Продам земельный участок'
    
            elif self.estate == self.ESTATE_COUNTRY:
                if self.adtype == self.TYPE_LEASE:
                    if self.count_floor:
                        result = u'Сдам %s этаж. дом в аренду' % self.count_floor + (u' посуточно' if self.limit == VKAdvert.LIMIT_DAY else u'')
                    else:
                        result = u'Сдам дом в аренду' + (u' посуточно' if self.limit == VKAdvert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Продам дом'
    
            elif self.estate == self.ESTATE_COMMERCIAL:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Сдам помещение в аренду' + (u' посуточно' if self.limit == VKAdvert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Продам помещение'
        elif self.need == self.NEED_DEMAND:
            if self.estate == self.ESTATE_LIVE:
                if self.live == VKAdvert.LIVE_ROOM:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сниму комнату' + (u' посуточно' if self.limit == VKAdvert.LIMIT_DAY else u'')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Куплю комнату'
                elif self.live == VKAdvert.LIVE_FLAT:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сниму квартиру' + (u' посуточно' if self.limit == VKAdvert.LIMIT_DAY else u'')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Куплю квартиру'
                    if self.rooms:
                        result += u' (%s комн.)' % self.rooms
    
            elif self.estate == self.ESTATE_TERRITORY:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Арендую земельный участок'
                elif self.adtype == self.TYPE_SALE:
                    result = u'Куплю земельный участок'
    
            elif self.estate == self.ESTATE_COUNTRY:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Возьму дом в аренду' + (u' посуточно' if self.limit == VKAdvert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Куплю дом'
    
            elif self.estate == self.ESTATE_COMMERCIAL:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Возьму помещение в аренду' + (u' посуточно' if self.limit == VKAdvert.LIMIT_DAY else u'')
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
                        result = u'Сдам комн.' + (u' посут.' if self.limit == VKAdvert.LIMIT_DAY else u'')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Продам комн.'
                elif self.live == self.LIVE_FLAT:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сдам' + (u' посут.' if self.limit == VKAdvert.LIMIT_DAY else u'')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Продам'
                    if self.rooms:
                        result += u' %s комн.кв.' % self.rooms
                    else:
                        result += u' кв.'

            elif self.estate == self.ESTATE_TERRITORY:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Сдам зем.участок' + (u' посут.' if self.limit == VKAdvert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Продам зем.участок'

            elif self.estate == self.ESTATE_COUNTRY:
                if self.adtype == self.TYPE_LEASE:
                    if self.count_floor:
                        result = u'Сдам %s этаж. дом' % self.count_floor + (u' посут.' if self.limit == VKAdvert.LIMIT_DAY else u'')
                    else:
                        result = u'Сдам дом' + (u' посут.' if self.limit == VKAdvert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Продам дом'

            elif self.estate == self.ESTATE_COMMERCIAL:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Сдам помещение' + (u' посут.' if self.limit == VKAdvert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Продам помещение'
        elif self.need == self.NEED_DEMAND:
            if self.estate == self.ESTATE_LIVE:
                if self.live == VKAdvert.LIVE_ROOM:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сниму комн.' + (u' посут.' if self.limit == VKAdvert.LIMIT_DAY else u'')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Куплю комн.'
                elif self.live == VKAdvert.LIVE_FLAT:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сниму кв.' + (u' посут.' if self.limit == VKAdvert.LIMIT_DAY else u'')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Куплю кв.'
                    if self.rooms:
                        result += u' (%s комн.)' % self.rooms

            elif self.estate == self.ESTATE_TERRITORY:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Арендую участок'
                elif self.adtype == self.TYPE_SALE:
                    result = u'Куплю участок'

            elif self.estate == self.ESTATE_COUNTRY:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Возьму дом в аренду' + (u' посут.' if self.limit == VKAdvert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Куплю дом'

            elif self.estate == self.ESTATE_COMMERCIAL:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Возьму помещение в аренду' + (u' посут.' if self.limit == VKAdvert.LIMIT_DAY else u'')
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
                    result = u'Сдается'
                elif self.adtype == self.TYPE_SALE:
                    result = u'Продается'

            elif self.need == self.NEED_DEMAND:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Снять'
                elif self.adtype == self.TYPE_SALE:
                    result = u'Купить'
            return result

        def obj():
            result = u''
            if self.estate == VKAdvert.ESTATE_LIVE:
                result = VKAdvert.LIVES[self.live].lower()
            elif self.estate == VKAdvert.ESTATE_COUNTRY:
                result = VKAdvert.COUNTRIES[self.country].lower()
            elif self.estate == VKAdvert.ESTATE_COMMERCIAL:
                result = VKAdvert.COMMERCIALS[self.commercial].lower() + u' помещение'
            elif self.estate == VKAdvert.ESTATE_TERRITORY:
                result = VKAdvert.TERRITORIES[self.territory].lower()
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
            if self.estate in [VKAdvert.ESTATE_LIVE, VKAdvert.ESTATE_COUNTRY] and self.adtype == VKAdvert.TYPE_LEASE:
                if self.limit == VKAdvert.LIMIT_DAY:
                    return u'посуточно'
                else:
                    return u'длительно'
            return u''

        def room_text():
            if (self.estate == VKAdvert.ESTATE_LIVE and self.live == VKAdvert.LIVE_FLAT) or \
                (self.estate == VKAdvert.ESTATE_COUNTRY):
                if self.rooms:
                    return u'%s комнатная' % self.rooms
            return u''

        def floor_text():
            if self.estate == VKAdvert.ESTATE_COUNTRY:
                return u'%s этаж' % self.count_floor
            return u''

        def square_text():
            if self.estate in [VKAdvert.ESTATE_COMMERCIAL, VKAdvert.ESTATE_TERRITORY]:
                if self.square:
                    return u'%.0f м2' % self.square
            return u''

        result = u' '.join([action(), limit_text(), room_text(), floor_text(), obj(), square_text(), town_name(), metro_name(), address_text()])
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
            if self.estate == VKAdvert.ESTATE_LIVE:
                result = VKAdvert.LIVES[self.live].lower()
            elif self.estate == VKAdvert.ESTATE_COUNTRY:
                result = VKAdvert.COUNTRIES[self.country].lower()
            elif self.estate == VKAdvert.ESTATE_COMMERCIAL:
                result = VKAdvert.COMMERCIALS[self.commercial].lower() + u' помещение'
            elif self.estate == VKAdvert.ESTATE_TERRITORY:
                result = VKAdvert.TERRITORIES[self.territory].lower()
            return result

        def room_text():
            if (self.estate == VKAdvert.ESTATE_LIVE and self.live == VKAdvert.LIVE_FLAT) or \
                    (self.estate == VKAdvert.ESTATE_COUNTRY):
                if self.need == VKAdvert.NEED_SALE:
                    if self.rooms:
                        return u'%s комнатная' % self.rooms
                elif self.need == VKAdvert.NEED_DEMAND:
                    if self.rooms:
                        return u'%s комнатная' % self.rooms
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
            if self.estate in [VKAdvert.ESTATE_LIVE, VKAdvert.ESTATE_COUNTRY] and self.adtype == VKAdvert.TYPE_LEASE:
                if self.limit == VKAdvert.LIMIT_DAY:
                    return u'посуточно'
                else:
                    return u'длительно'
            return u''

        def address_text():
            if self.address:
                return self.address.strip().replace(u',', '')
            else:
                return ''

        def owner_tags():
            return u'Собственник, от собстенника, Без комиссии, Без агентов, База собственников'

        def flat_tags():
            return u'База квартир'

        def sale_tags():
            return u'объявления продажа, объявления продаю'

        def lease_tags():
            return u'объявления аренда, объявления сдам'

        result = [
            u' '.join([action(), obj()]),
            u' '.join([action(), obj(), town_name()]),
            (u' '.join([action(), obj(), limit_text()]) if self.estate in [VKAdvert.ESTATE_LIVE, VKAdvert.ESTATE_COUNTRY] and self.adtype == VKAdvert.TYPE_LEASE else u''),
            (u' '.join([room_text(), obj()]) if self.estate == VKAdvert.ESTATE_LIVE and self.live==VKAdvert.LIVE_FLAT else u''),
            metro_name(),
            address_text(),
            (flat_tags() if self.estate==VKAdvert.ESTATE_LIVE and self.live==VKAdvert.LIVE_FLAT else u''),
            (sale_tags() if self.adtype==VKAdvert.TYPE_SALE else u''),
            (lease_tags() if self.adtype==VKAdvert.TYPE_LEASE else u''),
            u'База недвижимость, Объявления, бесплатные объявления, частные объявления, доска объявлений, бесплатные доски, дать объявление, бесплатные доски объявлений, сайт объявления',
        ]
        return u', '.join(result)

    def get_absolute_url(self):
        url = [self.town.slug]
        if self.estate:
            url.append(VKAdvert.ESTATES_SLUG[self.estate])
        url.append(VKAdvert.TYPES_SLUG[self.adtype])
        prefix = []
        if self.estate == VKAdvert.ESTATE_LIVE:
            if self.live == VKAdvert.LIVE_ROOM:
                prefix.append('komnata')
            elif self.live == VKAdvert.LIVE_FLAT:
                if self.rooms:
                    prefix.append('%s_komnatnaya_kvartira' % self.rooms)
                else:
                    prefix.append('kvartira')
        elif self.estate == VKAdvert.ESTATE_COUNTRY:
            if self.country:
                prefix.append(VKAdvert.COUNTRIES_SLUG[self.country])
            else:
                prefix.append(VKAdvert.ESTATES_SLUG[self.estate])
        elif self.estate == VKAdvert.ESTATE_TERRITORY:
            if self.territory:
                prefix.append(VKAdvert.TERRITORIES_SLUG[self.territory])
            else:
                prefix.append(VKAdvert.ESTATES_SLUG[self.estate])
        elif self.estate == VKAdvert.ESTATE_COMMERCIAL:
            if self.commercial:
                prefix.append(VKAdvert.COMMERCIALS_SLUG[self.commercial])
            else:
                prefix.append(VKAdvert.ESTATES_SLUG[self.estate])
        return '/%s/%s/vkid%s' % ('/'.join(url), '_'.join(prefix), self.id)

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

    def clear_cache(self):
        # delete_template_fragment_cache('catalog_preview', unicode(self.id))
        # delete_template_fragment_cache('catalog_preview_vert', unicode(self.id))
        # delete_template_fragment_cache('catalog_preview_client', unicode(self.id), unicode(False))
        # delete_template_fragment_cache('catalog_preview_client', unicode(self.id), unicode(True))
        # delete_template_fragment_cache('catalog_preview_agent24', unicode(self.id))
        # delete_template_fragment_cache('catalog_preview_client_clients_count', unicode(self.id))
        #
        # delete_template_fragment_cache('roomas_catalog_preview', unicode(self.id))
        pass

    def clear_user_cache(self, user):
        delete_template_fragment_cache('vkcatalog_preview_tel', unicode(self.id), unicode(user.id))

    @staticmethod
    def get_catalog_title(args, request):
        def action():
            """
            Операция с недвижимостью
            """
            result = u''
            if 'type' in args:
                if args['type'] == VKAdvert.TYPE_LEASE:
                    result = u'Аренда'
                elif args['type'] == VKAdvert.TYPE_SALE:
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
                if args['type'] == VKAdvert.TYPE_LEASE:
                    result = u' длительно'
                elif args['type'] == VKAdvert.TYPE_SALE:
                    result = u''
                elif args['type'] == 'LP':
                    result = u' посуточно'
            else:
                return u''
            return result

        def obj():
            result = u' недвижимости'
            if 'estate' in args:
                if args['estate'] == VKAdvert.ESTATE_LIVE:
                    if 'rooms' in args:
                        if args['rooms'] == 'R':
                            result = u'комната'
                        else:
                            result = u'%s комнатная квартира' % args['rooms']
                    else:
                        result = VKAdvert.ESTATES[args['estate']].lower() + u' недвижимость'
                elif args['estate'] == VKAdvert.ESTATE_COUNTRY:
                    if 'country' in args:
                        result = VKAdvert.COUNTRIES[args['country']]
                    else:
                        result = VKAdvert.ESTATES[args['estate']].lower() + u' недвижимость'
                elif args['estate'] == VKAdvert.ESTATE_COMMERCIAL:
                    if 'commercial' in args:
                        result = VKAdvert.COMMERCIALS[args['commercial']].lower() + u' нежилое помещение'
                    else:
                        result = VKAdvert.ESTATES[args['estate']].lower() + u' недвижимость'
                elif args['estate'] == VKAdvert.ESTATE_TERRITORY:
                    if 'territory' in args:
                        result = VKAdvert.TERRITORIES[args['territory']].lower()
                    else:
                        result = VKAdvert.ESTATES[args['estate']].lower()
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

    @staticmethod
    def get_catalog_url(args=[]):
        params = args.copy()
        parts = []
        if 'town' in params:
            town = get_object_or_404(Town, id=params['town'])
            parts.append(town.slug)
            del params['town']

            if params.get('estate', '') in VKAdvert.ESTATES_SLUG:
                parts.append(VKAdvert.ESTATES_SLUG[params['estate']])

                exists_type = False
                if params.get('type', '') in VKAdvert.TYPES:
                    parts.append(VKAdvert.TYPES_SLUG[params['type']])
                    del params['type']
                    exists_type = True

                if params.get('type', '') == 'LP':
                    parts.append('sdam-posutochno')
                    del params['type']
                    exists_type = True

                if exists_type:
                    if params['estate'] == VKAdvert.ESTATE_LIVE:
                        if 'rooms' in params:
                            if len(params['rooms']) == 1:
                                if params['rooms'] == 'R':
                                    parts.append('komnata')
                                else:
                                    parts.append('%s-komnatnaya-kvartira' % params['rooms'])
                                del params['rooms']
                    elif params['estate'] == VKAdvert.ESTATE_COUNTRY:
                        if 'country' in params:
                            if len(params['country']) == 1:
                                if params['country'] in VKAdvert.COUNTRIES:
                                    parts.append(VKAdvert.COUNTRIES_SLUG[params['country']])
                                    del params['country']
                    elif params['estate'] == VKAdvert.ESTATE_COMMERCIAL:
                        if 'commercial' in params:
                            if len(params['commercial']) == 1:
                                if params['commercial'] in VKAdvert.COMMERCIALS:
                                    parts.append(VKAdvert.COMMERCIALS_SLUG[params['commercial']])
                                    del params['commercial']
                    elif params['estate'] == VKAdvert.ESTATE_TERRITORY:
                        if 'territory' in params:
                            if len(params['territory']) == 1:
                                if params['territory'] in VKAdvert.TERRITORIES:
                                    parts.append(VKAdvert.TERRITORIES_SLUG[params['territory']])
                                    del params['territory']

                if exists_type:
                    if ('metro' in params) and (not isinstance(params.get('metro'), list)) and params['estate'] in [VKAdvert.ESTATE_LIVE, VKAdvert.ESTATE_TERRITORY, VKAdvert.ESTATE_COMMERCIAL]:
                        metro_list = Metro.objects.filter(id=params['metro'])
                        if metro_list:
                            parts.append('metro-' + metro_list[0].slug)
                            del params['metro']
                    if 'district' in params and params['estate'] in [VKAdvert.ESTATE_COUNTRY]:
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

        return '/vk/' + ('/'.join(parts)) + '/' + ('?' if len(get_params) else '') + urllib.urlencode(get_params)

    @property
    def is_archive(self):
        """
        Флаг, в архиве или нет объявление
        """
        if self.adtype == VKAdvert.TYPE_LEASE:
            td = datetime.now() - timedelta(days=settings.ARCHIVE_LEASE_DAYS)
            return td > self.date
        else:
            td = datetime.now() - timedelta(days=settings.ARCHIVE_SALE_DAYS)
            return td > self.date

    def check_spam(self, actions=False):
        # проверка по черному списку
        result = VKBlacklist.check_vkid(self.owner_vkid)
        if result:
            return result

        # проверка на мошеннический спам
        spam_query = Q(owner_vkid=self.owner_vkid,
                       estate=self.estate,
                       adtype=self.adtype,
                       need=self.need,
                       date__gte=datetime.now() - timedelta(days=2))
        spam_query &= (~Q(metro=self.metro) | Q(metro__isnull=True))
        if self.id:
            spam_query &= ~Q(id=self.id)
        if (self.estate == VKAdvert.ESTATE_LIVE) and (self.live == VKAdvert.LIVE_FLAT):
            spam_query &= (~Q(live=self.live) | ~Q(rooms=self.rooms) | Q(rooms__isnull=True))
        if (self.estate == VKAdvert.ESTATE_LIVE) and (self.live == VKAdvert.LIVE_ROOM):
            spam_query &= ~Q(live=self.live)

        spam_list = VKAdvert.objects.filter(spam_query)
        if spam_list:
            msg = [u'найден спам от собственника ВК №%s id %s' % (spam_list[0].id, spam_list[0].owner_vkid)]
            if actions:
                ids = [str(advert.id) for advert in spam_list]
                VKBlacklist.add_vkid(self.owner_vkid, 'Определен как спамер объявлений ' + (', '.join(ids)))
                msg.append(u'VKID %s добавлен в черный список' % self.owner_vkid)
                VKAdvert.objects.filter(owner_vkid=self.owner_vkid).update(status=VKAdvert.STATUS_BLOCKED)
                msg.append(u'Объявления с id %s заблокированы' % self.owner_id)
            return u'\n'.join(msg)
        return False

    @staticmethod
    def get_duplicates(exclude_id=None, tel=None, vkid=None):
        """
        Поиск дубликатов среди опубликованных объявлений
        """
        query = (Q(owner_tel=tel) | Q(owner_vkid=vkid))
        query &= Q(date__gte=datetime.now() - timedelta(days=2))
        query &= ~Q(status=VKAdvert.STATUS_BLOCKED)
        return VKAdvert.objects.filter(query)\
            .exclude(id=exclude_id if exclude_id else 0)

    @staticmethod
    def block_by_tel(tel):
        return VKAdvert.objects.filter(owner_tel__icontains=tel).exclude(status=VKAdvert.STATUS_BLOCKED).update(status=VKAdvert.STATUS_BLOCKED)

    @staticmethod
    def block_by_vkid(vkid):
        return VKAdvert.objects.filter(owner_vkid=vkid).exclude(status=VKAdvert.STATUS_BLOCKED).update(status=VKAdvert.STATUS_BLOCKED)
    
    def parse(self, text):
        import re
        text_lower = text.lower()
        if re.findall(u'(мебель|меблирован)', text_lower, re.IGNORECASE | re.UNICODE):
            self.furniture = True
        if re.findall(u'(парковка|паркинг|парк\.)', text_lower, re.IGNORECASE | re.UNICODE):
            self.parking = True
        if re.findall(u'(гараж)', text_lower, re.IGNORECASE | re.UNICODE):
            self.garage = True
        if u'консьерж' in text_lower:
            self.concierge = True
        if re.findall(u'(евро[\ |\-]*ремонт|хорош.{0,5}ремонт|качественн.{0,5}ремонт|нов.{0,5}ремонт)', text_lower, re.IGNORECASE | re.UNICODE):
            self.euroremont = True
        if re.findall(u'(охрана|охр\.)', text_lower, re.IGNORECASE | re.UNICODE):
            self.guard = True
        if re.findall(u'(tv|телевизор|кабельное|[\ |\.|\,|\-|\!|\t|\n]тв[\ |\.|\,|\-|\!|\t|\n])', text_lower, re.IGNORECASE | re.UNICODE):
            self.tv = True
        if re.findall(u'(стиральн.{0,5}машин|машинка)', text_lower, re.IGNORECASE | re.UNICODE):
            self.washer = True
        if re.findall(u'(wi[\ |\-]*fi|интернет)', text_lower, re.IGNORECASE | re.UNICODE):
            self.internet = True
        if re.findall(u'(телефон)', text_lower, re.IGNORECASE | re.UNICODE):
            self.phone = True
        if re.findall(u'(балкон[\ |\.|\,|\-|\!|\t|\n]|лоджия)', text_lower, re.IGNORECASE | re.UNICODE):
            self.balcony = True
        if u'холодильник' in text_lower:
            self.refrigerator = True
        if re.findall(u'(быт.{0,6}техника)', text_lower, re.IGNORECASE | re.UNICODE):
            self.refrigerator = True
            self.washer = True
        if u'посуточно' in text_lower:
            self.limit = self.LIMIT_DAY
        if re.findall(u'(сан[\ |\.]*узел раздельный|раздельный сан[\ |\.]*узел|с/у разд)', text_lower, re.IGNORECASE | re.UNICODE):
            self.separate_wc = True
        if re.findall(u'(с детьми|с реб[е|ё]нк)', text_lower, re.IGNORECASE | re.UNICODE):
            self.live_child = True
        if re.findall(u'(семьи)', text_lower, re.IGNORECASE | re.UNICODE):
            self.live_pare = True
        if re.findall(u'(лифт)', text_lower, re.IGNORECASE | re.UNICODE):
            self.lift = True

    def __setattr__(self, key, value):
        super(VKAdvert, self).__setattr__(key, value)
        if key == 'date':
            self.date_vashdom = self.date + timedelta(minutes=random.randrange(5, 30), seconds=random.randrange(1, 50))
            self.date_smart = self.date + timedelta(minutes=random.randrange(5, 30), seconds=random.randrange(1, 50))
            self.date_roomas = self.date + timedelta(minutes=random.randrange(5, 30), seconds=random.randrange(1, 50))
            self.date_stopagent = self.date + timedelta(minutes=random.randrange(5, 30), seconds=random.randrange(1, 50))

    @staticmethod
    def reset_date():
        offset = 0
        while True:
            advert_list = VKAdvert.objects.all().order_by('-id')[offset:offset+100]
            for advert in advert_list:
                advert.date = advert.date
                advert.save()
                print '%s' % advert.id
            if not advert_list:
                break
            offset += 100

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
                  'floor',
                  'count_floor',
                  'owner_name',
                  'owner_tel',
                    'owner_vkid',
                  ]

        result = {}
        for field in fields:
            if not getattr(self, field) is None:
                result[field] = getattr(self, field)
        result['live'] = u'room' if self.live == VKAdvert.LIVE_ROOM else u'flat'
        result['date'] = self.date.strftime("%d-%m-%Y %H:%M")
        result['base'] = u'vk'
        result['images'] = []
        site = Site.objects.get_current()
        for image in self.images.all():
            result['images'].append(u'http://%s%s' % (site.domain, image.image.url))
        return result

    def publish(self):
        # from main.task import request_vk_to_client
        # if (self.town.slug == 'sankt-peterburg' or self.town.slug == 'moskva') and self.status == VKAdvert.STATUS_VIEW:
        #     request_vk_to_client.apply_async(args=[self.id], countdown=900)
        pass


class VKBlacklist(models.Model):
    """
    Черный список телефонов
    """
    vkid = models.CharField(verbose_name='VID', max_length=50, default='')
    body = models.TextField(verbose_name='Описание', default='', blank=True, null=True)

    class Meta:
        verbose_name = u'Элемент черного ВК списка'
        verbose_name_plural = u'Черный список ВК'
        ordering = ['vkid']

    def __unicode__(self):
        return self.tel

    @staticmethod
    def add_vkid(vkid, desc=''):
        blacklist = VKBlacklist(vkid=vkid, body=desc)
        blacklist.save()

    @staticmethod
    def check_vkid(vkid):
        blacklist = VKBlacklist.objects.filter(vkid=vkid)
        if blacklist:
            return  u'VKID %s есть в черном списке как %s' % (vkid, blacklist[0].vkid)
        return False