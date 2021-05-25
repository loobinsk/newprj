# -*- coding: utf-8 -*-
from lxml import html, etree
from lxml.html import fromstring
from lxml.html import tostring
import requests
import re
import os
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
import time
import sys
import inspect #
from urllib import unquote

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger('avito')
proxy_list = [
#    '194.226.34.132:5555'
#    '188.170.233.101:3128',
#    '84.201.254.47:3128'
]

# reload(sys)
# sys.setdefaultencoding('utf-8')


class AvitoCollector(Collector):
    domain = 'https://m.avito.ru'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; STF-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'
    }

    metro_list = None
    district_list = None
    town = None
    parser = None
    cached_ids = []

    def process_elements(self, doc, adtype, limit, need=Advert.NEED_SALE, set_moderate=True, level=Advert.CHECK_SPAM_LOW):
        element_list = doc.xpath('//div[contains(@data-marker, "item-wrapper")]')
        need_wait = False
        logger.info('Найдено %s объявлений' % len(element_list))
        for element in element_list:
            if need_wait:
                seconds = random.randrange(70, 100)
                logger.info('### ждем %s секунд ###' % seconds)
                time.sleep(seconds)
                need_wait = False

            item_link = element.xpath('.//a[contains(@data-marker, "item/link")]')
            if not item_link:
                logger.info('item_link не найден')
                pass
            else:
                m = re.search(u'\_([0-9]+)$', item_link[0].get('href'))
                if m:
                    advert_id = m.group(1)
                    if not advert_id:
                        logger.info('Пустой код')
                        continue
                    # if advert_id in self.cached_ids:
                    #     logger.info('%s уже проверено' % advert_id)
                    #     continue
                    txt = u'avito_' + advert_id
                    logger.info(txt)
                    advert_list = Advert.objects.filter(extnum=txt)
                    if advert_list:
                        logger.info('Объявление есть в базе')
                        continue
                else:
                    logger.info('Код объявления не распознан')
                    continue


                options = webdriver.ChromeOptions()
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-dev-shm-usage')
                #options.add_argument('--proxy-server=%s' % random.choice(proxy_list))
                options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 9; STF-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36")
                driver = webdriver.Chrome(executable_path="%s/chromedriver" % os.getcwd(), chrome_options=options)

                driver.get(item_link[0].get('href'))
                driver.implicitly_wait(10)
                time.sleep(10)
                #logger.info(driver.page_source)

                logger.info("=======================")

                self.cached_ids.append(advert_id)

                advert = Advert(town=self.town,
                                adtype = adtype,
                                need = need,
                                status=Advert.STATUS_MODERATE if set_moderate else Advert.STATUS_VIEW,
                                limit=limit,
                                user=User.objects.get(username='admin'),
                                date=datetime.now(),
                                parser=self.parser,
                                extnum=u'avito_' + advert_id)

                # Название объявления, количество комнат, площадь помещения, этаж/количество этажей
                title_path = driver.find_elements_by_xpath('.//h1[contains(@data-marker,"item-description/title")]')
                if title_path:
                    title = title_path[0].text
                    if (u'Квартира' in title) or (u'Студия' in title) or \
                            re.findall(u'(сниму.{1,5}квартиру)', title.lower(), re.UNICODE | re.IGNORECASE) or \
                            re.findall(u'(куплю.{1,5}квартиру)', title.lower(), re.UNICODE | re.IGNORECASE):
                        advert.estate = Advert.ESTATE_LIVE
                        advert.live = Advert.LIVE_FLAT
                        logger.info('Найдена квартира')

                    if u'Комната' in title or u'Комнату' in title:
                        advert.estate = Advert.ESTATE_LIVE
                        advert.live = Advert.LIVE_ROOM
                        logger.info('Найдена комната')


                    for room in xrange(1, 6):
                        if u'%s-к квартир' % room in title:
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
                            logger.info('Найдено комнат: %s' % room)
                    if not advert.rooms:
                        advert.rooms = 1

                    try:
                        area_size = re.search('\s([0-9|\.]+)[\s|,]', title.encode('utf-8'))
                        if area_size:
                            advert.square = float(area_size.group(1).replace(',', '.'))
                            logger.info('Найдена площадь: %s м^2' % advert.square)
                        else:
                            area_object = driver.find_elements_by_xpath('.//div[contains(@data-marker, "item-properties-item(4)/description")]')
                            if area_object:
                                area_path = area_object[0].text
                                try:
                                    advert.square = float(area_path)
                                except Exception:
                                    print(area_size)
                                    logger.info('Площадь не найдена: %s' % title.encode('utf-8'))
                            else:
                                print(area_size)
                                logger.info('Площадь не найдена: %s' % title.encode('utf-8'))
                    except Exception, err:
                        logger.info(traceback.format_exc())

                    for floor in xrange(1, 50):
                        if u'на %s этаже' % floor in txt:
                            advert.floor = floor
                            logger.info('Найден этаж: %s' % floor)
                    for floors in xrange(1, 50):
                        if u'%s-этажного' % floors in txt:
                            advert.count_floor = floors
                            logger.info('Найдены этажи: %s' % floors)

                # Цена, указанная в объявлении
                price_path = driver.find_elements_by_xpath('.//span[@data-marker="item-description/price"]')
                if price_path:
                    price_regexp = re.search(u'([0-9|\s]+)₽', price_path[0].text)
                    if price_regexp:
                        try:
                            advert.price = int(price_regexp.group(1).replace(u' ', u'').replace(u'\u00A0', u''))
                            logger.info('Найдена цена: %s' % advert.price)
                        except Exception, err:
                            logger.info(traceback.format_exc())

                if not advert.price:
                    logger.info('Цена не найдена')
                    driver.quit()
                    continue


                # Получение координат, адреса
                page_script_path = driver.find_elements_by_xpath('.//script')
                if page_script_path:
                    for script in page_script_path:
                        script_text = driver.execute_script('return arguments[0].innerHTML', script)
                        if script_text is not None and script_text.startswith('window.__initialData__'):
                            try:
                                script_text = unquote(script_text)
                                jsondata = json.loads(re.findall(r'window\.__initialData__ = "(.+)";', script_text)[0])

                                try:
                                    coords = jsondata["item"]['item']["coords"]
                                    advert.latitude = float(coords[u"lat"])
                                    advert.longitude = float(coords[u"lng"])
                                    logger.info('Получены координаты (lat: %s, long: %s)' % (advert.latitude, advert.longitude))
                                except Exception, err:
                                    logger.info(traceback.format_exc())


                                try:
                                    address = jsondata["item"]['item']["address"]
                                    advert.address = address.strip()
                                    try:
                                        logger.info(address)
                                    except Exception, err:
                                        logger.info(traceback.format_exc())
                                    try:
                                        logger.info(address.encode('cp1251'))
                                    except Exception, err:
                                        logger.info(traceback.format_exc())
                                    try:
                                        logger.info(address.encode('utf-8'))
                                    except Exception, err:
                                        logger.info(traceback.format_exc())
                                    try:
                                        logger.info(address.encode('cp1252'))
                                    except Exception, err:
                                        logger.info(traceback.format_exc())
                                    req = u'https://geocode-maps.yandex.ru/1.x/?geocode={}&format=json'.format(
                                            address, encoding='utf8'
                                    )
                                    # if float(coords[u"lat"]) and float(coords[u"lng"]):
                                    #     req = u'{}&ll={},{}'.format(
                                    #         req,
                                    #         float(coords[u"lat"]),
                                    #         float(coords[u"lng"])
                                    #     )
                                    try:
                                        res = requests.get(req)
                                        try:
                                            #print(res.json())
                                            short_address = res.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['name']
                                            logger.info('Получен короткий адрес: %s' % short_address.encode('utf-8'))
                                            advert.address = short_address
                                        except KeyError, err:
                                            logger.info(res.text)
                                            logger.info(traceback.format_exc())
                                            logger.info('Геокодер не нашел адрес по запросу %s' % req.encode('utf-8'))
                                    except Exception, err:
                                        logger.info('Ошибка при попытке получить короткий адрес:')
                                        logger.info(traceback.format_exc())
                                except Exception, err:
                                    logger.info(traceback.format_exc())

                                try:
                                    if 'metro' in jsondata['item']['item']['refs']:
                                        logger.info('Метро в JSON')
                                        metro_path = jsondata['item']['item']['refs']['metro']
                                        for key in metro_path:
                                            for metro in self.metro_list:
                                                if metro.title.lower() in metro_path[key]['name'].lower():
                                                    advert.metro = metro
                                                    logger.info('Найдено метро: %s' % metro)
                                                    break
                                            else:
                                                logger.info('Метро не найдено')
                                except Exception, err:
                                    logger.info(traceback.format_exc())

                            except Exception, err:
                                logger.info(traceback.format_exc())
                            break
                    else:
                        logger.info('JSON не найден')

                # Получение метро
                # metro_path = driver.find_elements_by_xpath('.//span[@data-marker="delivery/location"]')
                # if metro_path:
                #     ad_metro = metro_path[0].text
                #     for metro in self.metro_list:
                #         if metro.title.lower() in ad_metro.lower():
                #             advert.metro = metro
                #             logger.info('Найдено метро: %s' % metro)
                #             break

                # Поиск имени владельца объявления
                contact_path = driver.find_elements_by_xpath('.//span[contains(@data-marker, "seller-info/name")]')
                if contact_path:
                    advert.owner_name = contact_path[0].text.strip()
                    logger.info('Получено имя владельца: %s' % advert.owner_name.encode('utf-8'))
                    if u'агент' in advert.owner_name.lower():
                        logger.info('Пользователь является агентом. Пропуск')
                        driver.quit()
                        continue

                # Получение описания объявления
                description_path = driver.find_elements_by_xpath('.//div[contains(@data-marker, "item-description/text")]')
                if description_path:
                    advert.body = description_path[0].text
                    logger.info('Получено описание: %s' % advert.body.encode('utf-8'))
                    advert.parse(advert.body)
                    if u'комиссия' in advert.body.lower():
                        logger.info('В объявлении имеется комиссия. Пропуск')
                        driver.quit()
                        continue

                # Получение метро, если оно не найдено, и района
                if not advert.metro and advert.latitude and advert.longitude:
                    try:
                        logger.info('Получение метро')
                        doc_text = self.download_url(u'http://geocode-maps.yandex.ru/1.x/?results=1&kind=metro&geocode=%s,%s' % (advert.longitude, advert.latitude), encoding='utf8')
                        doccoord = fromstring(doc_text)
                        metro_name = doccoord.xpath('//name')
                        if metro_name:
                            txt = metro_name[0].text_content()
                            for metro in self.metro_list:
                                if metro.title.lower() in txt.lower():
                                    advert.metro = metro
                                    logger.info('Получено метро: %s' % metro)
                                    break
                    except Exception, err:
                        logger.info(traceback.format_exc())

                    if not advert.district and advert.latitude and advert.longitude:
                        try:
                            logger.info('Получение района')
                            doc_text = self.download_url(
                                u'http://geocode-maps.yandex.ru/1.x/?results=1&kind=district&geocode=%s,%s' % (
                                advert.longitude, advert.latitude), encoding='utf8')
                            doccoord = fromstring(doc_text)
                            district_name = doccoord.xpath('//name')
                            if district_name:
                                txt = district_name[0].text_content()
                                for district in self.district_list:
                                    if district.title.lower() in txt.lower():
                                        advert.district = district
                                        logger.info('Получен район: %s' % district)
                                        break
                            if not advert.district:
                                district_name = doccoord.xpath('//description')
                                if district_name:
                                    txt = district_name[0].text_content()
                                    for district in self.district_list:
                                        if district.title.lower() in txt.lower():
                                            advert.district = district
                                            logger.info('Получен район: %s' % district)
                                            break
                        except Exception, err:
                            logger.info(traceback.format_exc())

                # получение изображений
                # proxy = random.choice(proxy_list)
                # r = requests.get(item_link[0].get('href'), cookies=self.cookies, allow_redirects=True, headers=self.headers, proxies={'http':proxy, 'https':proxy})
                # #print(r.encoding)
                # doc_advert = fromstring(r.text)
                # doc_advert.make_links_absolute(self.domain)
                # nodes = doc_advert.xpath('//script')
                # if nodes:
                #     for script in nodes:
                #         if script.text != None and script.text.startswith('window.__initialData__'):
                #             try:
                #                 text = re.sub(r'(window.__initialData__ *= *|\|\| *{ *} *;)', '', script.text)
                #                 text = re.sub(r'(window.__mobileInfo__ *= {.*}.*;*)', '', text)
                #                 text = re.sub(r'(window.__pluginsData__ *= {.*}.*;*)', '', text)

                #                 jsondata = json.loads(text)
                #                 try:
                #                     photos = jsondata['item']['item']["images"]
                #                     logger.info('нашли {} фото'.format(len(photos)))
                #                     for photo in photos:
                #                         try:
                #                             logger.info(photo)
                #                             if '1280x960' in photo:
                #                                 src = photo['1280x960']
                #                             elif '640x480' in photo:
                #                                 src = photo['640x480']
                #                             elif '240x180' in photo:
                #                                 src = photo['240x180']
                #                             # src = re.sub('https', 'http', src)
                #                             logger.info(src)
                #                             src = src.decode().encode('ascii')
                #                             image = UserImage(user=advert.user)
                #                             if image.load_image_avito_crop(src, logger=logger):
                #                                 # image.image.path = image.image.path.encode('ascii', ignore='errors')
                #                                 # image.image.name = image.image.name.encode('ascii', ignore='errors')
                #                                 image.save()
                #                                 advert.save()
                #                                 # for attribute in dir(image.image):
                #                                 #     if attribute[0] != '_':
                #                                 #         print(attribute, ':', getattr(image.image, attribute))
                #                                 advert.images.add(image)
                #                         except Exception, err:
                #                             logger.info(traceback.format_exc())
                #                 except KeyError:
                #                     logger.info( traceback.format_exc())
                #                     logger.info('у объявления нет фото')
                #                 except Exception, err:
                #                     logger.info( traceback.format_exc())

                #             except Exception, err:
                #                 logger.info( traceback.format_exc())
                nodes = driver.find_elements_by_xpath('.//script')
                if nodes:
                    for script in nodes:
                        script_text = driver.execute_script('return arguments[0].innerHTML', script)
                        if script_text is not None and script_text.startswith('window.__initialData__'):
                            try:
                                script_text = unquote(script_text)
                                jsondata = json.loads(re.findall(r'window\.__initialData__ = "(.+)";', script_text)[0])

                                try:
                                    photos = jsondata['item']['item']["images"]
                                    logger.info('Найдено фото: %s' % len(photos))
                                    for photo in photos:
                                        try:
                                            #print(photo)
                                            if '1280x960' in photo:
                                                src = photo['1280x960']
                                            elif '640x480' in photo:
                                                src = photo['640x480']
                                            elif '240x180' in photo:
                                                src = photo['240x180']
                                            #src = re.sub('https', 'http', src)
                                            logger.info(src)
                                            image = UserImage(user=advert.user)
                                            if image.load_image_avito_crop(src):
                                                image.save()
                                                advert.save()
                                                advert.images.add(image)
                                                advert.save()
                                        except Exception, err:
                                            logger.info(traceback.format_exc())
                                except KeyError:
                                    logger.info(traceback.format_exc())
                                    logger.info('У данного объявления нет фото.')
                                except Exception, err:
                                    logger.info(traceback.format_exc())

                            except Exception, err:
                                logger.info(traceback.format_exc())

                # Парсинг телефона
                phone_button = driver.find_elements_by_xpath('//a[contains(@data-marker, "item-contact-bar/call")]')
                if phone_button:
                    phone_button[0].click()
                    seconds = random.randrange(2, 5)
                    logger.info('### ждем %s секунд перед открытием номера###' % seconds)
                    time.sleep(seconds)
                   # logger.info(driver.page_source)
                    phone = driver.find_elements_by_xpath('//span[contains(@data-marker, "phone-popup/phone-number")]')
                    if phone:
                        advert.owner_tel = clear_tel(phone[0].text.encode('utf-8'))
                        logger.info('Найден телефон: %s' % advert.owner_tel)
                        result = advert.check_spam(actions=True, level=level)
                        if result:
                            logger.info(result)
                    else:
                        logger.info('Телефон не найден, но модальное окно было открыто')
                        driver.quit()
                        continue
                else:
                    logger.info('Телефон не найден')
                    driver.quit()
                    continue


                advert.save()

                #print(advert.owner_tel)

                if advert.status == Advert.STATUS_VIEW:
                    advert.find_clients()
                    advert.find_metro_distance()
                    if advert.check_owner():
                        advert.save()
                    advert.publish()
                    logger.info(advert.id)

                driver.quit()

        return True

    def process_url(self, url, adtype, limit, need=Advert.NEED_SALE, set_moderate=True, level=Advert.CHECK_SPAM_LOW):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 9; STF-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36")
        driver = webdriver.Chrome(executable_path="%s/chromedriver" % os.getcwd(), chrome_options=options)
        driver.get(url)
        driver.implicitly_wait(10)
        time.sleep(10)

        source = driver.page_source
        # print('pg:',source)
        driver.quit()

        #r = requests.get(url, cookies=self.cookies, allow_redirects=True, headers=self.headers)
        # self.cookies = dict(r.cookies.items())
        # logger.info('process_url request code = %s', r.status_code)
        doc = fromstring(source)
        doc.make_links_absolute(self.domain)
        self.process_elements(doc, adtype, limit, need, set_moderate)

    def login(self):
        data = {
            'login': ' ',
            'password': ' ',
            'next': '/profile',
            'from': ''
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 9; STF-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
            'Referer': 'https://m.avito.ru/profile',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4,bg;q=0.2'

        }
        r = requests.get('https://m.avito.ru/profile/login', headers=headers)
        self.cookies.update(r.cookies.items())
        r = requests.post('https://m.avito.ru/profile/login', data=data, headers=headers, cookies=self.cookies, allow_redirects=False)
        self.cookies.update(r.cookies.items())
        return r.status_code == 302

    def collect(self):
        print('Go')
        logger.info('#### САНКТ ПЕТЕРБУРГ ####')
        start =datetime.now()

        self.cached_ids = cache.get('parser_avito_ids', [])
        self.cookies = cache.get('parser_avito_cookies', {})

        self.town = Town.objects.get(id=2)
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()
        self.parser = Parser.objects.get(title='avito')
        try:
            logger.info('#### КВАРТИРЫ ####')
            self.process_url('https://m.avito.ru/sankt-peterburg/kvartiry/sdam/na_dlitelnyy_srok?owner[]=private', adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG)
            # self.process_url('https://m.avito.ru/sankt-peterburg/kvartiry/snimu/na_dlitelnyy_srok?user=1',
            #                  adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, need=Advert.NEED_DEMAND, set_moderate=True, level=Advert.CHECK_SPAM_STRONG)

            # self.process_url('https://m.avito.ru/sankt-peterburg/kvartiry/prodam?user=1',
            #                  adtype=Advert.TYPE_SALE, limit=Advert.LIMIT_LONG, need=Advert.NEED_SALE, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
            # self.process_url('https://m.avito.ru/sankt-peterburg/kvartiry/kuplyu?user=1',
            #                  adtype=Advert.TYPE_SALE, limit=Advert.LIMIT_LONG, need=Advert.NEED_DEMAND, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
        except Exception, err:
            logger.info(traceback.format_exc())

        try:
            logger.info('#### КОМНАТЫ ####')
            self.process_url('https://m.avito.ru/sankt-peterburg/komnaty/sdam/na_dlitelnyy_srok?owner[]=private', adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG)
            # self.process_url('https://m.avito.ru/sankt-peterburg/komnaty/snimu/na_dlitelnyy_srok?user=1',
            #                  adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, need=Advert.NEED_DEMAND, set_moderate=False)

            # self.process_url('https://m.avito.ru/sankt-peterburg/komnaty/prodam?user=1',
            #                  adtype=Advert.TYPE_SALE, limit=Advert.LIMIT_LONG, need=Advert.NEED_SALE, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
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
            self.process_url('https://m.avito.ru/moskva/kvartiry/sdam/na_dlitelnyy_srok?owner[]=private',
                             adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, set_moderate=True, level=Advert.CHECK_SPAM_STRONG)
            # self.process_url('https://m.avito.ru/moskva/kvartiry/sdam/posutochno?user=1',
            #                  adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_DAY, set_moderate=True)
            # self.process_url('https://m.avito.ru/moskva/kvartiry/snimu/na_dlitelnyy_srok?user=1',
            #                  adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, need=Advert.NEED_DEMAND, set_moderate=True, level=Advert.CHECK_SPAM_STRONG)

            # self.process_url('https://m.avito.ru/moskva/kvartiry/prodam?user=1',
            #                  adtype=Advert.TYPE_SALE, limit=Advert.LIMIT_LONG, need=Advert.NEED_SALE, set_moderate=True, level=Advert.CHECK_SPAM_STRONG)
            # self.process_url('https://m.avito.ru/moskva/kvartiry/kuplyu?user=1',
            #                  adtype=Advert.TYPE_SALE, limit=Advert.LIMIT_LONG, need=Advert.NEED_DEMAND, set_moderate=True, level=Advert.CHECK_SPAM_STRONG)
        except Exception, err:
            logger.info(traceback.format_exc())

        try:
            logger.info('#### КОМНАТЫ ####')
            self.process_url('https://m.avito.ru/moskva/komnaty/sdam/na_dlitelnyy_srok?owner[]=private',
                             adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, set_moderate=True, level=Advert.CHECK_SPAM_STRONG)
            # self.process_url('https://m.avito.ru/moskva/komnaty/sdam/posutochno?user=1',
            #                  adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_DAY, set_moderate=True, level=Advert.CHECK_SPAM_STRONG)
            # self.process_url('https://m.avito.ru/moskva/komnaty/snimu/na_dlitelnyy_srok?user=1',
            #                  adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, need=Advert.NEED_DEMAND, set_moderate=True)

            # self.process_url('https://m.avito.ru/moskva/komnaty/prodam?user=1',
            #                  adtype=Advert.TYPE_SALE, limit=Advert.LIMIT_LONG, need=Advert.NEED_SALE, set_moderate=True, level=Advert.CHECK_SPAM_STRONG)
        except Exception, err:
            logger.info(traceback.format_exc())

        print 'москва %s' % (datetime.now() - start).seconds
        start = datetime.now()

        logger.info('#### НОВОСИБИРСК ####')
        self.town = Town.admin_objects.get(slug='novosibirsk')
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()
        try:
            logger.info('#### КВАРТИРЫ ####')
            self.process_url('https://m.avito.ru/novosibirsk/kvartiry/sdam/na_dlitelnyy_srok?owner[]=private',
                             adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
            # self.process_url('https://m.avito.ru/novosibirsk/kvartiry/sdam/posutochno?user=1',
            #                  adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_DAY, set_moderate=False)
            # self.process_url('https://m.avito.ru/novosibirsk/kvartiry/snimu/na_dlitelnyy_srok?user=1',
            #                  adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, need=Advert.NEED_DEMAND, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)

            # self.process_url('https://m.avito.ru/novosibirsk/kvartiry/prodam?user=1',
            #                  adtype=Advert.TYPE_SALE, limit=Advert.LIMIT_LONG, need=Advert.NEED_SALE, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
            # self.process_url('https://m.avito.ru/novosibirsk/kvartiry/kuplyu?user=1',
            #                  adtype=Advert.TYPE_SALE, limit=Advert.LIMIT_LONG, need=Advert.NEED_DEMAND, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
        except Exception, err:
            logger.info(traceback.format_exc())

        try:
            logger.info('#### КОМНАТЫ ####')
            self.process_url('https://m.avito.ru/novosibirsk/komnaty/sdam/na_dlitelnyy_srok?owner[]=private',
                             adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
            # self.process_url('https://m.avito.ru/novosibirsk/komnaty/sdam/posutochno?user=1',
            #                  adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_DAY, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
            # self.process_url('https://m.avito.ru/novosibirsk/komnaty/snimu/na_dlitelnyy_srok?user=1',
            #                  adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, need=Advert.NEED_DEMAND, set_moderate=False)

            # self.process_url('https://m.avito.ru/novosibirsk/komnaty/prodam?user=1',
            #                  adtype=Advert.TYPE_SALE, limit=Advert.LIMIT_LONG, need=Advert.NEED_SALE, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
        except Exception, err:
            logger.info(traceback.format_exc())

        print 'новосибирск %s' % (datetime.now() - start).seconds
        start = datetime.now()

        logger.info('#### ЕКАТЕРИНБУРГ ####')
        self.town = Town.admin_objects.get(slug='ekaterinburg')
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()
        try:
            logger.info('#### КВАРТИРЫ ####')
            self.process_url('https://m.avito.ru/ekaterinburg/kvartiry/sdam/na_dlitelnyy_srok?owner[]=private',
                             adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
            # self.process_url('https://m.avito.ru/ekaterinburg/kvartiry/sdam/posutochno?user=1',
            #                  adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_DAY, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
            # self.process_url('https://m.avito.ru/ekaterinburg/kvartiry/snimu/na_dlitelnyy_srok?user=1',
            #                  adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, need=Advert.NEED_DEMAND, set_moderate=False)

            # self.process_url('https://m.avito.ru/ekaterinburg/kvartiry/prodam?user=1',
            #                  adtype=Advert.TYPE_SALE, limit=Advert.LIMIT_LONG, need=Advert.NEED_SALE, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
            # self.process_url('https://m.avito.ru/ekaterinburg/kvartiry/kuplyu?user=1',
            #                  adtype=Advert.TYPE_SALE, limit=Advert.LIMIT_LONG, need=Advert.NEED_DEMAND, set_moderate=False)
        except Exception, err:
            logger.info(traceback.format_exc())

        try:
            logger.info('#### КОМНАТЫ ####')
            self.process_url('https://m.avito.ru/ekaterinburg/komnaty/sdam/na_dlitelnyy_srok?owner[]=private',
                             adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
            # self.process_url('https://m.avito.ru/ekaterinburg/komnaty/sdam/posutochno?user=1',
            #                  adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_DAY, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
            # self.process_url('https://m.avito.ru/ekaterinburg/komnaty/snimu/na_dlitelnyy_srok?user=1',
            #                  adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG, need=Advert.NEED_DEMAND, set_moderate=False)

            # self.process_url('https://m.avito.ru/ekaterinburg/komnaty/prodam?user=1',
            #                  adtype=Advert.TYPE_SALE, limit=Advert.LIMIT_LONG, need=Advert.NEED_SALE, set_moderate=False, level=Advert.CHECK_SPAM_STRONG)
        except Exception, err:
            logger.info(traceback.format_exc())

        print 'екатеринбург %s' % (datetime.now() - start).seconds

        if len(self.cached_ids) > 1000:
            self.cached_ids = self.cached_ids[(len(self.cached_ids) - 1000):]
        cache.set('parser_avito_ids', self.cached_ids, 6 * 60 * 60)
        cache.set('parser_avito_cookies', self.cookies, 84320)
        logger.info('#### ВЫХОД ####')
