# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uimg', '0004_auto_20160424_1921'),
        ('uprofile', '0001_initial'),
        ('main', '0001_initial'),
        ('sites', '0001_initial'),
        ('uvideo', '__first__'),
    ]

    operations = [
        migrations.AddField(
            model_name='weekperm',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vkadvert',
            name='district',
            field=models.ForeignKey(verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb9\xd0\xbe\xd0\xbd', blank=True, to='main.District', null=True),
        ),
        migrations.AddField(
            model_name='vkadvert',
            name='images',
            field=models.ManyToManyField(related_name='vkadverts', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', to='uimg.UserImage', blank=True),
        ),
        migrations.AddField(
            model_name='vkadvert',
            name='metro',
            field=models.ForeignKey(verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x82\xd1\x80\xd0\xbe', blank=True, to='main.Metro', null=True),
        ),
        migrations.AddField(
            model_name='vkadvert',
            name='owner_photo',
            field=models.ForeignKey(blank=True, to='uimg.UserImage', null=True),
        ),
        migrations.AddField(
            model_name='vkadvert',
            name='town',
            field=models.ForeignKey(verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', to='main.Town'),
        ),
        migrations.AddField(
            model_name='vkadvert',
            name='viewed',
            field=models.ManyToManyField(related_name='vkviewed', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='town',
            name='site',
            field=models.ManyToManyField(to='sites.Site', null=True, verbose_name=b'\xd0\xa1\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b', blank=True),
        ),
        migrations.AddField(
            model_name='tariff',
            name='perms',
            field=models.ManyToManyField(related_name='tariffs', verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb0\xd0\xb2\xd0\xb0 \xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd1\x84\xd0\xb0', to='main.Perm', blank=True),
        ),
        migrations.AddField(
            model_name='tariff',
            name='town',
            field=models.ManyToManyField(to='main.Town', verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4\xd0\xb0', blank=True),
        ),
        migrations.AddField(
            model_name='subscribecode',
            name='subscribe',
            field=models.ForeignKey(to='main.Subscribe'),
        ),
        migrations.AddField(
            model_name='subscribecode',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='subscribed',
            field=models.ManyToManyField(related_name='subscribed', verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb4\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='unsubscribed',
            field=models.ManyToManyField(related_name='unsubscribed', verbose_name=b'\xd0\x9e\xd1\x82\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='stopagentadvert',
            name='metro',
            field=models.ForeignKey(verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x82\xd1\x80\xd0\xbe', blank=True, to='main.Metro', null=True),
        ),
        migrations.AddField(
            model_name='stopagentadvert',
            name='town',
            field=models.ForeignKey(verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', to='main.Town'),
        ),
        migrations.AddField(
            model_name='searchrequest',
            name='advert_not_send',
            field=models.ManyToManyField(related_name='search_request_not_send', to='main.Advert', blank=True),
        ),
        migrations.AddField(
            model_name='searchrequest',
            name='advert_noticed',
            field=models.ManyToManyField(related_name='search_request_noticed', verbose_name=b'\xd0\xa3\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xbe\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbe\xd0\xb1 \xd0\xb7\xd0\xb0\xd1\x8f\xd0\xb2\xd0\xba\xd0\xb5', to='main.Advert', blank=True),
        ),
        migrations.AddField(
            model_name='searchrequest',
            name='clients',
            field=models.ManyToManyField(to='main.Advert', blank=True),
        ),
        migrations.AddField(
            model_name='searchrequest',
            name='company',
            field=models.ForeignKey(verbose_name=b'\xd0\x90\xd0\xb3\xd0\xb5\xd0\xbd\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe', blank=True, to='main.Company', null=True),
        ),
        migrations.AddField(
            model_name='searchrequest',
            name='district',
            field=models.ManyToManyField(to='main.District', verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb9\xd0\xbe\xd0\xbd', blank=True),
        ),
        migrations.AddField(
            model_name='searchrequest',
            name='metro',
            field=models.ManyToManyField(to='main.Metro', verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x82\xd1\x80\xd0\xbe', blank=True),
        ),
        migrations.AddField(
            model_name='searchrequest',
            name='site',
            field=models.ForeignKey(verbose_name=b'\xd0\xa1\xd0\xb0\xd0\xb9\xd1\x82', blank=True, to='sites.Site', null=True),
        ),
        migrations.AddField(
            model_name='searchrequest',
            name='town',
            field=models.ForeignKey(verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', to='main.Town'),
        ),
        migrations.AddField(
            model_name='searchrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='regviewed',
            name='advert',
            field=models.ForeignKey(default=0, to='main.Advert'),
        ),
        migrations.AddField(
            model_name='regviewed',
            name='user',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='referraluser',
            name='referral',
            field=models.ForeignKey(to='main.Referral'),
        ),
        migrations.AddField(
            model_name='referraluser',
            name='user',
            field=models.ForeignKey(to='uprofile.GlobalUser'),
        ),
        migrations.AddField(
            model_name='referralreferer',
            name='referral',
            field=models.ForeignKey(to='main.Referral'),
        ),
        migrations.AddField(
            model_name='referralpayment',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='referralpayment',
            name='referral',
            field=models.ForeignKey(to='main.Referral'),
        ),
        migrations.AddField(
            model_name='referral',
            name='site',
            field=models.ForeignKey(verbose_name='\u0421\u0430\u0439\u0442', to='sites.Site'),
        ),
        migrations.AddField(
            model_name='referral',
            name='user',
            field=models.ForeignKey(verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c', to='uprofile.GlobalUser'),
        ),
        migrations.AddField(
            model_name='promotion',
            name='site',
            field=models.ForeignKey(default=1, verbose_name='\u0421\u0430\u0439\u0442', to='sites.Site'),
        ),
        migrations.AddField(
            model_name='promocode',
            name='promotion',
            field=models.ForeignKey(verbose_name='\u041f\u0440\u043e\u043c\u043e\u0430\u043a\u0446\u0438\u044f', to='main.Promotion'),
        ),
        migrations.AddField(
            model_name='promocode',
            name='user',
            field=models.ForeignKey(default=None, blank=True, to='uprofile.GlobalUser', null=True, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
        ),
        migrations.AddField(
            model_name='paymentitem',
            name='tariff',
            field=models.ForeignKey(default=None, blank=True, to='main.Tariff', null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='items',
            field=models.ManyToManyField(to='main.PaymentItem', blank=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='promocode',
            field=models.ForeignKey(default=None, blank=True, to='main.Promocode', null=True, verbose_name='\u041f\u0440\u043e\u043c\u043e\u043a\u043e\u0434'),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='news',
            name='images',
            field=models.ManyToManyField(to='uimg.UserImage', blank=True),
        ),
        migrations.AddField(
            model_name='news',
            name='site',
            field=models.ForeignKey(to='sites.Site', blank=True),
        ),
        migrations.AddField(
            model_name='news',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='news',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='uvideo.UserVideo', null=True),
        ),
        migrations.AddField(
            model_name='metrodistance',
            name='advert',
            field=models.ForeignKey(to='main.Advert'),
        ),
        migrations.AddField(
            model_name='metrodistance',
            name='metro',
            field=models.ForeignKey(to='main.Metro'),
        ),
        migrations.AddField(
            model_name='metro',
            name='town',
            field=models.ForeignKey(verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', to='main.Town'),
        ),
        migrations.AddField(
            model_name='district',
            name='town',
            field=models.ForeignKey(verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', to='main.Town'),
        ),
        migrations.AddField(
            model_name='connectedservice',
            name='company',
            field=models.ForeignKey(default=None, blank=True, to='main.Company', null=True, verbose_name=b'\xd0\x90\xd0\xb3\xd0\xb5\xd0\xbd\xd1\x82\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe'),
        ),
        migrations.AddField(
            model_name='connectedservice',
            name='perm',
            field=models.ForeignKey(related_name='connectedservice', verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb0\xd0\xb2\xd0\xb0', to='main.Perm'),
        ),
        migrations.AddField(
            model_name='connectedservice',
            name='tariff',
            field=models.ForeignKey(default=None, blank=True, to='main.Tariff', null=True, verbose_name=b'\xd0\xa2\xd0\xb0\xd1\x80\xd0\xb8\xd1\x84'),
        ),
        migrations.AddField(
            model_name='connectedservice',
            name='user',
            field=models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'\xd0\x90\xd0\xb3\xd0\xb5\xd0\xbd\xd1\x82'),
        ),
        migrations.AddField(
            model_name='complain',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='complain',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='company',
            name='owner',
            field=models.ForeignKey(related_name='owner', on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'\xd0\x92\xd0\xbb\xd0\xb0\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x86', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='town',
            field=models.ForeignKey(default=1, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', to='main.Town'),
        ),
        migrations.AddField(
            model_name='clientrequest',
            name='adverts',
            field=models.ManyToManyField(to='main.Advert', blank=True),
        ),
        migrations.AddField(
            model_name='clientrequest',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xd0\x90\xd0\xb3\xd0\xb5\xd0\xbd\xd1\x82', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='blacklist',
            name='town',
            field=models.ForeignKey(default=None, blank=True, to='main.Town', null=True, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4'),
        ),
        migrations.AddField(
            model_name='advert',
            name='block_user',
            field=models.ForeignKey(related_name='blocked_adverts', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xbe\xd0\xba\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xb2\xd1\x88\xd0\xb8\xd0\xb9 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c'),
        ),
        migrations.AddField(
            model_name='advert',
            name='buy_company',
            field=models.ManyToManyField(related_name='buy_adverts', to='main.Company', blank=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='buy_users',
            field=models.ManyToManyField(related_name='buy_adverts', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='clients',
            field=models.ManyToManyField(related_name='_advert_clients_+', to='main.Advert', blank=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='company',
            field=models.ForeignKey(verbose_name=b'\xd0\x90\xd0\xb3\xd0\xb5\xd0\xbd\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe', blank=True, to='main.Company', null=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='district',
            field=models.ForeignKey(verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb9\xd0\xbe\xd0\xbd', blank=True, to='main.District', null=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='favorites',
            field=models.ManyToManyField(related_name='favorites', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='folded',
            field=models.ManyToManyField(related_name='folded', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='images',
            field=models.ManyToManyField(to='uimg.UserImage', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='metro',
            field=models.ForeignKey(verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x82\xd1\x80\xd0\xbe', blank=True, to='main.Metro', null=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='moderator',
            field=models.ForeignKey(related_name='moderated', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'\xd0\x9c\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'),
        ),
        migrations.AddField(
            model_name='advert',
            name='need_metro',
            field=models.ManyToManyField(related_name='need_adverts', to='main.Metro', blank=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='parser',
            field=models.ForeignKey(default=None, blank=True, to='main.Parser', null=True, verbose_name=b'\xd0\x9f\xd0\xb0\xd1\x80\xd1\x81\xd0\xb5\xd1\x80'),
        ),
        migrations.AddField(
            model_name='advert',
            name='town',
            field=models.ForeignKey(verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', to='main.Town'),
        ),
        migrations.AddField(
            model_name='advert',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='user_noticed',
            field=models.ManyToManyField(related_name='advert_noticed', verbose_name=b'\xd0\xa3\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xbe\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbe\xd0\xb1 \xd0\xbe\xd0\xb1\xd1\x8a\xd1\x8f\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb8', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='viewed',
            field=models.ManyToManyField(related_name='viewed', through='main.RegViewed', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='regviewed',
            unique_together=set([('advert', 'user')]),
        ),
    ]
