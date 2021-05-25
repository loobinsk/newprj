#-*- coding: utf-8 -*-
from .base import BaseProvider
from mail_templated import send_mail


class Provider(BaseProvider):

    def send(self, to, msg):
        send_mail('smsgate/email.html', context={
            'subject': 'Отправлено СМС %s' % to,
            'phone': to,
            'message': msg
        }, recipient_list=[self.options.get('MAILTO')], fail_silently=True)