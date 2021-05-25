#-*- coding: utf-8 -*-
from lxml import html, etree
from lxml.html import fromstring
from lxml.html import tostring
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
import json
from django.core.cache import cache
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger('domofond')


class DomofondCollector(Collector):
    domain = 'http://www.domofond.ru/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    }

    metro_list = None
    district_list = None
    town = None
    parser = None
    cached_ids = []

    def process_elements(self, url, doc, adtype, limit, need=Advert.NEED_SALE, set_moderate=True, level=Advert.CHECK_SPAM_LOW):
        element_list = doc.xpath('//a[contains(@class, "long-item-card__item___ubItG")]')
        need_wait = False
        for element in element_list:
            # print(element)
            if need_wait:
                seconds = random.randrange(15, 30)
                logger.info('### ждем %s секунд ###' % seconds)
                time.sleep(seconds)
                need_wait = False

            item_link = element.get('href')
            if item_link:
                print('[OK]', item_link)
                m = re.search(u'\-([0-9]+)$', item_link)
                if m:
                    advert_id = m.group(1)
                    if not advert_id:
                        logger.info('Пустой код')
                        continue
                    if advert_id in self.cached_ids:
                        continue
                    txt = u'domofond_' + advert_id
                    logger.info(txt)
                    advert_list = Advert.objects.filter(extnum=txt)
                    if advert_list:
                        logger.info('Объявление есть в базе')
                        continue
                else:
                    logger.info('Код объявления не распознан')
                    continue

                headers = self.headers.copy()
                headers['referer'] = url

                # r = requests.get(item_link, cookies=self.cookies, allow_redirects=True, headers=headers)
                # doc_advert = fromstring(r.text)
                # doc_advert.make_links_absolute(self.domain)

                options = webdriver.ChromeOptions()
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-dev-shm-usage')
                options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 YaBrowser/20.2.3.211 Yowser/2.5 Safari/537.36")
                driver = webdriver.Chrome(executable_path="%s/chromedriver" % os.getcwd(), chrome_options=options)
                driver.implicitly_wait(10)

                driver.get(item_link)

                logger.info("=======================")
                logger.info(item_link)
                need_wait = True

                self.cached_ids.append(advert_id)

                advert = Advert(town=self.town,
                                adtype = adtype,
                                need = need,
                                status=Advert.STATUS_MODERATE if set_moderate else Advert.STATUS_VIEW,
                                limit=limit,
                                user_id=1,
                                date=datetime.now(),
                                parser=self.parser,
                                extnum=u'domofond_' + advert_id)

                #заголовок
                nodes = driver.find_elements_by_xpath('.//h1')
                if nodes:
                    txt = nodes[0].text
                    if u'квартира в аренду' in txt:
                        advert.estate = Advert.ESTATE_LIVE
                        advert.live = Advert.LIVE_FLAT
                        logger.info('нашли квартиру')
                    if u'комната в аренду' in txt:
                        advert.estate = Advert.ESTATE_LIVE
                        advert.live = Advert.LIVE_ROOM
                        logger.info('нашли комнату')

                    for room in xrange(1, 6):
                        if u'%s-комнат' % room in txt:
                            advert.rooms = room
                            if advert.rooms > 4:
                                advert.rooms = 4
                            if advert.rooms == 1:
                                advert.live_flat1 = True
                            elif advert.rooms == 2:
                                advert.live_flat2 = True
                            elif advert.rooms == 3:
                                advert.live_flat3 = True
                            elif advert.rooms >= 4:
                                advert.live_flat4 = True
                            logger.info('нашли %s комнат' % room)
                    if not advert.rooms:
                        advert.rooms = 1

                    # try:
                    #     m = re.search(u'([0-9|\.]+) м', txt)
                    #     if m:
                    #         advert.square = int(m.group(1))
                    #         logger.info('нашли площадь %s м' %advert.square)
                    # except Exception, err:
                    #     logger.info( traceback.format_exc())
                    #

                    # for floors in xrange(1, 50):
                    #     if (u'%s-этажного' % floors) in txt:
                    #         advert.count_floor = floors
                    #         logger.info('нашли этажи %s' % floors)

                # цена
                nodes = driver.find_elements_by_xpath('//div[contains(@class, "information__price___2Lpc0")]/span')
                if nodes:
                    txt = nodes[0].text.replace(' ', '')
                    txt = txt.replace(u'₽', '')
                    if txt:
                        try:
                            advert.price = int(txt)
                            logger.info('нашли цену %s' % advert.price)
                        except Exception, err:
                            logger.info( traceback.format_exc())

                if not advert.price and need == Advert.NEED_SALE:
                    logger.info('цена не найдена')
                    driver.quit()
                    continue

                # метро
                nodes = driver.find_elements_by_xpath('.//div[@class="information__metro___2zFqN"]')
                if nodes:
                    txt = nodes[0].text
                    txt = re.sub(r'<div[^\<]+</div>', '', txt)
                    for metro in self.metro_list:
                        if metro.title.lower() in txt.lower():
                            advert.metro = metro
                            logger.info('получено метро')
                            break

                # адрес
                nodes = driver.find_elements_by_xpath('.//a[@class="information__address___1ZM6d"]')
                if nodes:
                    advert.address = nodes[0].text.strip()
                    logger.info('получен адрес')

                #координаты
                # nodes = doc_advert.xpath('.//div[@id="item-map"]')
                # if nodes:
                #     try:
                #         advert.latitude = float(nodes[0].get('data-coords-lat'))
                #         advert.longitude = float(nodes[0].get('data-coords-lng'))
                #         logger.info('получен координаты')
                #     except Exception, err:
                #         logger.info( traceback.format_exc())

                #имя владельца
                nodes = driver.find_elements_by_xpath('.//h3[@class="saller-information__title___mzWjG"]')
                if nodes:
                    advert.owner_name = nodes[0].text.strip()
                    logger.info('получено имя владельца')
                    if u'агент' in advert.owner_name.lower():
                        logger.info('это агент')
                        driver.quit()
                        continue

                #описание
                nodes = driver.find_elements_by_xpath('.//div[@class="description__description___2FDOM"]')
                if nodes:
                    advert.body = nodes[0].text.strip()
                    logger.info('получено описание')
                    advert.parse(advert.body)

                    #if u'комисси' in advert.body.lower():
                        #logger.info('есть комиссия')
                        #driver.quit()
                        #continue

                # свойства
                nodes = driver.find_elements_by_xpath('//div[@class="detail-information__row___29Fu6"]')
                if nodes:
                    for node in nodes:
                        txt = node.text\
                            .replace('\u00A0', '')\
                            .replace('&nbsp;', '')
                        if u'Этаж' in txt:
                            m = re.search(u'([0-9]+)\/([0-9]+)', txt)
                            if m:
                                try:
                                    advert.floor = int(m.group(1))
                                    logger.info('нашли этаж %s' % advert.floor)
                                except Exception, err:
                                    logger.info(traceback.format_exc())
                                try:
                                    advert.count_floor = int(m.group(2))
                                    logger.info('нашли количество этажей %s' % advert.count_floor)
                                except Exception, err:
                                    logger.info(traceback.format_exc())

                        if u'Площадь' in txt:
                            m = re.search(u'([0-9]+) м²', txt)
                            if m:
                                try:
                                    advert.square = float(m.group(1))
                                    logger.info('нашли площадь %s' % advert.square)
                                except Exception, err:
                                    logger.info(traceback.format_exc())

                        if u'Холодильник' in txt:
                            advert.refrigerator = True
                        if u'Стиральная' in txt:
                            advert.washer = True
                        if u'балкон' in txt:
                            advert.balcony = True
                        if u'Стиральная машина' in txt:
                            advert.washer = True
                        if u'Wi-Fi' in txt:
                            advert.internet = True
                        if u'Телевизор' in txt:
                            advert.tv = True
                        if u'Кондиционер' in txt:
                            advert.conditioner = True


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
                nodes = driver.find_elements_by_xpath('.//button[@data-marker="show-number"]')
                if nodes:
                    nodes[0].click()
                    phone = driver.find_elements_by_xpath('//a[@class="show-number-button__link___lB7O7"]')
                    if phone:
                        txt = phone[0].text
                        if txt.startswith('8'):
                            txt = '7' + txt[1:]
                        owner_tel = clear_tel(txt)
                        logger.info(u'открыл телефон %s' % owner_tel)
                        advert.owner_tel = owner_tel
                        result = advert.check_spam(actions=True, level=level)
                        if result:
                            logger.info(result)
                    else:
                        logger.info('кнопка телефона не найдена')
                else:
                    logger.info('кнопка телефона не найдена')

                #     href = self.domain + nodes[0].get('data-url')
                #     try:
                #         h = {
                #             'referer': nodes[0].get('href'),
                #             'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/39.0.2171.65 Chrome/39.0.2171.65 Safari/537.36',
                #             'x-requested-with': 'XMLHttpRequest',
                #         }
                #         r = requests.post(href, cookies=self.cookies, headers=h)
                #         need_wait = True
                #         if r.status_code == 200:
                #             text = r.text
                #             m = re.findall(u'#(\d+)#', text, re.UNICODE)
                #             if m:
                #                 txt = m[0]
                #                 if txt.startswith('8'):
                #                     txt = '7' + txt[1:]
                #                 owner_tel = clear_tel(txt)
                #                 logger.info(u'открыл телефон %s' % owner_tel)
                #                 advert.owner_tel = owner_tel
                #                 result = advert.check_spam(actions=True, level=level)
                #                 if result:
                #                     logger.info(result)
                #     except Exception,  err:
                #         logger.info(traceback.format_exc())
                # else:
                #     logger.info('кнопка телефона не найдена')

                if not advert.owner_tel:
                    logger.info('телефон не найден')
                    driver.quit()
                    continue

                advert.save()

               # page_script_path = driver.find_elements_by_xpath('.//script')
               # if page_script_path:
               #     for script in page_script_path:
               #         script_text = driver.execute_script('return arguments[0].innerHTML', script)
               #         if script_text is not None and script_text.startswith('window.__INITIAL_DATA__'):
               #             jsondata = json.loads(re.findall(r'window.__INITIAL_DATA__ = (.+)', script_text)[0])
               #             logger.info('Найдено %s фоток' % len(jsondata['itemState']['item']['galleries'][0]['images']))
               #             for image in jsondata['itemState']['item']['galleries'][0]['images']:
               #                 try:
               #                     src = image[-1]['url']
               #                     image = UserImage(user=advert.user)
               #                     if image.load_image_domofond_crop(src):
               #                         image.save()
               #                         advert.images.add(image)
               #                 except Exception, err:
               #                     logger.debug(traceback.format_exc())
               #             break

                # try:
                #     elems = driver.xpath('//div[@class="fotorama"]/a')
                #     if elems:
                #         logger.info('найдено %s фоток' % len(elems))
                #         for a in elems:
                #             try:
                #                 src = a.get('href')
                #                 logger.info(src)
                #                 image = UserImage(user=advert.user)
                #                 if image.load_image_domofond_crop(src):
                #                     image.save()
                #                     advert.images.add(image)
                #             except Exception, err:
                #                 logger.info(traceback.format_exc())
                # except Exception, err:
                #     logger.debug(traceback.format_exc())

                if advert.status == Advert.STATUS_VIEW:
                    advert.find_clients()
                advert.find_metro_distance()
                if advert.check_owner():
                    advert.save()
                logger.info(advert.id)

        return True

    def process_url(self, url, adtype, limit, need=Advert.NEED_SALE, set_moderate=True, level=Advert.CHECK_SPAM_LOW):
        r = requests.get(url, cookies=self.cookies, allow_redirects=True, headers=self.headers)
        # self.cookies = dict(r.cookies.items())
        doc = fromstring(r.text)
        doc.make_links_absolute(self.domain)
        self.process_elements(url, doc, adtype, limit, need, set_moderate, level)

    def collect(self):
        logger.info('#### САНКТ ПЕТЕРБУРГ ####')
        start = datetime.now()

        self.cached_ids = cache.get('parser_domofond_ids', [])
        self.cookies = cache.get('parser_domofond_cookies', {})

        self.town = Town.objects.get(id=2)
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()
        self.parser = Parser.objects.get(title='domofond')
        try:
            logger.info('#### КВАРТИРЫ ####')
            self.process_url('http://www.domofond.ru/arenda-kvartiry-sankt_peterburg-c3414?RentalRate=Month&PrivateListingType=PrivatePerson',
                             adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, set_moderate=True, level=Advert.CHECK_SPAM_STRONG)
        except Exception, err:
            logger.info(traceback.format_exc())

        try:
            logger.info('#### КОМНАТЫ ####')
            self.process_url('http://www.domofond.ru/arenda-komnaty-sankt_peterburg-c3414?NoCommission=True&NoDeposit=True&RentalRate=Month&PrivateListingType=PrivatePerson',
                             adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, set_moderate=True, level=Advert.CHECK_SPAM_STRONG)

        except Exception, err:
            logger.info(traceback.format_exc())
        print 'питер %s' % (datetime.now() - start).seconds
        start = datetime.now()

        logger.info('#### МОСКВА ####')
        self.town = Town.admin_objects.get(slug='moskva')
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()
        try:
            logger.info('#### КВАРТИРЫ ####')
            self.process_url('http://www.domofond.ru/arenda-kvartiry-moskva-c3584?NoCommission=True&NoDeposit=True&RentalRate=Month&PrivateListingType=PrivatePerson',
                             adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, set_moderate=True, level=Advert.CHECK_SPAM_STRONG)
        except Exception, err:
            logger.info(traceback.format_exc())

        try:
            logger.info('#### КОМНАТЫ ####')
            self.process_url('http://www.domofond.ru/arenda-komnaty-moskva-c3584?NoCommission=True&NoDeposit=True&RentalRate=Month&PrivateListingType=PrivatePerson',
                             adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, set_moderate=True, level=Advert.CHECK_SPAM_STRONG)
        except Exception, err:
            logger.info(traceback.format_exc())

        print 'москва %s' % (datetime.now() - start).seconds
        start = datetime.now()

        # logger.info('#### НОВОСИБИРСК ####')
        # self.town = Town.admin_objects.get(slug='novosibirsk')
        # self.metro_list = self.town.metro_set.all()
        # self.district_list = self.town.district_set.all()
        # try:
        #     logger.info('#### КВАРТИРЫ ####')
        #     self.process_url('https://m.avito.ru/novosibirsk/kvartiry/sdam/na_dlitelnyy_srok?user=1',
        #                      adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
        # except Exception, err:
        #     logger.info(traceback.format_exc())
        #
        # try:
        #     logger.info('#### КОМНАТЫ ####')
        #     self.process_url('https://m.avito.ru/novosibirsk/komnaty/sdam/na_dlitelnyy_srok?user=1',
        #                      adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
        # except Exception, err:
        #     logger.info(traceback.format_exc())
        #
        # print 'новосибирск %s' % (datetime.now() - start).seconds
        # start = datetime.now()
        #
        # logger.info('#### ЕКАТЕРИНБУРГ ####')
        # self.town = Town.admin_objects.get(slug='ekaterinburg')
        # self.metro_list = self.town.metro_set.all()
        # self.district_list = self.town.district_set.all()
        # try:
        #     logger.info('#### КВАРТИРЫ ####')
        #     self.process_url('https://m.avito.ru/ekaterinburg/kvartiry/sdam/na_dlitelnyy_srok?user=1',
        #                      adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
        # except Exception, err:
        #     logger.info(traceback.format_exc())
        #
        # try:
        #     logger.info('#### КОМНАТЫ ####')
        #     self.process_url('https://m.avito.ru/ekaterinburg/komnaty/sdam/na_dlitelnyy_srok?user=1',
        #                      adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
        # except Exception, err:
        #     logger.info(traceback.format_exc())
        #
        # print 'екатеринбург %s' % (datetime.now() - start).seconds

        if len(self.cached_ids) > 1000:
            self.cached_ids = self.cached_ids[(len(self.cached_ids) - 1000):]
        cache.set('parser_domofond_ids', self.cached_ids, 6 * 60 * 60)
        cache.set('parser_domofond_cookies', self.cookies, 84320)
        logger.info('#### ВЫХОД ####')
