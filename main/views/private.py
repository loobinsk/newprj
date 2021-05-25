#-*- coding: utf-8 -*-
from main.models import Company
from django.http import HttpResponseRedirect
from gutils.views import AjaxableResponseMixin
from django.conf import settings
from django.views.generic import FormView
from mail_templated import send_mail
from main.form import FeedbackForm_Client
from uprofile.models import User


class ClientPermMixin(object):
    """
    Проверка прав на доступ в клиентскую часть
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            company = request.user.company
            if (request.user.has_perm('uprofile.view_client') and not request.is_moder) or (request.user.has_perm('uprofile.view_moderate') and request.is_moder):
                return super(ClientPermMixin, self).dispatch(request, *args, **kwargs)
            elif company and (company.status == Company.STATUS_ACTIVE) and (request.user.status == User.STATUS_ACTIVE) and not request.is_moder:
                # проверка доступа по дням
                if request.user.has_access():
                    return super(ClientPermMixin, self).dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to='/login/')


class ModerPermMixin(object):
    """
    Проверка прав на доступ в модераторскую часть
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            if (request.user.has_perm('uprofile.view_moderate') and request.is_moder):
                return super(ModerPermMixin, self).dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to='/login/')


class FeedbackView_Client(ClientPermMixin, AjaxableResponseMixin, FormView):
    form_class = FeedbackForm_Client
    success_url = '/'
    template_name = 'main/client/feedback.html'

    def form_valid(self, form):
        emails = settings.NOTICE_SUPPORT_EMAIL
        if self.request.user.company:
            if self.request.user.company.id == 1:
                emails = settings.NOTICE_SUPPORT_MSK_EMAIL
            elif self.request.user.company.id == 2:
                emails = settings.NOTICE_SUPPORT_SPB_EMAIL
        elif self.request.user.town:
            if self.request.user.town.id == 1:
                emails = settings.NOTICE_SUPPORT_MSK_EMAIL
            elif self.request.user.town.id == 2:
                emails = settings.NOTICE_SUPPORT_SPB_EMAIL
        send_mail('main/email/feedback_client.html', {
            'user': self.request.user,
            'company': self.request.user.company,
            'is_moder': self.request.user.has_perms('uprofile.view_moderate'),
            'body': form.cleaned_data['desc'],
            'title': form.cleaned_data['title'],
            'subject': 'Новый вопрос из личного кабинета'
        },
              recipient_list=emails,
              fail_silently=True)
        return super(FeedbackView_Client, self).form_valid(form)

    def get_model_dict(self):
        return {
            'message': 'Ваш запрос отправлен'
        }
