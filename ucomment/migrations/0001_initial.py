# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, null=True, verbose_name=b'\xd0\x92\xd0\xb0\xd1\x88\xd0\xb5 \xd0\xb8\xd0\xbc\xd1\x8f', blank=True)),
                ('text', models.TextField(default=b'', max_length=500, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442', blank=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 6, 11, 15, 25, 9, 548198), verbose_name='\u0414\u0430\u0442\u0430')),
                ('key', models.CharField(max_length=50, verbose_name='\u041a\u043b\u044e\u0447 \u0432\u0435\u0442\u043a\u0438', db_index=True)),
                ('url', models.URLField(default=b'', max_length=250, null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', models.ForeignKey(verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439', blank=True, to='ucomment.Comment', null=True)),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439',
                'verbose_name_plural': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438',
            },
        ),
    ]
