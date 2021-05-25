#-*- coding: utf-8 -*-
from .base import BaseProvider
from xml.dom import minidom
from lxml import etree
import requests


SERVER_URL = '95.213.129.83'


class AlohaErrorException(Exception):
    pass


class Provider(BaseProvider):

    def send(self, to, msg):
        impl = minidom.getDOMImplementation()
        doc = impl.createDocument(None, 'request', None)

        security = doc.createElement('security')
        doc.documentElement.appendChild(security)

        login = doc.createElement('login')
        login.setAttribute('value', self.options.get('LOGIN', ''))
        security.appendChild(login)

        password = doc.createElement('password')
        password.setAttribute('value', self.options.get('PASSWORD', ''))
        security.appendChild(password)

        message = doc.createElement('message')
        message.setAttribute('type', 'sms')
        doc.documentElement.appendChild(message)

        sender = doc.createElement('sender')
        sender.appendChild(doc.createTextNode(self.options.get('SENDER', '')))
        message.appendChild(sender)

        text = doc.createElement('text')
        text.appendChild(doc.createTextNode(msg))
        message.appendChild(text)

        abonent = doc.createElement('abonent')
        abonent.setAttribute('phone', to)
        abonent.setAttribute('number_sms', '1')
        message.appendChild(abonent)

        headers = {'Content-type': 'text/xml; charset=utf-8'}
        r = requests.post('http://%s/xml/' % SERVER_URL, data=doc.toxml(encoding='utf8'), headers=headers)
        response = etree.fromstring(r.text.encode('utf8'))

        errors = response.xpath(u'//response/error')
        if errors:
            raise AlohaErrorException(errors[0].text)

        informations = response.xpath(u'//response/information')
        if informations:
            if informations[0].text == u'send':
                return True
            else:
                raise AlohaErrorException(informations[0].text)

        return True
