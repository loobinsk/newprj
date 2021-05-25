# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime, timedelta
from .general import Town, Metro
from django.db.models import Q


class StopAgentAdvert(models.Model):
    """
    Обявления StopAgent
    """

    LIVE_FLAT = 'F'
    LIVE_ROOM = 'R'
    LIVES = {
        LIVE_FLAT: u'Квартира',
        LIVE_ROOM: u'Комната'
    }

    date = models.DateTimeField('Дата подачи', default=datetime.now, db_index=True)
    town = models.ForeignKey(Town, verbose_name='Город', db_index=True)
    metro = models.ForeignKey(Metro, verbose_name='Метро', blank=True, null=True)
    live = models.CharField('Тип жилой недвижимости', max_length=1, default=LIVE_FLAT, choices=LIVES.items(), db_index=True)
    rooms = models.IntegerField('Количество комнат', blank=True, null=True)
    extnum = models.CharField('Внешний код', max_length=50, default=None, null=True, blank=True, db_index=True)
    owner_tel = models.CharField('Телефон собственника', max_length=50, null=True, blank=True, db_index=True)
    owner_name = models.CharField('Имя собственника', max_length=50, null=True, blank=True, default=None)

    class Meta:
        verbose_name = u'Объявление Stopagent'
        verbose_name_plural = u'Объявления Stopagent'
        ordering = ['-date']

    def __unicode__(self):
        return self.extnum

    def get_match_adverts(self):
        from main.models import Advert
        # проверка объявлений
        pattern = self.owner_tel.replace(u'X', u'([0-9])')
        query = Q(need=Advert.NEED_SALE,
                                company=None,
                                town=self.town,
                                estate=Advert.ESTATE_LIVE,
                                adtype=Advert.TYPE_LEASE,
                                owner_tel__regex=pattern,
                                live=self.live,
                                date__gte=self.date-timedelta(days=7))

        if not self.metro and self.owner_name:
            query &= Q(owner_name__iexact=self.owner_name)
        else:
            query &= (Q(metro=self.metro) | Q(metrodistance__metro=self.metro))
        if self.live == StopAgentAdvert.LIVE_FLAT:
            query &= Q(rooms=self.rooms)
        return Advert.objects.filter(query).distinct()

    def check_adverts(self, moderator='automoder_stopagent'):
        from main.models import Advert, User
        advert_list = self.get_match_adverts()
        for advert in advert_list:
            if advert.status != Advert.STATUS_VIEW:
                advert.status = Advert.STATUS_VIEW
                advert.moderate_date = self.date
                advert.moderator = User.admin_objects.get(username=moderator)
            if self.date > advert.date:
                advert.date = self.date
            advert.save()
            advert.find_clients()
            advert.publish()