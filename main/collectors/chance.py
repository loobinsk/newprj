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
import random
import pyocr
import pyocr.builders
from PIL import Image
from StringIO import StringIO
from django.conf import settings
from django.core.cache import cache

logger = logging.getLogger('chance')


class ChanceCollector(Collector):
    domain = 'http://chance.ru/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    }

    metro_list = None
    district_list = None
    town = None
    parser = None
    cached_ids = []

    def process_elements(self, doc, adtype, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_FLAT, set_moderate=True, level=Advert.CHECK_SPAM_LOW):
        element_list = doc.xpath('//div[@class="item-list"]/ul[@class="catalog-list"]/li')
        need_wait = False
        for element in element_list:
            if need_wait:
                seconds = random.randrange(10, 15)
                logger.info('### ждем %s секунд ###' % seconds)
                time.sleep(seconds)
                need_wait = False

            item_link = element.xpath('.//h3/a')
            if item_link:
                # logger.info(item_link[0].get('href'))

                m = re.search(u'/([0-9]+)$', item_link[0].get('href'))
                if m:
                    advert_id = m.group(1)
                    if not advert_id:
                        logger.info('Пустой код')
                        continue
                    if advert_id in self.cached_ids:
                        continue
                    self.cached_ids.append(advert_id)
                    txt = u'chance_' + advert_id
                    logger.info('====================================')
                    logger.info(txt)
                    advert_list = Advert.objects.filter(extnum=txt)
                    if advert_list:
                        logger.info('Объявление есть в базе')
                        continue
                else:
                    logger.info('Номер объявления не найден')
                    continue

                if u'квартиру' in item_link[0].text_content() or \
                    u'комнату' in item_link[0].text_content():
                    logger.info('не комната и не квартира')

                r = requests.get(item_link[0].get('href'), cookies=self.cookies, allow_redirects=True, headers=self.headers)
                doc_advert = fromstring(r.text)
                doc_advert.make_links_absolute(self.domain)

                logger.info("=======================")

                advert = Advert(town=self.town,
                                adtype = adtype,
                                need = Advert.NEED_SALE,
                                estate=estate,
                                live=live,
                                status=Advert.STATUS_MODERATE,
                                user=User.objects.get(username='admin'),
                                date=datetime.now(),
                                parser=self.parser,
                                extnum=u'chance_' + advert_id)

                if not set_moderate:
                    advert.status = Advert.STATUS_VIEW

                #цена
                nodes = doc_advert.xpath('//div[@class="coast"]')
                if nodes:
                    txt = nodes[0].get('content')
                    try:
                        advert.price = int(txt)
                        logger.info('нашли цену %s' % advert.price)
                    except Exception, err:
                        logger.info( traceback.format_exc())

                if not advert.price:
                    logger.info('цена не найдена')
                    continue

                #имя владельца
                nodes = doc_advert.xpath('//span[@itemprop="name"]/a')
                if nodes:
                    try:
                        advert.owner_name = nodes[0].text_content().strip()
                        logger.info('получено имя владельца')
                        if not u'seller' in nodes[0].get('href'):
                            logger.info('это агент')
                            continue
                        if u'агент' in advert.owner_name.lower():
                            logger.info('это агент')
                            continue
                    except Exception, err:
                        logger.info( traceback.format_exc())

                #описание
                nodes = doc_advert.xpath('//div[@class="content-box full-desc"]')
                if nodes:
                    advert.body = nodes[0].text_content().strip().replace(u'Описание', u'')
                    logger.info('получено описание')

                    advert.parse(advert.body)

                #свойства
                nodes = doc_advert.xpath('//div[@class="content-box options clearfix"]/table/tbody/tr')
                if nodes:
                    for tr in nodes:
                        th = tr.xpath('.//th')
                        td = tr.xpath('.//td')
                        if th and td:
                            if u'Этажность дома' in th[0].text_content():
                                try:
                                    advert.count_floor = int(td[0].text_content().strip())
                                    logger.info('этажей %s' % advert.count_floor)
                                except Exception, err:
                                    logger.info( traceback.format_exc())
                            if u'Этаж' == th[0].text_content():
                                try:
                                    advert.floor = int(td[0].text_content().strip())
                                    logger.info('этаж %s' % advert.floor)
                                except Exception, err:
                                    logger.info( traceback.format_exc())
                            if u'Срок аренды' in th[0].text_content():
                                if u'посуточно' in td[0].text_content():
                                    advert.limit == Advert.LIMIT_DAY
                                    logger.info('посуточно')
                            if u'Жилая площадь' in th[0].text_content():
                                try:
                                    txt = td[0].text_content().strip()
                                    m = re.search(u'([0-9|\.|\ ]+)м', txt)
                                    if m:
                                        advert.living_square = float(m.group(1))
                                        logger.info('жилая площадь %s' % advert.living_square)
                                except Exception, err:
                                    logger.info( traceback.format_exc())
                            if u'Общая площадь' in th[0].text_content():
                                try:
                                    txt = td[0].text_content().strip()
                                    m = re.search(u'([0-9|\.|\ ]+)м', txt)
                                    if m:
                                        advert.square = float(m.group(1))
                                        logger.info('общая площадь %s' % advert.square)
                                except Exception, err:
                                    logger.info( traceback.format_exc())
                            if u'Кол-во комнат' in th[0].text_content():
                                try:
                                    advert.rooms = int(td[0].text_content().strip())
                                    logger.info('комнат %s' % advert.rooms)
                                except Exception, err:
                                    logger.info( traceback.format_exc())
                            if u'Адрес' in th[0].text_content():
                                advert.address = td[0].text_content().strip()
                                logger.info('найден адрес')
                            if u'Метро' in th[0].text_content():
                                txt = td[0].text_content().strip()
                                for metro in self.metro_list:
                                    if metro.title.lower() in txt.lower():
                                        advert.metro = metro
                                        logger.info('получено метро')
                                        break
                if not advert.rooms:
                    advert.rooms = 1

                #больше инфы
                nodes = doc_advert.xpath('//div[@class="more-info"]/ul/li')
                if nodes:
                    for li in nodes:
                        txt = li.text_content().lower()
                        if u'интернет' in txt:
                            advert.internet = True
                        if u'мебель' in txt:
                            advert.furniture = True
                        if u'телевизор' in txt:
                            advert.tv = True
                        if u'стиральная машина' in txt:
                            advert.washer = True
                        if u'xолодильник' in txt:
                            advert.refrigerator = True

                # проверка цены на ценовую политику
#                if advert.limit == Advert.LIMIT_LONG and advert.town.slug=='sankt-peterburg' and advert.adtype==Advert.TYPE_LEASE \
#                        and advert.need == Advert.NEED_SALE:
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_ROOM):
#                        if advert.price < 8000:
#                            logger.info('Не подходит: Комнаты от 8000 до (ограничения нет)')
#                            continue
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 1):
#                        if advert.price < 17000:
#                            logger.info('Не подходит: 1 ком.кв. от 17000 до (ограничения нет)')
#                            continue
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 2):
#                        if advert.price < 19000:
#                            logger.info('Не подходит: 2 ком.кв. от 19000 до (ограничения нет)')
#                            continue
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 3):
#                        if advert.price < 20000:
  #                          logger.info('Не подходит: 3 ком.кв. от 20000 до (ограничения нет)')
 #                           continue
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms >= 4):
#                        if advert.price < 22000:
#                            logger.info('Не подходит: 4 и более ком.кв. от 22000 до (ограничения нет)')
#                            continue
#
#                if advert.town.slug == 'moskva' and advert.limit == Advert.LIMIT_LONG \
  #                      and advert.need == Advert.NEED_SALE and adtype == Advert.TYPE_LEASE:
  #                  if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_ROOM):
  #                      if advert.price < 10000 or advert.price > 50000:
  #                          logger.info('Не подходит: Комнаты от 10000 до 50000')
 #                           continue
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 1):
#                        if advert.price < 20000 or advert.price > 100000:
#                            logger.info('Не подходит: 1 ком.кв. от 20000 до 100000')
 #                           continue
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 2):
#                        if advert.price < 25000 or advert.price > 100000:
#                            logger.info('Не подходит: 2 ком.кв. от 250000 до 100000')
#                            continue
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 3):
#                        if advert.price < 30000 or advert.price > 100000:
#                            logger.info('Не подходит: 3 ком.кв. от 30000 до 100000')
#                            continue
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms >= 4):
#                        if advert.price < 35000 or advert.price > 100000:
#                            logger.info('Не подходит: 4 и более ком.кв. от 35000 до 100000')
#                            continue
#
#                if advert.town.slug == 'novosibirsk' and advert.limit == Advert.LIMIT_LONG \
#                        and advert.need == Advert.NEED_SALE and adtype == Advert.TYPE_LEASE:
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_ROOM):
#                        if advert.price < 7000 or advert.price > 11000:
#                           logger.info('Не подходит: Комнаты от 7000 до 11000')
#                            continue
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 1):
#                        if advert.price < 15000 or advert.price > 21000:
#                            logger.info('Не подходит: 1 ком.кв. от 15000 до 21000')
#                            continue
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 2):
#                        if advert.price < 17000 or advert.price > 25000:
#                            logger.info('Не подходит: 2 ком.кв. от 17000 до (25000')
#                            continue
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 3):
#                        if advert.price < 17000 or advert.price > 33000:
#                            logger.info('Не подходит: 3 ком.кв. от 17000 до 33000')
#                            continue
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms >= 4):
#                       if advert.price < 18000 or advert.price > 35000:
#                           logger.info('Не подходит: 4 и более ком.кв. от 18000 до 35000')
#                            continue

#                if advert.town.slug == 'ekaterinburg' and advert.limit == Advert.LIMIT_LONG \
#                        and advert.need == Advert.NEED_SALE and advert.adtype == Advert.TYPE_LEASE:
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_ROOM) and advert.need == Advert.NEED_SALE:
#                        if advert.price < 7000 or advert.price > 11000:
#                            logger.info('Не подходит: Комнаты от 7000 до 11000')
#                            continue
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 1):
#                        if advert.price < 9000 or advert.price > 21000:
#                            logger.info('Не подходит: 1 ком.кв. от 9000 до 21000')
#                            continue
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 2):
#                        if advert.price < 12000 or advert.price > 25000:
#                            logger.info('Не подходит: 2 ком.кв. от 12000 до (25000')
#                            continue
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 3):
#                        if advert.price < 17000 or advert.price > 33000:
#                            logger.info('Не подходит: 3 ком.кв. от 17000 до 33000')
#                            continue
#                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms >= 4):
#                        if advert.price < 18000 or advert.price > 35000:
#                            logger.info('Не подходит: 4 и более ком.кв. от 18000 до 35000')
#                            continue

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
                        if not advert.district:
                            district_name = doccoord.xpath('//description')
                            if district_name:
                                txt = district_name[0].text_content()
                                for district in self.district_list:
                                    if district.title.lower() in txt.lower():
                                        advert.district = district
                                        logger.info('получен район')
                                        break
                    except Exception, err:
                        logger.info(traceback.format_exc())

                # телефон
                nodes = doc_advert.xpath('//a[@class="phone-image-img"]/img')
                if nodes:
                    try:
                        href = nodes[0].get('src')
                        logger.info(href)
                        owner_tel = self.get_txt_from_image(href)
                        if owner_tel.startswith('8'):
                            owner_tel = '7' + owner_tel[1:]
                        owner_tel = clear_tel(owner_tel)
                        logger.info(u'открыл телефон %s' % owner_tel)
                        advert.owner_tel = owner_tel
                        result = advert.check_spam(actions=True, level=level)
                        if result:
                            logger.info(result)
                            continue
                    except Exception, err:
                        logger.info(traceback.format_exc())
                else:
                    logger.info('ссылка телефона не найдена')

                if not advert.owner_tel:
                    logger.info('телефон не найден')
                    continue

                advert.save()

                elems = doc_advert.xpath('//li[@class="gallery-slide"]/a')
                if elems:
                    logger.info('найдено %s фоток' % len(elems))
                    for a in elems:
                        try:
                            src = a.get('href')
                            logger.info(src)
                            image = UserImage(user=advert.user)
                            if image.load_image_chance_crop(src):
                                image.save()
                                advert.images.add(image)
                        except Exception, err:
                            logger.debug(traceback.format_exc())

                advert.find_metro_distance()
                if advert.check_owner():
                    advert.save()
                advert.publish()

        return True

    def get_txt_from_image(self, url):
        r = requests.get(url)
        img = Image.open(StringIO(r.content))

        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            logger.info("No OCR tool found")
            return False
        tool = tools[0]
        logger.info("Will use tool '%s'" % (tool.get_name()))

        lang = 'chance'
        if settings.DEBUG:
            lang = 'eng'

        txt = tool.image_to_string(img, lang=lang, builder=pyocr.builders.TextBuilder())
        logger.info('распознан')
        logger.info(txt)
        return txt

    def process_url(self, url, adtype, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_FLAT, set_moderate=True, level=Advert.CHECK_SPAM_LOW):
        r = requests.get(url, cookies=self.cookies, allow_redirects=True, headers=self.headers)
        self.cookies = dict(r.cookies.items())
        doc = fromstring(r.text)
        doc.make_links_absolute(self.domain)
        self.process_elements(doc, adtype=adtype, estate=estate, live=live, set_moderate=set_moderate, level=level)


    def collect(self):
        self.cached_ids = cache.get('parser_chance_ids', [])

        self.parser = Parser.objects.get(title='chance')

        logger.info('#### САНКТ-ПЕТЕРБУРГ ####')
        self.town = Town.objects.get(id=2)
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()

        try:
            logger.info('#### КВАРТИРЫ ####')
            self.process_url('http://chance.ru/sankt-peterburg/estate-apartment-lease?is_store=private&field_srokarendaposutochnonadl=%D0%BD%D0%B0%20%D0%B4%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%81%D1%80%D0%BE%D0%BA',
                                  adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_FLAT)

#            self.process_url('http://chance.ru/sankt-peterburg/estate-apartment-sale?is_store=private&items_per_page=100',
#                                  adtype=Advert.TYPE_SALE, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_FLAT, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)

        except Exception, err:
            logger.info(traceback.format_exc())

        try:
            logger.info('#### КОМНАТЫ ####')
            self.process_url('http://chance.ru/sankt-peterburg/estate-rooms-lease?is_store=private&field_srokarendaposutochnonadl=%D0%BD%D0%B0%20%D0%B4%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%81%D1%80%D0%BE%D0%BA',
                             adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_ROOM)
        except Exception, err:
            logger.info(traceback.format_exc())


        logger.info('#### МОСКВА ####')
        self.town = Town.objects.get(slug='moskva')
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()

        try:
            logger.info('#### КВАРТИРЫ ####')
            self.process_url('http://chance.ru/moskva/estate-apartment-lease?is_store=private&field_srokarendaposutochnonadl=%D0%BD%D0%B0%20%D0%B4%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%81%D1%80%D0%BE%D0%BA',
                                  adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_FLAT)

#            self.process_url('http://chance.ru/moskva/estate-apartment-sale?is_store=private&items_per_page=100',
#                                  adtype=Advert.TYPE_SALE, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_FLAT, set_moderate=True, level=Advert.CHECK_SPAM_STRONG)

        except Exception, err:
            logger.info(traceback.format_exc())

        try:
            logger.info('#### КОМНАТЫ ####')
            self.process_url('http://chance.ru/moskva/estate-rooms-lease?is_store=private&field_srokarendaposutochnonadl=%D0%BD%D0%B0%20%D0%B4%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%81%D1%80%D0%BE%D0%BA',
                             adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_ROOM)
        except Exception, err:
            logger.info(traceback.format_exc())


        logger.info('#### НОВОСИБИРСК ####')
        self.town = Town.objects.get(slug='novosibirsk')
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()

        try:
            logger.info('#### КВАРТИРЫ ####')
            self.process_url('http://chance.ru/novosibirskaya-oblast/estate-apartment-lease?is_store=private&field_srokarendaposutochnonadl=%D0%BD%D0%B0%20%D0%B4%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%81%D1%80%D0%BE%D0%BA',
                                  adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_FLAT, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)

#            self.process_url('http://chance.ru/novosibirskaya-oblast/estate-apartment-sale?is_store=private&items_per_page=100&r=1485203807',
#                                  adtype=Advert.TYPE_SALE, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_FLAT, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)

        except Exception, err:
            logger.info(traceback.format_exc())

        try:
            logger.info('#### КОМНАТЫ ####')
            self.process_url('http://chance.ru/novosibirskaya-oblast/estate-rooms-lease?is_store=private&field_srokarendaposutochnonadl=%D0%BD%D0%B0%20%D0%B4%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%81%D1%80%D0%BE%D0%BA',
                             adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_ROOM, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
        except Exception, err:
            logger.info(traceback.format_exc())


        logger.info('#### ЕКАТЕРИНБУРГ ####')
        self.town = Town.objects.get(slug='ekaterinburg')
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()

        try:
            logger.info('#### КВАРТИРЫ ####')
            self.process_url('http://chance.ru/sverdlovskaya-oblast/estate-apartment-lease?is_store=private&field_srokarendaposutochnonadl=%D0%BD%D0%B0%20%D0%B4%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%81%D1%80%D0%BE%D0%BA',
                                  adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_FLAT, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)

#            self.process_url('http://chance.ru/sverdlovskaya-oblast/estate-apartment-sale?is_store=private',
#                                  adtype=Advert.TYPE_SALE, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_FLAT, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)

        except Exception, err:
            logger.info(traceback.format_exc())

        try:
            logger.info('#### КОМНАТЫ ####')
            self.process_url('http://chance.ru/sverdlovskaya-oblast/estate-rooms-lease?is_store=private&field_srokarendaposutochnonadl=%D0%BD%D0%B0%20%D0%B4%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%81%D1%80%D0%BE%D0%BA',
                             adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_ROOM, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
        except Exception, err:
            logger.info(traceback.format_exc())

        if len(self.cached_ids) > 1000:
            self.cached_ids = self.cached_ids[(len(self.cached_ids) - 1000):]
        cache.set('parser_chance_ids', self.cached_ids, 6 * 60 * 60)

        logger.info('#### ВЫХОД ####')
