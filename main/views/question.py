#-*- coding: utf-8 -*-
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from main.models import Question
from gutils.views import BreadcrumbMixin, AjaxPageMixin, AjaxableResponseMixin, UpdateAccessMixin
from django.core.urlresolvers import reverse
from gutils.views import class_view_decorator
from django.contrib.auth.decorators import permission_required
from main.form import QuestionForm, FaqForm
from datetime import datetime


class QuestionListView(BreadcrumbMixin, ListView):
    """
    Список городов
    """
    model = Question
    context_object_name = 'question_list'
    paginate_by = 50
    template_name = 'main/question/page.html'

    def get_breadcrumbs(self):
        return super(QuestionListView, self).get_breadcrumbs() + [('FAQ', reverse('client:question:list'))]

    def get_queryset(self):
        return Question.objects.exclude(answer='').order_by('-date')


class QuestionDetailView(BreadcrumbMixin, DetailView):
    model = Question
    template_name = 'main/question/detail.html'
    context_object_name = 'question'

    def get_breadcrumbs(self):
        return [(u'FAQ', reverse('question:list')),
                (u'Вопрос №%s' % self.object.id, reverse('question:detail', kwargs={'pk':self.object.id}))]


@class_view_decorator(permission_required('main.view_question'))
class QuestionListView_Client(BreadcrumbMixin, ListView):
    """
    Список городов
    """
    model = Question
    context_object_name = 'question_list'
    paginate_by = 50
    template_name = 'main/client/question/page.html'

    def get_breadcrumbs(self):
        return super(QuestionListView_Client, self).get_breadcrumbs() + [('FAQ', reverse('question:list'))]

    def get_queryset(self):
        return Question.objects.exclude(answer=None).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(QuestionListView_Client, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_question')
        return context


@class_view_decorator(permission_required('main.view_question'))
class QuestionDetailView_Client(BreadcrumbMixin, AjaxPageMixin, DetailView):
    model = Question
    template_name = 'main/client/question/detail.html'
    template_name_ajax = 'main/client/question/detail-ajax.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView_Client, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_question')
        return context

    def get_breadcrumbs(self):
        return [(u'FAQ', reverse('client:question:list')),
                (u'Вопрос №%s' % self.object.id, reverse('client:question:detail', kwargs={'pk':self.object.id}))]


@class_view_decorator(permission_required('main.view_question'))
class QuestionPreviewView(DetailView):
    model = Question
    template_name = 'main/client/question/preview.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super(QuestionPreviewView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_question')
        return context


@class_view_decorator(permission_required('main.add_question'))
class QuestionCreateView(AjaxableResponseMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'main/client/question/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(QuestionCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:question:create')
        return context

    def get_model_dict(self):
        return {
            'url': reverse('client:question:detail', kwargs={'pk': self.object.id})
        }

    def form_valid(self, form):
        form.instance.date = datetime.now()
        return super(QuestionCreateView, self).form_valid(form)


class FaqCreateView(AjaxableResponseMixin, CreateView):
    model = Question
    form_class = FaqForm
    template_name = 'main/question/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(FaqCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('question:create')
        return context

    def get_model_dict(self):
        return {
            'message': u'Ваш вопрос отправлен администрации сайта под номером %s' % self.object.id
        }

    def form_valid(self, form):
        form.instance.date = datetime.now()
        return super(FaqCreateView, self).form_valid(form)


@class_view_decorator(permission_required('main.change_question'))
class QuestionUpdateView(AjaxableResponseMixin, UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'main/client/question/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(QuestionUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('client:question:edit', kwargs={'pk': self.object.id})
        return context

    def get_model_dict(self):
        return {
            'url': reverse('client:question:detail', kwargs={'pk': self.object.id})
        }


@class_view_decorator(permission_required('main.delete_question'))
class QuestionDeleteView(AjaxableResponseMixin, DeleteView):
    model = Question
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super(QuestionDeleteView, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return {
            'url': reverse('client:question:list')
        }