# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import vashdom.models
import uprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('uprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(default=b'', max_length=10, verbose_name='\u041f\u0430\u0440\u043e\u043b\u044c')),
                ('start_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430')),
                ('end_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f')),
                ('count', models.IntegerField(default=0, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('tel', models.CharField(default=b'', max_length=20, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('main_base', models.BooleanField(default=True, verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0431\u0430\u0437\u0430')),
                ('vk_base', models.BooleanField(default=False, verbose_name='\u0411\u0430\u0437\u0430 \u0412\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u0435')),
            ],
            options={
                'ordering': ['-start_date'],
                'verbose_name': '\u041f\u0430\u0440\u043e\u043b\u044c',
                'verbose_name_plural': '\u041f\u0430\u0440\u043e\u043b\u0438',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'w', max_length=1, choices=[(b'i', b'Input'), (b'c', b'\xd0\x9f\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb6 \xd0\xb7\xd0\xb0\xd0\xb2\xd0\xb5\xd1\x80\xd1\x88\xd0\xb5\xd0\xbd'), (b'r', b'\xd0\x9f\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb6 \xd0\xbe\xd1\x82\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd'), (b'e', b'\xd0\x9e\xd1\x88\xd0\xb8\xd0\xb1\xd0\xba\xd0\xb0 \xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb6\xd0\xb0'), (b'w', b'\xd0\x9e\xd0\xb6\xd0\xb8\xd0\xb4\xd0\xb0\xd0\xb5\xd1\x82 \xd0\xbe\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd1\x8b')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('transaction_id', models.CharField(max_length=255, blank=True)),
                ('currency', models.CharField(default=b'RUB', max_length=10)),
                ('sum', models.DecimalField(default=b'0.0', max_digits=9, decimal_places=2)),
                ('total', models.DecimalField(default=b'0.0', max_digits=9, decimal_places=2)),
                ('delivery', models.DecimalField(default=b'0.0', max_digits=9, decimal_places=2)),
                ('tax', models.DecimalField(default=b'0.0', max_digits=9, decimal_places=2)),
                ('description', models.TextField(default=b'', blank=True)),
                ('extra_data', models.TextField(default=b'', blank=True)),
                ('token', models.CharField(default=b'', max_length=36, blank=True)),
                ('hash_md5', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('request_mode', models.CharField(blank=True, max_length=20, null=True, choices=[(b'RES_PAID', b'\xd0\xbe\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd1\x81\xd1\x82\xd0\xbe\xd1\x8f\xd0\xbb\xd0\xb0\xd1\x81\xd1\x8c'), (b'RES_ERROR', b'\xd0\xbf\xd1\x80\xd0\xb8 \xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb6\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb8\xd0\xb7\xd0\xbe\xd1\x88\xd0\xbb\xd0\xb8 \xd0\xbe\xd1\x88\xd0\xb8\xd0\xb1\xd0\xba\xd0\xb8'), (b'RES_BILLED', b'\xd0\xb7\xd0\xb0\xd1\x8f\xd0\xb2\xd0\xba\xd0\xb0 \xd0\xbe\xd1\x82\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb0 \xd0\xbd\xd0\xb0 \xd0\xbe\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd1\x83'), (b'RES_CREATED', b'\xd0\xb7\xd0\xb0\xd1\x8f\xd0\xb2\xd0\xba\xd0\xb0 \xd0\xb7\xd0\xb0\xd1\x80\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb0'), (b'RES_CANCEL', b'\xd0\xbf\xd0\xbe\xd0\xba\xd1\x83\xd0\xbf\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c \xd0\xbe\xd1\x82\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0\xd0\xbb\xd1\x81\xd1\x8f \xd0\xbe\xd1\x82 \xd0\xbf\xd0\xbe\xd0\xba\xd1\x83\xd0\xbf\xd0\xba\xd0\xb8'), (b'RES_HOLD', b'\xd0\xb7\xd0\xb0\xd1\x8f\xd0\xb2\xd0\xba\xd0\xb0 \xd0\xbf\xd1\x80\xd0\xb8\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb0')])),
                ('tel', models.CharField(default=b'', max_length=20, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('notified', models.BooleanField(default=False, verbose_name='\u0423\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u043e')),
                ('session_key', models.CharField(default=b'', max_length=100, blank=True)),
                ('password', models.ForeignKey(default=None, blank=True, to='vashdom.Password', null=True, verbose_name='\u0412\u044b\u0434\u0430\u043d\u043d\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c')),
                ('promocode', models.ForeignKey(related_name='vashdom_payments', default=None, blank=True, to='main.Promocode', null=True, verbose_name='\u041f\u0440\u043e\u043c\u043e\u043a\u043e\u0434')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': '\u0417\u0430\u043a\u0430\u0437',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b',
            },
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=250, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('desc', models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('price', models.FloatField(default=100, verbose_name='\u0426\u0435\u043d\u0430')),
                ('order', models.IntegerField(default=500, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430', blank=True)),
                ('count', models.IntegerField(default=0, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u0439')),
                ('days', models.IntegerField(default=0, verbose_name='\u0414\u043d\u0438')),
                ('main_base', models.BooleanField(default=True, verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0431\u0430\u0437\u0430')),
                ('vk_base', models.BooleanField(default=False, verbose_name='\u0411\u0430\u0437\u0430 \u0412\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u0435')),
                ('hidden', models.BooleanField(default=False, verbose_name='\u0421\u043a\u0440\u044b\u0442\u044b\u0439')),
                ('code', models.CharField(default=b'', max_length=50, null=True, verbose_name='\u0421\u0438\u043c\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043a\u043e\u0434', blank=True)),
                ('town', models.ForeignKey(related_name='vashdom_tariffs', default=1, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', to='main.Town')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': '\u0422\u0430\u0440\u0438\u0444',
                'verbose_name_plural': '\u0422\u0430\u0440\u0438\u0444\u044b',
            },
        ),
        migrations.CreateModel(
            name='VashdomAdvert',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('main.advert',),
        ),
        migrations.CreateModel(
            name='VashdomUser',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('uprofile.user',),
            managers=[
                ('objects', vashdom.models.VashdomUserManager()),
                ('admin_objects', uprofile.models.UserAdminManager()),
            ],
        ),
        migrations.CreateModel(
            name='VashdomVKAdvert',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('main.vkadvert',),
        ),
        migrations.AddField(
            model_name='payment',
            name='tariff',
            field=models.ForeignKey(default=None, to='vashdom.Tariff', null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='town',
            field=models.ForeignKey(related_name='vashdom_payments', default=1, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', to='main.Town'),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(related_name='vashdom_payments', default=None, blank=True, to='vashdom.VashdomUser', null=True, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
        ),
        migrations.AddField(
            model_name='password',
            name='adverts',
            field=models.ManyToManyField(to='main.Advert', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='password',
            name='town',
            field=models.ForeignKey(default=1, verbose_name='\u0413\u043e\u0440\u043e\u0434', to='main.Town'),
        ),
        migrations.AddField(
            model_name='password',
            name='user',
            field=models.ForeignKey(related_name='vashdom_passwords', default=None, blank=True, to='vashdom.VashdomUser', null=True, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
        ),
        migrations.AddField(
            model_name='password',
            name='vkadverts',
            field=models.ManyToManyField(to='main.VKAdvert', null=True, blank=True),
        ),
    ]
