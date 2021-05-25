# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('main', '0002_auto_20160424_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metatag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('code', models.CharField(default=b'', max_length=50, null=True, verbose_name=b'C\xd0\xb8\xd0\xbc\xd0\xb2\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xba\xd0\xbe\xd0\xb4', blank=True)),
                ('path', models.CharField(default=b'', max_length=250, null=True, verbose_name=b'URL', blank=True)),
                ('title', models.CharField(default=b'', max_length=250, null=True, verbose_name=b'Page title', blank=True)),
                ('keywords', models.CharField(default=b'', max_length=250, null=True, verbose_name=b'Keywords', blank=True)),
                ('description', models.CharField(default=b'', max_length=250, null=True, verbose_name=b'Description', blank=True)),
                ('page_title', models.CharField(default=b'', max_length=250, null=True, verbose_name=b'Page title', blank=True)),
                ('og_title', models.CharField(default=b'', max_length=250, null=True, verbose_name=b'Opengraph title', blank=True)),
                ('og_image', models.CharField(default=b'', max_length=250, null=True, verbose_name=b'Opengraph image url', blank=True)),
                ('site', models.ForeignKey(verbose_name=b'\xd0\xa1\xd0\xb0\xd0\xb9\xd1\x82', to='sites.Site')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u0442\u0430\u0442\u0435\u0433',
                'verbose_name_plural': '\u041c\u0435\u0442\u0430\u0442\u0435\u0433\u0438',
            },
        ),
        migrations.AlterField(
            model_name='advert',
            name='parser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='main.Parser', null=True, verbose_name=b'\xd0\x9f\xd0\xb0\xd1\x80\xd1\x81\xd0\xb5\xd1\x80'),
        ),
        migrations.AlterField(
            model_name='clientrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 19, 25, 17, 101631), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8', db_index=True),
        ),
        migrations.AlterField(
            model_name='complain',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 19, 25, 17, 51668), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='connectedservice',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 19, 25, 17, 85845), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xba\xd0\xbe\xd0\xbd\xd1\x86\xd0\xb0 \xd0\xb4\xd0\xb5\xd0\xb9\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='connectedservice',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 19, 25, 17, 85801), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0 \xd0\xb4\xd0\xb5\xd0\xb9\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 19, 25, 17, 69653), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 19, 25, 17, 72961), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='searchrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 19, 25, 17, 91752), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8', db_index=True),
        ),
        migrations.AlterField(
            model_name='subscribecode',
            name='code',
            field=models.CharField(default=b'k59krj0rs6t03qr58qrrr5phm9no8i', max_length=30, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xb4'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 19, 25, 17, 72011), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='vkadvert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 19, 25, 17, 108369), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8', db_index=True),
        ),
    ]
