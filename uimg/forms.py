#-*- coding: utf-8 -*-
from django import forms
from uimg.models import UserImage
from django.template import loader, Context
from gutils.forms import BootstrapFormMixin


class MultiUploadImageWidget(forms.MultipleHiddenInput):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('uimg/image-upload-input.html')
        return tmpl.render(Context({
            'input': super(MultiUploadImageWidget, self).render(name, value, attrs=None, choices=()),
            'id': name,
        }))


class SingleUploadImageWidget(forms.HiddenInput):
    def render(self, name, value, attrs=None):
        tmpl = loader.get_template('uimg/image-upload-input.html')
        return tmpl.render(Context({
            'input': super(SingleUploadImageWidget, self).render(name, value, attrs=None),
            'id': name,
            }))


class ImageDescForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ['desc']