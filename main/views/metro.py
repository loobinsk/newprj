#-*- coding: utf-8 -*-
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView, View
from main.models import Town, Metro
from gutils.views import BreadcrumbMixin, AjaxPageMixin, AjaxableResponseMixin
from django.core.urlresolvers import reverse
from gutils.views import class_view_decorator
from django.contrib.auth.decorators import permission_required
from main.form import MetroForm
from django.shortcuts import get_object_or_404
from annoying.decorators import ajax_request
from django.utils.decorators import method_decorator


@class_view_decorator(permission_required('main.view_metro'))
class MetroPreviewView(DetailView):
    model = Metro
    template_name = 'main/client/metro/preview.html'
    context_object_name = 'metro'

    def get_context_data(self, **kwargs):
        context = super(MetroPreviewView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_metro')
        return context


@class_view_decorator(permission_required('main.add_metro'))
class MetroCreateView(AjaxableResponseMixin, CreateView):
    model = Metro
    form_class = MetroForm
    template_name = 'main/client/metro/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(MetroCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:metro:create')
        return context

    def get(self, request, *args, **kwargs):
        town = get_object_or_404(Town, id=request.GET.get('town'))
        self.initial['town'] = town.id
        return super(MetroCreateView, self).get(request, *args, **kwargs)

    def get_model_dict(self):
        return {
        }


@class_view_decorator(permission_required('main.change_metro'))
class MetroUpdateView(AjaxableResponseMixin, UpdateView):
    model = Metro
    form_class = MetroForm
    template_name = 'main/client/metro/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(MetroUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:metro:edit', kwargs={'pk': self.object.id})
        return context

    def get_model_dict(self):
        return {
        }


@class_view_decorator(permission_required('main.delete_metro'))
class MetroDeleteView(AjaxableResponseMixin, DeleteView):
    model = Metro
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super(MetroDeleteView, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return {
        }


class MetroTypeheadView(View):
    """
    Автодополнение метро
    """
    @method_decorator(ajax_request)
    def get(self, request, *args, **kwargs):
        options = []
        if self.request.GET.get('query'):
            town_id = request.GET.get('town', None)
            town = None
            if town_id:
                town_list = Town.objects.filter(id=town_id)
                if town_list:
                    town = town_list[0]
            if not town:
                town = request.current_town
            qs = Metro.objects.filter(title__icontains=self.request.GET.get('query').strip(), town=town)
            for metro in qs[:10]:
                options.append({
                    'id': metro.id,
                    'title': metro.title
                })
        return options