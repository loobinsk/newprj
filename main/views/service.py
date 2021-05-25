#-*- coding: utf-8 -*-
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.core.urlresolvers import reverse
from main.models import ConnectedService, Company
from gutils.views import AjaxableResponseMixin, BreadcrumbMixin, AjaxPageMixin, AdminRequiredMixin
from main.form import ConnectedServiceForm
from uprofile.models import User
from django.http.response import Http404


class ConnectedServicePreviewView(AdminRequiredMixin, DetailView):
    model = ConnectedService
    template_name = 'main/client/service/preview.html'
    context_object_name = 'service'


class ConnectedServiceCreateView(AdminRequiredMixin, AjaxableResponseMixin, CreateView):
    model = ConnectedService
    form_class = ConnectedServiceForm
    template_name = 'main/client/service/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ConnectedServiceCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:service:create')
        return context

    def get(self, request, *args, **kwargs):
        company_list = Company.objects.filter(id=request.GET.get('company'))
        if company_list:
            self.initial['company'] = company_list[0].id
        user_list = User.objects.filter(id=request.GET.get('user'))
        if user_list:
            self.initial['user'] = user_list[0].id
        if not company_list and not user_list:
            raise Http404()
        return super(ConnectedServiceCreateView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        return super(ConnectedServiceCreateView, self).form_valid(form)

    def get_model_dict(self):
        return {
            'url': reverse('client:service:preview', kwargs={'pk': self.object.id})
        }


class ConnectedServiceUpdateView(AdminRequiredMixin, AjaxableResponseMixin, UpdateView):
    model = ConnectedService
    form_class = ConnectedServiceForm
    template_name = 'main/client/service/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ConnectedServiceUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:service:edit', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        return super(ConnectedServiceUpdateView, self).form_valid(form)

    def get_model_dict(self):
        return {
            'url': reverse('client:service:preview', kwargs={'pk': self.object.id})
        }


class ConnectedServiceDeleteView(AdminRequiredMixin, AjaxableResponseMixin, DeleteView):
    model = ConnectedService
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super(ConnectedServiceDeleteView, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return { }