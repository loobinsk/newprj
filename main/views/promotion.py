#-*- coding: utf-8 -*-
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from main.models import Promotion, Promocode
from gutils.views import BreadcrumbMixin, AjaxableResponseMixin, AdminRequiredMixin
from django.core.urlresolvers import reverse
from gutils.views import class_view_decorator
from django.contrib.auth.decorators import permission_required
from main.form import PromotionForm, PromocodeForm
from django.shortcuts import get_object_or_404
from django.db.models import Q, Count


@class_view_decorator(permission_required('main.view_promotion'))
class PromotionListView(AdminRequiredMixin, BreadcrumbMixin, ListView):
    model = Promotion
    context_object_name = 'promotion_list'
    paginate_by = 50
    template_name = 'main/client/promotion/page.html'

    def get_queryset(self):
        return Promotion.objects.all().order_by('-start_date').\
            annotate(count_promocodes=Count('promocode')).\
            select_related('site')

    def get_context_data(self, **kwargs):
        context = super(PromotionListView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_promotion')
        return context

    def get_breadcrumbs(self):
        return [('Промоакции', reverse('client:promotion:list'))]


@class_view_decorator(permission_required('main.view_promotion'))
class PromotionPreviewView(AdminRequiredMixin, DetailView):
    model = Promotion
    template_name = 'main/client/promotion/preview.html'
    context_object_name = 'promotion'

    def get_context_data(self, **kwargs):
        context = super(PromotionPreviewView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_promotion')
        return context


@class_view_decorator(permission_required('main.add_promotion'))
class PromotionCreateView(AdminRequiredMixin, AjaxableResponseMixin, CreateView):
    model = Promotion
    form_class = PromotionForm
    template_name = 'main/client/promotion/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(PromotionCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:promotion:create')
        return context

    def form_valid(self, form):
        return super(PromotionCreateView, self).form_valid(form)

    def get_model_dict(self):
        return { }


@class_view_decorator(permission_required('main.change_promotion'))
class PromotionUpdateView(AdminRequiredMixin, AjaxableResponseMixin, UpdateView):
    model = Promotion
    form_class = PromotionForm
    template_name = 'main/client/promotion/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(PromotionUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:promotion:edit', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        return super(PromotionUpdateView, self).form_valid(form)

    def get_model_dict(self):
        return { }


@class_view_decorator(permission_required('main.delete_promotion'))
class PromotionDeleteView(AdminRequiredMixin, AjaxableResponseMixin, DeleteView):
    model = Promotion
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super(PromotionDeleteView, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return { }
    
    
@class_view_decorator(permission_required('main.view_promocode'))
class PromocodeListView(AdminRequiredMixin, BreadcrumbMixin, ListView):
    model = Promocode
    context_object_name = 'promocode_list'
    paginate_by = 50
    template_name = 'main/client/promocode/page.html'
    promotion = None

    def get(self, request, *args, **kwargs):
        if self.request.GET.get('promotion'):
            self.promotion = get_object_or_404(Promotion, id=self.request.GET.get('promotion'))
        return super(PromocodeListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        query = Q()
        if self.promotion:
            query &= Q(promotion=self.promotion)
        return Promocode.admin_objects.filter(query).order_by('-id').select_related('promotion')

    def get_context_data(self, **kwargs):
        context = super(PromocodeListView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_promocode')
        context['promotion'] = self.promotion
        return context

    def get_breadcrumbs(self):
        return [('Промокоды', reverse('client:promocode:list'))]


@class_view_decorator(permission_required('main.view_promocode'))
class PromocodePreviewView(AdminRequiredMixin, DetailView):
    model = Promocode
    template_name = 'main/client/promocode/preview.html'
    context_object_name = 'promocode'
    queryset = Promocode.admin_objects.all()

    def get_context_data(self, **kwargs):
        context = super(PromocodePreviewView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_promocode')
        return context


@class_view_decorator(permission_required('main.add_promocode'))
class PromocodeCreateView(AdminRequiredMixin, AjaxableResponseMixin, CreateView):
    model = Promocode
    form_class = PromocodeForm
    template_name = 'main/client/promocode/form.html'
    success_url = '/'
    queryset = Promocode.admin_objects.all()

    def get_context_data(self, **kwargs):
        context = super(PromocodeCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:promocode:create')
        return context

    def form_valid(self, form):
        return super(PromocodeCreateView, self).form_valid(form)

    def get_model_dict(self):
        return { }


@class_view_decorator(permission_required('main.change_promocode'))
class PromocodeUpdateView(AdminRequiredMixin, AjaxableResponseMixin, UpdateView):
    model = Promocode
    form_class = PromocodeForm
    template_name = 'main/client/promocode/form.html'
    success_url = '/'
    queryset = Promocode.admin_objects.all()

    def get_context_data(self, **kwargs):
        context = super(PromocodeUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:promocode:edit', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        return super(PromocodeUpdateView, self).form_valid(form)

    def get_model_dict(self):
        return { }


@class_view_decorator(permission_required('main.delete_promocode'))
class PromocodeDeleteView(AdminRequiredMixin, AjaxableResponseMixin, DeleteView):
    model = Promocode
    success_url = '/'
    queryset = Promocode.admin_objects.all()

    def delete(self, request, *args, **kwargs):
        return super(PromocodeDeleteView, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return { }