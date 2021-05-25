# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=50, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('code', models.CharField(default=b'', max_length=50, verbose_name='\u0421\u0438\u043c\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043a\u043e\u0434')),
                ('group_id', models.CharField(default=b'', max_length=20, verbose_name='\u041a\u043e\u0434 \u0433\u0440\u0443\u043f\u043f\u044b \u0412\u041a')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u043d\u0430\u043b',
                'verbose_name_plural': '\u041a\u0430\u043d\u0430\u043b\u044b',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('canal', models.ForeignKey(to='vkposting.Canal')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login', models.CharField(max_length=50, verbose_name='\u041b\u043e\u0433\u0438\u043d')),
                ('password', models.CharField(max_length=50, verbose_name='\u041f\u0430\u0440\u043e\u043b\u044c')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0444\u0438\u043b\u044c',
                'verbose_name_plural': '\u041f\u0440\u043e\u0444\u0438\u043b\u0438',
            },
        ),
        migrations.AddField(
            model_name='canal',
            name='profile',
            field=models.ForeignKey(default=None, verbose_name='\u041f\u0440\u043e\u0444\u0438\u043b\u044c', to='vkposting.Profile'),
        ),
    ]
