#-*- coding: utf-8 -*-
from django import template
from ufile.forms import UserFileForm
from ufile.models import UserFile

register = template.Library()


@register.inclusion_tag('ufile/file-upload-form.html')
def file_upload_multiple(field):
    if field.name in field.form.initial:
        file_list = UserFile.objects.filter(id__in=field.form.initial[field.name])
    else:
        file_list = []
    return {
        'id': field.name,
        'form': UserFileForm(),
        'file_list': file_list
    }

@register.inclusion_tag('ufile/file-list-block.html', takes_context=True)
def file_list_block(context, file_list, title='Файлы'):
    return {
        'title': title,
        'file_list': file_list,
        'STATIC_URL': context['STATIC_URL']
    }
