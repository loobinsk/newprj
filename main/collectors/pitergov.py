#-*- coding: utf-8 -*-
from lxml import html
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

logger = logging.getLogger('pitergov')


class PitergovCollector(Collector):
    domain = 'http://www.pitergov.ru/'
    catalog_url = 'http://www.pitergov.ru//base.php'
    login_url = 'http://www.pitergov.ru//index.php'
    logout_url = 'http://www.pitergov.ru//exit.php'
    demo_url = 'http://www.pitergov.ru//index.php?user=demo&pass=demo'
    phone_url = 'http://www.pitergov.ru//modules/phone.php'

    metro_list = None
    district_list = None
    town = None
    parser = None

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

            # проверка агента
            if u'Агент' in tds[9].text_content():
                logger.info('Это агент')
                continue

            # идентификатор
            advert_id = tds[9].xpath('.//a')[0].get('id').replace(u'complain', '')
            txt = u'piter_' + advert_id
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
                doc_text = self.download_url('http://www.pitergov.ru/modules/map.php?id=%s' % advert_id)
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
            txt = tds[7].text_content().strip().replace(u'Оставить комментарий', u'').\
                replace(u'Виден только Вам', u'')
            advert.body = Abbr.abbry(txt)
            logger.info('Получен комментарий объявления')
            if u'Есть TV' in txt:
                advert.tv = True
                logger.info('тв')
            if u'Балкон' in txt:
                advert.balcony = True
                logger.info('балкон')
            if u'Тр. ремонта' in txt:
                advert.need_remont = True
                logger.info('нужен ремонт')
            if u'без рем.' in txt:
                advert.no_remont = True
                logger.info('без ремонта')
            advert.parse(advert.body)

            try:
                m = re.search(ur"(\d+)/(\d+)/(\d+)", txt)
                if m:
                    advert.square = int(m.group(1))
                    advert.living_square = int(m.group(2))
                    advert.kitchen_square = int(m.group(3))
                    logger.info('получены площади кухни и жилой площади')
                else:
                    m = re.search(ur"(\d+)м2", txt)
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

            if advert.live == Advert.LIVE_ROOM and (advert.price<7000 or advert.price>100000):
                logger.info('Не подходит по цене 7000-50000')
                continue

            elif advert.live == Advert.LIVE_FLAT and advert.rooms == 1 and (advert.price<15000 or advert.price>100000):
                logger.info('Не подходит 1к по цене 15000-100000')
                continue

            elif advert.live == Advert.LIVE_FLAT and advert.rooms == 2 and (advert.price<18000 or advert.price>100000):
                logger.info('Не подходит 2к по цене 18000-100000')
                continue

            elif advert.live == Advert.LIVE_FLAT and advert.rooms == 3 and (advert.price<18000 or advert.price>100000):
                logger.info('Не подходит 3к  по цене 18000-92000')
                continue

            elif advert.live == Advert.LIVE_FLAT and advert.rooms == 4 and (advert.price<20000 or advert.price>100000):
                logger.info('Не подходит 4к по цене 20000-100000')
                continue

            # получение телефона
            r = requests.post(self.phone_url, data={'id': advert_id}, cookies=self.cookies)
            need_wait = True
            r.encoding = self.encoding
            telre = re.compile(r">([0-9\ \+]+)</span>")
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
                    for duplicate in duplicate_list:
                        if duplicate.status == Advert.STATUS_VIEW:
                            logger.info(u'найден размещенный дубликат %s' % duplicate.id)
                            continue
                        else:
                            duplicate.status = Advert.STATUS_BLOCKED
                            logger.info(u'дубликат %s удален' % duplicate.id)
                            duplicate.save()

                m = re.search(ur'</span><br>(.+)<br><div', st)
                if m:
                    advert.owner_name = m.group(1)
                    logger.info('найден владелец')
            else:
                logger.info('Телефон не найден')
                logger.info(st.encode('utf8'))
                continue

            advert.save()

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

            advert.find_clients()
            advert.find_metro_distance()
            advert.find_surrounding_objects()
            advert.publish()

    def login(self, adtype):
        logger.info('Вход на сайт Pitergov %s' % adtype)
        r = requests.get(self.domain)
        self.cookies = dict(r.cookies.items())
        params = {}
        if adtype == self.TYPE_LEASE:
            params['user_name'] = u'gid.rafa'
            params['user_pass'] = u'0O519rTY45IoS'
            logger.info(params['user_name'])
        params['auth'] = u'Войти'

        r = requests.post(self.login_url, data=params, cookies=self.cookies, allow_redirects=True)

    def logout(self):
        logger.info('Выход с сайта')
        r = requests.post(self.logout_url, cookies=self.cookies, allow_redirects=True)

    def collect(self, adtype):
        self.town = Town.objects.get(id=2)
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()
        self.parser = Parser.objects.get(title='pitergov')
        self.login(adtype)
        try:
            if adtype == Advert.TYPE_LEASE:
                doc = fromstring(self.download_url(self.catalog_url))
                doc.make_links_absolute(self.domain)
                self.process_elements(doc)
        except Exception, err:
            logger.info(traceback.format_exc())

        self.logout()