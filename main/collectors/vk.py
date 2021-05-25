# -*- coding: utf-8 -*-
from main.collectors.base import Collector
import requests
import json
from main.models.vkadvert import VKAdvert, VKBlacklist
from main.models.general import Town, clear_tel, clear_tel_list, Blacklist, Metro, District
from uimg.models import UserImage
import re
from datetime import datetime
import hashlib
import traceback
import logging
import vk_api
from django.conf import settings


logger = logging.getLogger('vk')


class VKCollector(Collector):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    }

    LEASE_REGEX = u'(сдам|сдаю|сдаем|сдается|сдача|сдадим|ищу|ищем)'
    LEASE_DEMAIN_REGEX = u'(сниму|снимем|снимет|снимут)'
    SALE_REGEX = u'(продам|продаю|продаем|продается|продажа|продадим)'
    SALE_DEMAND_REGEX = u'(куплю|купим)'
    FLAT_REGEX = u'(квартира|квартиру|квартиры|однушку|двушку)'
    FLATROOM_REGEX = u'(комната|комнату)'
    PHONE_REGEX = u'([0-9][0-9|\(\)\ \-]{7,20}[0-9])'
    ROOM_REGEX = u'(\d)(\ ?-?х?к?\ ?ком|\ ?-?\ ?к\.?\ ?кв)'
    PRICE_REGEX = u'([0-9|\ |\.]{4,10})(\ ?р|\ ?руб\ |\ ?\+)'
    PRICE1000_REGEX = u'([0-9|\ |\.]{1,10})(\ ?т\.?р|\ ?тыс\.)'
    SQUARE_REGEX = u'([0-9|\ ]{2,10})(\ ?м\.?\ |\ ?кв?\.?м)'
    DEMAND_REGEX = '(длит[.*]{1,10}срок|семейн|семья|район|гарантир)'
    AGENT_REGEX = '(комисс|скидка|агентск|агентство недвижимости|доск[.]{1, 20}объявлений)'
    api = None

    def collect_search(self, query, limit, adtype=VKAdvert.TYPE_LEASE, live=VKAdvert.LIVE_FLAT, need=VKAdvert.NEED_SALE):
        # r = requests.get('https://api.vk.com/method/newsfeed.search?q=%s&count=%s&offset=%s&extended=1' % (query, 100, offset))
        # data = json.loads(r.text)
        data = self.api.newsfeed.search(q=query, count=200, extended=1)

        for element in data['items']:
            logger.info('----')
            logger.info(element['id'])
            try:
                advert_id = u'%s_%s' % (element['owner_id'], element['id'])
                if VKAdvert.objects.filter(extnum=advert_id).count() > 0:
                    logger.info('Объявление есть в базе')
                    continue
                owner_vkid = element['owner_id']
                if owner_vkid < 0:
                    if u'signer_id' in element:
                        owner_vkid = element['signer_id']
                        if owner_vkid < 0:
                            logger.info('Это группа')
                            continue
                    else:
                        logger.info('Это группа')
                        # logger.info(element)
                        continue

                advert = VKAdvert(adtype=adtype,
                                    need=need,
                                    estate=VKAdvert.ESTATE_LIVE,
                                    live=live,
                                    owner_vkid=owner_vkid,
                                    # owner_name=element['user']['first_name'], # + u' ' + element['user']['last_name'],
                                    extnum=advert_id,
                                    date=datetime.fromtimestamp(element['date']))

                text = element['text']

                if adtype == VKAdvert.TYPE_LEASE and need == VKAdvert.NEED_SALE:
                    m = re.search(self.LEASE_REGEX, text, re.IGNORECASE | re.UNICODE)
                    if not m:
                        logger.info('не сдается')
                        continue

                if adtype == VKAdvert.TYPE_LEASE and need == VKAdvert.NEED_DEMAND:
                    m = re.search(self.LEASE_DEMAIN_REGEX, text, re.IGNORECASE | re.UNICODE)
                    if not m:
                        logger.info('не сдается')
                        continue

                if adtype == VKAdvert.TYPE_SALE and need == VKAdvert.NEED_SALE:
                    m = re.search(self.SALE_REGEX, text, re.IGNORECASE | re.UNICODE)
                    if not m:
                        logger.info('не продается')
                        continue

                if adtype == VKAdvert.TYPE_SALE and need == VKAdvert.NEED_DEMAND:
                    m = re.search(self.SALE_DEMAND_REGEX, text, re.IGNORECASE | re.UNICODE)
                    if not m:
                        logger.info('не покупается')
                        continue

                if live == VKAdvert.LIVE_FLAT:
                    m = re.search(self.FLAT_REGEX, text, re.IGNORECASE | re.UNICODE)
                    if not m:
                        logger.info('не квартира')
                        continue

                if live == VKAdvert.LIVE_ROOM:
                    m = re.search(self.FLATROOM_REGEX, text, re.IGNORECASE | re.UNICODE)
                    if not m:
                        logger.info('не комната')
                        continue

                if u'http://' in text or \
                                u'https://' in text or \
                                u'.ru' in text or \
                                u'.com' in text:
                    logger.info('есть внешние ссылки')
                    continue

                if re.findall(self.AGENT_REGEX, text, re.IGNORECASE | re.UNICODE):
                    logger.info('это агент')
                    continue


                text = text.replace(u'<br>', u'\r\n')                               #удалил викиразметку
                text = re.sub(ur'#[\w|.,!#%{}()@]+', u'', text, flags=re.UNICODE)   #удалил хештеги
                # text = re.sub(ur'http[\w|.,:\\/!#%{}()@-]+', u'', text, flags=re.UNICODE)   #удалил ссылки

                if len(text) < 50 and need == VKAdvert.NEED_SALE:
                    logger.info('короткий текст')
                    continue

                # проверка совпадений хеша
                text_hash = hashlib.md5()
                text_hash.update(text.encode('utf8'))
                if VKAdvert.objects.filter(body_hash=text_hash.hexdigest()).count() > 0:
                    logger.info('такой текст объявления уже есть')
                    continue

                # кол-во доп информации
                options_count = 0

                # скрыть телефоны
                m = re.findall(self.PHONE_REGEX, text, re.IGNORECASE | re.UNICODE)
                if m:
                    tel_list = []
                    for str in m:
                        # print str
                        text = text.replace(str, u'[phone]')
                        if str.startswith(u'8'):
                            tel_list.append(u'7' + str[1:])
                        else:
                            tel_list.append(str)
                    owner_tel = u', '.join(tel_list)
                    advert.owner_tel = clear_tel_list(owner_tel)
                    result = Blacklist.check_list(advert.owner_tel)
                    if result:
                        logger.info(result)
                        continue

                duplicate_list = VKAdvert.get_duplicates(tel=advert.owner_tel, vkid=advert.owner_vkid)
                if duplicate_list:
                    logger.info(u'найден дубликат №%s vkid %s' % (duplicate_list[0].id, duplicate_list[0].owner_vkid))
                    continue

                advert.body = text
                advert.body_hash = text_hash.hexdigest()

                # количество комнат
                m = re.search(self.ROOM_REGEX, text, re.IGNORECASE | re.UNICODE)
                if m:
                    try:
                        advert.rooms = int(m.group(1).replace(u' ', u''))
                        options_count += 1
                        # print 'нашли комнаты %s' % advert.rooms
                    except Exception, err:
                        logger.info(traceback.format_exc())
                if not advert.rooms and (u'однушка' in text.lower() or u'однушку' in text.lower() or u'однокомн' in text.lower()):
                    advert.rooms = 1
                    options_count += 1
                    # print 'нашли комнаты %s' % advert.rooms
                if not advert.rooms and (u'двушка' in text.lower() or u'двушку' in text.lower() or u'двухкомн' in text.lower()):
                    advert.rooms = 2
                    options_count += 1
                    # print 'нашли комнаты %s' % advert.rooms

                #цена
                m = re.search(self.PRICE_REGEX, text, re.IGNORECASE | re.UNICODE)
                if m:
                    try:
                        advert.price = int(m.group(1)\
                                            .replace(u' ', u'')\
                                            .replace(u'.', u'')
                            )
                        options_count += 1
                        # print 'найдена цена %s' % advert.price
                    except Exception, err:
                        logger.info(traceback.format_exc())
                m = re.search(self.PRICE1000_REGEX, text, re.IGNORECASE | re.UNICODE)
                if m:
                    try:
                        advert.price = int(m.group(1)\
                                            .replace(u' ', u'')\
                                            .replace(u'.', u'')
                            )
                        if advert.adtype == VKAdvert.TYPE_LEASE and advert.price < 1000:
                            advert.price *= 1000
                        if advert.adtype == VKAdvert.TYPE_SALE and advert.price < 100000:
                            advert.price *= 1000
                        options_count += 1
                        # print 'найдена цена %s' % advert.price
                    except Exception, err:
                        logger.info(traceback.format_exc())

                #площадь
                m = re.search(self.SQUARE_REGEX, text, re.IGNORECASE | re.UNICODE)
                if m:
                    try:
                        advert.square = float(m.group(1)\
                                            .replace(u' ', u'')\
                                            .replace(u'.', u'')
                            )
                        options_count += 1
                        # print 'найдена площадь %s' % advert.square
                    except Exception, err:
                        logger.info(traceback.format_exc())

                advert.parse(advert.body)

                # получаю информацию о пользователе для определения города
                # r = requests.get('https://api.vk.com/method/users.get?v=5.62&user_ids=%s&fields=city,country,photo_100' % advert.owner_vkid, timeout=3)
                user_data = self.api.users.get(user_ids=advert.owner_vkid, fields='city,country,photo_100')
                # user_data = json.loads(r.text)
                user = user_data[0]
                logger.info(user)
                if 'city' in user:
                    town_list = Town.admin_objects.filter(vkid=user['city']['id'])
                else:
                    town_list = None
                if town_list:
                    advert.town = town_list[0]
                    advert.owner_name = user['first_name']
                else:
                    # print 'Город не найден'
                    continue

                metro_list = advert.town.metro_set.all()
                for metro in metro_list:
                    if metro.title.lower() in advert.body.lower():
                        advert.metro = metro
                        options_count += 1

                district_list = advert.town.district_set.all()
                for district in district_list:
                    if district.title.lower() in advert.body.lower():
                        district.metro = district
                        options_count += 1

                if need == VKAdvert.NEED_DEMAND and re.findall(self.DEMAND_REGEX, text, re.IGNORECASE | re.UNICODE):
                    options_count += 1
                if need == VKAdvert.NEED_DEMAND and advert.owner_tel:
                    options_count += 1

                if options_count == 0:
                    logger.info('мало доп информации')
                    continue

                result = advert.check_spam(actions=True)
                if result:
                    logger.info(result)
                    continue

            	logger.info('save')
                advert.save()
                advert.publish()
                # print 'записано'

                img = UserImage()
                if img.load_image(user['photo_100']):
                    advert.owner_photo = img
                    advert.save()

                if 'attachments' in element:
                    for attach in element['attachments']:
                        if 'photo' in attach:
                            # print attach['photo']['src_big']
                            img = UserImage()
                            if img.load_image(attach['photo']['src_big']):
                                advert.images.add(img)
            except Exception, err:
                logger.info(traceback.format_exc())


    def collect(self):
        vk_session = vk_api.VkApi(token=settings.VK_ACCESS_TOKEN)
        # try:
        #     vk_session.authorization()
        # except vk_api.AuthError as error_msg:
        #     print(error_msg)
        #     return
        self.api = vk_session.get_api()
        if self.api:

            # поиск сдачи квартир
            self.collect_search('+сдам +квартиру', 100, adtype=VKAdvert.TYPE_LEASE, live=VKAdvert.LIVE_FLAT)
            # self.collect_search('+сдаю +квартиру', 100, adtype=VKAdvert.TYPE_LEASE, live=VKAdvert.LIVE_FLAT)
            # self.collect_search('+сдается +квартира', 100, adtype=VKAdvert.TYPE_LEASE, live=VKAdvert.LIVE_FLAT)

            # поиск сдачи комнат
            self.collect_search('+сдам +комнату', 100, adtype=VKAdvert.TYPE_LEASE, live=VKAdvert.LIVE_ROOM)
            # self.collect_search('+сдаю +комнату', 100, adtype=VKAdvert.TYPE_LEASE, live=VKAdvert.LIVE_ROOM)
            # self.collect_search('+сдается +комната', 100, adtype=VKAdvert.TYPE_LEASE, live=VKAdvert.LIVE_ROOM)

            # поиск продаж квартир
            self.collect_search('+продам +квартиру', 100, adtype=VKAdvert.TYPE_SALE, live=VKAdvert.LIVE_FLAT)

            # поиск снятия квартир
            self.collect_search('+сниму +квартиру', 100, adtype=VKAdvert.TYPE_LEASE, live=VKAdvert.LIVE_FLAT, need=VKAdvert.NEED_DEMAND)

            # поиск снятия комнат
            self.collect_search('+сниму +комнату', 100, adtype=VKAdvert.TYPE_LEASE, live=VKAdvert.LIVE_ROOM, need=VKAdvert.NEED_DEMAND)

            # поиск купли квартир
            self.collect_search('+куплю +квартиру', 100, adtype=VKAdvert.TYPE_SALE, live=VKAdvert.LIVE_FLAT, need=VKAdvert.NEED_DEMAND)