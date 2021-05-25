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


logger = logging.getLogger('stopagent')


class StopagentCollector(Collector):
    domain = 'http://stopagent.ru/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    }

    metro_list = None
    district_list = None
    town = None

    def process_elements(self, doc):
        element_list = doc.xpath('//ul[@class="search_results"]/li')
        logger.info(len(element_list))
        for element in element_list:
            advert_link = element.xpath('.//div[@class="search_results_text"]/a')
            if advert_link:
                if u'http://stopagent.ru/id' in advert_link[0].get('href'):
                    advert_id = advert_link[0].get('href').replace(u'http://stopagent.ru/id', u'')
                    exists_adverts = StopAgentAdvert.objects.filter(extnum=advert_id)
                    if exists_adverts:
                        continue
                    else:
                        advert = StopAgentAdvert(extnum=advert_id, town=self.town)
                        r = requests.get(advert_link[0].get('href'), cookies=self.cookies, allow_redirects=True, headers=self.headers)
                        doc_advert = fromstring(r.text)
                        doc_advert.make_links_absolute(self.domain)
                        nodes = doc_advert.xpath('//div[@class="header_gray_top"]')
                        if nodes:
                            txt = nodes[0].text_content()
                            if u'комнату' in txt:
                                advert.live = StopAgentAdvert.LIVE_ROOM
                            else:
                                advert.live = StopAgentAdvert.LIVE_FLAT
                                for room in xrange(1, 5):
                                    if (u'%s к' % room) in txt:
                                        advert.rooms = room
                        else:
                            continue

                        nodes = doc_advert.xpath('//div[@class="adv_text"]/h1')
                        if nodes:
                            txt = nodes[0].text_content()
                            for metro in self.metro_list:
                                if metro.title.lower() in txt.lower():
                                    advert.metro = metro
                                    break
                        else:
                            continue

                        nodes = doc_advert.xpath('//div[@class="number"]')
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

                        nodes = doc_advert.xpath('//div[@class="password_box"]/div[@class="owner"]')
                        if nodes:
                            txt = nodes[0].text_content().replace(u' ', u'') \
                                .replace(u'Владелец:', u'') \
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
            self.process_url('http://stopagent.ru/arenda/?city=spb')
        except Exception, err:
            logger.info(traceback.format_exc())

        logger.info('#### ВЫХОД ####')
