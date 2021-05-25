# coding=utf8
from django.db import models
from paysto.models import BasePayment
from robokassa.signals import result_received, fail_page_visited, success_page_visited
from walletone.signals import payment_received as w1_payment_result
from django.conf import settings
from datetime import datetime, timedelta
import string
import random
from uprofile.models import User
from main.models import Town, Advert, Metro, District, VKAdvert, Promocode
from django.shortcuts import get_object_or_404
import urllib
from django.contrib.auth.models import UserManager as BaseUserManager
from django.db.models import Q
from decimal import Decimal
from mail_templated import send_mail
import logging


class VashdomAdvert(Advert):
    class Meta:
        proxy = True

    @staticmethod
    def get_catalog_url(args=[]):
        params = args.copy()
        parts = []
        if 'town' in params:
            town = get_object_or_404(Town, id=params['town'])
            parts.append(town.slug)
            del params['town']

            if 'rooms' in params:
                if not isinstance(params['rooms'], list):
                    if 'R' == params['rooms']:
                        parts.append('komnata')
                    else:
                        parts.append('kvartira')
                        if params['rooms'] != 'F':
                            parts.append('%s-komnatnaya' % params['rooms'])
                    del params['rooms']

            if ('metro' in params) and (not isinstance(params.get('metro'), list)):
                metro_list = Metro.objects.filter(id=params['metro'])
                if metro_list:
                    parts.append('metro-' + metro_list[0].slug)
                    del params['metro']


        get_params = []
        for key, value in params.iteritems():
            if isinstance(value, list):
                for v in value:
                    get_params.append((key, v))
            else:
                get_params.append((key, value))

        return '/' + ('/'.join(parts)) + '/' + ('?' if len(get_params) else '') + urllib.urlencode(get_params)

    @staticmethod
    def is_hot(self):
        if self.price:
            if self.town.slug == 'moskva':
                if self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_ROOM:
                    return self.price <= 15000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 1:
                    return self.price <= 28000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 2:
                    return self.price <= 39000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 3:
                    return self.price <= 45000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms >= 4:
                    return self.price <= 55000
            if self.town.slug == 'sankt-peterburg':
                if self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_ROOM:
                    return self.price <= 9000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 1:
                    return self.price <= 18000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 2:
                    return self.price <= 23000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 3:
                    return self.price <= 25000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms >= 4:
                    return self.price <= 28000
            if self.town.slug == 'novosibirsk':
                if self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_ROOM:
                    return self.price <= 10000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 1:
                    return self.price <= 19000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 2:
                    return self.price <= 23000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 3:
                    return self.price <= 25000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms >= 4:
                    return self.price <= 27000
                pass
            if self.town.slug == 'ekaterinburg':
                if self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_ROOM:
                    return self.price <= 9000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 1:
                    return self.price <= 17000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 2:
                    return self.price <= 21000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 3:
                    return self.price <= 25000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms >= 4:
                    return self.price <= 28000

        return False

    @property
    def title(self):
        result = ''
        if self.need == self.NEED_SALE:
            if self.estate == self.ESTATE_LIVE:
                if self.live == self.LIVE_ROOM:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сдам комнату' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Продам комнату'
                elif self.live == self.LIVE_FLAT:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сдам %s квартиру' % (u'%s комнатную' % self.rooms if self.rooms else '') + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Продам %s квартиру' % (u'%s комнатную' % self.rooms if self.rooms else '')

            elif self.estate == self.ESTATE_TERRITORY:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Аренда земельного участка' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Продам земельный участок'

            elif self.estate == self.ESTATE_COUNTRY:
                if self.adtype == self.TYPE_LEASE:
                    if self.count_floor:
                        result = u'Сдам %s этажный дом в аренду' % self.count_floor + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                    else:
                        result = u'Сдам дом в аренду' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Продам дом'

            elif self.estate == self.ESTATE_COMMERCIAL:
                if self.adtype == self.TYPE_LEASE:
                    result = u'Сдам помещение в аренду' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                elif self.adtype == self.TYPE_SALE:
                    result = u'Продам помещение'
        elif self.need == self.NEED_DEMAND:
            if self.estate == self.ESTATE_LIVE:
                if self.live == Advert.LIVE_ROOM:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сниму комнату' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Куплю комнату'
                elif self.live == Advert.LIVE_FLAT:
                    if self.adtype == self.TYPE_LEASE:
                        result = u'Сниму квартиру' + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
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

    @staticmethod
    def get_catalog_title(args, request):
        def action():
            """
            Операция с недвижимостью
            """
            result = u'Снять'
            return result

        def limit():
            """
            Срок
            """
            result = u''
            # if 'type' in args:
            #     if args['type'] == Advert.TYPE_LEASE:
            #         result = u' длительно'
            #     elif args['type'] == Advert.TYPE_SALE:
            #         result = u''
            #     elif args['type'] == 'LP':
            #         result = u' посуточно'
            # else:
            #     return u''
            return result

        def obj():
            result = u' недвижимость'
            if 'rooms' in args:
                rooms = args['rooms']
            else:
                rooms = request.GET.getlist('rooms')
            room_array = []
            if 'R' in rooms:
                room_array.append(u'комнату')
            if 'F' in rooms:
                room_array.append(u'квартиру')
            exists_flat = False
            for r in ['1', '2', '3', '4']:
                if r in rooms:
                    room_array.append(r)
                    exists_flat = True
            if room_array:
                result = u', '.join(room_array)
                if exists_flat:
                    result += u'-комнатную квартиру'
            else:
                result =u' квартиру или комнату'
            return result

        def town_name():
            if 'town' in args:
                town = Town.objects.get(id=args['town'])
            else:
                town = request.current_town
            return u'в ' + town.title_d

        def metro_name():
            metro_id = None
            if 'metro' in args:
                metro_id = args['metro']
            if len(request.GET.getlist('metro', [])) == 1:
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
            if len(request.GET.getlist('district', [])) == 1:
                district_id = request.GET.get('district')
            if district_id:
                try:
                    district_list = District.objects.filter(id=district_id)
                    if district_list:
                        return u'в районе %s' % district_list[0].title
                except:
                    pass
            return ''

        result = u' '.join([action(), obj(), town_name(), metro_name(), district_name()])
        return result

    @staticmethod
    def get_advert_query(town=None):
        result = Q(status=Advert.STATUS_VIEW,
                      need=Advert.NEED_SALE,
                      company=None,
                      adtype=Advert.TYPE_LEASE,
                      limit=Advert.LIMIT_LONG,
                      estate=Advert.ESTATE_LIVE)
        if town:
            price_query = Q()
            if town.slug == 'moskva':
                price_query |= (Q(live=Advert.LIVE_ROOM, price__gte=12000, price__lte=35000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=1, price__gte=25000, price__lte=45000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=2, price__gte=30000, price__lte=82000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=3, price__gte=40000, price__lte=92000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms__gte=4, price__gte=45000, price__lte=100000))
            elif town.slug == 'sankt-peterburg':
                price_query |= (Q(live=Advert.LIVE_ROOM, price__gte=7000, price__lte=19000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=1, price__gte=15000, price__lte=39000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=2, price__gte=18000, price__lte=45000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=3, price__gte=18000, price__lte=49000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms__gte=4, price__gte=20000, price__lte=65000))
            elif town.slug == 'novosibirsk':
                price_query |= (Q(live=Advert.LIVE_ROOM, price__gte=7000, price__lte=11000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=1, price__gte=15000, price__lte=21000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=2, price__gte=11000, price__lte=25000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=3, price__gte=17000, price__lte=33000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms__gte=4, price__gte=18000, price__lte=35000))
            elif town.slug == 'ekaterinburg':
                price_query |= (Q(live=Advert.LIVE_ROOM, price__gte=7000, price__lte=11000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=1, price__gte=9000, price__lte=21000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=2, price__gte=12000, price__lte=25000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=3, price__gte=17000, price__lte=33000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms__gte=4, price__gte=18000, price__lte=35000))

            result &= price_query

        return result

    @staticmethod
    def get_autoposting_query(town=None):
        result = Q(status=Advert.STATUS_VIEW,
                      need=Advert.NEED_SALE,
                      company=None,
                      adtype=Advert.TYPE_LEASE,
                      limit=Advert.LIMIT_LONG,
                      estate=Advert.ESTATE_LIVE)
        if town:
            price_query = Q()
            if town.slug == 'moskva':
                price_query |= (Q(live=Advert.LIVE_ROOM, price__gte=12000, price__lte=17000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=1, price__gte=27000, price__lte=32000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=2, price__gte=38000, price__lte=42000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=3, price__gte=40000, price__lte=50000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms__gte=4, price__gte=45000, price__lte=60000))
            elif town.slug == 'sankt-peterburg':
                price_query |= (Q(live=Advert.LIVE_ROOM, price__gte=9000, price__lte=12000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=1, price__gte=17000, price__lte=21000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=2, price__gte=20000, price__lte=24000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=3, price__gte=22000, price__lte=27000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms__gte=4, price__gte=24000, price__lte=28000))
            elif town.slug == 'novosibirsk':
                price_query |= (Q(live=Advert.LIVE_ROOM, price__gte=7000, price__lte=11000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=1, price__gte=9000, price__lte=21000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=2, price__gte=12000, price__lte=25000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=3, price__gte=17000, price__lte=33000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms__gte=4, price__gte=18000, price__lte=35000))
            elif town.slug == 'ekaterinburg':
                price_query |= (Q(live=Advert.LIVE_ROOM, price__gte=7000, price__lte=11000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=1, price__gte=9000, price__lte=21000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=2, price__gte=12000, price__lte=25000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms=3, price__gte=17000, price__lte=33000))
                price_query |= (Q(live=Advert.LIVE_FLAT, rooms__gte=4, price__gte=18000, price__lte=35000))

            result &= price_query

        return result

    @property
    def description(self):
        if self.need == Advert.NEED_SALE and not self.company:
            text = self.properties.get('desc.vashdom', '')
            if not text:
                text = self.generate_description()
                self.properties['desc.vashdom'] = text
                self.save()
            return text
        else:
            return self.body

    def get_absolute_url(self):
        url = [self.town.slug]
        if self.live == VashdomAdvert.LIVE_ROOM:
            url.append('komnata')
        elif self.live == VashdomAdvert.LIVE_FLAT:
            url.append('kvartira')
            if self.rooms:
                url.append('%s-komnatnaya' % self.rooms)
        if self.metro:
            url.append('metro-%s' % self.metro.slug)
        return '/%s/id%s' % ('/'.join(url), self.id)

    @staticmethod
    def deserialize(data):
        from vashdom.api import Advert2Serializer
        from uimg.models import UserImage
        import traceback

        logger = logging.getLogger('import')
        try:
            exists = VashdomAdvert.objects.filter(data.get('id'))
            if not exists:
                logger.infdebugo(data.get('id'))
                data['id'] = None
                data['date'] = datetime.now()
                images = data['image']
                data['images'] = []
                serializer = Advert2Serializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    for image in images:
                        try:
                            img = UserImage()
                            if img.load_image(image['image']):
                                img.save()
                            serializer.instance.images.add(img)
                        except:
                            logger.debug(traceback.format_exc())
                else:
                    logger.debug(serializer.errors)
        except:
            logger.debug(traceback.format_exc())



class VashdomVKAdvert(VKAdvert):
    class Meta:
        proxy = True

    @staticmethod
    def get_catalog_url(args=[]):
        params = args.copy()
        parts = []
        if 'town' in params:
            town = get_object_or_404(Town, id=params['town'])
            parts.append(town.slug)
            del params['town']

            if 'rooms' in params:
                if not isinstance(params['rooms'], list):
                    if 'R' == params['rooms']:
                        parts.append('komnata')
                    else:
                        parts.append('kvartira')
                        parts.append('%s-komnatnaya' % params['rooms'])
                    del params['rooms']

            if ('metro' in params) and (not isinstance(params.get('metro'), list)):
                metro_list = Metro.objects.filter(id=params['metro'])
                if metro_list:
                    parts.append('metro-' + metro_list[0].slug)
                    del params['metro']


        get_params = []
        for key, value in params.iteritems():
            if isinstance(value, list):
                for v in value:
                    get_params.append((key, v))
            else:
                get_params.append((key, value))

        return '/vk/' + ('/'.join(parts)) + '/' + ('?' if len(get_params) else '') + urllib.urlencode(get_params)

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
                        result = u'Сдам %s квартиру' % (u'%s комнатную' % self.rooms if self.rooms else '') + (u' посуточно' if self.limit == Advert.LIMIT_DAY else u'')
                    elif self.adtype == self.TYPE_SALE:
                        result = u'Продам %s квартиру' % (u'%s комнатную' % self.rooms if self.rooms else '')

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

    @staticmethod
    def get_catalog_title(args, request):
        def action():
            """
            Операция с недвижимостью
            """
            result = u''
            if 'type' in args:
                if args['type'] == Advert.TYPE_LEASE:
                    result = u'Снять'
                elif args['type'] == Advert.TYPE_SALE:
                    result = u'Купить'
                elif args['type'] == 'LP':
                    result = u'Снять'
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
                        rooms = args['rooms']
                    else:
                        rooms = request.GET.getlist('rooms')
                    room_array = []
                    if 'R' in rooms:
                        room_array.append(u'комнату')
                    exists_flat = False
                    for r in ['1', '2', '3', '4']:
                        if r in rooms:
                            room_array.append(r)
                            exists_flat = True
                    if room_array:
                        result = u', '.join(room_array)
                        if exists_flat:
                            result += u'-комнатную квартиру'
                    else:
                        result =u' квартиру или комнату'
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
            else:
                town = request.current_town
            return u'в ' + town.title_d

        def metro_name():
            metro_id = None
            if 'metro' in args:
                metro_id = args['metro']
            if len(request.GET.getlist('metro', [])) == 1:
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
            if len(request.GET.getlist('district', [])) == 1:
                district_id = request.GET.get('district')
            if district_id:
                try:
                    district_list = District.objects.filter(id=district_id)
                    if district_list:
                        return u'в районе %s' % district_list[0].title
                except:
                    pass
            return ''

        result = u' '.join([action(), obj(), town_name(), metro_name(), district_name()])
        return result

    @staticmethod
    def is_hot(self):
        if self.price:
            if self.town.slug == 'moskva':
                if self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_ROOM:
                    return self.price <= 15000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 1:
                    return self.price <= 28000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 2:
                    return self.price <= 39000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 3:
                    return self.price <= 45000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms >= 4:
                    return self.price <= 55000
            if self.town.slug == 'sankt-peterburg':
                if self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_ROOM:
                    return self.price <= 9000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 1:
                    return self.price <= 18000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 2:
                    return self.price <= 23000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 3:
                    return self.price <= 25000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms >= 4:
                    return self.price <= 28000
            if self.town.slug == 'novosibirsk':
                if self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_ROOM:
                    return self.price <= 10000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 1:
                    return self.price <= 19000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 2:
                    return self.price <= 23000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 3:
                    return self.price <= 25000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms >= 4:
                    return self.price <= 27000
                pass
            if self.town.slug == 'ekaterinburg':
                if self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_ROOM:
                    return self.price <= 9000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 1:
                    return self.price <= 17000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 2:
                    return self.price <= 21000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms == 3:
                    return self.price <= 25000
                elif self.estate == Advert.ESTATE_LIVE and self.live == Advert.LIVE_FLAT and self.rooms >= 4:
                    return self.price <= 28000

        return False

    def get_absolute_url(self):
        url = [self.town.slug]
        if self.live == VashdomVKAdvert.LIVE_ROOM:
            url.append('komnata')
        elif self.live == VashdomVKAdvert.LIVE_FLAT:
            url.append('kvartira')
            if self.rooms:
                url.append('%s-komnatnaya' % self.rooms)
        if self.metro:
            url.append('metro-%s' % self.metro.slug)
        return '/vk/%s/vkid%s' % ('/'.join(url), self.id)

class VashdomUserManager(BaseUserManager):
    def get_queryset(self):
        return super(VashdomUserManager, self).get_queryset().filter(site=VashdomUser.SITE_ID)


class VashdomUser(User):

    SITE_ID = 5

    class Meta:
        proxy = True

    objects = VashdomUserManager()


class Tariff(models.Model):
    """
    Тариф
    """

    title = models.CharField(verbose_name=u'Название', max_length=250, default='')
    desc = models.TextField(u'Описание', null=True, blank=True)
    price = models.FloatField(u'Цена', default=100)
    order = models.IntegerField(u'Сортировка', blank=True, default=500)
    count = models.IntegerField(u'Количество объявлений', default=0)
    days = models.IntegerField(u'Дни', default=0)
    town = models.ForeignKey(Town, verbose_name='Город', default=1, related_name='vashdom_tariffs')
    main_base = models.BooleanField(u'Основная база', default=True)
    vk_base = models.BooleanField(u'База ВКонтакте', default=False)
    hidden = models.BooleanField(u'Скрытый', default=False)
    code = models.CharField(u'Символьный код', max_length=50, default='', null=True, blank=True)

    class Meta:
        verbose_name = u'Тариф'
        verbose_name_plural = u'Тарифы'
        ordering = ['title']

    def __unicode__(self):
        return self.title


class Payment(BasePayment):
    """
    Оплата
    """

    user = models.ForeignKey(VashdomUser, verbose_name=u'Пользователь',
                             related_name='vashdom_payments', on_delete=models.CASCADE, null=True, blank=True, default=None)
    tariff = models.ForeignKey(Tariff, null=True, default=None)
    town = models.ForeignKey(Town, verbose_name='Город', default=1, related_name='vashdom_payments')
    tel = models.CharField(u'Телефон', max_length=20, default='', blank=True, null=True)
    email = models.EmailField(u'Email', default=None, blank=True, null=True)
    password = models.ForeignKey('Password', verbose_name=u'Выданный пароль', blank=True, null=True, default=None)
    promocode = models.ForeignKey(Promocode, verbose_name=u'Промокод', default=None, blank=True, null=True, related_name='vashdom_payments')
    notified = models.BooleanField(u'Уведомлено', default=False)
    session_key = models.CharField(default='', max_length=100, blank=True)

    class Meta:
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'
        ordering = ['-created']

    def __unicode__(self):
        return unicode(self.id)

    def success(self):
        if self.user:
            if not self.user.is_active and self.tariff.price > 0:
                self.user.is_active = True
                self.user.save()

        password = Password(start_date=datetime.now(),
                            end_date=datetime.now() + timedelta(days=self.tariff.days),
                            count=self.tariff.count,
                            town=self.town,
                            tel=self.tel,
                            email=self.email,
                            user=self.user,
                            main_base=self.tariff.main_base,
                            vk_base=self.tariff.vk_base)
        password.gen_password()
        password.save()
        self.password = password
        self.save()
        if self.tariff.price > 0 and self.tel:
            password.send_sms()
        if self.tariff.price > 0 and self.email:
            password.send_email()

    def fail(self):
        pass

    def recalc_total(self):
        self.total = Decimal(self.sum)
        if self.promocode:
            self.total -= self.promocode.get_discount(self.sum)

    @property
    def total_discount(self):
        result = Decimal(0)
        if self.promocode:
            result += self.promocode.get_discount(self.sum)
        return result


def payment_received(sender, **kwargs):
    payment = Payment.objects.get(id=kwargs['InvId'])
    if payment.status != Payment.STATUS_CONFIRMED:
        payment.change_status(Payment.STATUS_CONFIRMED)
        payment.success()


def payment_success_page_visited(sender, **kwargs):
    payment = Payment.objects.get(id=kwargs['InvId'])
    if payment.status != Payment.STATUS_CONFIRMED:
        payment.change_status(Payment.STATUS_CONFIRMED)
        payment.success()


def w1_payment_received(**kwargs):
    w1payment=kwargs['payment']
    payment = Payment.objects.get(id=w1payment.WMI_PAYMENT_NO)
    if payment.status != Payment.STATUS_CONFIRMED:
        payment.change_status(Payment.STATUS_CONFIRMED)
        payment.success()


def payment_fail(sender, **kwargs):
    payment = Payment.objects.get(id=kwargs['InvId'])
    payment.change_status(Payment.STATUS_REJECTED)
    payment.fail()

if settings.SITE_ID == 5:
    result_received.connect(payment_received)
    success_page_visited.connect(payment_success_page_visited)
    fail_page_visited.connect(payment_fail)
    w1_payment_result.connect(w1_payment_received)


class Password(models.Model):
    """
    Пароли доступа
    """
    user = models.ForeignKey(VashdomUser, verbose_name=u'Пользователь',
                             related_name='vashdom_passwords', on_delete=models.CASCADE, null=True, blank=True, default=None)
    password = models.CharField(u'Пароль', max_length=10, default='')
    start_date = models.DateTimeField(u'Дата начала', default=datetime.now)
    end_date = models.DateTimeField(u'Дата окончания', default=datetime.now)
    count = models.IntegerField(u'Количество', default=0)
    town = models.ForeignKey(Town, verbose_name=u'Город', default=1)
    tel = models.CharField(u'Телефон', max_length=20, default='')
    email = models.EmailField(u'Email', default=None, blank=True, null=True)
    main_base = models.BooleanField(u'Основная база', default=True)
    vk_base = models.BooleanField(u'База ВКонтакте', default=False)
    adverts = models.ManyToManyField(Advert, blank=True, null=True)
    vkadverts = models.ManyToManyField(VKAdvert, blank=True, null=True)

    class Meta:
        verbose_name = u'Пароль'
        verbose_name_plural = u'Пароли'
        ordering = ['-start_date']

    def __unicode__(self):
        return self.password

    def gen_password(self):
        self.password = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(8))

    def send_sms(self):
        try:
            from smsgate.gate import SmsGate
            gate = SmsGate()
            gate.send(self.tel, 'BAZAVASHDOM: %s' % self.password)
        except:
            pass

    def send_email(self):
        try:
            send_mail('vashdom/email/password.html', {
                password: self.password
            }, recipient_list=[self.email], fail_silently=True)
        except:
            pass

    @property
    def elapsed_time(self):
        if self.end_date < datetime.now():
            return 'Подписка истекла'
        else:
            delta = self.end_date - datetime.now()
            return "%s д. %s ч. %s мин." % (delta.days, delta.seconds // 3600, delta.seconds % 3600 // 60)