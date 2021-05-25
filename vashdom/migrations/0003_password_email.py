# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vashdom', '0002_auto_20171226_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='password',
            name='email',
            field=models.EmailField(default=None, max_length=254, null=True, verbose_name='Email', blank=True),
        ),
    ]
