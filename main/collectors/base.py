#-*- coding: utf-8 -*-
import requests


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
