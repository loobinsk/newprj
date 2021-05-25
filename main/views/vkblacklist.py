#-*- coding: utf-8 -*-
from django.views.generic import ListView, DeleteView
from main.models import VKBlacklist
from gutils.views import BreadcrumbMixin, AjaxableResponseMixin
from django.core.urlresolvers import reverse
from gutils.views import class_view_decorator
from django.contrib.auth.decorators import permission_required
from main.form import VKBlacklistFilterForm


@class_view_decorator(permission_required('main.view_vkblacklist'))
class VKBlacklistListView(BreadcrumbMixin, ListView):
    """
    Список городов
    """
    model = VKBlacklist
    context_object_name = 'blacklist_list'
    paginate_by = 50
    template_name = 'main/client/vkblacklist/page.html'

    def get_queryset(self):
        qs = super(VKBlacklistListView, self).get_queryset()
        if self.request.GET.get('vkid'):
            qs = qs.filter(vkid=self.request.GET.get('vkid'))
        return qs

    def get_breadcrumbs(self):
        return super(VKBlacklistListView, self).get_breadcrumbs() + [('Черный список Вконтакте', reverse('client:vkblacklist:list'))]

    def get_context_data(self, **kwargs):
        context = super(VKBlacklistListView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_vkblacklist')
        context['filter_form'] = VKBlacklistFilterForm(data=self.request.GET)
        return context


@class_view_decorator(permission_required('main.delete_vkblacklist'))
class VKBlacklistDeleteView(AjaxableResponseMixin, DeleteView):
    model = VKBlacklist
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super(VKBlacklistDeleteView, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return {
            'url': reverse('client:vkblacklist:list')
        }