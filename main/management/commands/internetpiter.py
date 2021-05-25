#-*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from lxml import html
from lxml.html.soupparser import fromstring
import requests
import re
from datetime import datetime
import traceback
from main.models import Advert, Town, Metro, clear_tel_list, Company, Parser
from uprofile.models import User
from uimg.models import UserImage
from django.db.models import Q


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


class InternerPiterCollector(Collector):
    domain = 'http://www.arenda-piter.ru/'
    catalog_url = 'http://www.arenda-piter.ru/workpage.php?page=online'
    town = None

    def process_elements(self, doc):
        town = Town.admin_objects.get(id=2) #питер
        metro_list = town.metro_set.all()
        district_list = town.district_set.all()

        element_list = doc.xpath('//table[@class="tbm_01"]/tr')
        print "Загружено %s объявлений\r\n\r\n" % len(element_list)
        n = 0
        for element in element_list:
            try:
                if element.get('class') == 'trm_head':      #пропуск заголовка таблицы
                    continue

                n += 1
                print 'Обработка %s объявления--------------------------------' % n

                advert_id = element.get('id').replace(u'idtr', '')
                print 'Номер объявления'
                print advert_id
                if Advert.objects.filter(extnum=advert_id).count()>0:
                    print 'Такое объявление есть в базе'
                    continue

                advert = Advert(extnum=advert_id)
                #тип сделки
                elems = element.xpath('.//td[@class="tdm_01"]')
                if elems:
                    txt = elems[0].text_content()
                    for rooms in xrange(1, 7):              #квартиры
                        if u'%sк.кв.' % rooms in txt:
                            advert.estate = Advert.ESTATE_LIVE
                            advert.live = Advert.LIVE_FLAT
                            advert.rooms = rooms
                            print '%s комнатная квартира' % rooms
                            break
                    if u'комната' in txt:
                        for rooms in xrange(1, 7):              #комнаты
                            if u'к%s' % rooms in txt:
                                advert.estate = Advert.ESTATE_LIVE
                                advert.live = Advert.LIVE_ROOM
                                advert.rooms = rooms
                                print '%s комната(ы)' % rooms
                                break
                    if u'помещение' in txt:
                        for rooms in xrange(1, 7):              #офисы
                            if u'%sк' % rooms in txt:
                                advert.estate = Advert.ESTATE_COMMERCIAL
                                advert.rooms = rooms
                                print 'офис %s комната(ы)' % rooms
                                break
                    for rooms in xrange(1, 7):              #дом
                        if u'дом(%sк)' % rooms in txt:
                            advert.estate = Advert.ESTATE_COUNTRY
                            advert.rooms = rooms
                            print 'дом с %s комнатами' % rooms
                            break

                    if u'сдам' in txt:
                        advert.adtype = Advert.TYPE_LEASE
                        print 'тип объявления - сдам'
                    elif u'продам' in txt:
                        advert.adtype = Advert.TYPE_SALE
                        print 'тип объявления - продам'

                    m = re.search(u'(\d\d:\d\d)(\d\d\.\d\d.\d\d)', txt)
                    if m:
                        try:
                            advert.date = datetime.strptime(m.group(), '%H:%M%d.%m.%y')
                            print 'дата %s' % advert.date
                        except:
                            pass


                # адрес
                elems = element.xpath('.//td[@class="tdm_02"]')
                if elems:
                    txt = elems[0].text_content().strip()
                    txt = txt.replace(u'на карте', u'')
                    advert.address = txt
                    print 'получен адрес'

                    #получение координат
                    try:
                        address_txt = advert.address
                        if not (u'г.' in address_txt):
                            address_txt = u'Россия, ' + town.title + ', ' + address_txt
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

                    # район
                    for district in district_list:
                        if district.title.lower() in txt.lower():
                            advert.district = district
                            print 'получен район'
                            break

                # метро
                elems = element.xpath('.//td[@class="tdm_03"]')
                if elems:
                    txt = elems[0].text_content()
                    for metro in metro_list:
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
                            for metro in metro_list:
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
                            for district in district_list:
                                if district.title.lower() in txt.lower():
                                    advert.district = district
                                    print 'получен район'
                                    break
                    except Exception, err:
                        print traceback.format_exc()

                #общая площадь
                elems = element.xpath('.//td[@class="tdm_041"]')
                if elems:
                    txt = elems[0].text_content()
                    try:
                        advert.square = float(txt)
                        print 'получена площадь помещения %s' % advert.square
                    except:
                        pass

                #жилая площадь
                elems = element.xpath('.//td[@class="tdm_042"]')
                if elems:
                    txt = elems[0].text_content()
                    try:
                        advert.living_square = float(txt)
                        print 'получена жилая площадь помещения %s' % advert.living_square
                    except:
                        pass

                #площадь кухни
                elems = element.xpath('.//td[@class="tdm_043"]')
                if elems:
                    txt = elems[0].text_content()
                    try:
                        advert.kitchen_square = float(txt)
                        print 'получена площадь кухни %s' % advert.kitchen_square
                    except:
                        pass

                #Этаж
                elems = element.xpath('.//td[@class="tdm_044"]')
                if elems:
                    txt = elems[0].text_content()
                    floors = txt.split('/')
                    try:
                        if len(floors) == 1:
                            advert.floor = int(floors[0])
                            print 'получен этаж %s' % advert.floor
                        if len(floors) == 2:
                            advert.floor = int(floors[0])
                            advert.count_floor = int(floors[1])
                            print 'получен этаж и кол-во этажей всего %s/%s' % (advert.floor, advert.count_floor)
                    except:
                        pass

                #Цена
                elems = element.xpath('.//td[@class="tdm_05"]')
                if elems:
                    txt = elems[0].text_content()
                    try:
                        m = re.search(u'([\.0-9]+)', txt.strip(), flags=re.IGNORECASE)
                        if m:
                            advert.price = float(m.group(0).replace('.', ''))
                            print 'получена цена %s' % advert.price
                    except:
                        pass

                #Условия сделки
                if advert.adtype == Advert.TYPE_LEASE:
                    elems = element.xpath('.//td[@class="tdm_07"]')
                    if elems:
                        txt = elems[0].text_content()
                        if u'мес' in txt:
                            advert.limit = Advert.LIMIT_LONG
                            print 'на длительный срок'
                            if advert.live == Advert.LIVE_ROOM:
                                if advert.price < 8000:
                                    continue
                            if (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 1):
                                if advert.price < 10000:
                                    continue
                            if (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 2):
                                if advert.price < 10000:
                                    continue
                            if (advert.live == Advert.LIVE_FLAT) and (advert.rooms == 3):
                                if advert.price < 20000:
                                    continue
                            if (advert.live == Advert.LIVE_FLAT) and (advert.rooms >= 4):
                                if advert.price < 20000:
                                    continue
                        if u'сут' in txt:
                            advert.limit = Advert.LIMIT_DAY
                            print 'посуточно'

                #Примечание
                elems = element.xpath('.//td[@class="tdm_08"]')
                if elems:
                    table = elems[0].xpath('table')
                    if table:
                        txt = table[0].text_content()
                        if u'Меб+' in txt:
                            advert.furniture = True
                            print 'с мебелью'
                        if u'Тв+' in txt:
                            advert.tv = True
                            print 'с телевизором'
                        if u'Хол+' in txt:
                            advert.refrigerator = True
                            print 'с холодильником'
                        if u'СтМ+' in txt:
                            advert.washer = True
                            print 'со стиральной машиной'
                        if u'Тел+' in txt:
                            advert.phone = True
                            print 'с телефоном'
                        if u'Инт+' in txt:
                            advert.internet = True
                            print 'с интернетом'

                    txt = ''
                    desc = self.download_url(u'http://www.arenda-piter.ru/ajax_dp.php?action=dop_podr&id=' + advert_id)
                    if desc:
                        advert.body = desc
                        txt = desc
                        advert.parse(advert.body)

                    if u'Блк' in txt:
                        advert.balcony = True
                        print 'с балконом'
                    if u'Есть Лифт' in txt:
                        advert.lift = True
                        print 'с лифтом'
                    if u'Евро/Рем' in txt:
                        advert.euroremont = True
                        print 'с евроремонтом'
                    if (u'Паркинг' in txt) or (u'Автостоянка' in txt):
                        advert.parking = True
                        print 'с парковкой'

                    company = None
                    try:
                        company_page = elems[0].xpath(u'.//a[@title="Страница фирмы"]')
                        if company_page:
                            href = company_page[0].get('href')
                            company = self.get_company_from_href(href)
                            if company:
                                print 'получено агентство'

                    except Exception, err:
                        print traceback.format_exc()

                    agent = None
                    try:
                        agent_page = elems[0].xpath(u'.//a[@title="Страница риэлтора"]')
                        if agent_page:
                            href = agent_page[0].get('href')
                            agent = self.get_agent_from_href(href)
                            if agent:
                                print 'Получен агент'
                    except Exception, err:
                        print traceback.format_exc()

                    if not agent:
                        print 'Агент не найден'
                        continue
                    else:
                        advert.user = agent
                        if not company:
                            extnum = 'p%s' % agent.extnum
                            companu_list = Company.objects.filter(extnum=extnum)
                            if companu_list:
                                company = companu_list[0]
                            else:
                                company = Company.objects.get(extnum='spb_brokers')
                            print 'Создана агенство для агента'
                        advert.company = company
                        agent.company = company
                        agent.save()

                advert.town = town
                advert.parser = Parser.objects.get(title='arenda-piter')
                advert.save()
                advert.find_clients()
                advert.find_metro_distance()
                advert.find_surrounding_objects()
                print 'Объявление сохранено  с кодом %s\r\n\r\n\r\n' % advert.id

                # Фотки
                # elems = element.xpath('.//td[@class="tdm_09"]')
                # if elems:
                #     a = elems[0].xpath('.//a')
                #     if a:
                #         try:
                #             src = u'http://www.arenda-piter.ru/foto_for_listing.php?big=1&nom=' + advert_id
                #             image = UserImage(user=agent)
                #             image.load_image(src)
                #             image.save()
                #             advert.images.add(image)
                #         except Exception, err:
                #             print traceback.format_exc()

            except Exception, err:
                print traceback.format_exc()

    def get_company_from_href(self, href):
        company = None
        m = re.search('agentstvo=([0-9]+)', href)
        company_id = m.group(1) if m else None
        print 'Агентство с кодом %s' % company_id
        company_list = Company.objects.filter(extnum=company_id)
        if company_list:
            company = company_list[0]
            print 'Агенство есть в нашей базе'
        else:
            doc_company = fromstring(self.download_url(href))
            doc_company.make_links_absolute(self.domain)
            print 'Загружена страница агентства'
            company = Company(extnum=company_id, is_real=False, town=self.town)
            title = doc_company.xpath('//div[@class="tbl04"]/table/tr/td/div')
            if title:
                company.title = title[0].text_content().encode('utf8').strip()
                print 'Получено название агентства'

            logo = doc_company.xpath('//div[@class="tbl04"]/div/table[1]/tr/td/div/img')
            if logo:
                try:
                    company.load_logo(logo[0].get('src'))
                    print 'загружен логотип агентства'
                except Exception, err:
                    print traceback.format_exc()

            tbl = doc_company.xpath('//table[@class="tarif_tbl"][1]')
            if tbl:
                for tr in tbl[0].xpath('.//tr'):
                    tds = tr.xpath('.//td')
                    if u'Адрес' in tds[0].text_content():
                        company.address = tds[1].text_content().encode('utf8')
                        print 'получен адрес агентства'
                    if u'Телефон' in tds[0].text_content():
                        company.tel = clear_tel_list(html.tostring(tds[1]).encode('utf8').replace('<br>', ', '))
                        print 'получен телефон агентства'
                    if u'Почта' in tds[0].text_content():
                        txt = tds[1].text_content().encode('utf8').split(',')
                        m1 = re.search('"(.+)"', txt[0])
                        m2 = re.search('"(.+)"', txt[1])
                        company.email = "%s@%s" % (m1.group(1), m2.group(1))
                        print 'получен емайл агенства'
                    if u'ОГРН/ИНН' in tds[0].text_content():
                        ogrn = tds[1].text_content().split('/')
                        if len(ogrn) > 0:
                            company.ogrn = ogrn[0].encode('utf8').strip()
                            print 'получен огрн'
                        if len(ogrn) > 1:
                            company.inn = ogrn[1].encode('utf8').strip()
                            print 'получен инн'
            company.status = Company.STATUS_ACTIVE
            company.save()
            print 'Создано новое агентство'
        return company

    def get_agent_from_href(self, href):
        agent = None
        m = re.search('agent=([0-9]+)', href)
        agent_id = m.group(1) if m else None
        print 'Агент с кодом %s' % agent_id
        # agent_list = User.objects.filter(extnum=agent_id)
        # if agent_list:
        #     agent = agent_list[0]
        #     print 'Агент есть в нашей базе'
        # else:
        doc_agent = fromstring(self.download_url(href))
        doc_agent.make_links_absolute(self.domain)
        print 'загружена страница агента'
        agent = User(extnum=agent_id)
        tbl = doc_agent.xpath('//table[@class="tarif_tbl"][1]')
        if tbl:
            for tr in tbl[0].xpath('.//tr'):
                tds = tr.xpath('.//td')
                if u'Имя, Отчество' in tds[0].text_content():
                    agent.first_name = tds[1].text_content().encode('utf8')
                    print 'получено фио агента'
                if u'Телефон' in tds[0].text_content():
                    agent.tel = clear_tel_list(tds[1].text_content()).encode('utf8')
                    print 'получен телефон агента'
                if u'Почта' in tds[0].text_content():
                    txt = tds[1].text_content().encode('utf8').split(',')
                    m1 = re.search('"(.+)"', txt[0])
                    m2 = re.search('"(.+)"', txt[1])
                    agent.agent_email = "%s@%s" % (m1.group(1), m2.group(1))
                    agent.email = ''
                    agent.gen_username('comp_')
                    print 'получен емайл агента %s' % agent.agent_email
        exists_user = []
        if agent.tel:
            exists_user = User.objects.filter(tel=agent.tel)
        if exists_user:
            agent = exists_user[0]
        else:
            if agent.agent_email:
                exists_user = User.objects.filter(email=agent.agent_email)
            if exists_user:
                agent = exists_user[0]
            else:
                if agent.extnum:
                    exists_user = User.objects.filter(extnum=agent.extnum)
                if exists_user:
                    agent = exists_user[0]
                else:
                    if not agent.agent_email:
                        print 'У агента нет мыла'
                        return None

                    logo = doc_agent.xpath('//div[@class="tbl04"]/table[1]/tr/td/div/table/tr/td/img')
                    if logo:
                        try:
                            agent.load_photo(logo[0].get('src'))
                            print 'загружено фото агента'
                        except Exception, err:
                            print traceback.format_exc()

                    agent.gen_password()
                    print 'сгенерирован пароль'
                    agent.save()
                    print 'Создан новый агент'
        return agent

    def collect(self):

        print 'Загрузка с сайта arenda-piter.ru'
        self.town = Town.objects.get(id=2)

        try:
            doc = fromstring(self.download_url(self.catalog_url))
            doc.make_links_absolute(self.domain)
            self.process_elements(doc)
        except Exception as ex:
            print ex

    def collect_all(self):

        print 'Загрузка с сайта arenda-piter.ru всех объявлений'

        for page in xrange(1, 3):
            print 'Страница %s' % page
            try:
                doc = fromstring(self.download_url(self.catalog_url + '&numpage=' + str(page)))
                doc.make_links_absolute(self.domain)
                self.process_elements(doc)
            except Exception as ex:
                print ex


class Command(BaseCommand):
    help = u'Загрузка объявлений internet-piter.ru'

    def handle(self, *args, **options):
        collect = InternerPiterCollector()
        collect.collect_all()