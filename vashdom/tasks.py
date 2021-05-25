# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from celery.task import periodic_task, task
from celery.schedules import crontab
import requests
import json


@task(queue='vashdom', options={'queue': 'vashdom'})
def forgotten_payments():
    from vashdom.models import VashdomUser, Payment
    from django.db.models import Count, Q
    from mail_templated import send_mail
    from main.models import Promotion, Promocode

    promotion = Promotion.objects.get(code='forgotten', site_id=VashdomUser.SITE_ID)

    user_list = VashdomUser.objects.all().\
        exclude(Q(vashdom_payments__status=Payment.STATUS_CONFIRMED) | Q(vashdom_payments__notified=True) |
                Q(vashdom_payments__created__lt=datetime.now()-timedelta(days=7)) | Q(vashdom_payments__created__gt=datetime.now()-timedelta(days=1)) | \
                Q(email='')).\
        annotate(count_payments=Count('vashdom_payments')).\
        filter(count_payments__gt=0)

    for user in user_list:
        payment_list = user.vashdom_payments.filter(Q(created__gte=datetime.now()-timedelta(days=7)) &
                                                    Q(created__lte=datetime.now()-timedelta(days=1)) &
                                                   (Q(status=Payment.STATUS_CONFIRMED) |
                                                   Q(notified=True)))
        if not payment_list:
            for payment in user.vashdom_payments.filter(created__gte=datetime.now()-timedelta(days=7),
                                                        created__lte=datetime.now()-timedelta(days=1),
                                                       status=Payment.STATUS_WAITING,
                                                       notified=False).order_by('-total')[:1]:

                promocode_list = Promocode.objects.filter(promotion=promotion, user=user, activated=False)
                if promocode_list:
                    promocode = promocode_list[0]
                else:
                    promocode = Promocode(promotion=promotion, user_id=user.id)
                    promocode.save()
                payment.notified = True
                payment.save()

                send_mail('vashdom/email/forgotten-payment.html',
                    {
                        'subject': 'У вас есть неоплаченный счет',
                        'user': payment.user,
                        'payment': payment,
                        'promocode': promocode
                    },
                    recipient_list=[user.email],
                    fail_silently=True)


@task(queue='vashdom', options={'queue': 'vashdom'})
def send_search_request_notice(id):
    from main.models import SearchRequest
    sr = SearchRequest.objects.get(id=id)
    sr.send_vashdom_notice()



@task(queue='vashdom', options={'queue': 'vashdom'})
def import_from_vashdom():
    from vashdom.models import VashdomAdvert

    r = requests.get('https://bazavashdom.ru/api/advert/')
    data = json.loads(r.text)
    for item in data['results']:
        VashdomAdvert.deserialize(item)


