#-*- coding: utf-8 -*-

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ucomment.models import Comment
from ucomment.forms import CommentForm
from gutils.views import LoginRequiredMixin, AjaxableResponseMixin
from datetime import datetime
from django.template import loader, Context
from django.shortcuts import get_object_or_404
from ucomment.signals import comment_create
from django.conf import settings


class CommentMixin(object):
    model = Comment
    form_class = CommentForm


class CommentCreateView(CommentMixin, AjaxableResponseMixin, CreateView):
    template_name = 'ucomment/form.html'
    success_url = '/'
    parent = None
    key = None
    url = None

    def read_params(self, request):
        parent_id = request.GET.get('parent')
        if not parent_id:
            parent_id = request.POST.get('parent')
        if parent_id:
            self.parent = get_object_or_404(Comment, id=parent_id)

        self.key = request.GET.get('key')
        if not self.key:
            self.key = request.POST.get('key')

        self.url = request.GET.get('url')
        if not self.url:
            self.url = request.META.get('HTTP_REFERER')

    def get(self, request, *args, **kwargs):
        self.read_params(request)
        return super(CommentCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if getattr(settings, 'COMMENT_AUTHORIZATION', False) and not self.request.user.is_authenticated():
            raise Exception(u'Необходимо авторизоваться или зарегистрироваться. чтобы оставить отзыв')
        self.read_params(request)
        return super(CommentCreateView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['parent'] = self.parent
        context['key'] = self.key
        context['need_auth'] = getattr(settings, 'COMMENT_AUTHORIZATION', False) and not self.request.user.is_authenticated()
        return context

    def get_initial(self):
        ar = super(CommentCreateView, self).get_initial()
        if self.parent:
            ar['parent'] = self.parent.id
        ar['key'] = self.key
        ar['url'] = self.url
        return ar

    def get_form_kwargs(self):
        kwargs = super(CommentCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        if not form.instance.text.strip():
            raise Exception(u'Текст сообщения пустой')
        if self.request.user.is_authenticated():
            last_comments = Comment.objects.filter(user=self.request.user).order_by('-date')[:1]
            if last_comments:
                timediff = datetime.now()-last_comments[0].date
                if timediff.total_seconds() <= 15:
                    raise Exception(u'Вы отправляете сообщения слишком часто')
            form.instance.user = self.request.user
        else:
            if not form.instance.name:
                raise Exception(u'Введите имя')
        form.instance.date = datetime.now()
        if not form.instance.url:
            form.instance.url = self.url
        if self.parent:
            form.instance.parent = self.parent
        result = super(CommentCreateView, self).form_valid(form)
        comment_create.send(sender=form.instance, user=self.request.user)
        return result

    def get_model_dict(self):
        tpl = loader.get_template('ucomment/preview.html')
        return {
            'parent': self.object.parent.id if self.object.parent else 0,
            'preview': tpl.render(Context({
                'comment': self.object,
                'user': self.request.user
            }))
        }


class CommentDeleteView(CommentMixin, LoginRequiredMixin, AjaxableResponseMixin, DeleteView):
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        comment = self.get_object()
        if (comment.user != request.user) and (not request.user.has_perm('ucomment.delete_comment')):
            raise Exception(u'Нет прав')
        return super(CommentDeleteView, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return {}


class CommentListView(CommentMixin, ListView):
    template_name = 'ucomment/list-ajax.html'
    paginate_by = 20
    context_object_name = 'comment_list'
    key = None

    def get(self, request, *args, **kwargs):
        self.key = request.GET.get('key')
        return super(CommentListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CommentListView, self).get_queryset().filter(key=self.key, level=0).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(CommentListView, self).get_context_data(**kwargs)
        context['key'] = self.key
        context['comment_list'] = [comment.get_descendants(include_self=True) for comment in context['comment_list']]
        return context