#-*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from main.models import Subscribe, SubscribeCode
from datetime import datetime
from django.shortcuts import get_object_or_404, Http404


class SubscribeView(TemplateView):
    template_name = 'main/subscribe/subscribe.html'
    subscribe = None

    def get(self, request, *args, **kwargs):
        code_list = SubscribeCode.objects.filter(code=request.GET.get('code'), active=True)
        if code_list:
            code = code_list[0]
            self.subscribe = code.subscribe
            self.subscribe.subscribed.add(code.user)
        # else:
        #     raise Http404()
        return super(SubscribeView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SubscribeView, self).get_context_data(**kwargs)
        context['subscribe'] = self.subscribe
        return context


class UnsubscribeView(TemplateView):
    template_name = 'main/subscribe/unsubscribe.html'
    subscribe = None

    def get(self, request, *args, **kwargs):
        code_list = SubscribeCode.objects.filter(code=request.GET.get('code'), active=False)
        if code_list:
            code = code_list[0]
            self.subscribe = code.subscribe
            self.subscribe.unsubscribed.add(code.user)
        # else:
        #     raise Http404()
        return super(UnsubscribeView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UnsubscribeView, self).get_context_data(**kwargs)
        context['subscribe'] = self.subscribe
        return context


