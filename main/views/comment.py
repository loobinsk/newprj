# -*- coding: utf-8 -*-
from django.views.generic import ListView
from gutils.views import BreadcrumbMixin
from ucomment.models import Comment
from django.core.urlresolvers import reverse


class CommentListView(BreadcrumbMixin, ListView):
    model = Comment
    template_name = 'main/client/comment/page.html'
    paginate_by = 50

    def get_queryset(self):
        return super(CommentListView, self).get_queryset().order_by('-date')

    def get_breadcrumbs(self):
        return [(u'Лента отзывов', reverse('client:comment:list'))]
