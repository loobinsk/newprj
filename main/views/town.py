#-*- coding: utf-8 -*-
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from main.models import Town, District, Metro
from gutils.views import BreadcrumbMixin, AjaxPageMixin, AjaxableResponseMixin
from django.core.urlresolvers import reverse
from gutils.views import class_view_decorator
from django.contrib.auth.decorators import permission_required
from main.form import TownForm


@class_view_decorator(permission_required('main.view_town'))
class TownListView(BreadcrumbMixin, ListView):
    """
    Список городов
    """
    model = Town
    context_object_name = 'town_list'
    paginate_by = 50
    template_name = 'main/client/town/page.html'

    def get_breadcrumbs(self):
        return super(TownListView, self).get_breadcrumbs() + [('Города', reverse('client:town:list'))]

    def get_context_data(self, **kwargs):
        context = super(TownListView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_town')
        return context


@class_view_decorator(permission_required('main.view_town'))
class TownDetailView(BreadcrumbMixin, AjaxPageMixin, DetailView):
    model = Town
    template_name = 'main/client/town/detail.html'
    template_name_ajax = 'main/client/town/detail-ajax.html'
    context_object_name = 'town'

    def get_context_data(self, **kwargs):
        context = super(TownDetailView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_town')
        context['district_list'] = District.objects.filter(town=self.object)
        context['metro_list'] = Metro.objects.filter(town=self.object)
        return context

    def get_breadcrumbs(self):
        return [(u'Города', reverse('client:town:list')),
                (self.object.title, reverse('client:town:detail', kwargs={'pk':self.object.id}))]


@class_view_decorator(permission_required('main.view_town'))
class TownPreviewView(DetailView):
    model = Town
    template_name = 'main/client/town/preview.html'
    context_object_name = 'town'

    def get_context_data(self, **kwargs):
        context = super(TownPreviewView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_town')
        return context


@class_view_decorator(permission_required('main.add_town'))
class TownCreateView(AjaxableResponseMixin, CreateView):
    model = Town
    form_class = TownForm
    template_name = 'main/client/town/form.html'

    def get_context_data(self, **kwargs):
        context = super(TownCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:town:create')
        return context

    def get_model_dict(self):
        return {
            'url': reverse('client:town:detail', kwargs={'pk': self.object.id})
        }


@class_view_decorator(permission_required('main.change_town'))
class TownUpdateView(AjaxableResponseMixin, UpdateView):
    model = Town
    form_class = TownForm
    template_name = 'main/client/town/form.html'

    def get_context_data(self, **kwargs):
        context = super(TownUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:town:edit', kwargs={'pk': self.object.id})
        return context

    def get_model_dict(self):
        return {
            'url': reverse('client:town:detail', kwargs={'pk': self.object.id})
        }


@class_view_decorator(permission_required('main.delete_town'))
class TownDeleteView(AjaxableResponseMixin, DeleteView):
    model = Town
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super(TownDeleteView, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return {
            'url': reverse('client:town:list')
        }