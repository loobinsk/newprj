from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('debug_toolbar.toolbar', namespace='djdt', app_name='debug_toolbar')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^adminpanel/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^paysto/', include('paysto.urls')),
    url(r'^robokassa/', include('robokassa.urls')),
    url(r'^w1/', include('walletone.urls')),
    url(r'', include('user_sessions.urls', 'user_sessions')),
    url(r'', include('uimg.urls')),
    url(r'', include('ufile.urls')),
    url(r'', include('uvideo.urls')),
    url(r'', include('uprofile.urls')),
    url(r'', include('ucomment.urls')),
    url(r'^captcha/', include('captcha.urls')),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
       'document_root': settings.STATIC_ROOT,
       }),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
       'document_root': settings.MEDIA_ROOT,
       }),

)
