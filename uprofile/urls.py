#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from uprofile.views import *


profile_patterns = patterns('profile',
                            url(r'^$', ActiveUserProfileView.as_view(), name='my'),
                            url(r'^avatar$', ChangeAvatarView.as_view(), name='change_avatar'),
                            )

urlpatterns = patterns('',
                       url(r'^profile/', include(profile_patterns, namespace='profile', app_name='uprofile')),
                       )