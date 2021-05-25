# -*- coding: utf-8 -*-
from main.exams.base import BaseExam
from main.models.general import get_tel_list
from django.core.cache import cache
import requests
import re
import json


class ListAgentExam(BaseExam):
    domain = 'http://smartagent.ru'
    auth_path = 'http://smartagent.ru/auth/ajax'
    test_path = 'http://smartagent.ru/search/all-objects/page/0'
    test_client_path = 'http://smartagent.ru/search/all-clients/page/0'
    cookies = {}
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0",
    }
    groups = {
        'spb':[{
            'id': 'spb1',
            'username': '+7 (952) 242-48-12',
            'password': '4354311143',
            'compid': '2279'
        }],
        'msk': [{
            'id': 'msk1',
            'username': u'+7 (915) 102-55-22',
            'password': u'49744',
            'compid': ''
        }]
    }
    group_id = 'spb'
    account = None

    def __init__(self, group_id='spb'):
        super(BaseExam, self).__init__()
        self.group_id = group_id
        self.account = self.groups[self.group_id][0]
        self.cookies = cache.get('listagent_cookies_%s' % self.account['id'], {})

    def _login(self):
        # print 'логинимся'
        r = requests.get(self.domain, cookies=self.cookies, headers=self.headers)
        self.cookies.update(r.cookies)

        data = {
            'login': self.account['username'],
            'password': self.account['password'],
        }
        if self.account['compid']:
            data['compid'] = self.account['compid']
        r = requests.post(self.auth_path, data=data, headers=self.headers, cookies=self.cookies)
        self.cookies.update(r.cookies)
        cache.set('listagent_cookies_%s' % self.account['id'], self.cookies)

    def _test_login(self):
        r = requests.get(self.domain, headers=self.headers, cookies=self.cookies, allow_redirects=False)
        return u'/auth/logout' in r.text

    def test(self, tel_list):
        if not self._test_login():
            self._login()
            if not self._test_login():
                # print 'не удается залогиниться'
                return ListAgentExam.RESULT_UNDEFINED

        result = ListAgentExam.RESULT_UNDEFINED
        for tel in get_tel_list(tel_list):
            data = {
                'phone': tel
            }
            r = requests.post(self.test_path, data=data, headers=self.headers, cookies=self.cookies)
            answer = json.loads(r.text)
            if u'params' in answer:
                if u'agentPhone' in answer[u'params']:
                    if answer[u'params'][u'agentPhone']:
                        result = ListAgentExam.RESULT_AGENT
                if u'isObject' in answer[u'params'] and result == ListAgentExam.RESULT_UNDEFINED:
                    if answer[u'params'][u'isObject']:
                        if u'Не соответствует качеству!' in answer['payload']:
                            result = ListAgentExam.RESULT_UNDEFINED
                        if u'type' in answer[u'params'] and answer[u'params'][u'type'] == u'board':
                            result = ListAgentExam.RESULT_OWNER
        return result

    def test_client(self, tel_list):
        if not self._test_login():
            self._login()
            if not self._test_login():
                # print 'не удается залогиниться'
                return ListAgentExam.RESULT_UNDEFINED

        result = ListAgentExam.RESULT_UNDEFINED
        for tel in get_tel_list(tel_list):
            data = {
                'phone': tel
            }
            r = requests.post(self.test_client_path, data=data, headers=self.headers, cookies=self.cookies)
            answer = json.loads(r.text)
            if u'params' in answer:
                if u'agentPhone' in answer[u'params']:
                    if answer[u'params'][u'agentPhone']:
                        result = ListAgentExam.RESULT_AGENT
                if u'isObject' in answer[u'params'] and result == ListAgentExam.RESULT_UNDEFINED:
                    # if answer[u'params'][u'isObject']:
                    if u'type' in answer[u'params'] and answer[u'params'][u'type'] == u'board':
                        if u'Не соответствует качеству!' in answer['payload']:
                            result = ListAgentExam.RESULT_UNDEFINED
                        else:
                            result = ListAgentExam.RESULT_OWNER
        return result