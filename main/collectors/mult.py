#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import re
import os
import requests
import traceback
import logging
from datetime import datetime
from time import sleep


from main.collectors.base import Collector
from main.models import Town, Advert, UserImage, Blacklist, Parser
from uprofile.models import User

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium

logger = logging.getLogger('mult')

class MultCollector(Collector):
    domian = 'https://multilisting.su'
    key = '394771d756c737c271a504e10f9a9e38'
    metro_list = None
    district_list = None
    town = None
    parser = None
    cached_ids = []
    cities = {
        1: ['Санкт петербург', 'https://multilisting.su/g-sankt-peterburg/for-rent-residential?advertisement%5Bowner%5D=1&advertisement%5Bprice_from%5D=6000&order=new', 35],
        2: ['Москва', 'https://multilisting.su/g-moskva/for-rent-residential?advertisement%5Bowner%5D=1&advertisement%5Bprice_from%5D=7000&order=new', 35],
        3: ['Новосибирск', 'https://multilisting.su/g-novosibirsk/for-rent-residential?advertisement%5Bowner%5D=1&advertisement%5Bprice_from%5D=4000&order=new', 13],
        4: ['Екатеринбург', 'https://multilisting.su/g-ekaterinburg/for-rent-residential?advertisement%5Bowner%5D=1&advertisement%5Bprice_from%5D=4000&order=new', 13],
    }


    def return_js(self, capcha_code):
        function_js = """window.findRecaptchaClients = function() {{
  // eslint-disable-next-line camelcase
  if (typeof (___grecaptcha_cfg) !== 'undefined') {{
    // eslint-disable-next-line camelcase, no-undef
    return Object.entries(___grecaptcha_cfg.clients).map(([cid, client]) => {{
      const data = {{ id: cid, version: cid >= 10000 ? 'V3' : 'V2' }};
      const objects = Object.entries(client).filter(([_, value]) => value && typeof value === 'object');

      objects.forEach(([toplevelKey, toplevel]) => {{
        const found = Object.entries(toplevel).find(([_, value]) => (
          value && typeof value === 'object' && 'sitekey' in value && 'size' in value
        ));
        if (found) {{
          const [sublevelKey, sublevel] = found;

          data.sitekey = sublevel.sitekey;
          const callbackKey = data.version === 'V2' ? 'callback' : 'promise-callback';
          const callback = sublevel[callbackKey];
          if (!callback) {{
            data.callback = null;
            data.function = null;
          }} else {{
            data.function = callback;
            const keys = [cid, toplevelKey, sublevelKey, callbackKey].map((key) => `['${{key}}']`).join('');
            data.callback = `___grecaptcha_cfg.clients${{keys}}`;
          }}
        }}
      }});
      return data;
    }});
  }}
  return [];
}}; find = window.findRecaptchaClients.call(); eval(find[0]['callback']+'("{0}")');""".format(capcha_code)
        return function_js


    def collect(self):
        logger.info(u'######СТАРТ######')
        print type(u'start')
        for key in xrange(1, 5):
            self.drivers = []
            self.y = 0
            self.city = self.cities.get(key)[0]
            url = self.cities.get(key)[1]
            self.count_card = self.cities.get(key)[2]
            logger.info('Сбор объявлений по городу: {0}'.format(self.city))
            try:
                self.start_func(url)
            except:
                logger.info(traceback.format_exc())
                for i in self.drivers:
                    i.quit()
                continue
        logger.info('######ЗАКОНЧЕНО######')


    def start_func(self, url):
        self.driver = self.get_driver()
        if self.city == 'Санкт петербург':
            self.town = Town.objects.get(id=2)
        elif self.city == 'Москва':
            self.town = Town.admin_objects.get(slug='moskva')
        elif self.city == 'Новосибирск':
            self.town = Town.admin_objects.get(slug='novosibirsk')
        elif self.city == 'Екатеринбург':
            self.town = Town.admin_objects.get(slug='ekaterinburg')
        self.metro_list = self.town.metro_set.all()
        self.district_list = self.town.district_set.all()
        self.parser = Parser.objects.get(title='multilisting')
        self.count = 0
        try:
            self.get_url_on_card(url, adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG)
        # self.get_url_on_card(url)
        except Exception as err:
            logger.info(traceback.format_exc())
        if self.count < self.count_card:
            try:
                url = url + '&page=2'
                self.get_url_on_card(url, adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_LONG)
                # self.get_url_on_card(url)
            except Exception as err:
                logger.info(traceback.format_exc())
        for i in self.drivers:
            i.quit()


    def get_driver(self):
        if int(len(self.drivers)) == int(0):
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(executable_path="%s/chromedriver" % os.getcwd(), options=options)
            driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                })
            """
            })
            # driver.set_window_size(1920, 1080)
            self.drivers.append(driver)
            logger.info(self.drivers)
            logger.info('Хром запустился')
            return driver
        else:
            logger.info('Уже имеется активная эмуляция браузера')


    def get_url_on_card(self, url, adtype, limit, need=Advert.NEED_SALE, set_moderate=False, level=Advert.CHECK_SPAM_LOW):
    # def get_url_on_card(self, url):
        self.url = url
        logger.info(url)
        self.driver.get(self.url)
        cards = self.driver.find_element_by_css_selector('body > div.container > div.result-container-action > ul').find_elements_by_tag_name('li')
        # if self.test_loock():
        for card in cards:
            if int(self.count) >= int(self.count_card):
                break
            try:
                url = card.find_element_by_class_name('header_adv_short').get_attribute('href')
            except selenium.common.exceptions.NoSuchElementException:
                continue
            advert_id = url.split('/')[-1].split('-')[0]
            txt = 'multilisting_' + advert_id
            advert_list = Advert.objects.filter(extnum=txt)
            if advert_list:
                continue
            print url
            logger.info('Получена ссылка на объявление: {0}'.format(txt))

            advert = Advert(town=self.town,
                            adtype = adtype,
                            need = need,
                            status=Advert.STATUS_MODERATE if set_moderate else Advert.STATUS_VIEW,
                            limit=limit,
                            user=User.objects.get(username='admin'),
                            date=datetime.now(),
                            parser=self.parser,
                            extnum='multilisting_' + advert_id)

            try:
                if self.get_metro_and_address(card, advert, adtype, limit, need, set_moderate):
                    continue
            except Exception:
                logger.info(traceback.format_exc())
            try:
                self.click_on_button(card)
            except Exception as err:
                logger.info(traceback.format_exc())
            try:
                self.driver.execute_script("window.open('{0}','_blank');".format(url))
                self.driver.switch_to_window(self.driver.window_handles[1])
            except Exception as err:
                logger.info(traceback.format_exc())

            self.cached_ids.append(advert_id)

            try:
                logger.info('- - - Получение данных из объявления - - -')
                self.request_on_card(advert, adtype, limit, need, set_moderate)
            # self.request_on_card()
            except Exception:
                logger.info(traceback.format_exc())

            self.y += 200

            try:
                self.driver.switch_to_window(self.driver.window_handles[0])
                self.driver.execute_script("window.scrollTo(0, {0})".format(self.y))
            except Exception:
                logger.info(traceback.format_exc())
            self.count += 1
            sleep(35)


    def get_metro_and_address(self, card, advert, adtype, limit, need=Advert.NEED_SALE, set_moderate=False, level=Advert.CHECK_SPAM_LOW):
        text = card.find_element_by_class_name('text-location').text
        # if u'метро' in text.lower().split(', ')[0].split():
            # metro_ = text.split(', ')[0].split('метро ')[-1]
        address = []
        for metro in self.metro_list:
            # if str(metro.title).lower() in str(metro_).lower():
            if str(metro.title).lower() in str(text).lower():
                advert.metro = metro
                text = text.split(', ')
                for t in text:
                    if not str(metro.title).lower() in str(t).lower():
                        address.append(t)
                logger.info('Найдено метро: %s' % metro)
                break
        if not advert.metro:
            logger.info('Метро не найдено')
            return True
        address = ', '.join(address)
        logger.info('Получен длинный адрес: %s' % address)
        advert.address = address.encode('utf-8').strip()
        return False




    def request_on_card(self, advert, adtype, limit, need=Advert.NEED_SALE, set_moderate=False, level=Advert.CHECK_SPAM_LOW):
    # def request_on_card(self):

        imgs_list = []

        # try:
        #     WebDriverWait(self.driver, 10).until(
        #                         EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.container > div > div:nth-child(10) > div.col-md-12.col-lg-7 > div.extendedFotoramaAction.extendedLoadedFotorama.fotorama.fotorama1610064019078 > div > div.fotorama__nav-wrap > div'))
        #                         )
        # except selenium.common.exceptions.TimeoutException:
        #     pass
        # html = self.driver.page_source
        # print(html)
        # html = html.encode('utf-8')
        # logger.info(type(html))
        # soup = BS(html, 'lxml')
        # title = soup.find('h1', attrs={'itemprop': "name"}).text
        title = self.driver.find_element_by_css_selector('body > div.container > div > h1').text
        if (u'Квартира' in title) or (u'Студия' in title) or \
                re.findall(u'(сдаю.{1,5}квартиру)', title.lower(), re.UNICODE | re.IGNORECASE) or \
                re.findall(u'(куплю.{1,5}квартиру)', title.lower(), re.UNICODE | re.IGNORECASE):
            advert.estate = Advert.ESTATE_LIVE
            advert.live = Advert.LIVE_FLAT
            logger.info('Найдена квартира/студия')
        elif u'комната' in title.lower() or u'комнату' in title.lower():
            advert.estate = Advert.ESTATE_LIVE
            advert.live = Advert.LIVE_ROOM
            logger.info('Найдена комната')
        print title

        # price = soup.find('span', {'itemprop': "price"}).text
        price = WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.container > div > div:nth-child(10) > div.apartment-top-container > div.col-md-12.col-lg-5 > span > div.h4'))
                    							).text
        # price = self.driver.find_element_by_css_selector('body > div.container > div > div:nth-child(10) > div.apartment-top-container > div.col-md-12.col-lg-5 > span > div.h4 > span').text
        price = ''.join(price.split()[1:])
        # price = re.search(u'([0-9|\s]+)₽', price)
        advert.price = int(price)
        print price
        logger.info('Найдена цена: {0}'.format(price))

        # ul = soup.find('ul', class_='list-unstyled').find_all('li')
        divs = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div[2]/span/div[3]').find_elements_by_class_name('apartment-desc__item')
        for li in divs:
            print li.text             
            if u'комнат:' in li.text.split():
                room = li.text.split()[-1]
                print room
                advert.rooms = room
                if advert.rooms == 1:
                    advert.live_flat1 = True
                elif advert.rooms == 2:
                    advert.live_flat2 = True
                elif advert.rooms == 3:
                    advert.live_flat3 = True
                elif advert.rooms >= 4:
                    advert.live_flat4 = True
                if not advert.rooms:
                    advert.rooms = 1
                logger.info('Комнатность: %s' % room)

            elif u'площадь:' in li.text.split():
                area = [area for area in li.text if area.isdigit() or area=='.']

                # area = float(li.text.split()[-1])
                area = float('.'.join(''.join(area).split('.')[0:2]))
                print area
                advert.square = area
                logger.info('Найдена площадь: %s м^2' % area)
            elif u'этажей:' in li.text.split():
                level_all = li.text.split()[-1]
                print level_all
                advert.count_floor = int(level_all)
                logger.info('Найдены этажи: %s' % level_all)
            elif u'этаж:' in li.text.split():
                level = li.text.split()[-1]
                print level
                advert.floor = int(level)
                logger.info('Найден этаж: %s' % level)

        try:
        # description = soup.find_all('div', class_='col-xs-12 col-lg-12')[1].find('p').text
            description = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]').text
            if 'описание' in description.lower().split():
                print description
                advert.body = description
                advert.parse(advert.body)
                logger.info('Найдено описание: %s' % description)
        #        if u'хостел' in advert.body.lower():
        #        logger.info('Хостел. Пропуск')
	
        except AttributeError:
            pass

        advert.owner_tel = self.phone.split('//8')[-1]
        logger.info('Найден номер телефона: %s' % self.phone.split('//8')[-1])

        try:
            # imgs = soup.find('div', class_='fotorama__nav-wrap').find_all('div', class_='fotorama__nav__frame fotorama__nav__frame--thumb')

            # imgs = soup.find('div', class_='extendedFotoramaAction').find_all('a')
            imgs = self.driver.find_element_by_class_name('fotorama__nav__shaft').find_elements_by_tag_name('img')
            for img in imgs:
                try:
                    img = img.get_attribute('src').split('?')[0]
                    img = 'medium'.join(img.split('thumb'))
                    print img
                except AttributeError:
                    continue
                # img = 'medium'.join( img.split('?')[0].split('thumb') )
                imgs_list.append(img)
                image = UserImage(user=advert.user)
                if image.load_image_avito_crop(img):
                    image.save()
                    advert.save()
                    advert.images.add(image)
                    advert.save()
            logger.info("Добавлены фотографии")

        except:
            logger.info('Фотографий не обнаружено')
        print imgs_list
        advert.save()
        if advert.status == Advert.STATUS_VIEW:
            advert.find_clients()
        advert.find_metro_distance()
        if advert.check_owner():
            advert.save()
        advert.publish()
        logger.info(advert.id)

        self.driver.execute_script('window.close();')
        print '*'*30 + '\n'*2


    def click_on_button(self, card):
        button = card.find_element_by_class_name('object__show-phone')
        self.driver.execute_script('arguments[0].click();', button)
        xxx = 0
        while True:
            if xxx == 5:
                button = WebDriverWait(self.driver, 7).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.modal.phone_modal_action.in > div > div > div.modal-header > button > span:nth-child(1)'))
                )
                self.driver.execute_script('arguments[0].click();', button)
                break
            try:
                self.phone = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.modal.phone_modal_action.in > div > div > div.modal-body > div > strong > a'))
                ).get_attribute('href')
                # self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/strong/a').get_attribute('href')
                print self.phone
                button = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.modal.phone_modal_action.in > div > div > div.modal-header > button > span:nth-child(1)'))
                )
                self.driver.execute_script('arguments[0].click();', button)
                break
            except:
                try:
                    self.passing_the_captcha()
                except AttributeError:
                    button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.modal.phone_modal_action.in > div > div > div.modal-header > button > span:nth-child(1)'))
                    )
                    self.driver.execute_script('arguments[0].click();', button)
            xxx += 1


    def passing_the_captcha(self):
        try:
            key_capcha = WebDriverWait(self.driver, 70).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'phone_recaptcha_action'))
            ).get_attribute('data-site-key')
            print key_capcha
            logger.info('Обнаружена капча')
            print 'https://rucaptcha.com/in.php?key={0}&method=userrecaptcha&googlekey={1}&pageurl={2}&json=1'.format(self.key, key_capcha, self.url)
            p = requests.post('https://rucaptcha.com/in.php?key={0}&method=userrecaptcha&googlekey={1}&pageurl={2}&json=1'.format(self.key, key_capcha, self.url))
            print p.json()
            json_data = p.json()
            id_capcha = json_data['request']
            while True:
                sleep(10)
                print 'https://rucaptcha.com/res.php?key={0}&action=get&id={1}&json=1'.format(self.key, id_capcha)
                r = requests.get('https://rucaptcha.com/res.php?key={0}&action=get&id={1}&json=1'.format(self.key, id_capcha)).json()
                print r
                if r['status'] == 1:
                    capcha_code = r['request']
                    break
            # js = """document.getElementsByClassName("g-recaptcha-response")[0].style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none;";"""
            js = """document.getElementsByClassName("g-recaptcha-response")[0].innerHTML="{0}";""".format(capcha_code)
            self.driver.execute_script(js)
            sleep(2)
            function_js = self.return_js(capcha_code)
            print function_js
            self.driver.execute_script(function_js)
            # js = """___grecaptcha_cfg.clients[0].V.V.callback("{0}");""".format(capcha_code)
            # js = """___grecaptcha_cfg.clients['0']['o']['o']['callback']("{0}");""".format(capcha_code)
            # try:
            #     self.driver.execute_script(js)
            # except selenium.common.exceptions.JavascriptException:
            #     pass
            logger.info('Ответ на капчу отправлен')
            print 'Отправлено'
        except:
            sleep(80)

    def test_loock(self):
        try:
            # a = WebDriverWait(self.driver, 30).until(
            #                 EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.container > div.result-container-action > ul > li:nth-child(1) > div.col-lg-3.col-md-3.col-sm-12.col-xs-12.object__meta > div > noindex > button'))
            #                 ).location
            a = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/ul/li[2]/div[2]/a'))
            ).location
            b = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/ul/li[2]/div[2]/a'))
            ).size
            try:
                dialog = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'modal-dialog'))
                )
                sleep(100)
                self.driver.find_elements_by_class_name('body').click()
            except:
                pass

            print a
            print b
            return True
        except:
            return False
