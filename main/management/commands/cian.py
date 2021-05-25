#-*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from lxml import html
from lxml.html.soupparser import fromstring
import requests
import re
from datetime import datetime
import traceback
from main.models import Advert, Town, Metro, clear_tel_list, Company, Blacklist
from uprofile.models import User
from uimg.models import UserImage


#простой коллектор сборщик
class Collector:
    encoding = 'cp1251'
    url = ''
    cookies = None

    def download_url(self, url, encoding='cp1251'):
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

    flat_sale_url = 'http://www.cian.ru/cat.php?deal_type=2&obl_id=1&city[0]=1'
    house_sale_url = 'http://www.cian.ru/cat.php?suburbian=yes&deal_type=2&obl_id=1&city[0]=1'
    commercial_sale_url = 'http://www.cian.ru/cat.php?offices=yes&deal_type=2&obl_id=1&city[0]=1'

    moderator = None
    town = None
    metro_list = None
    district_list = None

    def process_advert_page(self, advert, advert_doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, limit=Advert.LIMIT_DAY):
        #комиссия
        komissia = True
        elems = advert_doc.xpath('//td[@class="object_descr_td_l"]')
        if elems:
            txt = elems[0].text_content()
            if u'комиссия 0%' in txt:
                komissia = False

        #кол-во комнат
        elems = advert_doc.xpath('//div[@class="object_descr_title"]')
        if elems:
            txt = elems[0].text_content()
            if u'кв.' in txt:
                advert.estate = Advert.ESTATE_LIVE
                advert.live = Advert.LIVE_FLAT
                print 'квартира'
                for rooms in xrange(1, 7):              #квартиры
                    if u'%s-комн.' % rooms in txt:
                        advert.rooms = rooms
                        print '%s комнатная квартира' % rooms
                        break
            if u'комната' in txt:
                advert.estate = Advert.ESTATE_LIVE
                advert.live = Advert.LIVE_ROOM
                print 'комната'
                for rooms in xrange(1, 7):              #комнаты
                    if u'%s-комн.' % rooms in txt:
                        advert.rooms = rooms
                        print '%s комната(ы)' % rooms
                        break
            if (u'дом' in txt) or (u'таунхаус' in txt):
                advert.estate = Advert.ESTATE_COUNTRY
                print 'дом'
                for floor in xrange(1, 7):              #офисы
                    if u'%s этаж.' % floor in txt:
                        advert.count_floor = floor
                        print 'дом %s этаж(а)' % floor
                        break
                m = re.search(u'([0-9]+) м', txt)
                if m:
                    advert.square = int(m.group(1))
                    print 'получена общая площадь %s' % advert.square

            if u'участок' in txt:
                advert.estate = Advert.ESTATE_TERRITORY
                print 'участок'
                m = re.search(u'([0-9]+) м', txt)
                if m:
                    advert.square = int(m.group(1))
                    print 'получена общая площадь %s' % advert.square
                m = re.search(u'([0-9]+) сот.', txt)
                if m:
                    advert.square = int(m.group(1)) * 100
                    print 'получена общая площадь %s' % advert.square

        # адрес
        elems = advert_doc.xpath('//h1[@class="object_descr_addr"]')
        if elems:
            txt = elems[0].text_content().strip().replace(u'Москва,', u'')
            advert.address = txt
            print 'получен адрес'

            #получение координат
            try:
                address_txt = advert.address
                if not (u'Москва' in address_txt):
                    address_txt = self.town.title + ', ' + address_txt
                doc_text = self.download_url(u'http://geocode-maps.yandex.ru/1.x/?results=1&geocode=%s' % address_txt)
                doccoord = fromstring(doc_text)
                point = doccoord.xpath('//point/pos')
                if point:
                    xy = point[0].text_content().split(' ')
                    lon = float(xy[0])
                    lat = float(xy[1])
                    advert.longitude = lon
                    advert.latitude = lat
                    print 'получены координаты'
            except Exception, err:
                print traceback.format_exc()


        # метро
        elems = advert_doc.xpath('//div[@class="object_descr_metro"]')
        if elems:
            txt = elems[0].text_content()
            for metro in self.metro_list:
                if metro.title.lower() in txt.lower():
                    advert.metro = metro
                    print 'получено метро'
                    break

        #получение метро
        if not advert.metro and advert.latitude and advert.longitude:
            try:
                print 'запрос метро'
                doc_text = self.download_url(u'http://geocode-maps.yandex.ru/1.x/?results=1&kind=metro&geocode=%s,%s' % (advert.longitude, advert.latitude), encoding='utf8')
                doccoord = fromstring(doc_text)
                metro_name = doccoord.xpath('//name')
                if metro_name:
                    txt = metro_name[0].text_content()
                    for metro in self.metro_list:
                        if metro.title.lower() in txt.lower():
                            advert.metro = metro
                            print 'получено метро'
                            break
            except Exception, err:
                print traceback.format_exc()

        #получение района
        if not advert.district and advert.latitude and advert.longitude:
            try:
                print 'запрос района'
                doc_text = self.download_url(u'http://geocode-maps.yandex.ru/1.x/?results=1&kind=district&geocode=%s,%s' % (advert.longitude, advert.latitude), encoding='utf8')
                doccoord = fromstring(doc_text)
                district_name = doccoord.xpath('//name')
                if district_name:
                    txt = district_name[0].text_content()
                    for district in self.district_list:
                        if district.title.lower() in txt.lower():
                            advert.district = district
                            print 'получен район'
                            break
            except Exception, err:
                print traceback.format_exc()

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
                            print 'получена общая площадь %s' % advert.square
                    if u'Площадь:' in ths[0].text_content():
                        m = re.search('([0-9]+)', tds[0].text_content())
                        if m:
                            advert.square = int(m.group(0))
                            print 'получена общая площадь %s' % advert.square
                    if u'Жилая площадь:' in ths[0].text_content():
                        m = re.search('([0-9]+)', tds[0].text_content())
                        if m:
                            advert.living_square = int(m.group(0))
                            print 'получена жилая площадь %s' % advert.living_square
                    if u'Площадь кухни:' in ths[0].text_content():
                        m = re.search('([0-9]+)', tds[0].text_content())
                        if m:
                            advert.kitchen_square = int(m.group(0))
                            print 'получена площадь кухни %s' % advert.kitchen_square
                    if u'Балкон:' in ths[0].text_content():
                        if u'1' in tds[0].text_content():
                            advert.balcony = True
                            print 'балкон'
                    if u'Этаж:' in ths[0].text_content():
                        txt = tds[0].text_content()
                        floors = txt.split('/')
                        try:
                            if len(floors) == 1:
                                advert.floor = int(floors[0].replace('&nbsp;', '').replace('-', ''))
                                print 'получен этаж %s' % advert.floor
                            if len(floors) == 2:
                                advert.floor = int(floors[0].replace('&nbsp;', '').replace('-', ''))
                                advert.count_floor = int(floors[1].replace('&nbsp;', '').replace('-', ''))
                                print 'получен этаж и кол-во этажей всего %s/%s' % (advert.floor, advert.count_floor)
                        except:
                            pass

        # Цена
        elems = advert_doc.xpath('//div[@id="price_rur"]')
        if elems:
            try:
                txt = elems[0].text_content()
                advert.price = int(elems[0].text_content())
                print 'получена цена %s' % advert.price
            except:
                pass

        if not advert.price:
            print 'нет цены'


        #Примечание
        elems = advert_doc.xpath('//div[@class="object_descr_details clearfix"]')
        if elems:
            txt = elems[0].text_content()
            if u'мебель' in txt:
                advert.furniture = True
                print 'с мебелью'
            if u'ТВ' in txt:
                advert.tv = True
                print 'с телевизором'
            if u'холодильник' in txt:
                advert.refrigerator = True
                print 'с холодильником'
            if u'стиральная машина' in txt:
                advert.washer = True
                print 'со стиральной машиной'
            if u'телефон' in txt:
                advert.phone = True
                print 'с телефоном'
            if u'балкон' in txt:
                advert.balcony = True
                print 'с интернетом'


        # Телефон
        advert_tel = None
        elems = advert_doc.xpath('//strong[@class="object_descr_phone_orig"]')
        if elems:
            advert_tel = clear_tel_list(elems[0].text_content())
            print 'получен телефон'
        else:
            print 'телефон отсутствует'
            return

        # Описание
        elems = advert_doc.xpath('//div[@class="object_descr_text"]')
        if elems:
            advert.body = elems[0].text
            # advert.body = re.sub(u'([\-\ \(\)0-9]{10,})', u'+7 (XXX) XXX-XX-XX', elems[0].text)
            print 'получено описание'

        # риелтор
        elems = advert_doc.xpath('//span[@class="object_descr_realtor_name"]')
        if elems:
            txt = elems[0].text_content()
            if (u'ID:' in txt) and not komissia:
                # собственник ?
                advert.owner_tel = advert_tel
                advert.status = Advert.STATUS_VIEW
                advert.user = self.moderator
                if Blacklist.check_list(advert.owner_tel):
                    print 'Телефон в черном списке'
                    return
                print 'объявление собственника. Помещено на модерацию'
            else:
                company = None
                user = None
                if (u'частный маклер' in txt) or (u'ID:' in txt):
                    company_list = Company.objects.filter(title='Частные маклеры')
                    if company_list:
                        company = company_list[0]
                        print 'найдена группа частных маклеров'
                    else:
                        company = Company(title='Частные маклеры', status=Company.STATUS_ACTIVE, is_real=False)
                        company.save()
                        print 'создана группа частных маклеров'
                else:
                    company_list = Company.objects.filter(title=txt.encode('utf8'))
                    if company_list:
                        company = company_list[0]
                        print 'найдено агентство в базе'
                    else:
                        company = Company(title=txt.encode('utf8'), status=Company.STATUS_ACTIVE, is_real=False)
                        company.save()
                        print 'создано новое агентство'

                user_list = User.objects.filter(tel__contains=advert_tel)
                if user_list:
                    user = user_list[0]
                    print 'агент найден в базе'
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
                    print 'создан новый агент'

                advert.company = company
                advert.user = user

    def process_elements(self, doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, limit=Advert.LIMIT_DAY):
        self.town = Town.objects.get(id=1) #москва
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()
        self.moderator = User.objects.get(username='admin')

        element_list = doc.xpath('//table[@class="cat"]/tr')
        print "Загружено %s объявлений\r\n\r\n" % len(element_list)
        n = 0
        for element in element_list:
            try:
                if not element.get('id'):
                    continue

                n += 1
                print 'Обработка %s объявления--------------------------------' % n

                aid = element.get('id').replace(u'tr_', '')
                advert_id = "cian" + aid
                print 'Номер объявления'
                print advert_id
                if Advert.objects.filter(extnum=advert_id).count() > 0:
                    print 'Такое объявление есть в базе'
                    continue

                advert = Advert(extnum=advert_id, adtype=adtype, limit=limit, town=self.town)

                # дата
                elems = doc.xpath('//span[@id="added_%s"]' % aid)
                if elems:
                    txt = elems[0].text_content()
                    try:
                        advert.date = datetime.strptime(txt, '%d.%m.%y %H:%M')
                        print 'дата %s' % advert.date
                    except:
                        pass

                advert_doc = fromstring(self.download_url('http://www.cian.ru/%s/flat/%s/' % ('rent' if adtype==Advert.TYPE_LEASE else 'sale', aid), 'utf8'))
                advert_doc.make_links_absolute(self.domain)
                print 'загружена страница объявления'

                self.process_advert_page(advert, advert_doc, adtype, estate, limit)

                if not advert.price:
                    continue
                if not advert.user:
                    continue

                advert.save()
                advert.find_clients()
                print 'Объявление сохранено  с кодом %s' % advert.id

                # Фотки
                elems = advert_doc.xpath('//div[@class="object_descr_images_w"]/a')
                if elems:
                    print 'найдено %s фоток' % len(elems)
                    for a in elems:
                        try:
                            src = a.get('href')
                            print src
                            image = UserImage(user=advert.user)
                            if image.load_image_crop(src):
                                image.save()
                                advert.images.add(image)
                        except Exception, err:
                            print traceback.format_exc()
                print '\r\n\r\n\r\n'
            except Exception, err:
                print traceback.format_exc()

    def process_elements_house(self, doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_COUNTRY, limit=Advert.LIMIT_DAY):
        self.town = Town.objects.get(id=1) #москва
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()
        self.moderator = User.objects.get(username='admin')

        element_list = doc.xpath('//div[contains(@class, "offer_container")]')
        print "Загружено %s объявлений\r\n\r\n" % len(element_list)
        n = 0
        for element in element_list:
            try:
                if not element.get('id'):
                    continue

                n += 1
                print 'Обработка %s объявления--------------------------------' % n

                aid = element.get('id').replace(u'offer_', '')
                advert_id = "cian" + aid
                print 'Номер объявления'
                print advert_id
                if Advert.objects.filter(extnum=advert_id).count() > 0:
                    print 'Такое объявление есть в базе'
                    continue

                advert = Advert(extnum=advert_id, adtype=adtype, limit=limit, town=self.town, estate=estate)

                advert_doc = fromstring(self.download_url('http://www.cian.ru/%s/suburban/%s/' % ('rent' if adtype==Advert.TYPE_LEASE else 'sale', aid), 'utf8'))
                advert_doc.make_links_absolute(self.domain)
                print 'загружена страница объявления'

                self.process_advert_page(advert, advert_doc, adtype, estate, limit)

                if not advert.price:
                    continue

                advert.save()
                advert.find_clients()
                print 'Объявление сохранено  с кодом %s\r\n\r\n\r\n' % advert.id

                # Фотки
                elems = advert_doc.xpath('//div[@class="object_descr_images_w"]/a')
                if elems:
                    print 'найдено %s фоток' % len(elems)
                    for a in elems:
                        try:
                            src = a.get('href')
                            print src
                            image = UserImage(user=advert.user)
                            if image.load_image_crop(src):
                                image.save()
                                advert.images.add(image)
                        except Exception, err:
                            print traceback.format_exc()

            except Exception, err:
                print traceback.format_exc()

    def process_elements_commercial(self, doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_COMMERCIAL, limit=Advert.LIMIT_LONG):
        self.town = Town.objects.get(id=1) #москва
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()
        self.moderator = User.objects.get(username='admin')

        element_list = doc.xpath('//div[contains(@class, "offer_container")]')
        print "Загружено %s объявлений\r\n\r\n" % len(element_list)
        n = 0
        for element in element_list:
            try:
                if not element.get('id'):
                    continue

                n += 1
                print 'Обработка %s объявления--------------------------------' % n

                aid = element.get('id').replace(u'offer_', '')
                advert_id = "cian" + aid
                print 'Номер объявления'
                print advert_id
                if Advert.objects.filter(extnum=advert_id).count() > 0:
                    print 'Такое объявление есть в базе'
                    continue

                advert = Advert(extnum=advert_id, adtype=adtype, limit=limit, town=self.town, estate=estate)

                advert_doc = fromstring(self.download_url('http://www.cian.ru/%s/commercial/%s/' % ('rent' if adtype==Advert.TYPE_LEASE else 'sale', aid), 'utf8'))
                advert_doc.make_links_absolute(self.domain)
                print 'загружена страница объявления'

                self.process_advert_page(advert, advert_doc, adtype, estate, limit)

                if not advert.price:
                    continue

                advert.save()
                advert.find_clients()
                print 'Объявление сохранено  с кодом %s\r\n\r\n\r\n' % advert.id

                # Фотки
                elems = advert_doc.xpath('//div[@class="object_descr_images_w"]/a')
                if elems:
                    print 'найдено %s фоток' % len(elems)
                    for a in elems:
                        try:
                            src = a.get('href')
                            print src
                            image = UserImage(user=advert.user)
                            if image.load_image_crop(src):
                                image.save()
                                advert.images.add(image)
                        except Exception, err:
                            print traceback.format_exc()

            except Exception, err:
                print traceback.format_exc()

    def collect(self):

        print 'Загрузка с сайта cian.ru'

        try:
            print 'Аренда квартир посуточно ============================'
            doc = fromstring(self.download_url(self.flat_arenda_day_url))
            doc.make_links_absolute(self.domain)
            self.process_elements(doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, limit=Advert.LIMIT_DAY)

            print 'Аренда квартир длительно ============================'
            doc = fromstring(self.download_url(self.flat_arenda_long_url))
            doc.make_links_absolute(self.domain)
            self.process_elements(doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_LIVE, limit=Advert.LIMIT_LONG)

            print 'Аренда домов посуточно ============================'
            doc = fromstring(self.download_url(self.house_arenda_day_url))
            doc.make_links_absolute(self.domain)
            self.process_elements_house(doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_COUNTRY, limit=Advert.LIMIT_DAY)

            print 'Аренда домов длительно ============================'
            doc = fromstring(self.download_url(self.house_arenda_long_url))
            doc.make_links_absolute(self.domain)
            self.process_elements_house(doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_COUNTRY, limit=Advert.LIMIT_LONG)

            print 'Аренда помещений ============================'
            doc = fromstring(self.download_url(self.commercial_arenda_url))
            doc.make_links_absolute(self.domain)
            self.process_elements_commercial(doc, adtype=Advert.TYPE_LEASE, estate=Advert.ESTATE_COMMERCIAL, limit=Advert.LIMIT_LONG)

            print 'Продажа квартир ============================'
            doc = fromstring(self.download_url(self.flat_sale_url))
            doc.make_links_absolute(self.domain)
            self.process_elements(doc, adtype=Advert.TYPE_SALE, estate=Advert.ESTATE_LIVE, limit=Advert.LIMIT_LONG)

            print 'Продажа домов ============================'
            doc = fromstring(self.download_url(self.house_sale_url))
            doc.make_links_absolute(self.domain)
            self.process_elements_house(doc, adtype=Advert.TYPE_SALE, estate=Advert.ESTATE_COUNTRY, limit=Advert.LIMIT_LONG)

            print 'Продажа помещений ============================'
            doc = fromstring(self.download_url(self.commercial_sale_url))
            doc.make_links_absolute(self.domain)
            self.process_elements_commercial(doc, adtype=Advert.TYPE_SALE, estate=Advert.ESTATE_COMMERCIAL, limit=Advert.LIMIT_LONG)
        except Exception as ex:
            print ex

    # def collect_all(self):
    #
    #     print 'Загрузка с сайта arenda-piter.ru всех объявлений'
    #
    #     for page in xrange(1, 3):
    #         print 'Страница %s' % page
    #         try:
    #             doc = fromstring(self.download_url(self.catalog_url + '&numpage=' + str(page)))
    #             doc.make_links_absolute(self.domain)
    #             self.process_elements(doc)
    #         except Exception as ex:
    #             print ex


class Command(BaseCommand):
    help = u'Загрузка объявлений cian.ru'

    def handle(self, *args, **options):
        collect = CianCollector()
        collect.collect()