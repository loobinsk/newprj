#-*- coding: utf-8 -*-
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView, View
from main.models import District, Town, Metro
from gutils.views import BreadcrumbMixin, AjaxPageMixin, AjaxableResponseMixin
from django.core.urlresolvers import reverse
from gutils.views import class_view_decorator
from django.contrib.auth.decorators import permission_required
from main.form import DistrictForm
from django.shortcuts import get_object_or_404
from annoying.decorators import ajax_request
from django.utils.decorators import method_decorator


@class_view_decorator(permission_required('main.view_district'))
class DistrictPreviewView(DetailView):
    model = District
    template_name = 'main/client/district/preview.html'
    context_object_name = 'district'

    def get_context_data(self, **kwargs):
        context = super(DistrictPreviewView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_district')
        return context


@class_view_decorator(permission_required('main.add_district'))
class DistrictCreateView(AjaxableResponseMixin, CreateView):
    model = District
    form_class = DistrictForm
    template_name = 'main/client/district/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(DistrictCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:district:create')
        return context

    def get(self, request, *args, **kwargs):
        town = get_object_or_404(Town, id=request.GET.get('town'))
        self.initial['town'] = town.id
        return super(DistrictCreateView, self).get(request, *args, **kwargs)

    def get_model_dict(self):
        return {
        }


@class_view_decorator(permission_required('main.change_district'))
class DistrictUpdateView(AjaxableResponseMixin, UpdateView):
    model = District
    form_class = DistrictForm
    template_name = 'main/client/district/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(DistrictUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:district:edit', kwargs={'pk': self.object.id})
        return context

    def get_model_dict(self):
        return {
        }


@class_view_decorator(permission_required('main.delete_district'))
class DistrictDeleteView(AjaxableResponseMixin, DeleteView):
    model = District
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super(DistrictDeleteView, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return {
        }


class DistrictTypeheadView(View):
    """
    Автодополнение районов
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
            qs = District.objects.filter(title__icontains=self.request.GET.get('query').strip(), town=town)
            for district in qs[:10]:
                options.append({
                    'id': district.id,
                    'title': district.title
                })
        return options