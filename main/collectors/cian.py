#-*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from lxml import html
from lxml.html import fromstring
import requests
import re
from datetime import datetime
import traceback
from main.models import Advert, Town, Metro, clear_tel_list, Company, Blacklist, get_tel_list, Parser
from uprofile.models import User
from uimg.models import UserImage
import logging

logger = logging.getLogger('cian')

#простой коллектор сборщик
class Collector:
    encoding = 'utf8'
    url = ''
    cookies = None

    def download_url(self, url, encoding='utf8'):
        r = requests.get(url, cookies=self.cookies)
        r.encoding = encoding
        content = r.text
        return content

    def collect(self, filename, town):
        pass


class CianCollector(Collector):
    domain = 'http://www.cian.ru/'
    flat_arenda_day_url = 'http://www.cian.ru/cat.php?deal_type=1&obl_id=1&city[0]=1&type=2'
    flat_arenda_long_url = 'http://www.cian.ru/cat.php?deal_type=1&obl_id=1&city[0]=1&type=4'
    house_arenda_day_url = 'http://www.cian.ru/cat.php?suburbian=yes&deal_type=1&obl_id=1&city[0]=1&type=2'
    house_arenda_long_url = 'http://www.cian.ru/cat.php?suburbian=yes&deal_type=1&obl_id=1&city[0]=1&type=4'
    commercial_arenda_url = 'http://www.cian.ru/cat.php?offices=yes&deal_type=1&obl_id=1&city[0]=1'

    flat_sale_url = 'http://www.cian.ru/cat.php?deal_type=2&obl_id=1&city[0]=1&room0=1&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1'
    house_sale_url = 'http://www.cian.ru/cat.php?suburbian=yes&deal_type=2&obl_id=1&city[0]=1'
    commercial_sale_url = 'http://www.cian.ru/cat.php?offices=yes&deal_type=2&obl_id=1&city[0]=1'

    piter_flat_arenda_day_url = 'http://www.cian.ru/cat.php?deal_type=1&obl_id=10&city[0]=11622&type=2&zerocom=-1'
    piter_flat_arenda_long_url = 'http://www.cian.ru/cat.php?deal_type=1&obl_id=10&city[0]=11622&type=-2&zerocom=-1'

    msk_flat_arenda_url = 'http://www.cian.ru/cat.php?deal_type=1&obl_id=1&p=%s'
    spb_flat_arenda_url = 'http://www.cian.ru/cat.php?deal_type=1&obl_id=10&p=%s'
    nsk_flat_arenda_url = 'http://www.cian.ru/cat.php?deal_type=1&obl_id=33&p=%s'
    ekb_flat_arenda_url = 'http://www.cian.ru/cat.php?deal_type=1&obl_id=43&p=%s'



    moderator = None
    town = None
    metro_list = None
    district_list = None
    parser = None

    def process_advert_page(self, advert, advert_doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, limit=Advert.LIMIT_DAY, komissia0=False, set_moderate=False):
        #комиссия
        komissia = True
        elems = advert_doc.xpath('//td[@class="object_descr_td_l"]')
        if elems:
            txt = elems[0].text_content()
            if u'комиссия 0' in txt:
                komissia = False

        if komissia0 and komissia:
            logger.info('Комиссия не 0%')
            return False

        #кол-во комнат
        elems = advert_doc.xpath('//div[@class="object_descr_title"]')
        if elems:
            txt = elems[0].text_content()
            if u'кв.' in txt:
                advert.estate = Advert.ESTATE_LIVE
                advert.live = Advert.LIVE_FLAT
                logger.info( 'квартира')
                for rooms in xrange(1, 7):              #квартиры
                    if u'%s-комн.' % rooms in txt:
                        advert.rooms = rooms
                        logger.info( '%s комнатная квартира' % rooms)
                        break
            if u'комната' in txt:
                advert.estate = Advert.ESTATE_LIVE
                advert.live = Advert.LIVE_ROOM
                logger.info( 'комната')
                for rooms in xrange(1, 7):              #комнаты
                    if u'%s-комн.' % rooms in txt:
                        advert.rooms = rooms
                        logger.info( '%s комната(ы)' % rooms)
                        break
            if (u'дом' in txt) or (u'таунхаус' in txt):
                advert.estate = Advert.ESTATE_COUNTRY
                logger.info( 'дом')
                for floor in xrange(1, 7):              #офисы
                    if u'%s этаж.' % floor in txt:
                        advert.count_floor = floor
                        logger.info( 'дом %s этаж(а)' % floor)
                        break
                m = re.search(u'([0-9]+) м', txt)
                if m:
                    advert.square = int(m.group(1))
                    logger.info( 'получена общая площадь %s' % advert.square)

            if u'участок' in txt:
                advert.estate = Advert.ESTATE_TERRITORY
                logger.info( 'участок')
                m = re.search(u'([0-9]+) м', txt)
                if m:
                    advert.square = int(m.group(1))
                    logger.info( 'получена общая площадь %s' % advert.square)
                m = re.search(u'([0-9]+) сот.', txt)
                if m:
                    advert.square = int(m.group(1)) * 100
                    logger.info( 'получена общая площадь %s' % advert.square)

        # адрес
        elems = advert_doc.xpath('//h1[@class="object_descr_addr"]')
        if elems:
            txt = elems[0].text_content().strip().replace(u'Москва,', u'')
            advert.address = txt
            logger.info( 'получен адрес')

            #получение координат
            try:
                address_txt = advert.address
                if not (u'Москва' in address_txt):
                    address_txt = u'Россия, ' + self.town.title + ', ' + address_txt
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
        elems = advert_doc.xpath('//div[@class="object_descr_metro"]')
        if elems:
            txt = elems[0].text_content()
            for metro in self.metro_list:
                if metro.title.lower() in txt.lower():
                    advert.metro = metro
                    logger.info( 'получено метро')
                    break

        #получение метро
        if not advert.metro and advert.latitude and advert.longitude:
            try:
                logger.info( 'запрос метро')
                doc_text = self.download_url(u'http://geocode-maps.yandex.ru/1.x/?results=1&kind=metro&geocode=%s,%s' % (advert.longitude, advert.latitude), encoding='utf8')
                doccoord = fromstring(doc_text)
                metro_name = doccoord.xpath('//name')
                if metro_name:
                    txt = metro_name[0].text_content()
                    for metro in self.metro_list:
                        if metro.title.lower() in txt.lower():
                            advert.metro = metro
                            logger.info( 'получено метро')
                            break
            except Exception, err:
                logger.info( traceback.format_exc())

        #получение района
        if not advert.district and advert.latitude and advert.longitude:
            try:
                logger.info( 'запрос района')
                doc_text = self.download_url(u'http://geocode-maps.yandex.ru/1.x/?results=1&kind=district&geocode=%s,%s' % (advert.longitude, advert.latitude), encoding='utf8')
                doccoord = fromstring(doc_text)
                district_name = doccoord.xpath('//name')
                if district_name:
                    txt = district_name[0].text_content()
                    for district in self.district_list:
                        if district.title.lower() in txt.lower():
                            advert.district = district
                            logger.info( 'получен район')
                            break
                if not advert.district:
                    district_name = doccoord.xpath('//description')
                    if district_name:
                        txt = district_name[0].text_content()
                        for district in self.district_list:
                            if district.title.lower() in txt.lower():
                                advert.district = district
                                logger.info( 'получен район')
                                break
            except Exception, err:
                logger.info( traceback.format_exc())

        # свойства
        elems = advert_doc.xpath('//table[@class="object_descr_props"]')
        if elems:
            trs = elems[0].xpath('.//tr')
            for tr in trs:
                tds = tr.xpath('.//td')
                ths = tr.xpath('.//th')
                if tds and ths:
                    if u'Общая площадь:' in ths[0].text_content():
                        m = re.search('([0-9]+)', tds[0].text_content())
                        if m:
                            advert.square = int(m.group(0))
                            logger.info( 'получена общая площадь %s' % advert.square)
                    if u'Площадь:' in ths[0].text_content():
                        m = re.search('([0-9]+)', tds[0].text_content())
                        if m:
                            advert.square = int(m.group(0))
                            logger.info( 'получена общая площадь %s' % advert.square)
                    if u'Жилая площадь:' in ths[0].text_content():
                        m = re.search('([0-9]+)', tds[0].text_content())
                        if m:
                            advert.living_square = int(m.group(0))
                            logger.info( 'получена жилая площадь %s' % advert.living_square)
                    if u'Площадь кухни:' in ths[0].text_content():
                        m = re.search('([0-9]+)', tds[0].text_content())
                        if m:
                            advert.kitchen_square = int(m.group(0))
                            logger.info( 'получена площадь кухни %s' % advert.kitchen_square)
                    if u'Балкон:' in ths[0].text_content():
                        if u'1' in tds[0].text_content():
                            advert.balcony = True
                            logger.info( 'балкон')
                    if u'Этаж:' in ths[0].text_content():
                        txt = tds[0].text_content()
                        floors = txt.split('/')
                        try:
                            if len(floors) == 1:
                                advert.floor = int(floors[0].replace('&nbsp;', '').replace('-', ''))
                                logger.info( 'получен этаж %s' % advert.floor)
                            if len(floors) == 2:
                                advert.floor = int(floors[0].replace('&nbsp;', '').replace('-', ''))
                                advert.count_floor = int(floors[1].replace('&nbsp;', '').replace('-', ''))
                                logger.info( 'получен этаж и кол-во этажей всего %s/%s' % (advert.floor, advert.count_floor))
                        except:
                            pass

        # Цена
        elems = advert_doc.xpath('//div[@id="price_rur"]')
        if elems:
            try:
                advert.price = int(elems[0].text_content())
                logger.info( 'получена цена %s' % advert.price)
                if (advert.adtype == Advert.TYPE_SALE) and (advert.price < 50000):
                    advert.price *= 1000
                    logger.info( 'умножил на 1000')
            except:
                pass

        if not advert.price:
            logger.info('нет цены')
            return False

        if (self.town.id == 2) and (advert.limit == Advert.LIMIT_LONG) and (advert.TYPE_LEASE == advert.adtype):
            # проверка цены на ценовую политику
            if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_ROOM):
                if advert.price < 8000:
                    logger.info('Не подходит: Комнаты от 8000 до (ограничения нет)')
                    return False
            if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 1):
                if advert.price < 17000:
                    logger.info('Не подходит: 1 ком.кв. от 17000 до (ограничения нет)')
                    return False
            if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 2):
                if advert.price < 19000:
                    logger.info('Не подходит: 2 ком.кв. от 19000 до (ограничения нет)')
                    return False
            if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 3):
                if advert.price < 20000:
                    logger.info('Не подходит: 3 ком.кв. от 20000 до (ограничения нет)')
                    return False
            if (advert.estate == Advert.ESTATE_LIVE) and (advert.live == Advert.LIVE_FLAT) and (advert.rooms >= 4):
                if advert.price < 22000:
                    logger.info('Не подходит: 4 и более ком.кв. от 22000 до (ограничения нет)')
                    return False


        #Примечание
        elems = advert_doc.xpath('//div[@class="object_descr_details clearfix"]')
        if elems:
            txt = elems[0].text_content()
            advert.parse(txt)

        # Телефон
        advert_tel = None
        elems = advert_doc.xpath('//span[@class="object_descr_phones_row"]/strong/a')
        if elems:
            advert_tel = clear_tel_list(u', '.join(el.text_content() for el in elems))
            logger.info( u'получен телефон %s' % advert_tel)
        else:
            logger.info( 'телефон отсутствует')
            return False

        if not advert_tel:
            logger.info( 'телефон пустой')
            return False

        # Описание
        elems = advert_doc.xpath('//div[@class="object_descr_text"]')
        if elems:
            advert.body = elems[0].text.strip()
            advert.parse(advert.body)
            # advert.body = re.sub(u'([\-\ \(\)0-9]{10,})', u'+7 (XXX) XXX-XX-XX', elems[0].text)
            logger.info( 'получено описание')

        # риелтор
        elems = advert_doc.xpath('//span[@class="object_descr_realtor_name"]')
        if elems:
            txt = elems[0].text_content()
            if (u'ID:' in txt) and not komissia:
                # собственник ?
                advert.owner_tel = advert_tel
                if set_moderate:
                    advert.status = Advert.STATUS_MODERATE
                else:
                    advert.status = Advert.STATUS_VIEW
                advert.user = self.moderator
                if Blacklist.check_list(advert.owner_tel):
                    logger.info( 'Телефон в черном списке')
                    return False
                tel_list = get_tel_list(advert.owner_tel)
                for tel in tel_list:
                    duplicate_list = Advert.get_duplicates(advert.adtype, advert.estate, advert.need, tel=tel)
                    if duplicate_list:
                        logger.info(u'найден дубликат №%s тел %s' % (duplicate_list[0].id, duplicate_list[0].owner_tel))
                        return False
                if advert.status == Advert.STATUS_MODERATE:
                    logger.info( 'объявление собственника. Помещено на модерацию')
                else:
                    logger.info( 'объявление собственника. Размещено на сайте')
            else:
                company = None
                user = None
                if (u'частный маклер' in txt) or (u'ID:' in txt):
                    company_list = Company.objects.filter(title__iexact='Частные маклеры', town=self.town)
                    if company_list:
                        company = company_list[0]
                        logger.info( 'найдена группа частных маклеров')
                    else:
                        company = Company(title='Частные маклеры', status=Company.STATUS_ACTIVE, is_real=False, town=self.town)
                        company.save()
                        logger.info( 'создана группа частных маклеров')
                else:
                    company_list = Company.objects.filter(title__iexact=txt.strip(), town=self.town)
                    if company_list:
                        company = company_list[0]
                        logger.info( 'найдено агентство в базе')
                    else:
                        company = Company(title=txt.strip(), status=Company.STATUS_ACTIVE, is_real=False, town=self.town)
                        company.save()
                        logger.info( 'создано новое агентство')

                user_list = User.objects.filter(tel__contains=advert_tel)
                if user_list:
                    user = user_list[0]
                    logger.info( 'агент найден в базе')
                else:
                    user = User(first_name='Агент')
                    if company:
                        user.gen_username('comp%s_' % company.id)
                    else:
                        user.gen_username()
                    user.gen_password()
                    user.tel = advert_tel
                    user.company = company
                    user.save()
                    logger.info( 'создан новый агент')

                advert.company = company
                advert.user = user
        return True

    def process_elements(self, doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, limit=Advert.LIMIT_DAY, komissia0=False, set_moderate=False):
        self.moderator = User.objects.get(username='admin')

        element_list = doc.xpath('//table[@class="objects_items_list"]/tbody/tr')
        logger.info( "Загружено %s объявлений\r\n\r\n" % len(element_list))
        n = 0
        for element in element_list:
            try:
                if not element.get('id'):
                    continue

                n += 1
                logger.info( 'Обработка %s объявления--------------------------------' % n)

                aid = element.get('id').replace(u'tr_', u'').replace(u'offer_', u'')
                advert_id = "cian" + aid
                logger.info( 'Номер объявления')
                logger.info( advert_id)
                if Advert.objects.filter(extnum=advert_id).count() > 0:
                    logger.info( 'Такое объявление есть в базе')
                    continue

                advert = Advert(extnum=advert_id, adtype=adtype, limit=limit, town=self.town, parser=self.parser)

                # дата
                elems = doc.xpath('//span[@id="added_%s"]' % aid)
                if elems:
                    txt = elems[0].text_content()
                    try:
                        advert.date = datetime.strptime(txt, '%d.%m.%y %H:%M')
                        logger.info( 'дата %s' % advert.date)
                    except:
                        pass

                txt = self.download_url('http://www.cian.ru/%s/flat/%s/' % ('rent' if adtype==Advert.TYPE_LEASE else 'sale', aid), 'utf8')
                advert_doc = fromstring(txt)
                advert_doc.make_links_absolute(self.domain)
                logger.info( 'загружена страница объявления')

                if not self.process_advert_page(advert, advert_doc, adtype, estate, limit, komissia0, set_moderate):
                    continue

                if not advert.price:
                    logger.info('Нет цены')
                    continue

                if not advert.owner_tel and not advert.company:
                    logger.info('Нет телефона')
                    continue

                if not advert.user:
                    continue

                advert.save()
                if advert.status == Advert.STATUS_VIEW:
                    advert.find_clients()
                    advert.find_surrounding_objects()

                advert.find_metro_distance()
                if advert.check_owner():
                    advert.save()

                logger.info( 'Объявление сохранено  с кодом %s' % advert.id)

                # Фотки
                elems = advert_doc.xpath('//div[@class="object_descr_images_w"]/a')
                if elems:
                    logger.info( 'найдено %s фоток' % len(elems))
                    for a in elems:
                        try:
                            src = a.get('href')
                            logger.info( src)
                            image = UserImage(user=advert.user)
                            if image.load_image_cian_crop(src):
                                image.save()
                                advert.images.add(image)
                        except Exception, err:
                            logger.info( traceback.format_exc())
                logger.info( '\r\n\r\n\r\n')
            except Exception, err:
                logger.info( traceback.format_exc())

    def process_elements_house(self, doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_COUNTRY, limit=Advert.LIMIT_DAY):
        self.town = Town.objects.get(id=1) #москва
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()
        self.moderator = User.objects.get(username='admin')

        element_list = doc.xpath('//div[contains(@class, "offer_container")]')
        logger.info( "Загружено %s объявлений\r\n\r\n" % len(element_list))
        n = 0
        for element in element_list:
            try:
                if not element.get('id'):
                    continue

                n += 1
                logger.info( 'Обработка %s объявления--------------------------------' % n)

                aid = element.get('id').replace(u'offer_', '')
                advert_id = "cian" + aid
                logger.info( 'Номер объявления')
                logger.info( advert_id)
                if Advert.objects.filter(extnum=advert_id).count() > 0:
                    logger.info( 'Такое объявление есть в базе')
                    continue

                advert = Advert(extnum=advert_id, adtype=adtype, limit=limit, town=self.town, estate=estate, parser=self.parser)

                advert_doc = fromstring(self.download_url('http://www.cian.ru/%s/suburban/%s/' % ('rent' if adtype==Advert.TYPE_LEASE else 'sale', aid), 'utf8'))
                advert_doc.make_links_absolute(self.domain)
                logger.info( 'загружена страница объявления')

                self.process_advert_page(advert, advert_doc, adtype, estate, limit)

                if not advert.price:
                    logger.info('Нет цены')
                    continue

                if not advert.owner_tel and not advert.company:
                    logger.info('Нет телефона')
                    continue

                advert.save()
                if advert.status == Advert.STATUS_VIEW:
                    advert.find_clients()
                    advert.find_metro_distance()
                    advert.find_surrounding_objects()
                logger.info( 'Объявление сохранено  с кодом %s\r\n\r\n\r\n' % advert.id)

                # Фотки
                elems = advert_doc.xpath('//div[@class="object_descr_images_w"]/a')
                if elems:
                    logger.info( 'найдено %s фоток' % len(elems))
                    for a in elems:
                        try:
                            src = a.get('href')
                            logger.info( src)
                            image = UserImage(user=advert.user)
                            if image.load_image_cion_crop(src):
                                image.save()
                                advert.images.add(image)
                        except Exception, err:
                            logger.info( traceback.format_exc())

            except Exception, err:
                logger.info( traceback.format_exc())

    def process_elements_commercial(self, doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_COMMERCIAL, limit=Advert.LIMIT_LONG):
        self.town = Town.objects.get(id=1) #москва
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()
        self.moderator = User.objects.get(username='admin')

        element_list = doc.xpath('//div[contains(@class, "offer_container")]')
        logger.info( "Загружено %s объявлений\r\n\r\n" % len(element_list))
        n = 0
        for element in element_list:
            try:
                if not element.get('id'):
                    continue

                n += 1
                logger.info( 'Обработка %s объявления--------------------------------' % n)

                aid = element.get('id').replace(u'offer_', '')
                advert_id = "cian" + aid
                logger.info( 'Номер объявления')
                logger.info( advert_id)
                if Advert.objects.filter(extnum=advert_id).count() > 0:
                    logger.info( 'Такое объявление есть в базе')
                    continue

                advert = Advert(extnum=advert_id, adtype=adtype, limit=limit, town=self.town, estate=estate, parser=self.parser)

                advert_doc = fromstring(self.download_url('http://www.cian.ru/%s/commercial/%s/' % ('rent' if adtype==Advert.TYPE_LEASE else 'sale', aid), 'utf8'))
                advert_doc.make_links_absolute(self.domain)
                logger.info( 'загружена страница объявления')

                self.process_advert_page(advert, advert_doc, adtype, estate, limit)

                if not advert.price:
                    logger.info('Нет цены')
                    continue

                if not advert.owner_tel and not advert.company:
                    logger.info('Нет телефона')
                    continue

                advert.save()
                if advert.status == Advert.STATUS_VIEW:
                    advert.find_clients()
                    advert.find_metro_distance()
                    advert.find_surrounding_objects()
                logger.info( 'Объявление сохранено  с кодом %s\r\n\r\n\r\n' % advert.id)

                # Фотки
                elems = advert_doc.xpath('//div[@class="object_descr_images_w"]/a')
                if elems:
                    logger.info( 'найдено %s фоток' % len(elems))
                    for a in elems:
                        try:
                            src = a.get('href')
                            logger.info( src)
                            image = UserImage(user=advert.user)
                            if image.load_image_cian_crop(src):
                                image.save()
                                advert.images.add(image)
                        except Exception, err:
                            logger.info( traceback.format_exc())

            except Exception, err:
                logger.info( traceback.format_exc())

    def process_companies(self, link, start, end):
        for page in xrange(start, end):
            doc = fromstring(self.download_url(link % page))
            doc.make_links_absolute(self.domain)

            element_list = doc.xpath('//table[@class="objects_items_list"]/tbody/tr')
            logger.info( "Загружено %s объявлений\r\n\r\n" % len(element_list))
            n = 0
            for element in element_list:
                try:
                    if not element.get('id'):
                        continue
                    is_agent = False
                    elems = element.xpath('.//td[@class="objects_item_info_col_5"]')
                    if elems:
                        text = elems[0].text_content()
                        if re.findall('([0-9]{2,3}%)', text):
                            is_agent = True

                    if is_agent:
                        elems = element.xpath('.//span[@class="objects_item_realtor_name  "]')
                        agent_name = ''
                        if elems:
                            agent_name = elems[0].text_content().strip()
                        elems = element.xpath('.//td[@class="objects_item_info_col_8"]/div/a')
                        company_tels = []
                        for elem in elems:
                            tel_list = clear_tel_list(elem.text_content().strip())
                            company_tels.append(tel_list)
                            if not Blacklist.check_list(tel_list):
                                Blacklist.add_tel(tel_list, '', 'cian', town=self.town)
                                print tel_list

                        if u'ID:' not in agent_name:
                            company_list = Company.objects.filter(town=self.town, title=agent_name)
                            print company_list
                            if not company_list:
                                company = Company(town=self.town, title=agent_name, is_real=False, tel=u','.join(company_tels))
                                company.save()
                                print company.title


                except Exception, err:
                    logger.info(traceback.format_exc())
                    print traceback.format_exc()

    def collect(self):

        self.parser = Parser.objects.get(title='cian')

        try:
            logger.info('#### Загрузка с сайта cian.ru по Москве ####')
            self.town = Town.objects.get(id=1) #москва
            self.metro_list = self.town.metro_set.all()
            self.district_list = self.town.district_set.all()

            logger.info( 'Аренда квартир посуточно ============================')
            doc = fromstring(self.download_url(self.flat_arenda_day_url))
            doc.make_links_absolute(self.domain)
            self.process_elements(doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, limit=Advert.LIMIT_DAY)

            logger.info( 'Аренда квартир длительно ============================')
            doc = fromstring(self.download_url(self.flat_arenda_long_url))
            doc.make_links_absolute(self.domain)
            self.process_elements(doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, limit=Advert.LIMIT_LONG)

            logger.info( 'Аренда домов посуточно ============================')
            doc = fromstring(self.download_url(self.house_arenda_day_url))
            doc.make_links_absolute(self.domain)
            self.process_elements_house(doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_COUNTRY, limit=Advert.LIMIT_DAY)

            logger.info( 'Аренда домов длительно ============================')
            doc = fromstring(self.download_url(self.house_arenda_long_url))
            doc.make_links_absolute(self.domain)
            self.process_elements_house(doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_COUNTRY, limit=Advert.LIMIT_LONG)

            logger.info( 'Аренда помещений ============================')
            doc = fromstring(self.download_url(self.commercial_arenda_url))
            doc.make_links_absolute(self.domain)
            self.process_elements_commercial(doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_COMMERCIAL, limit=Advert.LIMIT_LONG)

            logger.info( 'Продажа квартир ============================')
            doc = fromstring(self.download_url(self.flat_sale_url))
            doc.make_links_absolute(self.domain)
            self.process_elements(doc, adtype=Advert.TYPE_SALE, estate=Advert.ESTATE_LIVE, limit=Advert.LIMIT_LONG)

            logger.info( 'Продажа домов ============================')
            doc = fromstring(self.download_url(self.house_sale_url))
            doc.make_links_absolute(self.domain)
            self.process_elements_house(doc, adtype=Advert.TYPE_SALE, estate=Advert.ESTATE_COUNTRY, limit=Advert.LIMIT_LONG)

            logger.info( 'Продажа помещений ============================')
            doc = fromstring(self.download_url(self.commercial_sale_url))
            doc.make_links_absolute(self.domain)
            self.process_elements_commercial(doc, adtype=Advert.TYPE_SALE, estate=Advert.ESTATE_COMMERCIAL, limit=Advert.LIMIT_LONG)

            # -----------------------------------------------

            logger.info('#### Загрузка с сайта cian.ru по ПИТЕРУ ####')
            self.town = Town.objects.get(id=2) #питер
            self.metro_list = self.town.metro_set.all()
            self.district_list = self.town.district_set.all()

            logger.info( 'Аренда квартир посуточно ============================')
            doc = fromstring(self.download_url(self.piter_flat_arenda_day_url))
            doc.make_links_absolute(self.domain)
            self.process_elements(doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, limit=Advert.LIMIT_DAY, komissia0=True, set_moderate=True)

            logger.info( 'Аренда квартир длительно ============================')
            doc = fromstring(self.download_url(self.piter_flat_arenda_long_url))
            doc.make_links_absolute(self.domain)
            self.process_elements(doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, limit=Advert.LIMIT_LONG, komissia0=True, set_moderate=True)

        except Exception as ex:
            print ex


    def collect_companies(self):
        # logger.info('#### Загрузка с сайта cian.ru по Москве ####')
        # self.town = Town.objects.get(slug='moskva') #москва
        # self.process_companies(self.msk_flat_arenda_url, 1, 500)
        #
        # logger.info('#### Загрузка с сайта cian.ru по Санк Питербургу ####')
        # self.town = Town.objects.get(slug='sankt-peterburg') #питер
        # self.process_companies(self.spb_flat_arenda_url, 1, 187)

        logger.info('#### Загрузка с сайта cian.ru по Новосибирску ####')
        self.town = Town.admin_objects.get(slug='novosibirsk') #новосибирск
        self.process_companies(self.nsk_flat_arenda_url, 1, 150)

        logger.info('#### Загрузка с сайта cian.ru по Екаберинбургу ####')
        self.town = Town.admin_objects.get(slug='ekaterinburg') #екатеринбург
        self.process_companies(self.ekb_flat_arenda_url, 1, 363)
