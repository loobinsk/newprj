#-*- coding: utf-8 -*-
from django import forms
from ufile.models import UserFile
from django.template import loader, Context


class MultiUploadFileWidget(forms.MultipleHiddenInput):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('ufile/file-upload-input.html')
        return tmpl.render(Context({
            'input': super(MultiUploadFileWidget, self).render(name, value, attrs=None, choices=()),
            'id': name,
        }))


class UserFileForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ['file']
