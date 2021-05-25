# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vkposting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='canal',
            name='type',
            field=models.CharField(default=b'vk', max_length=10, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf', choices=[(b'twitter', b'Twitter'), (b'vk', b'\xd0\x92\xd0\xba\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd0\xb5')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='access_token',
            field=models.CharField(default=b'', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='access_token_secret',
            field=models.CharField(default=b'', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='consumer_key',
            field=models.CharField(default=b'', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='consumer_secret',
            field=models.CharField(default=b'', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='canal',
            name='code',
            field=models.CharField(default=b'', max_length=50, verbose_name=b'\xd0\xa1\xd0\xb8\xd0\xbc\xd0\xb2\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xba\xd0\xbe\xd0\xb4'),
        ),
        migrations.AlterField(
            model_name='canal',
            name='group_id',
            field=models.CharField(default=b'', max_length=20, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xb4 \xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xbf\xd1\x8b \xd0\x92\xd0\x9a'),
        ),
        migrations.AlterField(
            model_name='canal',
            name='profile',
            field=models.ForeignKey(default=None, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd1\x84\xd0\xb8\xd0\xbb\xd1\x8c', to='vkposting.Profile'),
        ),
        migrations.AlterField(
            model_name='canal',
            name='title',
            field=models.CharField(default=b'', max_length=50, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='login',
            field=models.CharField(default=b'', max_length=50, null=True, verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xb8\xd0\xbd', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='password',
            field=models.CharField(default=b'', max_length=50, null=True, verbose_name=b'\xd0\x9f\xd0\xb0\xd1\x80\xd0\xbe\xd0\xbb\xd1\x8c', blank=True),
        ),
    ]
