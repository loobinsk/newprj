#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from ucomment.views import *

comment_patterns = patterns('comment',
                        url(r'^list$', CommentListView.as_view(), name='list'),
                         url(r'^create$', CommentCreateView.as_view(), name='create'),
                         url(r'^(?P<pk>\d+)/del', CommentDeleteView.as_view(), name='del'),
                         )

urlpatterns = patterns('',
                       url(r'^comment/', include(comment_patterns, namespace='comment', app_name='ucomment'))
)