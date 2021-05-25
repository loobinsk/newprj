# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.sites.models import Site
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField


class Metatag(models.Model):
    """
    Метатеги для страниц
    """
    name = models.CharField('Название', max_length=250)
    code = models.CharField('Cимвольный код', max_length=50, default='', blank=True, null=True)
    site = models.ForeignKey(Site, verbose_name='Сайт')
    path = models.CharField('URL', max_length=250, default='', blank=True, null=True)

    title = models.CharField('Title', max_length=250, default='', blank=True, null=True)
    keywords = models.CharField('Keywords', max_length=250, default='', blank=True, null=True)
    description = models.CharField('Description', max_length=250, default='', blank=True, null=True)
    page_title = models.CharField('Page title', max_length=250, default='', blank=True, null=True)
    og_title = models.CharField('Opengraph title', max_length=250, default='', blank=True, null=True)
    og_image = models.CharField('Opengraph image url', max_length=250, default='', blank=True, null=True)
    seotext = RichTextField('SEO-текст', default='', blank=True, null=True)

    class Meta:
        verbose_name = 'Метатег'
        verbose_name_plural = 'Метатеги'


    def render_title(self):
        return mark_safe(u'<title>%s</title>' % self.title)

    def render_keywords(self):
        return mark_safe(u'<meta name="keywords" content="%s"/>' % self.keywords)

    def render_description(self):
        return mark_safe(u'<meta name="description" content="%s"/>' % self.description)

    def render_page_title(self):
        return mark_safe(self.page_title)

    def render_ogtitle(self):
        return mark_safe(u'<meta name="og:title" content="%s"/>' % self.og_title)

    def render_ogimage(self):
        return mark_safe(u'<meta name="og:image" content="%s"/>' % self.og_image)