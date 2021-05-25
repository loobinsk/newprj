#-*- coding: utf-8 -*-
from django import forms
from uvideo.models import UserVideo
from django.template import loader, Context
from gutils.forms import BootstrapFormMixin


class UploadVideoWidget(forms.HiddenInput):
    def render(self, name, value, attrs=None):
        tmpl = loader.get_template('uvideo/video-upload-input.html')
        return tmpl.render(Context({
            'input': super(UploadVideoWidget, self).render(name, value, attrs=None),
            'id': name,
        }))


class UserVideoForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = UserVideo
        fields = ['url']
