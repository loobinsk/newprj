#-*- coding: utf-8 -*-
from main.models import Town
from django.conf import settings
from gsnru import moder_urls
from datetime import datetime, timedelta
from main.models import Referral, ReferralReferer
from django.contrib.sites.models import Site
from django.db import connection, connections, OperationalError
from django.core.cache import cache


class DbTestMiddleware(object):
    def process_request(self, request):
        if not settings.ENABLE_RESERVE_DB:
            enable_reserve = cache.get('enable_reserve_db', False)
            if not enable_reserve:
                try:
                    cursor = connections['default'].cursor()
                except OperationalError:
                    cache.set('enable_reserve_db', True, 60)
            settings.ENABLE_RESERVE_DB = enable_reserve


class TownMiddleware(object):
    def process_request(self, request):
        town = None
        if request.is_client and request.user.is_authenticated() and not request.user.is_staff:
            if request.is_moder:
                # если модеоская панел
                town = request.user.town
            else:
                # если агентская панель
                if request.user.company:
                    town = request.user.company.town
        else:
            # если публичная часть
            town_id = request.COOKIES.get('town')
            if town_id:
                town = Town.objects.get(id=town_id)
        if not town:
            town_list = Town.objects.filter(id=2)
            if town_list:
                town = town_list[0]
            else:
                town = None
        request.current_town = town


class ModerMiddleware(object):
    def process_request(self, request):
        host = request.get_host()
        if host == settings.MODER_PANEL_DOMAIN:
            request.urlconf = moder_urls
            request.is_moder = True
        else:
            request.is_moder = False

        if request.path.startswith('/client'):
            request.is_client = True
        else:
            request.is_client = False

class ReferralMiddleware(object):
    def process_request(self, request):
        request.referral = None
        if request.COOKIES.get('referral'):
            referral_list = Referral.objects.filter(site=Site.objects.get_current(), id=request.COOKIES.get('referral'))
            if referral_list:
                if referral_list[0].user != request.user:
                    request.referral = referral_list[0]

    def process_response(self, request, response):
        ref = request.GET.get('ref')
        if ref:
            referral_list = Referral.objects.filter(site=Site.objects.get_current(), code=ref)
            if referral_list:
                referral = referral_list[0]
                if referral.user != request.user:
                    max_age = 365 * 24 * 60 * 60
                    expires = datetime.strftime(datetime.now() + timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
                    response.set_cookie('referral', referral.id, max_age=max_age, expires=expires)
                    referral.conversion += 1
                    referral.save()
                    if 'HTTP_REFERER' in request.META:
                        referer = ReferralReferer(referral=referral, referer=request.META['HTTP_REFERER'][:250])
                        referer.save()
                    else:
                        referer = ReferralReferer(referral=referral, referer='')
                        referer.save()
        return response