# -*- coding: utf-8 -*-
import sys
from django.core import serializers
from django.db.models import get_app, get_models


def migrate(model, size=500, start=0, stop=0):
    if stop == 0:
        count = model.objects.using('mysql').count()
    else:
        count = stop
    print "%s objects in model %s" % (count, model)
    for i in range(start, count, size):
        print i
        original_data = model.objects.using('mysql').all().order_by('-id')[i:i+size]
        original_data_json = serializers.serialize("json", original_data)
        new_data = serializers.deserialize("json", original_data_json,
                                           using='default')
        for n in new_data:
            n.save(using='default')

        del original_data
        del original_data_json
        del new_data


def migrate_app(app_name):
    app = get_app(app_name)
    for model in get_models(app):
        if model._meta.verbose_name != u'Объявление':
            print model._meta.verbose_name
            migrate(model)
