# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('uimg', '0002_userimage_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 15, 20, 18, 38, 185172), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
    ]
