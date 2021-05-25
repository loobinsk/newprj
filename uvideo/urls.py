#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from uvideo.views import *

uimg_patterns = patterns('uvideo',
                         url(r'^create$', UserVideoCreateView.as_view(), name='create'),
                         url(r'^(?P<id>\w+)/del', UserVideoDeleteView.as_view(), name='del'),
                         )

urlpatterns = patterns('',
                       url(r'^uvideo/', include(uimg_patterns, namespace='video', app_name='uvideo'))
)