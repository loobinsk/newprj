#-*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.core import serializers
from main.models import Advert
from datetime import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = serializers.serialize("json", Advert.objects.filter(date__gte=datetime(2020, 1, 1)).all())
        out = open("2020.01.01.json", "w")
        out.write(data)
        out.close()
