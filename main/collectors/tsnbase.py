#-*- coding: utf-8 -*-
from lxml import html, etree
from lxml.html import fromstring
import requests
import re
from datetime import datetime
import time
import traceback
from main.collectors.base import Collector
from main.models import Town, Advert, UserImage, Blacklist, clear_tel, clear_tel_list, get_tel_list, Abbr, Parser
from uprofile.models import User
import logging
from django.utils.html import strip_tags

logger = logging.getLogger('tsnbase')


class TsnBaseCollector(Collector):
    domain = 'http://tsnbase.ru/'
    catalog_url = 'http://tsnbase.ru/result_rent.php'
    login_url = 'http://tsnbase.ru/index.php'
    logout_url = 'http://tsnbase.ru/?go=logout'

    metro_list = None
    district_list = None
    town = None
    parser = None

    def process_elements(self, doc):
        element_list = doc.xpath('//table[@class="results"]/tr[@align="center"]')
        live = None
        estate = None
        cur_district = None
        for element in element_list:
            tds = element.xpath('.//td')
            if len(tds) > 1:
                logger.info("=======================")


                advert = Advert(town=self.town,
                                status=Advert.STATUS_MODERATE,
                                district=cur_district,
                                estate=estate,
                                limit=Advert.LIMIT_LONG,
                                user=User.objects.get(username='admin'),
                                date=datetime.now(),
                                parser=self.parser)
                advert.adtype = Advert.TYPE_LEASE
                advert.need = Advert.NEED_SALE
                if estate == Advert.ESTATE_LIVE:
                    advert.live = live

                # идентификатор
                input_list = tds[0].xpath('.//input')
                if not input_list:
                    logger.info( 'Не найден код')
                    continue
                advert_id = input_list[0].get('value')
                if not advert_id:
                    logger.info( 'Пустой код')
                    continue
                txt = u'tsnbase_' + advert_id
                logger.info(txt)
                advert_list = Advert.objects.filter(extnum=txt)
                if advert_list:
                    logger.info('Объявление есть в базе')
                    continue

                advert.extnum = txt

                # дата
                try:
                    txt = tds[2].text_content().strip()[:8]
                    advert.date = datetime.strptime(txt, u'%d.%m.%y')
                    now = datetime.now()
                    advert.date = advert.date.replace(hour=now.hour, minute=now.minute, second=now.second)
                except Exception as ex:
                    logger.info( traceback.format_exc())

                # комнаты
                txt = tds[3].text_content().strip()
                if estate == Advert.ESTATE_LIVE:
                    try:
                        if u'(' in txt:
                            m = re.search(ur'\((\d+).\)', txt)
                            if m:
                                advert.rooms = int(m.group(1))
                                logger.info('Найдено кол-во комнат')
                        else:
                            advert.rooms = int(txt)
                            logger.info('Найдено кол-во комнат')
                    except Exception, err:
                        logger.info( traceback.format_exc())
                elif estate == Advert.ESTATE_COUNTRY:
                    try:
                        if u'ктж' in txt:
                            advert.country = Advert.COUNTRY_COTTAGE
                            logger.info('Найден коттедж')
                        elif u'дом' in txt:
                            advert.country = Advert.COUNTRY_HOUSE
                            logger.info('Найден дом')
                        elif u'дача' in txt:
                            advert.country = Advert.COUNTRY_DACHA
                            logger.info('Найден дача')
                        else:
                            advert.country = Advert.COUNTRY_HOUSE
                            logger.info('Найден по умолчанию дом')
                        m = re.search(ur'(\d+)', txt)
                        if m:
                            advert.rooms = int(m.group(1))
                            logger.info('Найдено кол-во комнат')
                    except Exception, err:
                        logger.info( traceback.format_exc())

                # адрес
                txt = tds[4].text_content().strip()
                advert.address = txt
                logger.info('Найден адрес')

                if advert.address:
                    #получение координат
                    try:
                        address_txt = u'Россия, ' + self.town.title + ', ' + advert.address
                        doc_text = self.download_url(u'http://geocode-maps.yandex.ru/1.x/?results=1&geocode=%s' % address_txt)
                        doccoord = fromstring(doc_text)
                        point = doccoord.xpath('//point/pos')
                        if point:
                            xy = point[0].text_content().split(' ')
                            lon = float(xy[0])
                            lat = float(xy[1])
                            advert.longitude = lon
                            advert.latitude = lat
                            logger.info( 'получены координаты')
                    except Exception, err:
                        logger.info( traceback.format_exc())

                # метро
                txt = tds[5].text_content().strip()
                if txt:
                    for metro in self.metro_list:
                        if metro.title.lower() in txt.lower():
                            advert.metro = metro
                            logger.info('получено метро')
                            break

                #получение метро
                if not advert.metro and advert.latitude and advert.longitude:
                    try:
                        logger.info('запрос метро')
                        doc_text = self.download_url(u'http://geocode-maps.yandex.ru/1.x/?results=1&kind=metro&geocode=%s,%s' % (advert.longitude, advert.latitude), encoding='utf8')
                        doccoord = fromstring(doc_text)
                        metro_name = doccoord.xpath('//name')
                        if metro_name:
                            txt = metro_name[0].text_content()
                            for metro in self.metro_list:
                                if metro.title.lower() in txt.lower():
                                    advert.metro = metro
                                    logger.info('получено метро')
                                    break
                    except Exception, err:
                        logger.info( traceback.format_exc())

                #получение района
                if not advert.district and advert.latitude and advert.longitude:
                    try:
                        logger.info('запрос района')
                        doc_text = self.download_url(u'http://geocode-maps.yandex.ru/1.x/?results=1&kind=district&geocode=%s,%s' % (advert.longitude, advert.latitude), encoding='utf8')
                        doccoord = fromstring(doc_text)
                        district_name = doccoord.xpath('//name')
                        if district_name:
                            txt = district_name[0].text_content()
                            for district in self.district_list:
                                if district.title.lower() in txt.lower():
                                    advert.district = district
                                    logger.info('получен район')
                                    break
                    except Exception, err:
                        logger.info(traceback.format_exc())

                # этаж
                txt = tds[6].text_content().strip()
                etag = txt.split(u'/')
                if len(etag) == 2:
                    try:
                        if etag[0]:
                            advert.floor = int(etag[0])
                        if etag[1]:
                            advert.count_floor = int(etag[1])
                        logger.info('найден этаж')
                    except Exception, err:
                        logger.info(traceback.format_exc())

                # общая площадь
                txt = tds[7].text_content().strip()
                try:
                    if float(txt):
                        advert.square = float(txt)
                        logger.info('найдена общая площадь')
                except Exception, err:
                    logger.info(traceback.format_exc())

                # жилая площадь
                txt = tds[8].text_content().strip()
                try:
                    if txt:
                        advert.living_square = txt
                        logger.info('найдена жилая площадь')
                except Exception, err:
                    logger.info(traceback.format_exc())

                # кухни площадь
                txt = tds[9].text_content().strip()
                try:
                    if float(txt):
                        advert.kitchen_square = float(txt)
                        logger.info('найдена площадь кухни')
                except Exception, err:
                    logger.info(traceback.format_exc())

                # наличие телефона
                txt = tds[10].text_content().strip()
                if u'+' in txt:
                    advert.phone = True
                    logger.info('найдено наличие телефона')

                # наличие мебели
                txt = tds[11].text_content().strip()
                if u'+' in txt:
                    advert.furniture = True
                    logger.info('найдено наличие мебели')

                # наличие холодильника
                txt = tds[12].text_content().strip()
                if u'+' in txt:
                    advert.refrigerator = True
                    logger.info('найдено наличие холодильника')

                # наличие стиралки
                txt = tds[13].text_content().strip()
                if u'+' in txt:
                    advert.washer = True
                    logger.info('найдено наличие стиралки')

                # цена
                txt = tds[14].text_content().strip()
                try:
                    advert.price = int(txt)
                    logger.info('найдена цена')
                except Exception, err:
                    logger.info(traceback.format_exc())
                    continue

                # телефон
                txt = strip_tags(html.tostring(tds[17], encoding='unicode').strip().replace(u'<br>', u', '))
                try:
                    owner_tel_list = get_tel_list(txt)
                    result_tel_list = []
                    is_agent = False
                    for owner_tel in owner_tel_list:
                        if owner_tel.startswith(u'8') and len(owner_tel) > 7:
                            owner_tel = u'7' + owner_tel[1:]
                        if len(owner_tel) <= 7:
                            owner_tel = u'7812' + owner_tel
                        logger.info('найден телефон')
                        result = Blacklist.check_tel(owner_tel)
                        if result:
                            logger.info(result)
                            is_agent = True
                        else:
                            duplicate_list = Advert.get_duplicates(advert.adtype, advert.estate, advert.need, tel=owner_tel)
                            if duplicate_list:
                                logger.info(u'найден дубликат №%s тел %s' % (duplicate_list[0].id, duplicate_list[0].owner_tel))
                                is_agent = True
                            else:
                                result_tel_list.append(owner_tel)
                    advert.owner_tel = u', '.join(result_tel_list)
                    if is_agent:
                        logger.info('агент')
                        continue
                except Exception, err:
                    logger.info(traceback.format_exc())

                if not advert.owner_tel:
                    logger.info( 'телефон не найден')
                    continue

                # комментарий
                txt = tds[18].text_content().strip()
                advert.body = Abbr.abbry(re.sub(ur'Взято с портала tsnbase.ru (\d+)', u'', txt))
                names = advert.body.split(u',')
                if names:
                    if u' ' not in names[0]:
                        advert.owner_name = names[0]
                logger.info( 'найден комментарий')

                if u'парк.' in advert.body:
                    advert.parking = True
                if u'охр.' in advert.body:
                    advert.guard = True
                if u'wi-fi' in advert.body:
                    advert.internet = True
                if u'гараж' in advert.body:
                    advert.garage = True


                advert.save()
            else:
                txt = tds[0].text_content().strip()
                for district in self.district_list:
                    if district.title.lower() in txt.lower():
                        cur_district = district
                        logger.info('###### переключились на район %s' % cur_district.id)
                        break
                if u'комнату' in txt:
                    live = Advert.LIVE_ROOM
                    estate = Advert.ESTATE_LIVE
                    logger.info('###### переключились на комнаты')
                elif (u'квартиру' in txt) or (u'элитное' in txt):
                    live = Advert.LIVE_FLAT
                    estate = Advert.ESTATE_LIVE
                    logger.info('###### переключились на квартиры')
                elif u'дом' in txt:
                    estate = Advert.ESTATE_COUNTRY
                    logger.info('###### переключились на дома')

        return len(element_list) >= 50


    def process_elements_day(self, doc):
        element_list = doc.xpath('//table[@class="results"]/tr[@align="center"]')
        live = None
        estate = None
        for element in element_list:
            tds = element.xpath('.//td')
            if len(tds) > 1:
                logger.info("=======================")


                advert = Advert(town=self.town,
                                status=Advert.STATUS_VIEW,
                                estate=estate,
                                district=cur_district,
                                limit=Advert.LIMIT_DAY,
                                user=User.objects.get(username='admin'),
                                date=datetime.now(),
                                parser=self.parser)
                advert.adtype = Advert.TYPE_LEASE
                advert.need = Advert.NEED_SALE
                if estate == Advert.ESTATE_LIVE:
                    advert.live = live

                # идентификатор
                input_list = tds[0].xpath('.//input')
                if not input_list:
                    logger.info( 'Не найден код')
                    continue
                advert_id = input_list[0].get('value')
                if not advert_id:
                    logger.info( 'Пустой код')
                    continue
                txt = u'tsnbase_' + advert_id
                logger.info(txt)
                advert_list = Advert.objects.filter(extnum=txt)
                if advert_list:
                    logger.info('Объявление есть в базе')
                    continue

                advert.extnum = txt

                # дата
                try:
                    txt = tds[2].text_content().strip()[:8]
                    advert.date = datetime.strptime(txt, u'%d.%m.%y')
                    now = datetime.now()
                    advert.date = advert.date.replace(hour=now.hour, minute=now.minute, second=now.second)
                except Exception as ex:
                    logger.info( traceback.format_exc())

                # комнаты
                txt = tds[3].text_content().strip()
                try:
                    if u'(' in txt:
                        m = re.search(ur'\((\d+).\)', txt)
                        if m:
                            advert.rooms = int(m.group(1))
                            logger.info('Найдено кол-во комнат')
                    else:
                        advert.rooms = int(txt)
                        logger.info('Найдено кол-во комнат')
                except Exception, err:
                    logger.info( traceback.format_exc())


                # адрес
                txt = tds[4].text_content().strip()
                advert.address = txt
                logger.info('Найден адрес')

                if advert.address:
                    #получение координат
                    try:
                        address_txt = u'Россия, ' + self.town.title + ', ' + advert.address
                        doc_text = self.download_url(u'http://geocode-maps.yandex.ru/1.x/?results=1&geocode=%s' % address_txt)
                        doccoord = fromstring(doc_text)
                        point = doccoord.xpath('//point/pos')
                        if point:
                            xy = point[0].text_content().split(' ')
                            lon = float(xy[0])
                            lat = float(xy[1])
                            advert.longitude = lon
                            advert.latitude = lat
                            logger.info( 'получены координаты')
                    except Exception, err:
                        logger.info( traceback.format_exc())

                # метро
                txt = tds[5].text_content().strip()
                if txt:
                    for metro in self.metro_list:
                        if metro.title.lower() in txt.lower():
                            advert.metro = metro
                            logger.info('получено метро')
                            break

                #получение метро
                if not advert.metro and advert.latitude and advert.longitude:
                    try:
                        logger.info('запрос метро')
                        doc_text = self.download_url(u'http://geocode-maps.yandex.ru/1.x/?results=1&kind=metro&geocode=%s,%s' % (advert.longitude, advert.latitude), encoding='utf8')
                        doccoord = fromstring(doc_text)
                        metro_name = doccoord.xpath('//name')
                        if metro_name:
                            txt = metro_name[0].text_content()
                            for metro in self.metro_list:
                                if metro.title.lower() in txt.lower():
                                    advert.metro = metro
                                    logger.info('получено метро')
                                    break
                    except Exception, err:
                        logger.info( traceback.format_exc())

                #получение района
                if not advert.district and advert.latitude and advert.longitude:
                    try:
                        logger.info('запрос района')
                        doc_text = self.download_url(u'http://geocode-maps.yandex.ru/1.x/?results=1&kind=district&geocode=%s,%s' % (advert.longitude, advert.latitude), encoding='utf8')
                        doccoord = fromstring(doc_text)
                        district_name = doccoord.xpath('//name')
                        if district_name:
                            txt = district_name[0].text_content()
                            for district in self.district_list:
                                if district.title.lower() in txt.lower():
                                    advert.district = district
                                    logger.info('получен район')
                                    break
                    except Exception, err:
                        logger.info(traceback.format_exc())

                # этаж
                txt = tds[6].text_content().strip()
                etag = txt.split(u'/')
                if len(etag) == 2:
                    try:
                        if etag[0]:
                            advert.floor = int(etag[0])
                        if etag[1]:
                            advert.count_floor = int(etag[1])
                        logger.info('найден этаж')
                    except Exception, err:
                        logger.info(traceback.format_exc())

                # общая площадь
                txt = tds[7].text_content().strip()
                try:
                    if float(txt):
                        advert.square = float(txt)
                        logger.info('найдена общая площадь')
                except Exception, err:
                    logger.info(traceback.format_exc())

                # жилая площадь
                txt = tds[8].text_content().strip()
                try:
                    if txt:
                        advert.living_square = txt
                        logger.info('найдена жилая площадь')
                except Exception, err:
                    logger.info(traceback.format_exc())

                # кухни площадь
                txt = tds[9].text_content().strip()
                try:
                    if float(txt):
                        advert.kitchen_square = float(txt)
                        logger.info('найдена площадь кухни')
                except Exception, err:
                    logger.info(traceback.format_exc())

                # наличие телефона
                txt = tds[10].text_content().strip()
                if u'+' in txt:
                    advert.phone = True
                    logger.info('найдено наличие телефона')

                # наличие мебели
                txt = tds[11].text_content().strip()
                if u'+' in txt:
                    advert.furniture = True
                    logger.info('найдено наличие мебели')

                # наличие холодильника
                txt = tds[12].text_content().strip()
                if u'+' in txt:
                    advert.refrigerator = True
                    logger.info('найдено наличие холодильника')

                # наличие стиралки
                txt = tds[13].text_content().strip()
                if u'+' in txt:
                    advert.phone = True
                    logger.info('найдено наличие стиралки')

                # цена
                txt = tds[14].text_content().strip()
                try:
                    advert.price = int(txt)
                    logger.info('найдена цена')
                except Exception, err:
                    logger.info(traceback.format_exc())
                    continue

                # телефон
                txt = strip_tags(html.tostring(tds[17], encoding='unicode').strip().replace(u'<br>', u', '))
                try:
                    owner_tel_list = get_tel_list(txt)
                    result_tel_list = []
                    is_agent = False
                    for owner_tel in owner_tel_list:
                        if owner_tel.startswith(u'8') and len(owner_tel) > 7:
                            owner_tel = u'7' + owner_tel[1:]
                        if len(owner_tel) <= 7:
                            owner_tel = u'7812' + owner_tel
                        logger.info('найден телефон')
                        result = Blacklist.check_tel(owner_tel)
                        if result:
                            logger.info(result)
                            is_agent = True
                        else:
                            result_tel_list.append(owner_tel)
                    advert.owner_tel = u', '.join(result_tel_list)
                    if is_agent:
                        logger.info('агент')
                        continue
                except Exception, err:
                    logger.info(traceback.format_exc())

                if not advert.owner_tel:
                    logger.info( 'телефон не найден')
                    continue

                # комментарий
                txt = tds[17].text_content().strip()
                advert.body = Abbr.abbry(re.sub(ur'Взято с портала tsnbase.ru (\d+)', u'', txt))
                names = advert.body.split(u',')
                if names:
                    if u' ' not in names[0]:
                        advert.owner_name = names[0]
                logger.info( 'найден комментарий')

                advert.parse(advert.body)

                advert.save()
                advert.find_clients()
                advert.find_metro_distance()
                advert.find_surrounding_objects()
                if advert.check_owner():
                    advert.save()
                advert.publish()
            else:
                txt = tds[0].text_content().strip()
                for district in self.district_list:
                    if district.title.lower() in txt.lower():
                        cur_district = district
                        logger.info('###### переключились на район %s' % cur_district.id)
                        break
                if u'комнату' in txt:
                    live = Advert.LIVE_ROOM
                    estate = Advert.ESTATE_LIVE
                    logger.info('###### переключились на комнаты')
                elif (u'квартиру' in txt) or (u'элитное' in txt):
                    live = Advert.LIVE_FLAT
                    estate = Advert.ESTATE_LIVE
                    logger.info('##### переключились на квартиры')
                elif u'дом' in txt:
                    estate = Advert.ESTATE_COUNTRY
                    logger.info('###### переключились на дома')


    def blacklist(self):
        self.login()
        try:
            for page in xrange(20):
                logger.info('страница %s' % page)
                r = requests.post(self.catalog_url, cookies=self.cookies, data={
                    'sort': '0',
                    'sort_ord': '1',
                    'only_on': '0',
                    'kkv1': '',
                    'kkv2': '',
                    'vsego1': '',
                    'vsego2': '',
                    'price1': '',
                    'price2': '',
                    'srok': '0',
                    'sg1': '',
                    'sg2': '',
                    'sk1': '',
                    'sk2': '',
                    'tel_kod': '812',
                    'tel_text': '',
                    'status': '0',
                    'date_range': '',
                    'firm_name': '',
                    'text': '',
                    'prim': '',
                    'start': page * 50
                })
                r.encoding = 'cp1251'

                doc = fromstring(r.text)
                doc.make_links_absolute(self.domain)

                element_list = doc.xpath('//table[@class="results"]/tr[@align="center"]')
                for element in element_list:
                    tds = element.xpath('.//td')
                    if len(tds) > 1:
                        txt = tds[16].text_content().strip()
                        if u'частное' not in txt:
                            # телефон
                            txt = strip_tags(html.tostring(tds[17], encoding='unicode').strip().replace(u'<br>', u', '))
                            try:
                                owner_tel_list = get_tel_list(txt)
                                for owner_tel in owner_tel_list:
                                    if owner_tel.startswith(u'8') and len(owner_tel) > 7:
                                        owner_tel = u'7' + owner_tel[1:]
                                    if len(owner_tel) <= 7:
                                        owner_tel = u'7812' + owner_tel
                                    if not Blacklist.check_tel(owner_tel):
                                        Blacklist.add_tel(owner_tel)
                                        logger.info(owner_tel)
                            except Exception, err:
                                logger.info(traceback.format_exc())
                        else:
                            logger.info('частное')
        except Exception, err:
            logger.info(traceback.format_exc())
        self.logout()

    def days(self):
        self.town = Town.objects.get(id=2)
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()
        self.login()
        try:
            # квартиры посуточно
            logger.info('КВАРТИРЫ ПОСУТОЧНО')
            for page in xrange(10):
                logger.info('страница %s' % page)
                r = requests.post(self.catalog_url, cookies=self.cookies, data={
                    's': '1',
                    'sort': '0',
                    'sort_ord': '1',
                    'only_on': '1',
                    'type[]': '1',
                    'kkv1': '',
                    'kkv2': '',
                    'vsego1': '',
                    'vsego2': '',
                    'price1': '',
                    'price2': '',
                    'srok': '0',
                    'sg1': '',
                    'sg2': '',
                    'sk1': '',
                    'sk2': '',
                    'tel_kod': '812',
                    'tel_text': '',
                    'status': '0',
                    'date_range': '',
                    'firm_name': '',
                    'text': '',
                    'prim': '',
                    'start': page * 50
                })
                r.encoding = 'cp1251'

                doc = fromstring(r.text)
                doc.make_links_absolute(self.domain)
                self.process_elements_day(doc)
        except Exception, err:
            logger.info(traceback.format_exc())

        try:
            # комнаты посуточно
            logger.info('КОМНАТЫ ПОСУТОЧНО')
            for page in xrange(3):
                logger.info('страница %s' % page)
                r = requests.post(self.catalog_url, cookies=self.cookies, data={
                    's': '1',
                    'sort': '0',
                    'sort_ord': '1',
                    'only_on': '1',
                    'type[]': '2',
                    'kkv1':'',
                    'kkv2': '',
                    'vsego1': '',
                    'vsego2': '',
                    'price1': '',
                    'price2': '',
                    'srok': '0',
                    'sg1': '',
                    'sg2': '',
                    'sk1': '',
                    'sk2': '',
                    'tel_kod': '812',
                    'tel_text': '',
                    'status': '0',
                    'date_range': '',
                    'firm_name': '',
                    'text': '',
                    'prim': '',
                    'start': page*50
                })
                r.encoding = 'cp1251'

                doc = fromstring(r.text)
                doc.make_links_absolute(self.domain)
                self.process_elements_day(doc)
        except Exception, err:
            logger.info(traceback.format_exc())

        self.logout()

    def login(self):
        logger.info('Вход на сайт tsnbase')
        r = requests.get(self.domain)
        self.cookies = dict(r.cookies.items())
        params = {}
        params['login'] = u'44525'
        params['password'] = u'dQSMBwxH'

        r = requests.post(self.login_url, data=params, cookies=self.cookies, allow_redirects=True)

    def logout(self):
        logger.info('Выход с сайта')
        r = requests.post(self.logout_url, cookies=self.cookies, allow_redirects=True)

    def collect(self):
        self.town = Town.objects.get(id=2)
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()
        self.parser = Parser.objects.get(title='tsnbase')
        self.login()
        now = datetime.now()
        try:
            # квартиры
            logger.info('КВАРТИРЫ')
            for page in xrange(10):
                logger.info('Страница %s' % page)
                r = requests.post(self.catalog_url, cookies=self.cookies, data={
                    'sort': '0',
                    'sort_ord': '1',
                    'only_on': '1',
                    'type[]': '1',
                    'kkv1':'',
                    'kkv2': '',
                    'vsego1': '',
                    'vsego2': '',
                    'price1': '',
                    'price2': '',
                    'srok': '0',
                    'sg1': '',
                    'sg2': '',
                    'sk1': '',
                    'sk2': '',
                    'tel_kod': '812',
                    'tel_text': '',
                    'status': '0',
                    'firm_name': '',
                    'text': '',
                    'prim': '',
                    'date_range': now.strftime('%d.%m.%Y') + " - " + now.strftime('%d.%m.%Y'),
                    'start': page*50
                })
                r.encoding = 'cp1251'

                doc = fromstring(r.text)
                doc.make_links_absolute(self.domain)
                if not self.process_elements(doc):
                    break
        except Exception, err:
            logger.info(traceback.format_exc())

        try:
            # комнаты
            logger.info('КОМНАТЫ')
            for page in xrange(10):
                logger.info('Страница %s' % page)
                r = requests.post(self.catalog_url, cookies=self.cookies, data={
                    'sort': '0',
                    'sort_ord': '1',
                    'only_on': '1',
                    'type[]': '2',
                    'kkv1':'',
                    'kkv2': '',
                    'vsego1': '',
                    'vsego2': '',
                    'price1': '',
                    'price2': '',
                    'srok': '0',
                    'sg1': '',
                    'sg2': '',
                    'sk1': '',
                    'sk2': '',
                    'tel_kod': '812',
                    'tel_text': '',
                    'status': '0',
                    'date_range': now.strftime('%d.%m.%Y') + " - " + now.strftime('%d.%m.%Y'),
                    'firm_name': '',
                    'text': '',
                    'prim': '',
                    'start': page*50
                })
                r.encoding = 'cp1251'

                doc = fromstring(r.text)
                doc.make_links_absolute(self.domain)
                if not self.process_elements(doc):
                    break
        except Exception, err:
            logger.info(traceback.format_exc())

        try:
            # дома
            logger.info('ДОМА')
            r = requests.post(self.catalog_url, cookies=self.cookies, data={
                'sort': '0',
                'sort_ord': '1',
                'only_on': '1',
                'type[]': '4',
                'kkv1':'',
                'kkv2': '',
                'vsego1': '',
                'vsego2': '',
                'price1': '',
                'price2': '',
                'srok': '0',
                'sg1': '',
                'sg2': '',
                'sk1': '',
                'sk2': '',
                'tel_kod': '812',
                'tel_text': '',
                'status': '0',
                'date_range': '',
                'firm_name': '',
                'text': '',
                'prim': ''
            })
            r.encoding = 'cp1251'

            doc = fromstring(r.text)
            doc.make_links_absolute(self.domain)
            self.process_elements(doc)
        except Exception, err:
            logger.info(traceback.format_exc())

        self.logout()