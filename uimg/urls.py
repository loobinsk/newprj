#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from uimg.views import *

uimg_patterns = patterns('uimg',
                         url(r'^create$', UserImageMultipleCreateView.as_view(), name='create_multi'),
                         url(r'^(?P<id>\w+)/del', UserImageDeleteView.as_view(), name='del'),
                         url(r'^(?P<id>\w+)/edit', UserImageUpdateView.as_view(), name='edit'),
                         url(r'^(?P<id>\w+)/preview', UserImagePreviewView.as_view(), name='preview'),
                         url(r'^lib/list$', UserImageLibraryListView.as_view(), name='list'),
                         url(r'^lib$', UserImageLibraryView.as_view(), name='lib'),
                         url(r'^(?P<id>\w+)/lib/preview', UserImageLibraryPreviewView.as_view(), name='preview'),
                         )

urlpatterns = patterns('',
                       url(r'^uimg/', include(uimg_patterns, namespace='img', app_name='uimg'))
)