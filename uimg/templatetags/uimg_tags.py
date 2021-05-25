#-*- coding: utf-8 -*-
from django import template
from uimg.models import UserImage

register = template.Library()


@register.inclusion_tag('uimg/image-upload-form.html')
def image_upload_multiple(field):
    if field.name in field.form.initial:
        image_list = UserImage.objects.filter(id__in=field.form.initial[field.name])
    else:
        image_list = []
    return {
        'id': field.name,
        'image_list': image_list
    }


@register.inclusion_tag('uimg/image-upload-single-form.html')
def image_upload_single(field):
    image = None
    if field.name in field.form.initial:
        if field.form.initial[field.name]:
            image = UserImage.objects.get(id=field.form.initial[field.name])
    return {
        'id': field.name,
        'image': image
    }


@register.inclusion_tag('uimg/image-list-preview.html')
def image_preview(image_list, url='#'):
    return {
        'image_list': image_list,
        'url': url
    }

@register.inclusion_tag('uimg/image-list-preview-100.html')
def image_preview_100(image_list, url='#'):
    return {
        'image_list': image_list,
        'url': url
    }

@register.inclusion_tag('uimg/image-list-gallery.html')
def image_gallery(image_list, url='#', id='', watermark=True):
    return {
        'image_list': image_list,
        'url': url,
        'id': id,
        'enable_watermark': watermark
    }

@register.inclusion_tag('uimg/image-list.html')
def image_detail(image_list, title='', id=''):
    return {
        'image_list': image_list,
        'title': title,
        'id': id
    }