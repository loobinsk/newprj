# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20171213_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 19, 29, 13, 747452), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8', db_index=True),
        ),
        migrations.AlterField(
            model_name='complain',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 19, 29, 13, 685239), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='connectedservice',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 19, 29, 13, 727950), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xba\xd0\xbe\xd0\xbd\xd1\x86\xd0\xb0 \xd0\xb4\xd0\xb5\xd0\xb9\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='connectedservice',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 19, 29, 13, 727900), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0 \xd0\xb4\xd0\xb5\xd0\xb9\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 19, 29, 13, 708142), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 19, 29, 13, 711759), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='searchrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 19, 29, 13, 735820), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8', db_index=True),
        ),
        migrations.AlterField(
            model_name='subscribecode',
            name='code',
            field=models.CharField(default=b'51s1qkdxmbwg1y5z1do1cpi42g5rg3', max_length=30, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xb4'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 19, 29, 13, 710583), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='vkadvert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 19, 29, 13, 853733), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8', db_index=True),
        ),
    ]
