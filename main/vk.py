#-*- coding: utf-8 -*-

from lxml import html
from lxml.html import fromstring
import requests
import re
import traceback
from main.models import Advert, Town


class VK:
    vk_cookies = dict()
    vk_hash = ''
    vk_timehash = ''
    group_id = ''
    group_url = ''
    username = ''
    password = ''

    def __init__(self, group_id=None, group_url=None, username=None, password=None, *args, **kwargs):
        if group_id:
            self.group_id = group_id
        if group_url:
            self.group_url = group_url
        if username:
            self.username = username
        if password:
            self.password = password

    #Авторизация вконтакте
    def login(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset':'windows-1251,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding':'gzip,deflate,sdch',
            'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
            'Content-Type':'application/x-www-form-urlencoded',
            'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'
        }
        r = requests.get('http://vk.com/', headers=headers)
        # print r.status_code, r.headers, r.cookies.items()
        cookie = dict(r.cookies.items())
        # print cookie
        doc = fromstring(r.text)
        inputs = doc.xpath(r'//input')
        params = {}
        for input in inputs:
            # print input
            if input.get('value'):
                params[input.get('name')] =input.get('value').encode('utf8')
            else:
                params[input.get('name')] =None

        headers = {
            # ':host': 'login.vk.com',
            # ':method': 'POST',
            # ':path': '/?act=login',
            # ':scheme': 'https',
            # ':version': 'HTTP/1.1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset':'windows-1251,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding':'gzip,deflate,sdch',
            'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
            'Content-Type':'application/x-www-form-urlencoded',
            'Origin':'http://vk.com',
            'Referer':'http://vk.com/login.php',
            'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.11 (KHTML, like Gecko) Ubuntu/12.04 Chromium/20.0.1132.47 Chrome/20.0.1132.47 Safari/536.11)'
        }

        data = dict(
            email=self.username,
            ip_h = params['ip_h'],
            lg_h = params['lg_h'],
            act = params['act'],
            _origin=params['_origin'],
            expire='',
            role="al_frame",
            captcha_sid="",
            captcha_key=""
        )

        # cookie['remixlang'] = '0'

        data['pass'] = self.password
        # print data

        #Отправляю данные авторизации
        r = requests.post('https://login.vk.com/?act=login', data=data, headers=headers, cookies=cookie, allow_redirects=False)
        # print r.url, r.status_code, r.headers, r.cookies.items()
        cookie = dict(cookie.items() + r.cookies.items())
        headers['Host'] ='vk.com'
        headers['Referer'] ='http://vk.com/login.php'
        # print '------------------cookie----------------'
        # print cookie
        # print '---------------------------------'
        if r.status_code==302:
            #Отправляю hash чтобы получить remixid
            r=requests.get(r.headers['location'], headers=headers, cookies=cookie, allow_redirects=False)
            # print r.url, r.status_code, r.headers, r.cookies.items()
            # print r.text
            cookie = dict(cookie.items() + r.cookies.items())
            # print '---------------------------------'
            self.vk_cookies = cookie
            # print self.vk_cookies

            self.get_hash()
            return True
            # print r.text
            # if r.status_code==302:
            #    r=requests.get('http://vk.com', headers=headers, cookies=self.vk_cookies, allow_redirects=True)
            #    print r.text
               # if r.status_code==302:
               #     r=requests.get('http://vk.com'+r.headers['location'], headers=headers, cookies=cookie, allow_redirects=False)
               #     print r.url, r.status_code, r.headers, r.cookies.items()
               #     print r.text
               #     cookie = dict(cookie.items() + r.cookies.items())
               #     print '---------------------------------'
        return False

    def get_hash(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset':'windows-1251,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding':'gzip,deflate,sdch',
            'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host': 'vk.com',
            'Referer': self.group_url,
            'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.11 (KHTML, like Gecko) Ubuntu/12.04 Chromium/20.0.1132.47 Chrome/20.0.1132.47 Safari/536.11)'
        }
        r = requests.post(self.group_url, headers=headers, cookies=self.vk_cookies, allow_redirects=True)
        hash_re = re.search(r'"post_hash":"(.+?)",', r.text.encode('utf-8'))
        self.vk_hash = hash_re.group(1)
        hash_re = re.search(r'"timehash":"(.+?)"},', r.text.encode('utf-8'))
        self.vk_timehash = hash_re.group(1)
        # print self.vk_hash
        # print self.vk_timehash

    def wall_post(self, text, attaches=[], logger=None):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset':'windows-1251,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding':'gzip,deflate,sdch',
            'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host': 'vk.com',
            'Referer': self.group_url,
            'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
            'X-Requested-With': "XMLHttpRequest"
        }
        data = dict(
            act='post',
            al='1',
            hash=self.vk_hash,
            message=text,
            to_id=self.group_id,
            type='own',
            official='',
            signed='',
            fixed='1',
            facebook_export="",
            friends_only="",
            status_export="",
        )
        data['from'] = ''
        # data['Message'] = '12412341234'
        nattaches = 0
        for attach in attaches:
            # print data
            if attach['type'] == 'share':
                id_share = self.share_link(attach['url'])
                if id_share:
                    nattaches += 1
                    # data['al_ad'] = 1
                    data['attach%s' % nattaches] = id_share
                    data['attach%s_type' % nattaches] = 'share'
                    data['url'] = attach['url']
                    if 'description' in attach:
                        data['description'] = attach['description']
                    if 'title' in attach:
                        data['title'] = attach['title']

            if attach['type'] == 'photo':
                id_share = self.share_photo(attach['url'], logger)
                if id_share:
                    nattaches += 1
                    # data['al_ad'] = 2
                    data['attach%s' % nattaches] = id_share
                    data['attach%s_type' % nattaches] = 'photo'

        # data['al_ad'] = nattaches

        # print self.vk_cookies
        # print headers
        # print data
        if logger:
            logger.info(data)
        r = requests.post('https://vk.com/al_wall.php', data=data, headers=headers, cookies=self.vk_cookies, allow_redirects=False)
        # print r.text
        if logger:
            logger.info(r.text)

    def share_link(self, url):
        # print 'share link' + url
        try:
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset':'windows-1251,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding':'gzip,deflate,sdch',
                'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
                'Content-Type':'application/x-www-form-urlencoded',
                'Host': 'vk.com',
                'Referer': self.group_url,
                'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.11 (KHTML, like Gecko) Ubuntu/12.04 Chromium/20.0.1132.47 Chrome/20.0.1132.47 Safari/536.11)'
            }
            data =dict(
                hash = self.vk_timehash,
                url = url,
            )
            r = requests.post('http://vk.com/share.php?act=url_attachment', data=data, headers=headers, cookies=self.vk_cookies, allow_redirects=True)
            # print r.text.encode('utf8')
            link_re = re.search(r'"share","(.+?)",', r.text.encode('utf-8'))
            # print link_re
            if not link_re:
                link_re = re.search(r'name="_query" value="(.+?)"', r.text.encode('utf-8'))
                # print link_re.group(1)
                data = {
                    '_query': link_re.group(1)
                }
                r = requests.post('http://vk.com/share.php?act=url_attachment_done', data=data, headers=headers, cookies=self.vk_cookies, allow_redirects=True)
                # print r.text.encode('utf8')
                link_re = re.search(r'"share","(.+?)",', r.text.encode('utf-8'))

            if link_re:
                return link_re.group(1)
        except Exception, err:
            print(traceback.format_exc())
        return False

    def share_photo(self, url, logger=None):
        if logger:
            logger.info('share photo ' + url)
        try:
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset':'windows-1251,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding':'gzip,deflate,sdch',
                'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
                'Content-Type':'application/x-www-form-urlencoded',
                'Host': 'vk.com',
                'Referer': self.group_url,
                'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.11 (KHTML, like Gecko) Ubuntu/12.04 Chromium/20.0.1132.47 Chrome/20.0.1132.47 Safari/536.11)'
            }
            data =dict(
                hash=self.vk_timehash,
                url=url,
                index='1',
                to_mail=''
            )
            if logger:
                logger.info(data)
            # print data
            # print headers
            # print self.vk_cookies
            r = requests.post('http://vk.com/share.php?act=url_attachment', data=data, headers=headers, cookies=self.vk_cookies, allow_redirects=True)
            photo_re = re.search(r'"photo","(.+?)",', r.text.encode('utf-8'))
            # print data
            if logger:
                logger.info(r.text.encode('utf8'))
            # print photo_re.group(1)
            if photo_re:
                return photo_re.group(1)
        except Exception, err:
            print(traceback.format_exc())
        return False

    def post_advert(self, advert, group_url, group_id):
        self.group_url = group_url
        self.group_id = group_id
        self.get_hash()

        comfort_list = advert.comfort_list
        comfort_text = []
        for comfort in comfort_list:
            if comfort[1]:
                comfort_text.append(comfort[2].decode('utf8'))

        attaches = [{'type':'share', 'url': u'http://bazavashdom.ru' + advert.get_absolute_url(),
                     'title': advert.title}]
        for image in advert.images.all()[:5]:
            attaches.append({'type':'photo', 'url': u'http://bazavashdom.ru' + image.image.url})

        tags = []
        if advert.town_id == 1:
            tags.append(u'#москва')
            tags.append(u'#мск')
        if advert.town_id == 2:
            tags.append(u'#петербург')
            tags.append(u'#спб')
        tags.append(u'#' + advert.metro.title.lower().replace(u' ', u'_').replace(u'-', u'_'))
        tags.append(u'#' + Advert.TYPES[advert.adtype].lower())
        tags.append(u'#' + Advert.LIVES[advert.live].lower())
        if advert.adtype == Advert.TYPE_LEASE:
            tags.append(u'#сдам')
        if advert.adtype == Advert.TYPE_SALE:
            tags.append(u'#продам')
        tags.append(u'#собственник')
        tags.append(u'#гсн_рф')

        self.wall_post(u'%s\r\n'
                     u'------------------\r\n'

                     u'Метро: %s\r\n'
                     u'Адрес: %s\r\n'
                     u'Цена: %s р. %s\r\n'
                     u'Площадь: %s м2\r\n'
                     u'Удобства: %s\r\n'
                     u'Город: %s\r\n'
                     u'------------------\r\n'

                     u'Смотреть предложение: %s\r\n'
                     u'------------------\r\n'
                     u'%s' % (advert.title,
                              advert.metro.title,
                              advert.address,
                              advert.price,
                              u'в месяц' if advert.limit==Advert.LIMIT_LONG else u'в сутки',
                              advert.square,
                              u', '.join(comfort_text),
                              advert.town.title,
                              u'http://bazavashdom.ru' + advert.get_absolute_url(),
                              u' '.join(tags)),
                     attaches=attaches)
        advert.vk_imported = True
        advert.save()

    def post_to_group(self, text, images, group_url, group_id, logger=None):
        self.group_url = group_url
        self.group_id = group_id
        self.get_hash()
        self.wall_post(text, attaches=[{'type': 'photo', 'url': img} for img in images], logger=logger)