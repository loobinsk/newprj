# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django.contrib.auth.models
import jsonfield.fields
import uprofile.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('sites', '0001_initial'),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, error_messages={b'unique': 'A user with that username already exists.'}, verbose_name='username', validators=[django.core.validators.RegexValidator(b'^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', b'invalid')])),
                ('first_name', models.CharField(max_length=50, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=50, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=datetime.datetime.now, verbose_name='date joined')),
                ('image', models.ImageField(upload_to=uprofile.models.get_user_avatar_path, null=True, verbose_name='\u0424\u043e\u0442\u043e', blank=True)),
                ('tel', models.CharField(max_length=50, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
                ('extnum', models.CharField(default=None, max_length=50, null=True, verbose_name='\u0412\u043d\u0435\u0448\u043d\u0438\u0439 \u043a\u043e\u0434', blank=True)),
                ('agent24_code', models.CharField(null=True, default=None, max_length=b'15', blank=True, unique=True, verbose_name='\u041a\u043e\u0434 \u0434\u043e\u0441\u0442\u0443\u043f\u0430')),
                ('buys', models.PositiveIntegerField(default=0, verbose_name='\u0412\u044b\u043a\u0443\u043f\u044b', blank=True)),
                ('agent_email', models.EmailField(default=b'', max_length=254, null=True, verbose_name='\u0410\u0433\u0435\u043d\u0442\u0441\u043a\u0438\u0439 email', blank=True)),
                ('status', models.CharField(default=b'a', max_length=1, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(b'a', b'\xd0\x90\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xb5\xd0\xbd'), (b'b', b'\xd0\x97\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xbe\xd0\xba\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd'), (b'm', b'\xd0\x9d\xd0\xb0 \xd0\xbc\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8')])),
                ('independent', models.BooleanField(default=True, verbose_name='\u041d\u0435\u0437\u0430\u0432\u0438\u0441\u0438\u043c\u044b\u0439 \u0430\u0433\u0435\u043d\u0442')),
                ('sex', models.CharField(default=b'm', max_length=1, verbose_name='\u041f\u043e\u043b', blank=True)),
                ('uuid', models.CharField(default=b'', max_length=250, verbose_name='UUID', blank=True)),
                ('agent24_view_owner', models.BooleanField(default=True, verbose_name='\u041e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u044f \u043e\u0442 \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a\u043e\u0432')),
                ('agent24_view_company', models.BooleanField(default=True, verbose_name='\u041e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u044f \u043e\u0442 \u0430\u0433\u0435\u043d\u0442\u0441\u0442\u0432')),
                ('properties', jsonfield.fields.JSONField(default={}, null=True, blank=True)),
                ('company', models.ForeignKey(default=None, blank=True, to='main.Company', null=True, verbose_name=b'\xd0\x90\xd0\xb3\xd0\xb5\xd0\xbd\xd1\x82\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe')),
                ('enable_perms', models.ManyToManyField(to='main.Perm', verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb4\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \xd1\x80\xd0\xb0\xd0\xb7\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8b \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd1\x83\xd0\xbf\xd0\xb0', blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('site', models.ForeignKey(default=None, blank=True, to='sites.Site', null=True, verbose_name=b'\xd0\xa1\xd0\xb0\xd0\xb9\xd1\x82')),
                ('town', models.ForeignKey(default=None, blank=True, to='main.Town', null=True, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'permissions': (('view_client', '\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u043a\u043b\u0438\u0435\u043d\u0442\u0441\u043a\u043e\u0439 \u0447\u0430\u0441\u0442\u0438'), ('view_moderate', '\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u043c\u043e\u0434\u0435\u0440\u0430\u0442\u043e\u0440\u0441\u043a\u043e\u0439 \u0447\u0430\u0441\u0442\u0438'), ('view_user', '\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0441\u043f\u0438\u0441\u043a\u0430 \u0430\u0433\u0435\u043d\u0442\u043e\u0432')),
            },
            managers=[
                ('objects', uprofile.models.UserManager()),
                ('admin_objects', uprofile.models.UserAdminManager()),
            ],
        ),
        migrations.CreateModel(
            name='GlobalUser',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('uprofile.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
                ('admin_objects', uprofile.models.UserAdminManager()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('username', 'site')]),
        ),
    ]
