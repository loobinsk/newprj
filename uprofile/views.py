#-*- coding: utf-8 -*-
from gutils.views import LoginRequiredMixin, AjaxableResponseMixin, BreadcrumbMixin
from django.views.generic import UpdateView, FormView, DetailView
from uprofile.models import User
from uprofile.forms import ProfileForm, AvatarForm
from django.core.urlresolvers import reverse
from main.views.private import ClientPermMixin
from sorl.thumbnail import get_thumbnail


class ActiveUserProfileView(ClientPermMixin, BreadcrumbMixin, AjaxableResponseMixin, UpdateView):
    template_name = 'uprofile/my-profile.html'
    model = User
    form_class = ProfileForm
    success_url = 'profile'

    def get_context_data(self, **kwargs):
        context = super(ActiveUserProfileView, self).get_context_data(**kwargs)
        context['avatar_form'] = AvatarForm()
        return context

    def get_object(self, queryset=None):
        user_list = User.objects.filter(id=self.request.user.id)
        if user_list:
            return user_list[0]
        else:
            return None

    def get_model_dict(self):
        return {}

    def get_breadcrumbs(self):
        return super(ActiveUserProfileView, self).get_breadcrumbs() + [('Мой профиль', reverse('profile:my'))]


class ChangeAvatarView(ClientPermMixin, AjaxableResponseMixin, FormView):
    form_class = AvatarForm
    success_url = '/'

    def form_valid(self, form):
        self.request.user.image = form.cleaned_data['image']
        self.request.user.save()
        return super(ChangeAvatarView, self).form_valid(form)

    def get_model_dict(self):
        thumb = get_thumbnail(self.request.user.image, '200x200', crop='center')
        return thumb.url