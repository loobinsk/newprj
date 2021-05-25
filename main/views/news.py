#-*- coding: utf-8 -*-
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView, FormView, View
from django.core.urlresolvers import reverse
from main.models import News
from gutils.views import AjaxableResponseMixin, BreadcrumbMixin, AjaxPageMixin
from main.form import NewsForm
from datetime import datetime
from gutils.views import class_view_decorator
from django.contrib.auth.decorators import permission_required
from main.views.private import ClientPermMixin
from django.conf import settings


# НОВОСТИ ===========================================
class NewsListView(BreadcrumbMixin, ListView):
    model = News
    template_name = 'main/news/page.html'
    paginate_by = 12

    def get_queryset(self):
        return News.objects.filter(moder=self.request.is_moder,
                                   client=self.request.is_client,
                                   site_id=settings.SITE_ID).order_by('-date').select_related()

    def get_breadcrumbs(self):
        return [(u'Новости', reverse('news:list'))]

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_news')
        return context


class NewsDetailView(BreadcrumbMixin, AjaxPageMixin, DetailView):
    model = News
    template_name = 'main/news/detail.html'
    template_name_ajax = 'main/news/detail-ajax.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(moder=False,
                                   client=False,
                                   site_id=settings.SITE_ID).order_by('-date').select_related()

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_news')
        return context

    def get_breadcrumbs(self):
        return [(u'Новости', reverse('news:list')),
                (self.object.title, reverse('news:detail', kwargs={'pk':self.object.id}))]


class NewsPreviewView(DetailView):
    model = News
    template_name = 'main/news/preview.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(moder=False,
                                   client=False,
                                   site_id=settings.SITE_ID).order_by('-date').select_related()

    def get_context_data(self, **kwargs):
        context = super(NewsPreviewView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_news')
        return context


class NewsListView_Client(ClientPermMixin, BreadcrumbMixin, ListView):
    model = News
    template_name = 'main/client/news/page.html'
    paginate_by = 12

    def get_queryset(self):
        return News.objects.filter(site_id=settings.SITE_ID).order_by('-date').select_related()

    def get_breadcrumbs(self):
        return [(u'Новости', reverse('client:news:list'))]

    def get_context_data(self, **kwargs):
        context = super(NewsListView_Client, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_news')
        return context


class NewsDetailView_Client(ClientPermMixin, BreadcrumbMixin, AjaxPageMixin, DetailView):
    model = News
    template_name = 'main/client/news/detail.html'
    template_name_ajax = 'main/client/news/detail-ajax.html'
    context_object_name = 'news'

    def get_queryset(self):
        return super(NewsDetailView_Client, self).get_queryset().filter(site_id=settings.SITE_ID)

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView_Client, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_news')
        return context

    def get_breadcrumbs(self):
        return [(u'Новости', reverse('client:news:list')),
                (self.object.title, reverse('client:news:detail', kwargs={'pk':self.object.id}))]


class NewsPreviewView_Client(ClientPermMixin, DetailView):
    model = News
    template_name = 'main/client/news/preview.html'
    context_object_name = 'news'

    def get_queryset(self):
        return super(NewsPreviewView_Client, self).get_queryset().filter(site_id=settings.SITE_ID)

    def get_context_data(self, **kwargs):
        context = super(NewsPreviewView_Client, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_news')
        return context


@class_view_decorator(permission_required('main.add_news'))
class NewsCreateView(AjaxableResponseMixin, CreateView):
    model = News
    form_class = NewsForm
    template_name = 'main/client/news/form.html'

    def get_context_data(self, **kwargs):
        context = super(NewsCreateView, self).get_context_data(**kwargs)
        if self.request.is_client:
            context['action'] = reverse('client:news:create')
        else:
            context['action'] = reverse('news:create')
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date = datetime.now()

        return super(NewsCreateView, self).form_valid(form)

    def get_model_dict(self):
        return {
            'url': reverse('client:news:detail', kwargs={'pk': self.object.id})
        }


@class_view_decorator(permission_required('main.change_news'))
class NewsUpdateView(AjaxableResponseMixin, UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'main/client/news/form.html'

    def get_context_data(self, **kwargs):
        context = super(NewsUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:news:edit', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        form.instance.date = datetime.now()
        return super(NewsUpdateView, self).form_valid(form)

    def get_model_dict(self):
        return {
            'url': reverse('client:news:detail', kwargs={'pk': self.object.id})
        }


@class_view_decorator(permission_required('main.delete_news'))
class NewsDeleteView(AjaxableResponseMixin, DeleteView):
    model = News
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super(NewsDeleteView, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return {
            'url': reverse('client:news:list')
        }