# coding=utf8
import json
from django.template.response import HttpResponse
import hashlib
from django.core.cache import cache
from django.shortcuts import render_to_response
from django.forms.models import model_to_dict
from functools import wraps
from django.utils.decorators import method_decorator
from django.template import Context


class AjaxPageMixin(object):
    template_name_ajax = None

    def dispatch(self, request, *args, **kwargs):
        if self.request.is_ajax():
            self.template_name = self.template_name_ajax
        return super(AjaxPageMixin, self).dispatch(request, *args, **kwargs)


class LoginRequiredMixin(object):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated():
            return render_to_response('main/need_auth.html')
        else:
            return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class AdminRequiredMixin(object):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_staff:
            return render_to_response('main/need_auth.html')
        else:
            return super(AdminRequiredMixin, self).dispatch(*args, **kwargs)


class OwnerRequiredMixin(object):
    def dispatch(self, *args, **kwargs):
        access = False
        if self.request.user.is_authenticated():
            if hasattr(self.request, 'domain_company'):
                if self.request.domain_company.user == self.request.user or self.request.domain_company.moderators.filter(id=self.request.user.id).count():
                    access = True

        if access:
            return super(OwnerRequiredMixin, self).dispatch(*args, **kwargs)
        else:
            return render_to_response('main/need_auth.html')


class AjaxableResponseMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            error_message = u''
            for field in form.errors:
                error_message += u'<p class="error"><span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span> %s</p>' % form.errors[field][0]
            return self.render_to_json_response({'message': error_message}, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'id': self.object.pk if hasattr(self, 'object') else None,
                'object': self.get_model_dict(),
                }
            return self.render_to_json_response(data)
        else:
            return response

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(AjaxableResponseMixin, self).dispatch(request, *args, **kwargs)
        except Exception as ex:
            if self.request.is_ajax():
                data = {
                    'message': unicode(ex)
                }
                return self.render_to_json_response(data, status=400)
            else:
                raise ex

    def delete(self, request, *args, **kwargs):
        del_id = self.get_object().pk
        response = super(AjaxableResponseMixin, self).delete(request, *args, **kwargs);
        if self.request.is_ajax():
            data = {
                'id': del_id,
                'object': self.get_model_dict(),
                }
            return self.render_to_json_response(data)
        else:
            return response

    def get_model_dict(self):
        return model_to_dict(self.object)

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax() and self.request.method == 'POST':
            return self.render_to_json_response({'result': True})
        else:
            return super(AjaxableResponseMixin, self).render_to_response(context, **response_kwargs)


class BreadcrumbMixin(object):
    def get_context_data(self, **kwargs):
        result =  super(BreadcrumbMixin, self).get_context_data(**kwargs)
        self.request.breadcrumbs(self.get_breadcrumbs())
        return result

    def get_breadcrumbs(self):
        return []


class UpdateAccessMixin(object):
    def form_valid(self, form):
        if not self.request.user == self.object.user:
            raise Exception(u'Нет права доступа')
        return super(UpdateAccessMixin, self).form_valid(form)

    def delete(self, request, *args, **kwargs):
        if not self.request.user == self.get_object().user:
            raise Exception(u'Нет права доступа')
        return super(UpdateAccessMixin, self).delete(request, *args, **kwargs)


def delete_template_fragment_cache(fragment_name='', *args):
    cache.delete('template.cache.%s.%s' % (fragment_name, hashlib.md5(u':'.join([arg for arg in args])).hexdigest()))


def content_type(func, type=None):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        response['content-type'] = type if type else 'text/html'
        return response
    return wrapper


def class_view_decorator(function_decorator):
    def simple_decorator(View):
        View.dispatch = method_decorator(function_decorator)(View.dispatch)
        return View
    return simple_decorator