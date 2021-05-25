#-*- coding: utf-8 -*-
from lxml import html, etree
from lxml.html import fromstring
import requests
import re
from datetime import datetime, timedelta
import traceback
from main.collectors.base import Collector
from main.models import Town, Metro, StopAgentAdvert, Advert, User
import logging
from django.db.models import Q


logger = logging.getLogger('kvarnado')


class KvarnadoCollector(Collector):
    domain = 'http://kvarnado.ru/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    }

    metro_list = None
    district_list = None
    town = None

    def process_elements(self, doc):
        element_list = doc.xpath('//div[@class="box catalog_ad_preview"]')
        logger.info(len(element_list))
        for element in element_list:
            advert_link = element.xpath('.//div[@class="link"]/span')
            if advert_link:
                m = re.findall('favorite\(this\, \'(.*)\'\)', advert_link[0].get('onclick'))
                if m:
                    advert_id = m[0]
                    exists_adverts = StopAgentAdvert.objects.filter(extnum=advert_id)
                    if exists_adverts:
                        continue
                    else:
                        advert = StopAgentAdvert(extnum=advert_id, town=self.town)

                        nodes = element.xpath('.//div[@class="type_text"]')
                        if nodes:
                            txt = nodes[0].text_content()
                            if u'Комната' in txt:
                                advert.live = StopAgentAdvert.LIVE_ROOM
                            elif u'Однокомнатная' in txt:
                                advert.live = StopAgentAdvert.LIVE_FLAT
                                advert.rooms = 1
                            elif u'Двухкомнатная' in txt:
                                advert.live = StopAgentAdvert.LIVE_FLAT
                                advert.rooms = 2
                            elif u'Трехкомнатная' in txt:
                                advert.live = StopAgentAdvert.LIVE_FLAT
                                advert.rooms = 3
                            elif u'Четырехкомнатная' in txt:
                                advert.live = StopAgentAdvert.LIVE_FLAT
                                advert.rooms = 4
                            else:
                                continue
                        else:
                            continue

                        nodes = element.xpath('.//div[@class="subway"]')
                        if nodes:
                            txt = nodes[0].text_content()
                            for metro in self.metro_list:
                                if metro.title.lower() in txt.lower():
                                    advert.metro = metro
                                    break
                        else:
                            continue

                        nodes = element.xpath('.//div[@class="show_phone"]')
                        if nodes:
                            txt = nodes[0].text_content().replace(u' ', u'').strip() \
                                .replace(u'-', u'') \
                                .replace(u'(', u'') \
                                .replace(u')', u'') \
                                .replace(u'показатьполностью', u'')
                            if txt.startswith(u'+7'):
                                txt = txt[2:]
                            if txt.startswith(u'8'):
                                txt = txt[1:]
                            advert.owner_tel = txt
                        else:
                            continue

                        nodes = element.xpath('.//div[@class="owner"]')
                        if nodes:
                            txt = nodes[0].text_content().replace(u' ', u'') \
                                .replace(u'Собственник', u'') \
                                .strip()
                            advert.owner_name = txt

                        advert.save()
                        advert.check_adverts(moderator='automoder_kvarnado')

        return True

    def process_url(self, url):
        r = requests.get(url, cookies=self.cookies, allow_redirects=True, headers=self.headers)
        self.cookies = dict(r.cookies.items())
        doc = fromstring(r.text)
        doc.make_links_absolute(self.domain)
        self.process_elements(doc)

    def collect(self):
        logger.info('#### Москва ####')

        self.town = Town.objects.get(id=1)
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()
        try:
            for page in xrange(1, 6):
                self.process_url('http://kvarnado.ru/аренда/поиск/?city=&time=1&minprice=&maxprice=&page=%s' % page)
        except Exception, err:
            logger.info(traceback.format_exc())

        logger.info('#### ВЫХОД ####')
