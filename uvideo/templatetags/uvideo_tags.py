#-*- coding: utf-8 -*-
from django import template
from uvideo.forms import UserVideoForm
from uvideo.models import UserVideo

register = template.Library()


@register.inclusion_tag('uvideo/video-upload-form.html')
def video_upload(field):
    if field.name in field.form.initial:
        video_list = UserVideo.objects.filter(id=field.form.initial[field.name])
    else:
        video_list = []
    return {
        'id': field.name,
        'form': UserVideoForm(),
        'video_list': video_list
    }

@register.inclusion_tag('uvideo/video.html')
def video(value):
    return {
        'video': value
    }

@register.inclusion_tag('uvideo/video-preview.html')
def video_preview(value, url='#'):
    return {
        'video': value,
        'url': url
    }

@register.inclusion_tag('uvideo/video-media.html')
def video_media():
    return {}
