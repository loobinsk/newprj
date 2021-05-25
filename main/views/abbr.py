#-*- coding: utf-8 -*-
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.core.urlresolvers import reverse
from main.models import Abbr
from gutils.views import AjaxableResponseMixin, BreadcrumbMixin, AjaxPageMixin, AdminRequiredMixin
from main.form import AbbrForm
from datetime import datetime


# Сокращения ===========================================
class AbbrListView(AdminRequiredMixin, BreadcrumbMixin, ListView):
    model = Abbr
    template_name = 'main/client/abbr/page.html'
    paginate_by = 20

    def get_breadcrumbs(self):
        return [(u'Сокращения', reverse('client:abbr:list'))]

    def get_context_data(self, **kwargs):
        context = super(AbbrListView, self).get_context_data()
        context['form'] = AbbrForm
        return context


class AbbrPreviewView(AdminRequiredMixin, DetailView):
    model = Abbr
    template_name = 'main/client/abbr/preview.html'
    context_object_name = 'abbr'

    def get_context_data(self, **kwargs):
        context = super(AbbrPreviewView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_abbr')
        return context


class AbbrCreateView(AdminRequiredMixin, AjaxableResponseMixin, CreateView):
    model = Abbr
    form_class = AbbrForm
    template_name = 'main/client/abbr/form.html'
    success_url = '/client/abbr/'


class AbbrDeleteView(AdminRequiredMixin, AjaxableResponseMixin, DeleteView):
    model = Abbr
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super(AbbrDeleteView, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return {
            'url': reverse('client:abbr:list')
        }