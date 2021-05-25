#-*- coding: utf-8 -*-
from lxml import html, etree
from lxml.html import fromstring
import requests
import re
from datetime import datetime
import time
import traceback
from main.collectors.base import Collector
from main.models import Town, Advert, UserImage, Blacklist, clear_tel, Abbr, Parser
from uprofile.models import User
import logging
from django.utils.html import strip_tags

logger = logging.getLogger('pyxi')


class PyxiCollector(Collector):
    domain = 'http://pyxi.ru/'
    catalog_url = 'http://pyxi.ru/base.php'
    catalog_sale_url = 'http://pyxi.ru/trade.php'
    catalog_sale_need = 'http://pyxi.ru/clients.php'
    login_url = 'http://pyxi.ru/index.php'
    logout_url = 'http://pyxi.ru/exit.php'
    demo_url = 'http://pyxi.ru/index.php?user=demo&pass=demo'
    phone_url = 'http://pyxi.ru/modules/phone.php'
    phone_url_c = 'http://pyxi.ru/modules/phone_c.php'
    img_path = '/var/www/sites/default/files/img_load/'

    metro_list = None
    district_list = None
    town = None
    parser = None
    parser_sale = None
    parser_need = None

    TYPE_LEASE = 'L'
    TYPE_SALE = 'S'
    TYPE_NEED = 'N'

    def process_elements(self, doc):
        element_list = doc.xpath('//*[@class="tableModalWrapper"]')
        need_wait = False
        for element in element_list:
            logger.info("=======================")
            if need_wait:
                logger.info('Ожидание 21 сек...')
                time.sleep(21)
                need_wait = False

            advert = Advert(town=self.town,
                            status=Advert.STATUS_VIEW,
                            estate=Advert.ESTATE_LIVE,
                            user=User.objects.get(username='admin'),
                            date=datetime.now(),
                            parser=self.parser)
            advert.adtype = Advert.TYPE_LEASE
            advert.need = Advert.NEED_SALE

            tds = element.xpath('.//td')

            # идентификатор
            advert_id = tds[9].xpath('.//a')[0].get('id').replace(u'complain', '')
            txt = u'pyxi_' + advert_id
            logger.info(txt)
            advert_list = Advert.objects.filter(extnum=txt)
            if advert_list:
                logger.info('Объявление есть в базе')
                continue
            advert.extnum = txt

            # тип недвижимости
            txt = tds[2].text_content().strip()
            if u'Комн' in txt:
                logger.info('Найдена комната')
                advert.live = Advert.LIVE_ROOM
            elif u'1к' in txt:
                logger.info('Найдена 1к квартира')
                advert.live = Advert.LIVE_FLAT
                advert.rooms = 1
            elif u'2к' in txt:
                logger.info('Найдена 2к квартира')
                advert.live = Advert.LIVE_FLAT
                advert.rooms = 2
            elif u'3к' in txt:
                logger.info('Найдена 3к квартира')
                advert.live = Advert.LIVE_FLAT
                advert.rooms = 3
            elif u'4к' in txt:
                logger.info('Найдена 4к квартира')
                advert.live = Advert.LIVE_FLAT
                advert.rooms = 4
            else:
                logger.info('Не найден тип недвижимости')
                continue

            # адрес
            txt = strip_tags(html.tostring(tds[3], encoding='unicode').replace(u'<br>', u'|')).strip()
            txt = txt.replace(u'ё', u'е')
            addr = txt.split(u'|')
            advert.address = addr[len(addr)-1]
            logger.info('Найден адрес')

            # метро
            if txt:
                for metro in self.metro_list:
                    if metro.title.lower() in txt.lower():
                        advert.metro = metro
                        logger.info('получено метро')
                        break

            #получение координат
            try:
                doc_text = self.download_url('http://pyxi.ru/modules/map.php?id=%s&base=0' % advert_id)
                m = re.search(ur'map.setCenter\(new YMaps.GeoPoint\(([0-9\.]+),([0-9\.]+)\)', doc_text)
                if m:
                    advert.longitude = float(m.group(1))
                    advert.latitude = float(m.group(2))
                logger.info('найдены координаты')
            except Exception as ex:
                print ex

            # мебель
            txt = tds[5].text_content().strip()
            if u'Стир+' in txt:
                advert.washer = True
                logger.info('стиралка')
            if u'Меб+' in txt:
                advert.furniture = True
                logger.info('мебель')
            if u'Хол+' in txt:
                advert.refrigerator = True
                logger.info('холодильник')

            # комментарий
            txt = tds[7].text_content().strip().replace(u'Оставить комментарий', u'')
            advert.body = Abbr.abbry(txt)
            logger.info('Получен комментарий объявления')
            advert.parse(advert.body)
            if u'Есть TV' in txt:
                advert.tv = True
                logger.info('тв')

            try:
                # алтернативная площадь
                p = re.compile(ur"(\d+)/([0-9|\ |\-]+)/(\d+)")
                m = p.search(txt)
                if m:
                    advert.square = int(m.group(1))
                    advert.living_square = int(m.group(2))
                    advert.kitchen_square = int(m.group(3))
                    logger.info('получены площади кухни и жилой площади')
                else:
                    p = re.compile(ur"(\d+)м2")
                    m = p.search(txt)
                    if m:
                        advert.square = int(m.group(1))
                        logger.info('получена площадь')
            except Exception, err:
                logger.info(traceback.format_exc())

            #этаж
            txt = tds[4].text_content().strip()
            etag = txt.split(u'/')
            if len(etag) == 2:
                try:
                    if etag[0]:
                        advert.floor = int(etag[0])
                    if etag[1]:
                        advert.count_floor = int(etag[1])
                    logger.info('найден этаж')
                except Exception, err:
                    logger.info( traceback.format_exc())

            # условия проживания
            txt = tds[6].text_content().strip()
            if u'1 Ж' in txt:
                advert.live_girl = True
            if (u'1-2 Ж' in txt) or (u'2 Ж' in txt):
                advert.live_girl = True
                advert.live_two = True
            if u'СП' in txt:
                advert.live_pare = True
            if u'С животными' in txt:
                advert.live_animal = True
            if u'1 М' in txt:
                advert.live_man = True
            if u'2 М' in txt:
                advert.live_man = True
                advert.live_two = True
            if u'С детьми' in txt:
                advert.live_child = True

            # цена
            try:
                advert.price = float(tds[8].xpath('.//span[@class="money"]')[0].text_content().strip())
                logger.info('получена цена %s' % advert.price)
            except Exception as ex:
                print ex

            if not advert.price:
                logger.info('нет цены')
                continue

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

            if advert.live == Advert.LIVE_ROOM and (advert.price<10000 or advert.price>50000):
                logger.info('Не подходит по цене 10000-50000')
                continue

            elif advert.live == Advert.LIVE_FLAT and advert.rooms == 1 and (advert.price<20000 or advert.price>100000):
                logger.info('Не подходит 1к по цене 20000-100000')
                continue

            elif advert.live == Advert.LIVE_FLAT and advert.rooms == 2 and (advert.price<25000 or advert.price>100000):
                logger.info('Не подходит 2к по цене 25000-100000')
                continue

            elif advert.live == Advert.LIVE_FLAT and advert.rooms == 3 and (advert.price<30000 or advert.price>100000):
                logger.info('Не подходит 3к  по цене 30000-92000')
                continue

            elif advert.live == Advert.LIVE_FLAT and advert.rooms == 4 and (advert.price<35000 or advert.price>100000):
                logger.info('Не подходит 4к по цене 35000-100000')
                continue

            # получение телефона
            r = requests.post(self.phone_url, data={'id': advert_id}, cookies=self.cookies)
            need_wait = True
            r.encoding = self.encoding
            telre = re.compile(r">([0-9|\ |\+]+)</span>")
            st = r.text[:120]
            phone_match = telre.search(st)
            if phone_match:
                advert.owner_tel = clear_tel(phone_match.group(1).strip())
                if advert.owner_tel.startswith('8'):
                    advert.owner_tel = '7' + advert.owner_tel[1:]
                logger.info('Найден телефон')
                result = Blacklist.check_tel(advert.owner_tel)
                if result:
                    logger.info(result)
                    continue
                duplicate_list = Advert.get_duplicates(advert.adtype, advert.estate, advert.need, tel=advert.owner_tel)
                if duplicate_list:
                    logger.info(u'найден дубликат №%s тел %s' % (duplicate_list[0].id, duplicate_list[0].owner_tel))
                    continue

                m = re.search(ur'</span><br>(.+)<br><div', st)
                if m:
                    advert.owner_name = m.group(1)
                    logger.info('найден владелец')
            else:
                logger.info('Телефон не найден')
                logger.info(st.encode('utf8'))
                if u'У Вас закончилась подписка' in st:
                    logger.info(u'Закончилась подписка')
                    return
                continue

            advert.save()
            advert.publish()
            advert.find_clients()
            advert.find_metro_distance()
            advert.find_surrounding_objects()

            elems = element.xpath('.//*[@class="img"]/a')
            if elems:
                logger.info('найдено %s фоток' % len(elems))
                for a in elems:
                    try:
                        src = a.get('href')
                        logger.info(src)
                        image = UserImage(user=advert.user)
                        if image.load_image(src):
                            image.save()
                            advert.images.add(image)
                    except Exception, err:
                        logger.debug(traceback.format_exc())

    def process_elements_sale(self, doc):
        element_list = doc.xpath('//*[@class="tableModalWrapper"]')
        need_wait = False
        for element in element_list:
            logger.info("=======================")
            if need_wait:
                logger.info('Ожидание 21 сек...')
                time.sleep(21)
                need_wait = False

            advert = Advert(town=self.town,
                            status=Advert.STATUS_VIEW,
                            estate=Advert.ESTATE_LIVE,
                            user=User.objects.get(username='admin'),
                            date=datetime.now(),
                            parser=self.parser_sale)
            advert.adtype = Advert.TYPE_SALE
            advert.need = Advert.NEED_SALE

            tds = element.xpath('.//td')

            # идентификатор
            advert_id = tds[0].xpath('.//p[@class="iconStar"]/a')[0].get('id')
            txt = u'pyxi_' + advert_id
            logger.info(txt)
            advert_list = Advert.objects.filter(extnum=txt)
            if advert_list:
                logger.info('Объявление есть в базе')
                continue
            advert.extnum = txt

            # дата
            try:
                txt = tds[1].text_content().strip()
                advert.date = datetime.strptime(txt, u'%d.%m.%y')
                now = datetime.now()
                advert.date = advert.date.replace(hour=now.hour, minute=now.minute, second=now.second)
                print advert.date
            except Exception as ex:
                print ex

            # тип недвижимости
            txt = tds[2].text_content().strip()
            if u'Комн' in txt:
                logger.info('Найдена комната')
                advert.live = Advert.LIVE_ROOM
            elif u'1к' in txt:
                logger.info('Найдена 1к квартира')
                advert.live = Advert.LIVE_FLAT
                advert.rooms = 1
            elif u'2к' in txt:
                logger.info('Найдена 2к квартира')
                advert.live = Advert.LIVE_FLAT
                advert.rooms = 2
            elif u'3к' in txt:
                logger.info('Найдена 3к квартира')
                advert.live = Advert.LIVE_FLAT
                advert.rooms = 3
            elif u'4к' in txt:
                logger.info('Найдена 4к квартира')
                advert.live = Advert.LIVE_FLAT
                advert.rooms = 4
            else:
                logger.info('Не найден тип недвижимости')
                continue

            # адрес
            txt = strip_tags(html.tostring(tds[3], encoding='unicode').replace(u'<br>', u'|')).strip()
            # txt = txt.replace(u'р-н', u'район, ')
            # txt = re.sub(ur'^(.+)транспортом', '', txt)
            # txt = re.sub(ur'^(.+)пешком', '', txt)
            # txt = re.sub(ur'м\.', '', txt)
            txt = txt.replace(u'ё', u'е')
            addr = txt.split(u'|')
            advert.address = addr[len(addr)-1]
            logger.info('Найден адрес')

            # метро
            if txt:
                for metro in self.metro_list:
                    if metro.title.lower() in txt.lower():
                        advert.metro = metro
                        logger.info('получено метро')
                        break

            #получение координат
            try:
                doc_text = self.download_url('http://pyxi.ru/modules/map.php?id=%s&base=0' % advert_id)
                m = re.search(ur'map.setCenter\(new YMaps.GeoPoint\(([0-9\.]+),([0-9\.]+)\)', doc_text)
                if m:
                    advert.longitude = float(m.group(1))
                    advert.latitude = float(m.group(2))
                logger.info('найдены координаты')
            except Exception as ex:
                print ex

            # БЛ
            txt = tds[5].text_content().strip()
            if u'1' in txt:
                advert.balcony = True
                logger.info( 'балкон')

            # комментарий
            txt = tds[8].text_content().strip().replace(u'Оставить комментарий', u'')
            advert.body = Abbr.abbry(txt)
            logger.info('Получен комментарий объявления')
            if (u'кондиц-р' in txt) or (u'кондицион' in txt):
                advert.conditioner = True
                logger.info('кондиционер')
            if u'Евро' in txt:
                advert.euroremont = True
                logger.info('евроремонт')
            if u'рем,' in txt:
                advert.redecoration = True
                logger.info('ремонт')
            if u'консьерж' in txt:
                advert.concierge = True
                logger.info('консьерж')
            if u'лодж ' in txt:
                advert.balcony = True
                logger.info('балкон')
            if u'Тр. ремонта' in txt:
                advert.need_remont = True
                logger.info('нужен ремонт')
            if u'есть агент' in txt:
                logger.info('есть агентт')
                continue

            # площади
            try:
                txt = tds[7].text_content().strip()
                squares = txt.split(u'/')
                if len(squares) == 3:
                    if squares[0]:
                        advert.square = int(squares[0])
                    if squares[1]:
                        advert.living_square = int(squares[1])
                    if squares[2]:
                        advert.kitchen_square = int(squares[2])
                    logger.info('получены площади')
            except Exception, err:
                logger.info(traceback.format_exc())

            #этаж
            txt = tds[4].text_content().strip()
            m = re.search(ur'(\d+)/(\d+)', txt)
            if m:
                try:
                    advert.floor = int(m.group(1))
                    advert.count_floor = int(m.group(2))
                    logger.info('найден этаж')
                except Exception, err:
                    logger.info( traceback.format_exc())

            # условия проживания
            txt = tds[6].text_content().strip()
            if u'разд' in txt:
                advert.separate_wc = True

            # цена
            try:
                advert.price = float(tds[9].xpath('.//span[@class="money"]')[0].text_content().strip()) * 1000
                logger.info('получена цена %s' % advert.price)
            except Exception as ex:
                print ex

            if not advert.price:
                logger.info('нет цены')
                continue

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

            # получение телефона
            r = requests.post(self.phone_url, data={'id': advert_id}, cookies=self.cookies)
            need_wait = True
            r.encoding = self.encoding
            telre = re.compile(r">([0-9|\ |\+]+)</span>")
            st = r.text[:120]
            phone_match = telre.search(st)
            if phone_match:
                advert.owner_tel = clear_tel(phone_match.group(1).strip())
                if advert.owner_tel.startswith('8'):
                    advert.owner_tel = '7' + advert.owner_tel[1:]
                logger.info('Найден телефон')
                result = Blacklist.check_tel(advert.owner_tel)
                if result:
                    logger.info(result)
                    continue
                duplicate_list = Advert.get_duplicates(advert.adtype, advert.estate, advert.need, tel=advert.owner_tel)
                if duplicate_list:
                    logger.info(u'найден дубликат №%s тел %s' % (duplicate_list[0].id, duplicate_list[0].owner_tel))
                    continue

                m = re.search(ur'</span><br>(.+)<br><div', st)
                if m:
                    advert.owner_name = m.group(1)
                    logger.info('найден владелец')
            else:
                logger.info('Телефон не найден')
                logger.info(st.encode('utf8'))
                if u'У Вас закончилась подписка' in st:
                    logger.info(u'Закончилась подписка')
                    return
                continue

            advert.save()
            advert.publish()
            advert.find_clients()

            elems = element.xpath('.//*[@class="img"]/a')
            if elems:
                logger.info('найдено %s фоток' % len(elems))
                for a in elems:
                    try:
                        src = a.get('href')
                        logger.info(src)
                        image = UserImage(user=advert.user)
                        if image.load_image(src):
                            image.save()
                            advert.images.add(image)
                    except Exception, err:
                        logger.debug(traceback.format_exc())

    def process_elements_need(self, doc):
        element_list = doc.xpath('//*[@class="tableModalWrapper"]')
        need_wait = False
        for element in element_list:
            logger.info("=======================")
            if need_wait:
                logger.info('Ожидание 21 сек...')
                time.sleep(21)
                need_wait = False

            tds = element.xpath('.//td')

            # идентификатор
            advert_id = tds[0].xpath('.//p[@class="iconStar"]/a')[0].get('id')
            txt = u'pyxi_' + advert_id
            logger.info(txt)
            advert_list = Advert.objects.filter(extnum=txt)
            if advert_list:
                logger.info('Объявление есть в базе')
                continue

            # получение телефона
            owner_tel = None
            owner_name = None
            r = requests.post(self.phone_url_c, data={'id': advert_id}, cookies=self.cookies)
            need_wait = True
            r.encoding = self.encoding
            telre = re.compile(r"([0-9|\ |\+]+)<br>")
            st = r.text[:120]
            phone_match = telre.search(st)
            if phone_match:
                owner_tel = clear_tel(phone_match.group(1).strip())
                if owner_tel.startswith('8'):
                    owner_tel = '7' + owner_tel[1:]
                logger.info('Найден телефон')
                result = Blacklist.check_tel(owner_tel)
                if result:
                    logger.info(result)
                    continue

                m = re.search(ur'<br>(.+)<br><div', st)
                if m:
                    owner_name = m.group(1)
                    logger.info('найден владелец')
            else:
                logger.info('Телефон не найден')
                logger.info(st.encode('utf8'))
                if u'У Вас закончилась подписка' in st:
                    logger.info(u'Закончилась подписка')
                    return
                continue

            # тип недвижимости
            est_list = strip_tags(html.tostring(tds[2], encoding='unicode').replace(u'<br>', u'|')).split(u'|')
            for est in est_list:
                if est.strip():
                    advert = Advert(town=self.town,
                                    status=Advert.STATUS_VIEW,
                                    estate=Advert.ESTATE_LIVE,
                                    user=User.objects.get(username='admin'),
                                    date=datetime.now(),
                                    parser=self.parser_need)
                    advert.adtype = Advert.TYPE_LEASE
                    advert.need = Advert.NEED_DEMAND
                    advert.extnum = u'pyxi_' + advert_id
                    advert.owner_tel = owner_tel
                    advert.owner_name = owner_name

                    if u'Комн' in est:
                        logger.info('Найдена комната')
                        advert.live = Advert.LIVE_ROOM
                    elif u'1к' in est:
                        logger.info('Найдена 1к квартира')
                        advert.live = Advert.LIVE_FLAT
                        advert.rooms = 1
                    elif u'2к' in est:
                        logger.info('Найдена 2к квартира')
                        advert.live = Advert.LIVE_FLAT
                        advert.rooms = 2
                    elif u'3к' in est:
                        logger.info('Найдена 3к квартира')
                        advert.live = Advert.LIVE_FLAT
                        advert.rooms = 3
                    elif u'4к' in est:
                        logger.info('Найдена 4к квартира')
                        advert.live = Advert.LIVE_FLAT
                        advert.rooms = 4
                    else:
                        logger.info('Не найден тип недвижимости')
                        continue

                    # мебель
                    txt = tds[5].text_content().strip()
                    if u'Стир+' in txt:
                        advert.washer = True
                        logger.info('стиралка')
                    if u'Меб+' in txt:
                        advert.furniture = True
                        logger.info('мебель')
                    if u'Хол+' in txt:
                        advert.refrigerator = True
                        logger.info('холодильник')

                    # комментарий
                    txt = tds[7].text_content().strip().replace(u'Оставить комментарий', u'')
                    advert.body = Abbr.abbry(txt)
                    logger.info('Получен комментарий объявления')
                    if u'Есть TV' in txt:
                        advert.tv = True
                        logger.info('тв')

                    try:
                        # алтернативная площадь
                        p = re.compile(ur"(\d+)/([0-9|\ |\-]+)/(\d+)")
                        m = p.search(txt)
                        if m:
                            advert.square = int(m.group(1))
                            advert.living_square = int(m.group(2))
                            advert.kitchen_square = int(m.group(3))
                            logger.info('получены площади кухни и жилой площади')
                        else:
                            p = re.compile(ur"(\d+)м2")
                            m = p.search(txt)
                            if m:
                                advert.square = int(m.group(1))
                                logger.info('получена площадь')
                    except Exception, err:
                        logger.info(traceback.format_exc())

                    #этаж
                    # txt = tds[4].text_content().strip()
                    # etag = txt.split(u'/')
                    # if len(etag) == 2:
                    #     try:
                    #         if etag[0]:
                    #             advert.floor = int(etag[0])
                    #         if etag[1]:
                    #             advert.count_floor = int(etag[1])
                    #         logger.info('найден этаж')
                    #     except Exception, err:
                    #         logger.info( traceback.format_exc())

                    # условия проживания
                    txt = tds[6].text_content().strip()
                    if u'1 Ж' in txt:
                        advert.live_girl = True
                    if (u'1-2 Ж' in txt) or (u'2 Ж' in txt):
                        advert.live_girl = True
                        advert.live_two = True
                    if u'СП' in txt:
                        advert.live_pare = True
                    if u'С животными' in txt:
                        advert.live_animal = True
                    if u'1 М' in txt:
                        advert.live_man = True
                    if u'2 М' in txt:
                        advert.live_man = True
                        advert.live_two = True
                    if u'С детьми' in txt:
                        advert.live_child = True

                    # цена
                    try:
                        advert.price = float(tds[8].xpath('.//span[@class="money"]')[0].text_content().strip())
                        logger.info('получена цена %s' % advert.price)
                    except Exception as ex:
                        print ex

                    if not advert.price:
                        logger.info('нет цены')
                        continue

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

                    advert.save()

                    # метро
                    mtr_list = tds[3].xpath('.//select/option')
                    for mtr in mtr_list:
                        txt = mtr.text_content().strip()
                        if txt:
                            for metro in self.metro_list:
                                if metro.title.lower() in txt.lower():
                                    if not advert.metro:
                                        advert.metro = metro
                                    else:
                                        advert.need_metro.add(metro)
                                    logger.info('получено метро')
                                    break

                    advert.find_clients()

    def login(self, adtype):
        logger.info('Вход на сайт %s' % adtype)
        r = requests.get(self.domain)
        self.cookies = dict(r.cookies.items())
        params = {}
        if adtype == self.TYPE_LEASE:
            # params['user_name'] = u'grand.an'
            # params['user_pass'] = u'RtS1025522%^1'
            params['user_name'] = u'an.neva'
            params['user_pass'] = u'an.neva_MAriNA777'
            logger.info(params['user_name'])
        elif adtype == self.TYPE_SALE:
            params['user_name'] = u'Mir0k77'
            params['user_pass'] = u'Mir0k77@mail.ru'
            logger.info(params['user_name'])
        elif adtype == 'need':
            params['user_name'] = u'Arenda8888'
            params['user_pass'] = u'SeMA8888'
            logger.info(params['user_name'])
        params['auth'] = u'Войти'

        r = requests.post(self.login_url, data=params, cookies=self.cookies, allow_redirects=True)

    def logout(self):
        logger.info('Выход с сайта')
        r = requests.post(self.logout_url, cookies=self.cookies, allow_redirects=True)

    def collect(self, adtype):
        self.town = Town.objects.get(id=1)
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()
        self.parser = Parser.objects.get(title='pyxi')
        self.parser_sale = Parser.objects.get(title='pyxi_sale')
        self.parser_need = Parser.objects.get(title='pyxi_need')
        self.login(adtype)
        try:
            if adtype == Advert.TYPE_LEASE:
                doc = fromstring(self.download_url(self.catalog_url))
                doc.make_links_absolute(self.domain)
                self.process_elements(doc)
            if adtype == Advert.TYPE_SALE:
                doc = fromstring(self.download_url(self.catalog_sale_url))
                doc.make_links_absolute(self.domain)
                self.process_elements_sale(doc)
            if adtype == 'need':
                doc = fromstring(self.download_url(self.catalog_sale_need))
                doc.make_links_absolute(self.domain)
                self.process_elements_need(doc)
        except Exception, err:
            logger.info(traceback.format_exc())

        self.logout()

    def collect_all_sale(self):
        self.town = Town.objects.get(id=1)
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()
        self.login(Advert.TYPE_SALE)
        try:
            for page in xrange(238, 600):
                print "Страница %s" % page
                doc = fromstring(self.download_url(self.catalog_sale_url + "?page=%s" % page))
                doc.make_links_absolute(self.domain)
                self.process_elements_sale(doc)
        except Exception, err:
            logger.info(traceback.format_exc())

        self.logout()