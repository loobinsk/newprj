# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('uimg', '0003_auto_20160315_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 24, 19, 21, 32, 271781), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
    ]
