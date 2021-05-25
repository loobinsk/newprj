from django.conf.urls import patterns, include, url
from django.contrib import admin
from sitemap import sitemaps
from django.contrib.sitemaps import views as sitemaps_views
from django.views.decorators.cache import cache_page
from main import urls as main_urls

urlpatterns = patterns('',
    url(r'', include('gsnru.service_urls')),
    url(r'', include(main_urls.urlpatterns)),

    # url(r'^sitemap.xml$', cache_page(86400, cache='file')(sitemaps_views.index), {'sitemaps': sitemaps, 'sitemap_url_name': 'sitemaps'}),
    # url(r'^sitemap-(?P<section>.+)\.xml$',
    #     cache_page(86400, cache='file')(sitemaps_views.sitemap),
    #     {'sitemaps': sitemaps}, name='sitemaps'),
)

handler404 = 'main.views.public.page_not_found'
