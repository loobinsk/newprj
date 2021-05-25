# -*- coding: utf-8 -*-
from celery.canvas import group
from django.conf import settings
from django.core.cache import cache
from datetime import datetime, timedelta
from uprofile.models import User
from main.models import Advert, Town, Company, District, SyncFiles


def auto_exams(town,  group, moder, moder_clients):
    from main.exams.listagent import ListAgentExam
    from main.models import Blacklist
    from django.db.models import Q
    import time
    import logging
    import traceback

    examined = 0

    cached_ids = cache.get('auto-exams-ids-%s' % town.id, {})
    if not isinstance(cached_ids, dict):
        cached_ids = {}

    logger = logging.getLogger('autoexam')

    exam = ListAgentExam(group_id=group)

    exclude_ids = []
    for id, count in cached_ids.items():
        if count in [1, 2]:
            exclude_ids.append(id)

    # объявления от собственников
    advert_list = Advert.objects.filter(status=Advert.STATUS_MODERATE,
                                        town=town,
                                        company=None,
                                        not_answer=False,
                                        need=Advert.NEED_SALE,
                                        date__lte=datetime.now()-timedelta(hours=1),
                                        date__gte=datetime.now()-timedelta(hours=24))\
        .exclude(Q(blocked=True) | Q(id__in=exclude_ids))\
        .order_by('-date')
    for advert in advert_list:
        try:
            logger.info(u'%s %s' % (advert.id, advert.owner_tel))
            if advert.id not in cached_ids:
                cached_ids[advert.id] = 0
            if cached_ids[advert.id] == 3:
                cached_ids[advert.id] = 0
            if cached_ids[advert.id] == 0:
                exam_result = exam.test(advert.owner_tel)
                logger.info('result %s' % exam_result)
                if exam_result == ListAgentExam.RESULT_AGENT:
                    Blacklist.add_tel(advert.owner_tel, desc='Агент с сайта ListAgent', town=town, tag='listagent')
                    advert.status = Advert.STATUS_BLOCKED
                    advert.moderator = moder
                    advert.moderate_date = datetime.now()
                    advert.save()
                    examined += 1
                elif exam_result == ListAgentExam.RESULT_OWNER:
                    advert.status = Advert.STATUS_VIEW
                    advert.moderator = moder
                    advert.moderate_date = datetime.now()
                    advert.date = datetime.now()
                    advert.save()
                    advert.publish()
                    advert.find_clients()
                    examined += 1
                time.sleep(10)
            cached_ids[advert.id] = cached_ids[advert.id] + 1
        except Exception, err:
            logger.info(traceback.format_exc())

    # объявления от клиентов
    advert_list = Advert.objects.filter(status=Advert.STATUS_MODERATE,
                                        town=town,
                                        company=None,
                                        not_answer=False,
                                        need=Advert.NEED_DEMAND,
                                        date__lte=datetime.now()-timedelta(hours=0),
                                        date__gte=datetime.now()-timedelta(hours=18))\
        .exclude(Q(blocked=True) | Q(id__in=exclude_ids))\
        .order_by('-date')
    for advert in advert_list:
        try:
            logger.info(u'%s %s' % (advert.id, advert.owner_tel))
            if advert.id not in cached_ids:
                cached_ids[advert.id] = 0
            if cached_ids[advert.id] == 3:
                cached_ids[advert.id] = 0
            if cached_ids[advert.id] == 0:
                exam_result = exam.test_client(advert.owner_tel)
                logger.info('result %s' % exam_result)
                if exam_result == ListAgentExam.RESULT_AGENT:
                    Blacklist.add_tel(advert.owner_tel, desc='Агент с сайта ListAgent', town=town, tag='listagent')
                    advert.status = Advert.STATUS_BLOCKED
                    advert.moderator = moder_clients
                    advert.moderate_date = datetime.now()
                    advert.save()
                    examined += 1
                elif exam_result == ListAgentExam.RESULT_OWNER:
                    advert.status = Advert.STATUS_VIEW
                    advert.moderator = moder_clients
                    advert.moderate_date = datetime.now()
                    advert.save()
                    advert.find_clients()
                    examined += 1
                time.sleep(10)
            cached_ids[advert.id] = cached_ids[advert.id] + 1
        except Exception, err:
            logger.info(traceback.format_exc())

    for id in exclude_ids:
        cached_ids[id] = cached_ids[id] + 1

    cache.set('auto-exams-ids-%s' % town.id, cached_ids, 60*60*3)

    return examined