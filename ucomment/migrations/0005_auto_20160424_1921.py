# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ucomment', '0004_auto_20150812_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 24, 19, 21, 32, 279198), verbose_name='\u0414\u0430\u0442\u0430'),
        ),
    ]
