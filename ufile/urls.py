#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from ufile.views import *

ufile_patterns = patterns('ufile',
                         url(r'^create$', UserFileCreateView.as_view(), name='create'),
                         url(r'^(?P<id>\w+)/del', UserFileDeleteView.as_view(), name='del'),
                         )

urlpatterns = patterns('',
                       url(r'^ufile/', include(ufile_patterns, namespace='file', app_name='ufile'))
)