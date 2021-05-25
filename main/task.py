#-*- coding: utf-8 -*-
from celery.task import task
from celery.task import periodic_task
from datetime import datetime, timedelta
from main.collectors.pitergov import PitergovCollector
from main.collectors.avito import AvitoCollector
from main.collectors.irr import IrrCollector
from main.collectors.chance import ChanceCollector
from main.collectors.vk import VKCollector
from main.collectors.stopagent import StopagentCollector
from main.collectors.kvarnado import KvarnadoCollector
from main.collectors.baza812 import Baza812Collector
from main.collectors.domofond import DomofondCollector
from main.collectors.mult import MultCollector
from main.models import Advert, Town, Company, District, SyncFiles, VKAdvert
from uprofile.models import User
from uimg.models import UserImage
import requests
from mail_templated import send_mail_admins, send_mail
from django.core.cache import cache
from django.conf import settings
from main.autoposting import post_spb, post_msk, post_nsk, post_ekb


@task(queue='default', options={'queue': 'default'})
def find_advert_clients(id):
    advert = Advert.objects.filter(id=id)
    if advert:
        advert[0].find_clients()


# @task(queue='default', options={'queue': 'default'})
# def find_additional_information(id):
#     advert = Advert.objects.filter(id=id)
#     if advert:
#         advert[0].find_metro_distance()
#         advert[0].find_surrounding_objects()


@task(queue='default', options={'queue': 'default'})
def find_search_request_clients(search_request):
    search_request.find_clients()


@task(queue='default', options={'queue': 'default'})
def send_search_request_notice(id):
    from main.models import SearchRequest
    sr = SearchRequest.objects.get(id=id)
    sr.send_client_notice()



@periodic_task(run_every=timedelta(minutes=10), queue='default', options={'queue': 'default'})
def clear_blocked_adverts():
    advert_list = Advert.objects.filter(blocked=True, block_date__lte=datetime.now() - timedelta(minutes=10))
    for advert in advert_list:
        advert.blocked = False
        advert.block_user = None
        advert.block_date = None
        advert.save()
        advert.clear_cache()


@periodic_task(run_every=timedelta(minutes=45), queue='parser', options={'queue': 'parser'})
def avito_collect():
    if not settings.DEBUG:
        lock_id = "avito-collect-lock"
        acquire_lock = lambda: cache.add(lock_id, "true", 60 * 25)
        release_lock = lambda: cache.delete(lock_id)
        if acquire_lock():
            try:
                collector = AvitoCollector()
                collector.collect()
            finally:
                release_lock()


@periodic_task(run_every=timedelta(minutes=2), queue='parser', options={'queue': 'parser'})
def mult_collect():
    if not settings.DEBUG:
        lock_id = "mult-collect-lock"
        acquire_lock = lambda: cache.add(lock_id, "true", 60 * 25)
        release_lock = lambda: cache.delete(lock_id)
        if acquire_lock():
            try:
                collector = MultCollector()
                collector.collect()
            finally:
                release_lock()


@periodic_task(run_every=timedelta(minutes=30), queue='parser', options={'queue': 'parser'})
def irr_collect():
    if not settings.DEBUG:
        lock_id = "irr-collect-lock"
        acquire_lock = lambda: cache.add(lock_id, "true", 60 * 25)
        release_lock = lambda: cache.delete(lock_id)
        if acquire_lock():
            try:
                collector = IrrCollector()
                collector.collect()
            finally:
                release_lock()


@periodic_task(run_every=timedelta(minutes=60), queue='parser', options={'queue': 'parser'})
def chance_collect():
    if not settings.DEBUG:
        lock_id = "chance-collect-lock"
        acquire_lock = lambda: cache.add(lock_id, "true", 60 * 25)
        release_lock = lambda: cache.delete(lock_id)
        if acquire_lock():
            try:
                collector = ChanceCollector()
                collector.collect()
            finally:
                release_lock()


@periodic_task(run_every=timedelta(minutes=60), queue='parser', options={'queue': 'parser'})
def domofond_collect():
    if not settings.DEBUG:
        lock_id = "domofond-collect-lock"
        acquire_lock = lambda: cache.add(lock_id, "true", 60 * 25)
        release_lock = lambda: cache.delete(lock_id)
        if acquire_lock():
            try:
                collector = DomofondCollector()
                collector.collect()
            finally:
                release_lock()


@periodic_task(run_every=timedelta(minutes=10), queue='parser', options={'queue': 'parser'})
def stopagent_collect():
    if not settings.DEBUG:
        lock_id = "stopagent-collect-lock"
        acquire_lock = lambda: cache.add(lock_id, "true", 60 * 10)
        release_lock = lambda: cache.delete(lock_id)
        if acquire_lock():
            try:
                collector = StopagentCollector()
                collector.collect()
            finally:
                release_lock()


@periodic_task(run_every=timedelta(minutes=10), queue='parser', options={'queue': 'parser'})
def kvarnado_collect():
    if not settings.DEBUG:
        lock_id = "kvarnado-collect-lock"
        acquire_lock = lambda: cache.add(lock_id, "true", 60 * 10)
        release_lock = lambda: cache.delete(lock_id)
        if acquire_lock():
            try:
                collector = KvarnadoCollector()
                collector.collect()
            finally:
                release_lock()


@periodic_task(run_every=timedelta(minutes=10), queue='parser', options={'queue': 'parser'})
def baza812_collect():
    if not settings.DEBUG:
        lock_id = "baza812-collect-lock"
        acquire_lock = lambda: cache.add(lock_id, "true", 60 * 10)
        release_lock = lambda: cache.delete(lock_id)
        if acquire_lock():
            try:
                collector = Baza812Collector()
                collector.collect()
            finally:
                release_lock()


@periodic_task(run_every=timedelta(minutes=5), queue='vk', options={'queue': 'vk'})
def vk_collect():
    if not settings.DEBUG:
        lock_id = "vk-collect-lock"
        acquire_lock = lambda: cache.add(lock_id, "true", 60 * 15)
        release_lock = lambda: cache.delete(lock_id)
        if acquire_lock():
            try:
                collector = VKCollector()
                collector.collect()
            finally:
                release_lock()


@periodic_task(run_every=timedelta(hours=24), queue='default', options={'queue': 'default'})
def delete_old_adverts():
    return Advert.objects.filter(moderate_date__lte=datetime.now() - timedelta(days=3), status=Advert.STATUS_MODERATE, not_answer=True).update(status=Advert.STATUS_BLOCKED)


# @periodic_task(run_every=timedelta(minutes=5), queue='default', options={'queue': 'default'})
# def sync_files():
#     if not settings.DEBUG:
#         SyncFiles.sync()


@periodic_task(run_every=timedelta(minutes=20), queue='exams', options={'queue': 'exams'})
def auto_exams_spb():
    examined = 0
    if not settings.DEBUG:
        lock_id = "auto-exams-spb-lock"
        acquire_lock = lambda: cache.add(lock_id, "true", 60 * 30)
        release_lock = lambda: cache.delete(lock_id)
        if acquire_lock():
            try:
                now = datetime.now()
                if now.hour >= 9 and now.hour <= 23:
                    from main.exams.automoder import auto_exams

                    moder = User.objects.get(username='automoder_piter')
                    moder_clients = User.objects.get(username='automoder_piter_client')
                    town = Town.objects.get(slug='sankt-peterburg')

                    examined = auto_exams(town, 'spb', moder, moder_clients)
            finally:
                release_lock()
    return examined


@periodic_task(run_every=timedelta(minutes=20), queue='exams', options={'queue': 'exams'})
def auto_exams_msk():
    examined = 0
    if not settings.DEBUG:
        lock_id = "auto-exams-msk-lock"
        acquire_lock = lambda: cache.add(lock_id, "true", 60 * 30)
        release_lock = lambda: cache.delete(lock_id)
        if acquire_lock():
            try:
                now = datetime.now()
                if now.hour >= 9 and now.hour <= 23:
                    from main.exams.automoder import auto_exams

                    moder = User.objects.get(username='automoder_msk')
                    moder_clients = User.objects.get(username='automoder_msk_client')
                    town = Town.objects.get(slug='moskva')

                    examined = auto_exams(town, 'msk', moder, moder_clients)
            finally:
                release_lock()
    return examined
