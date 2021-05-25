#-*- coding: utf-8 -*-
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView, View
from vashdom.models import Password
from gutils.views import BreadcrumbMixin, AjaxPageMixin, AjaxableResponseMixin, AdminRequiredMixin
from django.core.urlresolvers import reverse
from gutils.views import class_view_decorator
from django.contrib.auth.decorators import permission_required
from vashdom.forms import PasswordForm
from django.shortcuts import get_object_or_404
from uprofile.models import User


@class_view_decorator(permission_required('vashdom.view_password'))
class PasswordListView(AdminRequiredMixin, BreadcrumbMixin, ListView):
    model = Password
    context_object_name = 'password_list'
    paginate_by = 50
    template_name = 'main/client/password/page.html'

    def get_queryset(self):
        return Password.objects.all().order_by('-start_date')

    def get_context_data(self, **kwargs):
        context = super(PasswordListView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('vashdom.change_password')
        return context

    def get_breadcrumbs(self):
        return [('Пароли БазаВашДом', reverse('client:password:list'))]


class PasswordUserView(PasswordListView):
    template_name = 'main/client/user/passwords.html'
    user = None

    def get(self, request, *args, **kwargs):
        self.user = User.admin_objects.get(id=kwargs['pk'])
        return super(PasswordUserView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return Password.objects.filter(user=self.user).order_by('-start_date')

    def get_context_data(self, **kwargs):
        context = super(PasswordUserView, self).get_context_data(**kwargs)
        context['agent'] = self.user
        return context

    def get_breadcrumbs(self):
        return [('Пользователи', reverse('client:user:list')),
                (self.user.get_full_name(), reverse('client:user:detail', kwargs={'pk': self.user.id})),
                ('Пароли БазаВашДом', reverse('client:user:passwords', kwargs={'pk': self.user.id})), ]


@class_view_decorator(permission_required('vashdom.view_password'))
class PasswordPreviewView(AdminRequiredMixin, DetailView):
    model = Password
    template_name = 'main/client/password/preview.html'
    context_object_name = 'password'

    def get_context_data(self, **kwargs):
        context = super(PasswordPreviewView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('vashdom.change_password')
        return context


@class_view_decorator(permission_required('vashdom.add_password'))
class PasswordCreateView(AdminRequiredMixin, AjaxableResponseMixin, CreateView):
    model = Password
    form_class = PasswordForm
    template_name = 'main/client/password/form.html'
    success_url = '/'

    def get_initial(self):
        initial = super(PasswordCreateView, self).get_initial()
        if self.request.GET.get('user'):
            try:
                user = User.admin_objects.get(id=self.request.GET.get('user'))
                initial['user'] = user.id
                initial['tel'] = user.tel
            except:
                pass
        return initial

    def get_context_data(self, **kwargs):
        context = super(PasswordCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:password:create')
        return context

    def form_valid(self, form):
        if form.cleaned_data['generate'] or not form.cleaned_data['password']:
            form.instance.gen_password()
        if form.cleaned_data['sms']:
            form.instance.send_sms()
        return super(PasswordCreateView, self).form_valid(form)

    def get_model_dict(self):
        return {
        }


@class_view_decorator(permission_required('vashdom.change_password'))
class PasswordUpdateView(AdminRequiredMixin, AjaxableResponseMixin, UpdateView):
    model = Password
    form_class = PasswordForm
    template_name = 'main/client/password/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(PasswordUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:password:edit', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        if form.cleaned_data['generate'] or not form.cleaned_data['password']:
            form.instance.gen_password()
        if form.cleaned_data['sms']:
            form.instance.send_sms()
        return super(PasswordUpdateView, self).form_valid(form)

    def get_model_dict(self):
        return {
        }


@class_view_decorator(permission_required('vashdom.delete_password'))
class PasswordDeleteView(AdminRequiredMixin, AjaxableResponseMixin, DeleteView):
    model = Password
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super(PasswordDeleteView, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return {
        }


@class_view_decorator(permission_required('vashdom.view_password'))
class PasswordAdvertsListView(AdminRequiredMixin, BreadcrumbMixin, ListView):
    model = Password
    template_name = 'main/client/password/adverts.html'
    context_object_name = 'advert_list'
    password = None
    paginate_by = 50

    def get(self, request, *args, **kwargs):
        self.password = get_object_or_404(Password.objects.all(), id=kwargs['pk'])
        return super(PasswordAdvertsListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.password.adverts.all().order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(PasswordAdvertsListView, self).get_context_data(**kwargs)
        context['password'] = self.password
        return context

    def get_breadcrumbs(self):
        return super(PasswordAdvertsListView, self).get_breadcrumbs() + [
            ('Пароли ВашДом', reverse('client:password:list')),
            ('Объявления', reverse('client:password:adverts', kwargs={'pk': self.password.id})),
            ]