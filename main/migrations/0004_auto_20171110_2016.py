# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20171110_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='metatag',
            name='seotext',
            field=ckeditor.fields.RichTextField(default=b'', null=True, verbose_name=b'SEO-\xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82', blank=True),
        ),
        migrations.AlterField(
            model_name='clientrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 20, 16, 9, 405288), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8', db_index=True),
        ),
        migrations.AlterField(
            model_name='complain',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 20, 16, 9, 348195), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='connectedservice',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 20, 16, 9, 385941), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xba\xd0\xbe\xd0\xbd\xd1\x86\xd0\xb0 \xd0\xb4\xd0\xb5\xd0\xb9\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='connectedservice',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 20, 16, 9, 385893), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0 \xd0\xb4\xd0\xb5\xd0\xb9\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 20, 16, 9, 368722), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 20, 16, 9, 371920), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='searchrequest',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 20, 16, 9, 393874), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8', db_index=True),
        ),
        migrations.AlterField(
            model_name='subscribecode',
            name='code',
            field=models.CharField(default=b'i2exeyslaz1sfcl0ro3t8mmz7qj198', max_length=30, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xb4'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 20, 16, 9, 370973), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='vkadvert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 20, 16, 9, 418033), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8', db_index=True),
        ),
    ]
