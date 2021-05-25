#-*- coding: utf-8 -*-
from django.forms.widgets import RadioSelect, FileInput, CheckboxInput, CheckboxSelectMultiple


class BootstrapFormMixin(object):
    def __init__(self, *args, **kwargs):
        super(BootstrapFormMixin, self).__init__(*args, **kwargs)
        for field in self.fields:
            if not isinstance(self.fields[field].widget, (RadioSelect, FileInput, CheckboxInput, CheckboxSelectMultiple)):
                self.fields[field].widget.attrs['class'] = 'form-control ' + self.fields[field].widget.attrs.get('class', '')