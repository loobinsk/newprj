#-*- coding: utf-8 -*-
from celery.task import task
from celery.task import periodic_task
from datetime import datetime, timedelta
from main.models import Advert, Town
from django.core.cache import cache
from django.conf import settings
from main.vk import VK
import time
from lxml import etree
import traceback
import logging
from django.db.models import Q, Count
from main.templatetags.main_tags import fmt_price
from django.conf import settings
import os
from django.contrib.contenttypes.models import ContentType
from vkposting.models import Canal
from django.template.defaultfilters import truncatewords, truncatechars



@periodic_task(run_every=timedelta(hours=1), queue='post', options={'queue':'post'})
def post_spb():
    now = datetime.now()
    if now.hour >= 9 and now.hour<=23:
        ctype = ContentType.objects.get(model='advert')
        canal = Canal.objects.get(code='spb')
        adverts = Advert.objects.no_cache().raw('SELECT main_advert.* FROM main_advert '
                                    'left join vkposting_post on main_advert.id=vkposting_post.object_id and vkposting_post.content_type_id=%s and vkposting_post.canal_id=%s '
                                    'where vkposting_post.id IS NULL and '
                                    'main_advert.limit=\'l\' and '
                                    'main_advert.town_id=2 and '
                                    'main_advert.status=\'v\' and '
                                    'main_advert.need=\'s\' and '
                                    'main_advert.company_id IS NULL and '
                                    'main_advert.adtype=\'L\' and '
                                    'main_advert.estate=\'F\' and '
                                    'main_advert.price > 0 and '
                                    'main_advert.metro_id IS NOT NULL and '
                                    '(select count(*) from main_advert_images where main_advert.id=main_advert_images.advert_id) > 0'
                                    'ORDER BY main_advert.date desc LIMIT 1',
                                     [ctype.id, canal.id])
        if adverts:
            advert = adverts[0]
            title = u''
            if advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_ROOM:
                    title = u'комната'
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and advert.rooms:
                title = u'%s комнатная квартира' % advert.rooms
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and not advert.rooms:
                title = u'квартира'
            return canal.post({
                    'title': title,
                    'metro': advert.metro.title,
                    'address': advert.address,
                    'price': advert.price,
                    'url': 'bazavashdom.ru/id%s' % advert.id
                },
                images=[os.path.join(settings.BASE_DIR, image.image.path) for image in advert.images.all()[:10]],
                template='vashdom/posting/spb.txt',
                content_object=advert
            )


@periodic_task(run_every=timedelta(hours=1), queue='post', options={'queue':'post'})
def post_spb2():
    now = datetime.now()
    if now.hour >= 9 and now.hour<=23:
        ctype = ContentType.objects.get(model='advert')
        canal = Canal.objects.get(code='spb2')
        adverts = Advert.objects.no_cache().raw('SELECT main_advert.* FROM main_advert '
                                    'left join vkposting_post on main_advert.id=vkposting_post.object_id and vkposting_post.content_type_id=%s and vkposting_post.canal_id=%s '
                                    'where vkposting_post.id IS NULL and '
                                    'main_advert.limit=\'l\' and '
                                    'main_advert.town_id=2 and '
                                    'main_advert.status=\'v\' and '
                                    'main_advert.need=\'s\' and '
                                    'main_advert.company_id IS NULL and '
                                    'main_advert.adtype=\'L\' and '
                                    'main_advert.estate=\'F\' and '
                                    'main_advert.price > 0 and '
                                    'main_advert.metro_id IS NOT NULL and '
                                    '(select count(*) from main_advert_images where main_advert.id=main_advert_images.advert_id) > 0'
                                    'ORDER BY main_advert.date desc LIMIT 1',
                                     [ctype.id, canal.id])
        if adverts:
            advert = adverts[0]
            title = u''
            if advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_ROOM:
                    title = u'комната'
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and advert.rooms:
                title = u'%s комнатная квартира' % advert.rooms
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and not advert.rooms:
                title = u'квартира'
            return canal.post({
                    'title': title,
                    'metro': advert.metro.title,
                    'address': advert.address,
                    'price': advert.price,
                    'url': 'bazavashdom.ru/id%s' % advert.id
                },
                images=[os.path.join(settings.BASE_DIR, image.image.path) for image in advert.images.all()[:10]],
                template='vashdom/posting/spb2.txt',
                content_object=advert
            )


@periodic_task(run_every=timedelta(hours=1), queue='post', options={'queue':'post'})
def post_twitter_spb():
    now = datetime.now()
    if now.hour >= 9 and now.hour<=23:
        ctype = ContentType.objects.get(model='advert')
        canal = Canal.objects.get(code='tw_spb')
        adverts = Advert.objects.no_cache().raw('SELECT main_advert.* FROM main_advert '
                                    'left join vkposting_post on main_advert.id=vkposting_post.object_id and vkposting_post.content_type_id=%s and vkposting_post.canal_id=%s '
                                    'where vkposting_post.id IS NULL and '
                                    'main_advert.limit=\'l\' and '
                                    'main_advert.town_id=2 and '
                                    'main_advert.status=\'v\' and '
                                    'main_advert.need=\'s\' and '
                                    'main_advert.company_id IS NULL and '
                                    'main_advert.adtype=\'L\' and '
                                    'main_advert.estate=\'F\' and '
                                    'main_advert.price > 0 and '
                                    'main_advert.metro_id IS NOT NULL and '
                                    '(select count(*) from main_advert_images where main_advert.id=main_advert_images.advert_id) > 0'
                                    'ORDER BY main_advert.date desc LIMIT 1',
                                     [ctype.id, canal.id])
        if adverts:
            advert = adverts[0]
            title = u'#Сдается #безпосредников '
            if advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_ROOM:
                    title += u' комната'
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and advert.rooms:
                title += u' %s комнатная квартира' % advert.rooms
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and not advert.rooms:
                title += u' квартира'
            if advert.metro:
                title += u', м. %s' % advert.metro.title
            if advert.address:
                title += u', %s' % advert.address
            if advert.price:
                title += u', %sр.' % advert.price
            return canal.post({
                    'text': truncatechars(title, 80),
                    'tags': '#базавашдом',
                    'url': 'bazavashdom.ru/id%s' % advert.id
                },
                images=[os.path.join(settings.BASE_DIR, image.image.path) for image in advert.images.all()[:10]],
                template='vashdom/posting/tw_spb.txt',
                content_object=advert
            )


@periodic_task(run_every=timedelta(hours=1), queue='post', options={'queue':'post'})
def post_msk():
    now = datetime.now()
    if now.hour >= 9 and now.hour<=23:
        ctype = ContentType.objects.get(model='advert')
        canal = Canal.objects.get(code='msk')
        adverts = Advert.objects.no_cache().raw('SELECT main_advert.* FROM main_advert '
                                    'left join vkposting_post on main_advert.id=vkposting_post.object_id and vkposting_post.content_type_id=%s and vkposting_post.canal_id=%s '
                                    'where vkposting_post.id IS NULL and '
                                    'main_advert.limit=\'l\' and '
                                    'main_advert.town_id=1 and '
                                    'main_advert.status=\'v\' and '
                                    'main_advert.need=\'s\' and '
                                    'main_advert.company_id IS NULL and '
                                    'main_advert.adtype=\'L\' and '
                                    'main_advert.estate=\'F\' and '
                                    'main_advert.price > 0 and '
                                    'main_advert.metro_id IS NOT NULL and '
                                    '(select count(*) from main_advert_images where main_advert.id=main_advert_images.advert_id) > 0'
                                    'ORDER BY main_advert.date desc LIMIT 1',
                                     [ctype.id, canal.id])
        if adverts:
            advert = adverts[0]
            title = u''
            if advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_ROOM:
                    title = u'комната'
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and advert.rooms:
                title = u'%s комнатная квартира' % advert.rooms
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and not advert.rooms:
                title = u'квартира'
            return canal.post({
                    'title': title,
                    'metro': advert.metro.title,
                    'address': advert.address,
                    'price': advert.price,
                    'url': 'bazavashdom.ru/id%s' % advert.id
                },
                images=[os.path.join(settings.BASE_DIR, image.image.path) for image in advert.images.all()[:10]],
                template='vashdom/posting/msk.txt',
                content_object=advert
            )


@periodic_task(run_every=timedelta(hours=1), queue='post', options={'queue':'post'})
def post_msk2():
    now = datetime.now()
    if now.hour >= 9 and now.hour<=23:
        ctype = ContentType.objects.get(model='advert')
        canal = Canal.objects.get(code='msk2')
        adverts = Advert.objects.no_cache().raw('SELECT main_advert.* FROM main_advert '
                                    'left join vkposting_post on main_advert.id=vkposting_post.object_id and vkposting_post.content_type_id=%s and vkposting_post.canal_id=%s '
                                    'where vkposting_post.id IS NULL and '
                                    'main_advert.limit=\'l\' and '
                                    'main_advert.town_id=1 and '
                                    'main_advert.status=\'v\' and '
                                    'main_advert.need=\'s\' and '
                                    'main_advert.company_id IS NULL and '
                                    'main_advert.adtype=\'L\' and '
                                    'main_advert.estate=\'F\' and '
                                    'main_advert.price > 0 and '
                                    'main_advert.metro_id IS NOT NULL and '
                                    '(select count(*) from main_advert_images where main_advert.id=main_advert_images.advert_id) > 0'
                                    'ORDER BY main_advert.date desc LIMIT 1',
                                     [ctype.id, canal.id])
        if adverts:
            advert = adverts[0]
            title = u''
            if advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_ROOM:
                    title = u'комната'
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and advert.rooms:
                title = u'%s комнатная квартира' % advert.rooms
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and not advert.rooms:
                title = u'квартира'
            return canal.post({
                    'title': title,
                    'metro': advert.metro.title,
                    'address': advert.address,
                    'price': advert.price,
                    'url': 'bazavashdom.ru/id%s' % advert.id
                },
                images=[os.path.join(settings.BASE_DIR, image.image.path) for image in advert.images.all()[:10]],
                template='vashdom/posting/msk2.txt',
                content_object=advert
            )


@periodic_task(run_every=timedelta(hours=1), queue='post', options={'queue':'post'})
def post_twitter_msk():
    now = datetime.now()
    if now.hour >= 9 and now.hour<=23:
        ctype = ContentType.objects.get(model='advert')
        canal = Canal.objects.get(code='tw_msk')
        adverts = Advert.objects.no_cache().raw('SELECT main_advert.* FROM main_advert '
                                    'left join vkposting_post on main_advert.id=vkposting_post.object_id and vkposting_post.content_type_id=%s and vkposting_post.canal_id=%s '
                                    'where vkposting_post.id IS NULL and '
                                    'main_advert.limit=\'l\' and '
                                    'main_advert.town_id=1 and '
                                    'main_advert.status=\'v\' and '
                                    'main_advert.need=\'s\' and '
                                    'main_advert.company_id IS NULL and '
                                    'main_advert.adtype=\'L\' and '
                                    'main_advert.estate=\'F\' and '
                                    'main_advert.price > 0 and '
                                    'main_advert.metro_id IS NOT NULL and '
                                    '(select count(*) from main_advert_images where main_advert.id=main_advert_images.advert_id) > 0'
                                    'ORDER BY main_advert.date desc LIMIT 1',
                                     [ctype.id, canal.id])
        if adverts:
            advert = adverts[0]
            title = u'#Сдается #безпосредников '
            if advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_ROOM:
                    title += u' комната'
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and advert.rooms:
                title += u' %s комнатная квартира' % advert.rooms
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and not advert.rooms:
                title += u' квартира'
            if advert.metro:
                title += u', м. %s' % advert.metro.title
            if advert.address:
                title += u', %s' % advert.address
            if advert.price:
                title += u', %sр.' % advert.price
            return canal.post({
                    'text': truncatechars(title, 80),
                    'tags': '#базавашдом',
                    'url': 'bazavashdom.ru/id%s' % advert.id
                },
                images=[os.path.join(settings.BASE_DIR, image.image.path) for image in advert.images.all()[:10]],
                template='vashdom/posting/tw_msk.txt',
                content_object=advert
            )


@periodic_task(run_every=timedelta(hours=1), queue='post', options={'queue':'post'})
def post_nsk():
    now = datetime.now()
    if now.hour >= 6 and now.hour<=19:
        ctype = ContentType.objects.get(model='advert')
        canal = Canal.objects.get(code='nsk')
        adverts = Advert.objects.no_cache().raw('SELECT main_advert.* FROM main_advert '
                                    'left join vkposting_post on main_advert.id=vkposting_post.object_id and vkposting_post.content_type_id=%s and vkposting_post.canal_id=%s '
                                    'where vkposting_post.id IS NULL and '
                                    'main_advert.limit=\'l\' and '
                                    'main_advert.town_id=10 and '
                                    'main_advert.status=\'v\' and '
                                    'main_advert.need=\'s\' and '
                                    'main_advert.company_id IS NULL and '
                                    'main_advert.adtype=\'L\' and '
                                    'main_advert.estate=\'F\' and '
                                    'main_advert.price > 0 and '
                                    'main_advert.metro_id IS NOT NULL and '
                                    '(select count(*) from main_advert_images where main_advert.id=main_advert_images.advert_id) > 0'
                                    'ORDER BY main_advert.date desc LIMIT 1',
                                     [ctype.id, canal.id])
        if adverts:
            advert = adverts[0]
            title = u''
            if advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_ROOM:
                    title = u'комната'
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and advert.rooms:
                title = u'%s комнатная квартира' % advert.rooms
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and not advert.rooms:
                title = u'квартира'
            return canal.post({
                    'title': title,
                    'metro': advert.metro.title,
                    'address': advert.address,
                    'price': advert.price,
                    'url': 'bazavashdom.ru/id%s' % advert.id
                },
                images=[os.path.join(settings.BASE_DIR, image.image.path) for image in advert.images.all()[:10]],
                template='vashdom/posting/nsk.txt',
                content_object=advert
            )


@periodic_task(run_every=timedelta(hours=1), queue='post', options={'queue':'post'})
def post_twitter_nsk():
    now = datetime.now()
    if now.hour >= 9 and now.hour<=23:
        ctype = ContentType.objects.get(model='advert')
        canal = Canal.objects.get(code='tw_nsk')
        adverts = Advert.objects.no_cache().raw('SELECT main_advert.* FROM main_advert '
                                    'left join vkposting_post on main_advert.id=vkposting_post.object_id and vkposting_post.content_type_id=%s and vkposting_post.canal_id=%s '
                                    'where vkposting_post.id IS NULL and '
                                    'main_advert.limit=\'l\' and '
                                    'main_advert.town_id=10 and '
                                    'main_advert.status=\'v\' and '
                                    'main_advert.need=\'s\' and '
                                    'main_advert.company_id IS NULL and '
                                    'main_advert.adtype=\'L\' and '
                                    'main_advert.estate=\'F\' and '
                                    'main_advert.price > 0 and '
                                    'main_advert.metro_id IS NOT NULL and '
                                    '(select count(*) from main_advert_images where main_advert.id=main_advert_images.advert_id) > 0'
                                    'ORDER BY main_advert.date desc LIMIT 1',
                                     [ctype.id, canal.id])
        if adverts:
            advert = adverts[0]
            title = u'#Сдается #безпосредников '
            if advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_ROOM:
                    title += u' комната'
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and advert.rooms:
                title += u' %s комнатная квартира' % advert.rooms
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and not advert.rooms:
                title += u' квартира'
            if advert.metro:
                title += u', м. %s' % advert.metro.title
            if advert.address:
                title += u', %s' % advert.address
            if advert.price:
                title += u', %sр.' % advert.price
            return canal.post({
                    'text': truncatechars(title, 80),
                    'tags': '#базавашдом',
                    'url': 'bazavashdom.ru/id%s' % advert.id
                },
                images=[os.path.join(settings.BASE_DIR, image.image.path) for image in advert.images.all()[:10]],
                template='vashdom/posting/tw_nsk.txt',
                content_object=advert
            )


@periodic_task(run_every=timedelta(hours=1), queue='post', options={'queue':'post'})
def post_ekb():
    now = datetime.now()
    if now.hour >= 6 and now.hour<=19:
        ctype = ContentType.objects.get(model='advert')
        canal = Canal.objects.get(code='ekb')
        adverts = Advert.objects.no_cache().raw('SELECT main_advert.* FROM main_advert '
                                    'left join vkposting_post on main_advert.id=vkposting_post.object_id and vkposting_post.content_type_id=%s and vkposting_post.canal_id=%s '
                                    'where vkposting_post.id IS NULL and '
                                    'main_advert.limit=\'l\' and '
                                    'main_advert.town_id=6 and '
                                    'main_advert.status=\'v\' and '
                                    'main_advert.need=\'s\' and '
                                    'main_advert.company_id IS NULL and '
                                    'main_advert.adtype=\'L\' and '
                                    'main_advert.estate=\'F\' and '
                                    'main_advert.price > 0 and '
                                    'main_advert.metro_id IS NOT NULL and '
                                    '(select count(*) from main_advert_images where main_advert.id=main_advert_images.advert_id) > 0'
                                    'ORDER BY main_advert.date desc LIMIT 1',
                                     [ctype.id, canal.id])
        if adverts:
            advert = adverts[0]
            title = u''
            if advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_ROOM:
                    title = u'комната'
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and advert.rooms:
                title = u'%s комнатная квартира' % advert.rooms
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and not advert.rooms:
                title = u'квартира'
            return canal.post({
                    'title': title,
                    'metro': advert.metro.title,
                    'address': advert.address,
                    'price': advert.price,
                    'url': 'bazavashdom.ru/id%s' % advert.id
                },
                images=[os.path.join(settings.BASE_DIR, image.image.path) for image in advert.images.all()[:10]],
                template='vashdom/posting/ekb.txt',
                content_object=advert
            )


@periodic_task(run_every=timedelta(hours=1), queue='post', options={'queue':'post'})
def post_twitter_ekb():
    now = datetime.now()
    if now.hour >= 9 and now.hour<=23:
        ctype = ContentType.objects.get(model='advert')
        canal = Canal.objects.get(code='tw_ekb')
        adverts = Advert.objects.no_cache().raw('SELECT main_advert.* FROM main_advert '
                                    'left join vkposting_post on main_advert.id=vkposting_post.object_id and vkposting_post.content_type_id=%s and vkposting_post.canal_id=%s '
                                    'where vkposting_post.id IS NULL and '
                                    'main_advert.limit=\'l\' and '
                                    'main_advert.town_id=6 and '
                                    'main_advert.status=\'v\' and '
                                    'main_advert.need=\'s\' and '
                                    'main_advert.company_id IS NULL and '
                                    'main_advert.adtype=\'L\' and '
                                    'main_advert.estate=\'F\' and '
                                    'main_advert.price > 0 and '
                                    'main_advert.metro_id IS NOT NULL and '
                                    '(select count(*) from main_advert_images where main_advert.id=main_advert_images.advert_id) > 0'
                                    'ORDER BY main_advert.date desc LIMIT 1',
                                     [ctype.id, canal.id])
        if adverts:
            advert = adverts[0]
            title = u'#Сдается #безпосредников '
            if advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_ROOM:
                    title += u' комната'
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and advert.rooms:
                title += u' %s комнатная квартира' % advert.rooms
            elif advert.estate == Advert.ESTATE_LIVE and advert.live == Advert.LIVE_FLAT and not advert.rooms:
                title += u' квартира'
            if advert.metro:
                title += u', м. %s' % advert.metro.title
            if advert.address:
                title += u', %s' % advert.address
            if advert.price:
                title += u', %sр.' % advert.price
            return canal.post({
                    'text': truncatechars(title, 80),
                    'tags': '#базавашдом',
                    'url': 'bazavashdom.ru/id%s' % advert.id
                },
                images=[os.path.join(settings.BASE_DIR, image.image.path) for image in advert.images.all()[:10]],
                template='vashdom/posting/tw_ekb.txt',
                content_object=advert
            )