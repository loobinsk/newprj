#-*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap, FlatPageSitemap
from main.models import *
from django.core.urlresolvers import reverse


class HttpsFlatPageSitemap(FlatPageSitemap):
    protocol = 'http'

sitemaps = {
}