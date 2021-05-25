#-*- coding: utf-8 -*-
from django import forms
from uprofile.models import User
from gutils.forms import BootstrapFormMixin


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'tel', 'independent']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['independent'].help_text = 'Установите эту галочку, если хотите работать как независимый агент, ' \
                                               'оплачивать доступ самостоятельно и независимо от агентства'

    def clean_tel(self):
        from main.models import clear_tel
        return clear_tel(self.cleaned_data['tel'])


class AvatarForm(forms.Form):
    image = forms.ImageField()