#-*- coding: utf-8 -*-
from django import forms
from ucomment.models import *
from gutils.forms import BootstrapFormMixin
from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError


class CommentForm(BootstrapFormMixin, forms.ModelForm):
    captcha = CaptchaField(error_messages={'required': 'Введите символы с картинки', 'invalid': 'Неправильные символы с картинки'}, required=False)

    class Meta:
        model = Comment
        fields = ['text', 'key', 'parent', 'url', 'name']

    def __init__(self, user, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.user = user
        self.fields['text'].widget.attrs['rows'] = 4
        self.fields['text'].widget.attrs['placeholder'] = 'Напишите отзыв...'
        self.fields['key'].widget = forms.HiddenInput()
        self.fields['parent'].widget = forms.HiddenInput()
        self.fields['url'].widget = forms.HiddenInput()

    def clean_captcha(self):
        if not self.user.is_authenticated():
            data = self.data.get('captcha_1', '')
            if not data:
                raise ValidationError(u'Введите текст с картинки', code='required')
        return self.cleaned_data['captcha']
