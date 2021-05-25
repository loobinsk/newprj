#-*- coding: utf-8 -*-
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from main.models import Vacancy
from gutils.views import BreadcrumbMixin, AjaxPageMixin, AjaxableResponseMixin, UpdateAccessMixin
from django.core.urlresolvers import reverse
from gutils.views import class_view_decorator
from django.contrib.auth.decorators import permission_required
from main.form import VacancyForm
from datetime import datetime


class VacancyListView(BreadcrumbMixin, ListView):
    """
    Список городов
    """
    model = Vacancy
    context_object_name = 'vacancy_list'
    paginate_by = 50
    template_name = 'main/vacancy/page.html'

    def get_breadcrumbs(self):
        return super(VacancyListView, self).get_breadcrumbs() + [('Вакансии', reverse('client:vacancy:list'))]


class VacancyDetailView(BreadcrumbMixin, DetailView):
    model = Vacancy
    template_name = 'main/vacancy/detail.html'
    context_object_name = 'vacancy'

    def get_breadcrumbs(self):
        return [(u'Вакансии', reverse('vacancy:list')),
                (self.object.title, reverse('vacancy:detail', kwargs={'pk':self.object.id}))]


@class_view_decorator(permission_required('main.view_vacancy'))
class VacancyListView_Client(BreadcrumbMixin, ListView):
    """
    Список городов
    """
    model = Vacancy
    context_object_name = 'vacancy_list'
    paginate_by = 50
    template_name = 'main/client/vacancy/page.html'

    def get_breadcrumbs(self):
        return super(VacancyListView_Client, self).get_breadcrumbs() + [('Вакансии', reverse('vacancy:list'))]

    def get_queryset(self):
        return Vacancy.objects.filter(user=self.request.user).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(VacancyListView_Client, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_vacancy')
        return context


@class_view_decorator(permission_required('main.view_vacancy'))
class VacancyDetailView_Client(BreadcrumbMixin, AjaxPageMixin, DetailView):
    model = Vacancy
    template_name = 'main/client/vacancy/detail.html'
    template_name_ajax = 'main/client/vacancy/detail-ajax.html'
    context_object_name = 'vacancy'

    def get_context_data(self, **kwargs):
        context = super(VacancyDetailView_Client, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_vacancy')
        return context

    def get_breadcrumbs(self):
        return [(u'Вакансии', reverse('client:vacancy:list')),
                (self.object.title, reverse('client:vacancy:detail', kwargs={'pk':self.object.id}))]


@class_view_decorator(permission_required('main.view_vacancy'))
class VacancyPreviewView(DetailView):
    model = Vacancy
    template_name = 'main/client/vacancy/preview.html'
    context_object_name = 'vacancy'

    def get_context_data(self, **kwargs):
        context = super(VacancyPreviewView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_vacancy')
        return context


@class_view_decorator(permission_required('main.add_vacancy'))
class VacancyCreateView(AjaxableResponseMixin, CreateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = 'main/client/vacancy/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(VacancyCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:vacancy:create')
        return context

    def get_model_dict(self):
        return {
            'url': reverse('client:vacancy:detail', kwargs={'pk': self.object.id})
        }

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date = datetime.now()
        return super(VacancyCreateView, self).form_valid(form)


@class_view_decorator(permission_required('main.change_vacancy'))
class VacancyUpdateView(AjaxableResponseMixin, UpdateAccessMixin, UpdateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = 'main/client/vacancy/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(VacancyUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:vacancy:edit', kwargs={'pk': self.object.id})
        return context

    def get_model_dict(self):
        return {
            'url': reverse('client:vacancy:detail', kwargs={'pk': self.object.id})
        }


@class_view_decorator(permission_required('main.delete_vacancy'))
class VacancyDeleteView(AjaxableResponseMixin, UpdateAccessMixin, DeleteView):
    model = Vacancy
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super(VacancyDeleteView, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return {
            'url': reverse('client:vacancy:list')
        }