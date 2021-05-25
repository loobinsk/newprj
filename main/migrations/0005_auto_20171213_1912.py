# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20171110_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='metro',
            name='centr',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd1\x82\xd1\x80'),
        ),
        migrations.AlterField(
            model_name='clientrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 19, 11, 59, 563062), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8', db_index=True),
        ),
        migrations.AlterField(
            model_name='complain',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 19, 11, 59, 508142), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='connectedservice',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 19, 11, 59, 545337), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xba\xd0\xbe\xd0\xbd\xd1\x86\xd0\xb0 \xd0\xb4\xd0\xb5\xd0\xb9\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='connectedservice',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 19, 11, 59, 545288), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0 \xd0\xb4\xd0\xb5\xd0\xb9\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 19, 11, 59, 527652), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 19, 11, 59, 531423), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='searchrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 19, 11, 59, 551980), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8', db_index=True),
        ),
        migrations.AlterField(
            model_name='subscribecode',
            name='code',
            field=models.CharField(default=b'et5rica9b9ysku8wmt3wc17tabfev7', max_length=30, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xb4'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 19, 11, 59, 530326), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='vkadvert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 19, 11, 59, 570926), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8', db_index=True),
        ),
    ]
