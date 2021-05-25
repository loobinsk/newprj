# coding=utf8
from gutils.views import *
from ufile.models import *
from django.views.generic import CreateView, DeleteView
from datetime import datetime
from ufile.forms import UserFileForm
import os


class UserFileCreateView(LoginRequiredMixin, AjaxableResponseMixin, CreateView):
    model = UserFile
    form_class = UserFileForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date = datetime.now()
        form.instance.name = form.cleaned_data['file'].name
        return super(UserFileCreateView, self).form_valid(form)

    def get_model_dict(self):
        return {
            'url': self.object.file.url,
            'name': self.object.name,
        }


class UserFileDeleteView(LoginRequiredMixin, AjaxableResponseMixin, DeleteView):
    model = UserFile
    pk_url_kwarg = 'id'
    success_url = '/'

    def get_model_dict(self):
        return {}


