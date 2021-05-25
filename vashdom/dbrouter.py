# -*- coding: utf-8 -*-
from django.conf import settings


class MasterSlaveRouter:
    def db_for_read(self, model, **hints):
        if settings.ENABLE_RESERVE_DB:
            return 'master'
        else:
            return 'default'

    def db_for_write(self, model, **hints):
        return 'master'

    def allow_relation(self, obj1, obj2, **hints):
        return True