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


logger = logging.getLogger('baza812')


class Baza812Collector(Collector):
    domain = 'http://baza812.ru/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    }

    metro_list = None
    district_list = None
    town = None

    def process_elements(self, doc):
        element_list = doc.xpath('//div[@id="search-results"]/div[@class="item"]')
        logger.info(len(element_list))
        for element in element_list:
            advert_link = element.xpath('.//a[@class="showmoreinfo"]')
            if advert_link:
                if u'http://baza812.ru/item/show?itemId=' in advert_link[0].get('href'):
                    advert_id = u'b812_' + advert_link[0].get('href').replace(u'http://baza812.ru/item/show?itemId=', u'')
                    exists_adverts = StopAgentAdvert.objects.filter(extnum=advert_id)
                    if exists_adverts:
                        continue
                    else:
                        advert = StopAgentAdvert(extnum=advert_id, town=self.town)
                        r = requests.get(advert_link[0].get('href'), cookies=self.cookies, allow_redirects=True, headers=self.headers)
                        doc_advert = fromstring(r.text)
                        doc_advert.make_links_absolute(self.domain)
                        nodes = doc_advert.xpath('//div[@class="right-column"]/div')
                        if nodes:
                            txt = nodes[0].text_content()
                            if u'комната' in txt:
                                advert.live = StopAgentAdvert.LIVE_ROOM
                            else:
                                advert.live = StopAgentAdvert.LIVE_FLAT
                                for room in xrange(1, 5):
                                    if (u'%s комнатная квартира' % room) in txt:
                                        advert.rooms = room
                        else:
                            continue

                        nodes = doc_advert.xpath('//div[@class="right-column"]/p[contains(@class, "metro")]')
                        if nodes:
                            txt = nodes[0].text_content()
                            for metro in self.metro_list:
                                if metro.title.lower() in txt.lower():
                                    advert.metro = metro
                                    break
                        else:
                            continue

                        nodes = doc_advert.xpath('//div[@class="right-column"]/p[@class="owner-phone"]')
                        if nodes:
                            txt = nodes[0].text_content().replace(u' ', u'').strip() \
                                .replace(u'-', u'') \
                                .replace(u'(', u'') \
                                .replace(u')', u'')
                            if txt.startswith(u'+7'):
                                txt = txt[2:]
                            if txt.startswith(u'8'):
                                txt = txt[1:]
                            advert.owner_tel = txt
                        else:
                            continue

                        nodes = doc_advert.xpath('//div[@class="right-column"]/p[@class="owner-name"]')
                        if nodes:
                            txt = nodes[0].text_content() \
                                .replace(u'Владелец: ', u'') \
                                .strip()
                            advert.owner_name = txt

                        advert.save()
                        advert.check_adverts()

        return True

    def process_url(self, url):
        r = requests.get(url, cookies=self.cookies, allow_redirects=True, headers=self.headers)
        self.cookies = dict(r.cookies.items())
        doc = fromstring(r.text)
        doc.make_links_absolute(self.domain)
        self.process_elements(doc)

    def collect(self):
        logger.info('#### САНКТ ПЕТЕРБУРГ ####')

        self.town = Town.objects.get(id=2)
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()
        try:
            self.process_url('http://baza812.ru/catalog/search?metro=&dictrict=&search=1&price_from=&price_to=&days=1')
        except Exception, err:
            logger.info(traceback.format_exc())

        logger.info('#### ВЫХОД ####')
