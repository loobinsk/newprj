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
import base64
import pyocr
import pyocr.builders
from PIL import Image
from StringIO import StringIO
from django.conf import settings
from django.core.cache import cache

logger = logging.getLogger('irr')


class IrrCollector(Collector):
    domain = 'http://saint-petersburg.irr.ru/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    }

    metro_list = None
    district_list = None
    town = None
    parser = None
    cached_ids = []

    def process_elements(self, doc, adtype, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_FLAT, set_moderate=True):
        element_list = doc.xpath('//a[contains(@class, "productBlock")]')
        need_wait = False
        for element in element_list:
            if need_wait:
                seconds = random.randrange(10, 30)
                logger.info('### ждем %s секунд ###' % seconds)
                time.sleep(seconds)
                need_wait = False

            advert_id_list = re.findall(u'advert([0-9]*)\.html', element.get('href'))
            if advert_id_list:
                advert_id = advert_id_list[0]
            else:
                advert_id = None
            if not advert_id:
                logger.info('Пустой код')
                continue
            if advert_id in self.cached_ids:
                continue
            txt = u'irr_' + advert_id
            logger.info('====================================')
            logger.info(txt)
            advert_list = Advert.objects.filter(extnum=txt)
            if advert_list:
                logger.info('Объявление есть в базе')
                continue

            self.cached_ids.append(advert_id)

            item_link = element
            if item_link:
                logger.info(item_link.get('href'))
                r = requests.get(item_link.get('href'), cookies=self.cookies, allow_redirects=True, headers=self.headers)
                doc_text = r.text
                doc_advert = fromstring(doc_text)
                doc_advert.make_links_absolute(self.domain)

                logger.info("=======================")

                advert = Advert(town=self.town,
                                adtype = adtype,
                                need = Advert.NEED_SALE,
                                estate=estate,
                                live=live,
                                status=Advert.STATUS_MODERATE if set_moderate else Advert.STATUS_VIEW,
                                user=User.objects.get(username='admin'),
                                date=datetime.now(),
                                parser=self.parser,
                                extnum=u'irr_' + advert_id)

                #адрес
                nodes = doc_advert.xpath('//div[@class="productPage__infoItem"]/div[contains(@class, "productPage__infoTextBold")]')
                if nodes:
                    advert.address = nodes[0].text_content().strip()\
                        .replace(self.town.title+u', ', u'')

                # метро
                nodes = doc_advert.xpath('//div[@class="productPage__infoItem"]/div[contains(@class, "productPage__metro")]')
                if nodes:
                        txt = nodes[0].text_content()
                        for metro in self.metro_list:
                            if metro.title.lower() in txt.lower():
                                advert.metro = metro
                                logger.info('получен метро')
                                break

                # перебор характеристик
                lis = doc_advert.xpath('//div[@class="productPage__characteristicsItem"]')
                for li in lis:
                    name = li.xpath('.//span[@class="productPage__characteristicsItemTitle"]')
                    value = li.xpath('.//span[@class="productPage__characteristicsItemValue"]')
                    if u'комнаты' in name[0].text_content():
                        try:
                            advert.rooms = int(value[0].text_content())
                            logger.info('получены комнаты %s' % advert.rooms)
                        except Exception, err:
                            logger.info( traceback.format_exc())
                    if u'этаж' in name[0].text_content():
                        try:
                            value_list = value[0].text_content().split(u'из')
                            if len(value_list) >= 1:
                                advert.floor = int(value_list[0].strip())
                                logger.info('получены этаж %s' % advert.floor)
                            if len(value_list) == 2:
                                advert.count_floor = int(value_list[1].strip())
                                logger.info('получены этажи %s' % advert.count_floor)
                        except Exception, err:
                            logger.info( traceback.format_exc())
                    if u'общая площадь' in name[0].text_content():
                        try:
                            m = re.search(u'([0-9]+) м', value[0].text_content())
                            if m:
                                advert.square = float(m.group(1))
                                logger.info('получен общая площадь')
                        except Exception, err:
                            logger.info( traceback.format_exc())
                    if u'площадь кухни' in name[0].text_content():
                        try:
                            m = re.search(u'([0-9]+) м', value[0].text_content())
                            if m:
                                advert.kitchen_square = float(m.group(1))
                                logger.info('получен кухни')
                        except Exception, err:
                            logger.info( traceback.format_exc())
                    if u'жилая площадь' in name[0].text_content():
                        try:
                            m = re.search(u'([0-9]+) м', value[0].text_content())
                            if m:
                                advert.living_square = m.group(1)
                                logger.info('получен жилая площадь')
                        except Exception, err:
                            logger.info( traceback.format_exc())


                nodes = doc_advert.xpath('//li[@class="productPage__infoColumnBlockText"]')
                if nodes:
                    for node in nodes:
                        if u'Балкон' in node.text_content():
                            advert.balcony = True
                            logger.info('нашли балкон')
                        if u'Бытовая техника' in node.text_content():
                            advert.furniture = True
                            logger.info('нашли бытовую технику')
                        if u'Интернет' in node.text_content():
                            advert.internet = True
                            logger.info('нашли интернет')
                        if u'евроремонт' in node.text_content():
                            advert.euroremont = True
                            logger.info('нашли евроремонт')
                        if u'раздельный' in node.text_content():
                            advert.separate_wc = True
                            logger.info('нашли раздельный санузел')
                        if u'Лифты в здании' in node.text_content():
                            advert.lift = True
                            logger.info('нашли лифт')

                #цена
                nodes = doc_advert.xpath('//div[contains(@class, "productPage__price")]')
                if nodes:
                    txt = nodes[0].text_content().replace(u'\u00A0', u'').replace(u' ', u'')
                    m = re.search(u'([0-9]+)', txt)
                    if m:
                        try:
                            advert.price = int(m.group(1))
                            logger.info('нашли цену %s' % advert.price)
                        except Exception, err:
                            logger.info( traceback.format_exc())
                if not advert.price:
                    logger.info('цена не найдена')
                    continue

                # проверка цены на ценовую политику
                if advert.town.slug == 'sankt-peterburg' and advert.limit == Advert.LIMIT_LONG \
                        and advert.need == Advert.NEED_SALE and adtype == Advert.TYPE_LEASE:
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_ROOM):
                        if advert.price < 8000:
                            logger.info('Не подходит: Комнаты от 8000 до (ограничения нет)')
                            continue
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 1):
                        if advert.price < 17000:
                            logger.info('Не подходит: 1 ком.кв. от 17000 до (ограничения нет)')
                            continue
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 2):
                        if advert.price < 19000:
                            logger.info('Не подходит: 2 ком.кв. от 19000 до (ограничения нет)')
                            continue
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 3):
                        if advert.price < 20000:
                            logger.info('Не подходит: 3 ком.кв. от 20000 до (ограничения нет)')
                            continue
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms >= 4):
                        if advert.price < 22000:
                            logger.info('Не подходит: 4 и более ком.кв. от 22000 до (ограничения нет)')
                            continue

                if advert.town.slug == 'moskva' and advert.limit == Advert.LIMIT_LONG \
                        and advert.need == Advert.NEED_SALE and adtype == Advert.TYPE_LEASE:
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_ROOM):
                        if advert.price < 10000 or advert.price > 50000:
                            logger.info('Не подходит: Комнаты от 10000 до 50000')
                            continue
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 1):
                        if advert.price < 20000 or advert.price > 100000:
                            logger.info('Не подходит: 1 ком.кв. от 20000 до 100000')
                            continue
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 2):
                        if advert.price < 25000 or advert.price > 100000:
                            logger.info('Не подходит: 2 ком.кв. от 250000 до 100000')
                            continue
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 3):
                        if advert.price < 30000 or advert.price > 100000:
                            logger.info('Не подходит: 3 ком.кв. от 30000 до 100000')
                            continue
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms >= 4):
                        if advert.price < 35000 or advert.price > 100000:
                            logger.info('Не подходит: 4 и более ком.кв. от 35000 до 100000')
                            continue

                if advert.town.slug == 'novosibirsk' and advert.limit == Advert.LIMIT_LONG \
                        and advert.need == Advert.NEED_SALE and adtype == Advert.TYPE_LEASE:
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_ROOM) and advert.need == Advert.NEED_SALE:
                        if advert.price < 7000 or advert.price > 11000:
                            logger.info('Не подходит: Комнаты от 7000 до 11000')
                            continue
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 1):
                        if advert.price < 15000 or advert.price > 21000:
                            logger.info('Не подходит: 1 ком.кв. от 15000 до 21000')
                            continue
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 2):
                        if advert.price < 17000 or advert.price > 25000:
                            logger.info('Не подходит: 2 ком.кв. от 17000 до (25000')
                            continue
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 3):
                        if advert.price < 17000 or advert.price > 33000:
                            logger.info('Не подходит: 3 ком.кв. от 17000 до 33000')
                            continue
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms >= 4):
                        if advert.price < 18000 or advert.price > 35000:
                            logger.info('Не подходит: 4 и более ком.кв. от 18000 до 35000')
                            continue

                if advert.town.slug == 'ekaterinburg' and advert.limit == Advert.LIMIT_LONG \
                        and advert.need == Advert.NEED_SALE and adtype == Advert.TYPE_LEASE:
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_ROOM) and advert.need == Advert.NEED_SALE:
                        if advert.price < 7000 or advert.price > 11000:
                            logger.info('Не подходит: Комнаты от 7000 до 11000')
                            continue
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 1):
                        if advert.price < 9000 or advert.price > 21000:
                            logger.info('Не подходит: 1 ком.кв. от 9000 до 21000')
                            continue
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 2):
                        if advert.price < 12000 or advert.price > 25000:
                            logger.info('Не подходит: 2 ком.кв. от 12000 до (25000')
                            continue
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 3):
                        if advert.price < 17000 or advert.price > 33000:
                            logger.info('Не подходит: 3 ком.кв. от 17000 до 33000')
                            continue
                    if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms >= 4):
                        if advert.price < 18000 or advert.price > 35000:
                            logger.info('Не подходит: 4 и более ком.кв. от 18000 до 35000')
                            continue

                #координаты
                m = re.search(u'center: \[([0-9|\.]+),([0-9|\.]+)\],', doc_text)
                if m:
                    try:
                        advert.latitude = float(m.group(1))
                        advert.longitude = float(m.group(2))
                        logger.info('нашли координаты')
                    except Exception, err:
                        logger.info( traceback.format_exc())

                #определение агента
                nodes = doc_advert.xpath('//div[@class="productPage__infoTextBold productPage__infoTextBold_inline"]/a')
                if nodes:
                    try:
                        href = nodes[0].get('href')
                        if (not u'user' in href) or (href == u'#'):
                            logger.info(u'Это агент')
                            continue
                        advert.owner_name = nodes[0].text_content()
                    except Exception, err:
                        logger.info( traceback.format_exc())

                #описание
                nodes = doc_advert.xpath('//p[contains(@class, "js-productPageDescription")]')
                if nodes:
                    advert.body = nodes[0].text_content().strip()
                    logger.info('получено описание')
                    advert.parse(advert.body)

                    if u'комисси' in advert.body.lower():
                        logger.info('есть комиссия')
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
                nodes = doc_advert.xpath('//div[contains(@class, "js-productPagePhoneLabel")]')
                if nodes:
                    try:
                        coded_string = nodes[0].get('data-phone')
                        owner_tel = base64.b64decode(coded_string)
                        if owner_tel.startswith('8'):
                            owner_tel = '7' + owner_tel[1:]
                        owner_tel = clear_tel_list(owner_tel)
                        logger.info(u'открыл телефон %s' % owner_tel)
                        advert.owner_tel = owner_tel
                        result = advert.check_spam(actions=True)
                        if result:
                            logger.info(result)
                            continue
                    except Exception, err:
                        logger.info(traceback.format_exc())
                else:
                    logger.info('код телефона не найден')

                if not advert.owner_tel:
                    logger.info('телефон не найден')
                    continue

                advert.save()
                # advert.find_metro_distance()
                if advert.check_owner():
                    advert.save()
                # advert.publish()

                elems = doc_advert.xpath('//div[contains(@class, "productGallery")]/img')
                if elems:
                    logger.info('найдено %s фоток' % len(elems))
                    for a in elems:
                        try:
                            src = a.get('data-src')
                            logger.info(src)
                            image = UserImage(user=advert.user)
                            if image.load_irr_avito_crop(src):
                                image.save()
                                advert.images.add(image)
                        except Exception, err:
                            logger.debug(traceback.format_exc())

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

        lang = 'phone'
        if settings.DEBUG:
            lang = 'eng'

        txt = tool.image_to_string(img, lang=lang, builder=pyocr.builders.TextBuilder())
        logger.info('распознан')
        logger.info(txt)
        return txt

    def process_url(self, url, adtype, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_FLAT, set_moderate=True):
        try:
            r = requests.get(url,  cookies=self.cookies, allow_redirects=True, headers=self.headers)
            self.cookies = dict(r.cookies.items())
            doc = fromstring(r.text)
            doc.make_links_absolute(self.domain)
            self.process_elements(doc, adtype=adtype, estate=estate, live=live, set_moderate=set_moderate)
        except Exception, err:
            logger.info(traceback.format_exc())

    def collect(self):
        self.parser = Parser.objects.get(title='irr')
        self.cached_ids = cache.get('parser_irr_ids', [])

        # САНКТ ПЕТЕРБУРГ
        self.town = Town.objects.get(id=2)
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()

        # квартиры
        logger.info('#### КВАРТИРЫ ####')
        self.process_url('http://saint-petersburg.irr.ru/real-estate/rent/sankt-peterburg-gorod/search/price=%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B5+18000/currency=RUR/rent_period=3674653711/fee=%D0%BC%D0%B5%D0%BD%D1%8C%D1%88%D0%B5+1/list=list/sort/date_sort:desc/page_len60/',
                         adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_FLAT)
        # комнаты
        logger.info('#### КОМНАТЫ ####')
        self.process_url('http://saint-petersburg.irr.ru/real-estate/rooms-rent/search/price=%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B5+8000/currency=RUR/rent_period=3674653711/fee=%D0%BC%D0%B5%D0%BD%D1%8C%D1%88%D0%B5+1/list=list/sort/date_sort:desc/page_len60/',
                         adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_ROOM)


        # МОСКВА
        self.town = Town.objects.get(slug='moskva')
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()

        # квартиры
        logger.info('#### КВАРТИРЫ ####')
        self.process_url('http://irr.ru/real-estate/rent/search/price=%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B5+20000/currency=RUR/rent_period=3674653711/fee=%D0%BC%D0%B5%D0%BD%D1%8C%D1%88%D0%B5+1/list=list/sort/date_sort:desc/page_len60/',
                         adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_FLAT)
        # комнаты
        logger.info('#### КОМНАТЫ ####')
        self.process_url('http://irr.ru/real-estate/rooms-rent/search/price=%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B5+10000/currency=RUR/rent_period=3674653711/fee=%D0%BC%D0%B5%D0%BD%D1%8C%D1%88%D0%B5+1/list=list/sort/date_sort:desc/page_len60/',
                         adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_ROOM)


        # Новосибирск
        self.town = Town.objects.get(slug='novosibirsk')
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()

        # квартиры
        logger.info('#### КВАРТИРЫ ####')
        self.process_url('http://novosibirsk.irr.ru/real-estate/rent/search/price=%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B5%209000/currency=RUR/fee=%D0%BC%D0%B5%D0%BD%D1%8C%D1%88%D0%B5%201/',
                         adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_FLAT, set_moderate=False)

        # Екатеринбург
        self.town = Town.objects.get(slug='ekaterinburg')
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()

        # квартиры
        logger.info('#### КВАРТИРЫ ####')
        self.process_url('http://ekaterinburg.irr.ru/real-estate/rent/search/price=%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B5%209000/currency=RUR/fee=%D0%BC%D0%B5%D0%BD%D1%8C%D1%88%D0%B5%201/',
                         adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, live=Advert.LIVE_FLAT, set_moderate=False)


        if len(self.cached_ids) > 1000:
            self.cached_ids = self.cached_ids[(len(self.cached_ids) - 1000):]
        cache.set('parser_irr_ids', self.cached_ids, 6 * 60 * 60)
        logger.info('#### ВЫХОД ####')
