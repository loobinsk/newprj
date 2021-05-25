#-*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap, FlatPageSitemap
from main.models import Advert, VKAdvert, Town, News
from vashdom.models import VashdomAdvert
from django.core.urlresolvers import reverse
from django.conf import settings


class AdvertMSKSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    limit = 5000

    protocol = 'http'

    def items(self):
        town = Town.objects.get(id=1)
        return Advert.objects.filter(VashdomAdvert.get_advert_query(town)).select_related('town')

    def location(self, obj):
        return '/id%s' % obj.id


class AdvertSPBSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    limit = 5000

    protocol = 'http'

    def items(self):
        town = Town.objects.get(id=2)
        return Advert.objects.filter(VashdomAdvert.get_advert_query(town)).select_related('town')

    def location(self, obj):
        return '/id%s' % obj.id


class AdvertNSKSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    limit = 5000

    protocol = 'http'

    def items(self):
        town = Town.objects.get(slug='novosibirsk')
        return Advert.objects.filter(VashdomAdvert.get_advert_query(town)).select_related('town')

    def location(self, obj):
        return '/id%s' % obj.id


class AdvertEKBSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    limit = 5000

    protocol = 'http'

    def items(self):
        town = Town.objects.get(slug='ekaterinburg')
        return Advert.objects.filter(VashdomAdvert.get_advert_query(town)).select_related('town')

    def location(self, obj):
        return '/id%s' % obj.id


class VKAdvertSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    limit = 5000

    protocol = 'http'

    def items(self):
        town_list = Town.objects.all()
        return VKAdvert.objects.filter(status=VKAdvert.STATUS_VIEW, town__in=town_list).select_related('town')

    def location(self, obj):
        return '/vkid%s' % obj.id


class ViewSitemap(Sitemap):
    protocol = 'http'
    changefreq = "daily"
    priority = 0.5

    def items(self):
        result = ['home', 'tariff', 'contacts']
        town_list = Town.objects.all()
        params = {}
        for town in town_list:
            params['town'] = town.id
            result.append(Advert.get_catalog_url(params))
            # result.append(VKAdvert.get_catalog_url(params))
        return result

    def location(self, item):
        if '/' in item:
            return item
        else:
            return reverse(item)


class NewsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    protocol = 'http'

    def items(self):
        return News.objects.filter(client=False, moder=False, site_id=settings.SITE_ID)

sitemaps = {
    'flatpage': FlatPageSitemap,
    'catalog_msk': AdvertMSKSitemap,
    'catalog_spb': AdvertSPBSitemap,
    'catalog_nsk': AdvertNSKSitemap,
    'catalog_ekb': AdvertEKBSitemap,
    'catalog_vk': VKAdvertSitemap,
    'news': NewsSitemap,
    'views': ViewSitemap,
}