# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ucomment.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ucomment', '0002_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(upload_to=ucomment.models.get_comment_image_path, null=True, verbose_name='\u0424\u043e\u0442\u043e', blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 11, 23, 11, 25, 313809), verbose_name='\u0414\u0430\u0442\u0430'),
        ),
    ]
