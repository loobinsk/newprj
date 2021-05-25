#-*- coding: utf-8 -*-
from main.models import *
from datetime import datetime, timedelta
from django.db.models import Q


def clear_company_adverts():
    """
    Очистка ненужных объявлений
    :return:
    """
    while True:
        adverts = Advert.objects.filter(company__isnull=False)[:50]
        if adverts.count() == 0:
            break
        for advert in adverts:
            print(advert.date, advert.id, advert.status)
            advert.delete()


def clear_adverts():
    """
    Очистка ненужных объявлений
    :return:
    """
    while True:
        d = datetime(2018, 01, 01)
        adverts = Advert.objects.filter(date__lte=d).exclude(status=Advert.STATUS_VIEW).order_by('date')[:50]
        if adverts.count() == 0:
            break
        for advert in adverts:
            print(advert.date, advert.id, advert.status)
            advert.delete()


def clear_companies():
    while True:
        companies = Company.objects.all().exclude(id=258)[:50]
        if not companies:
            break
        for company in companies:
            print(company.id, company.title)
            company.delete()


def clear_users():
    User.admin_objects.filter(id__in=[1, 15413, 15805, 15804, 17412, 17373, 15162, 15432, 17320, 7047, 14081, 7758]).update(site_id=5)
    while True:
        users = User.admin_objects.all().exclude(site_id=5)[:50]
        if not users:
            break
        for user in users:
            print(user.id, user.username)
            user.delete()

def clear_news():
    News.objects.all().exclude(site_id=5).delete()
