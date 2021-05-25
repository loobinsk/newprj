# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from uprofile.models import GlobalUser
from django.contrib.sites.models import Site
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
import string
import random
from cache_utils.decorators import cached


class Referral(models.Model):
    """
    Реферральная ссылка
    """
    code = models.CharField(u'Код', max_length=50, default='', blank=True)
    user = models.ForeignKey(GlobalUser, verbose_name=u'Пользователь')
    site = models.ForeignKey(Site, verbose_name=u'Сайт')
    conversion = models.PositiveIntegerField(u'Количество переходов', default=0, blank=True)

    class Meta:
        verbose_name = u'Реферральная ссылка'
        verbose_name_plural = u'Реферральные ссылки'

    def __unicode__(self):
        return self.code

    def gen_code(self):
        for size in xrange(4, 20):
            for i in xrange(1, 20):
                self.code = ''.join(random.choice(string.digits) for x in range(size))
                if Referral.objects.filter(code=self.code).count() == 0:
                    return

    def save(self, *args, **kwargs):
        if not self.code:
            self.gen_code()
        return super(Referral, self).save(*args, **kwargs)

    @property
    def link(self):
        return 'http://%s/?ref=%s' % (self.site.domain, self.code)

    # @cached(3600)
    def get_user_count(slf):
        return ReferralUser.objects.filter(referral=slf).count()

    # @cached(3600)
    def get_payment_count(slf):
        return ReferralPayment.objects.filter(referral=slf).count()


class ReferralUser(models.Model):
    """
    Привлеченные пользователи
    """
    referral = models.ForeignKey(Referral)
    user = models.ForeignKey(GlobalUser)
    date = models.DateTimeField(u'Дата', default=datetime.now)

    class Meta:
        verbose_name = u'Привлеченный пользователь'
        verbose_name_plural = u'Привлеченные пользователи'
        ordering = ['-date']

    def __unicode__(self):
        return self.user.username


class ReferralPayment(models.Model):
    """
    Привлеченные платежи
    """
    referral = models.ForeignKey(Referral)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    payment = GenericForeignKey('content_type', 'object_id')
    date = models.DateTimeField(u'Дата', default=datetime.now)

    class Meta:
        verbose_name = u'Привлеченный платежи'
        verbose_name_plural = u'Привлеченные платежи'
        ordering = ['-date']

    def __unicode__(self):
        return unicode(self.payment.id)


class ReferralReferer(models.Model):
    """
    Привлеченные пользователи
    """
    referral = models.ForeignKey(Referral)
    referer = models.CharField(u'Referer', max_length=250)
    date = models.DateTimeField(u'Дата', default=datetime.now)

    class Meta:
        verbose_name = u'Переход реферала'
        verbose_name_plural = u'Переходы рефералов'
        ordering = ['-date']

    def __unicode__(self):
        return self.referer