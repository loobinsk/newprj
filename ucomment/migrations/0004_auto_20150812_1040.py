# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ucomment', '0003_auto_20150811_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='vkid',
            field=models.CharField(max_length=20, null=True, verbose_name=b'VK ID', blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 12, 10, 40, 45, 735628), verbose_name='\u0414\u0430\u0442\u0430'),
        ),
    ]
