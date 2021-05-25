#-*- coding: utf-8 -*-
from django.conf import settings


class SmsGate(object):

    options = {}

    def __init__(self, options={}):
        if options:
            self.options = options
        else:
            self.options = getattr(settings, 'SMSGATE', {})

    def send(self, to, message, provider=None):
        if self.options.get('DEBUG', True):
            provider = 'EMAIL'
        elif not provider:
            provider = self.options.get('DEFAULT_GATE', '')
        module = __import__('smsgate.providers.%s' % provider.lower(), fromlist=[''])
        p = module.Provider(options=self.options.get(provider, {}))
        return p.send(to, message)