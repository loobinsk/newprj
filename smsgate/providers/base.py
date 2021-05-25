#-*- coding: utf-8 -*-


class BaseProvider(object):
    options = {}

    def __init__(self, options={}):
        self.options = options

    def send(self, to, message):
        raise Exception('Not impelmented')