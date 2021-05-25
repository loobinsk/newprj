# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.sites.models import Site
from uprofile.models import GlobalUser
import string
import random
from django.conf import settings


class PromoException(BaseException):
    pass


class Promotion(models.Model):
    """
    Промоакция
    """
    title = models.CharField(u"Название", max_length=50, default='')
    start_date = models.DateTimeField(u'Дата начала', default=datetime.now)
    end_date = models.DateTimeField(u'Дата начала', default=datetime.now)
    site = models.ForeignKey(Site, verbose_name=u'Сайт', default=1)
    discount = models.PositiveIntegerField(u'Процент скидки', default=0)
    code = models.CharField(u'Символьный код', max_length=50, default=None, blank=True, null=True)
    prefix = models.CharField(u'Префикс', max_length=10, default='', blank=True)

    class Meta:
        verbose_name = u'Промоакция'
        verbose_name_plural = u'Промоакции'

    def __unicode__(self):
        return self.title


class PromocodeManager(models.Manager):
    def get_queryset(self):
        return super(PromocodeManager, self).get_queryset().filter(promotion__site=settings.SITE_ID)


class Promocode(models.Model):
    """
    Промокод на скидку
    """
    promotion = models.ForeignKey(Promotion, verbose_name=u'Промоакция')
    code = models.CharField(u'Код', max_length=50, default='', blank=True)
    user = models.ForeignKey(GlobalUser, verbose_name=u'Пользователь', default=None, null=True,blank=True)
    activated = models.BooleanField(u'Уже использован', default=False)

    objects = PromocodeManager()
    admin_objects = models.Manager()

    class Meta:
        verbose_name = u'Промокод'
        verbose_name_plural = u'Промокоды'

    def __unicode__(self):
        return self.code

    def activate(self):
        now = datetime.now()
        if self.promotion.start_date > now:
            raise PromoException(u'Промоакция еще не началась')
        if self.promotion.end_date < now:
            raise PromoException(u'Промоакция уже закончилась')
        if self.activated:
            raise PromoException(u'Промокод уже был активирован')
        if self.user:
            if self.promotion.site_id != self.user.site_id:
                raise PromoException(u'Нельзя активирован этот промокод')
            self.activated = True
            self.save()
        return True

    def gen_code(self):
        for size in xrange(4, 20):
            for i in xrange(1, 20):
                self.code = self.promotion.prefix + ''.join(random.choice(string.digits) for x in range(size))
                if Promocode.objects.filter(code=self.code).count() == 0:
                    return

    def save(self, *args, **kwargs):
        if not self.code:
            self.gen_code()
        return super(Promocode, self).save(*args, **kwargs)

    def get_discount(self, sum):
        from decimal import Decimal
        return Decimal(round(sum * Decimal(self.promotion.discount / 100.0), 0))