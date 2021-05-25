# -*- coding: utf-8 -*-
from django.views.generic import UpdateView, FormView
from gutils.views import BreadcrumbMixin, AjaxableResponseMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from vashdom.forms import ProfileForm, PaymentOrderForm, AvatarForm
from vashdom.models import Tariff, Password, VashdomUser
from django.db.models import Sum
from main.models import Town
from sorl.thumbnail import get_thumbnail


class ClientPermMixin(object):
    """
    Проверка прав на доступ в клиентскую часть
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return super(ClientPermMixin, self).dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to='/login/')


class ActiveUserProfileView(ClientPermMixin, BreadcrumbMixin, AjaxableResponseMixin, UpdateView):
    template_name = 'vashdom/profile.html'
    model = VashdomUser
    form_class = ProfileForm
    success_url = 'profile'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(ActiveUserProfileView, self).get_context_data(**kwargs)
        context['payment_form'] = PaymentOrderForm(town=self.request.current_town)
        context['tariff_list'] = Tariff.objects.filter(hidden=False).order_by('order')
        context['avatar_form'] = AvatarForm()
        context['payment_form'] = PaymentOrderForm(town=self.request.current_town, user=self.object)
        context['password_list'] = self.object.vashdom_passwords.all().order_by('-end_date')
        return context

    def get_object(self, queryset=None):
        user_list = VashdomUser.objects.filter(id=self.request.user.id)
        if user_list:
            return user_list[0]
        else:
            return None

    def get_model_dict(self):
        return {}

    def get_breadcrumbs(self):
        return super(ActiveUserProfileView, self).get_breadcrumbs() + [('Личный кабинет', reverse('profile:my'))]


class ChangeAvatarView(ClientPermMixin, AjaxableResponseMixin, FormView):
    form_class = AvatarForm
    success_url = '/'

    def form_valid(self, form):
        self.request.user.image = form.cleaned_data['image']
        self.request.user.save()
        return super(ChangeAvatarView, self).form_valid(form)

    def get_model_dict(self):
        thumb = get_thumbnail(self.request.user.image, '150x150', crop='center')
        return {
            'url': thumb.url
        }
