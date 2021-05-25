#-*- coding: utf-8 -*-
from django import template
from ucomment.models import *
from ucomment.forms import CommentForm
from django.conf import settings

register = template.Library()


@register.simple_tag(takes_context=True)
def show_comments(context, *args, **kwargs):
    list_template ='ucomment/list.html'
    if 'list_template' in kwargs:
        list_template = kwargs['list_template']
    key = u'_'.join([unicode(param) for param in args])
    need_auth = getattr(settings, 'COMMENT_AUTHORIZATION', False) and not context['request'].user.is_authenticated()
    tpl = template.loader.get_template(list_template)
    return tpl.render(template.Context({
        'user': context['user'],
        'comment_list': [comment.get_descendants(include_self=True) for comment in Comment.objects.filter(key=key, level=0).select_related('user').order_by('-date')[:20]],
        'comment_count': Comment.objects.filter(key=key, level=0).count(),
        'form': CommentForm(user=context['user'], initial={'key': key}),
        'key': key,
        'perms': context['perms'],
        'need_auth': need_auth
    }))


@register.inclusion_tag('ucomment/list.html', takes_context=True)
def show_my_comments(context, *args, **kwargs):
    key = u'_'.join([unicode(param) for param in args])
    return {
        'user': context['user'],
        'comment_list': Comment.objects.filter(key=key, user=context['request'].user).select_related('user'),
        'form': CommentForm(user=context['user'], initial={'key': key}),
        'key': key
    }


@register.inclusion_tag('ucomment/count.html')
def count_comments(*args):
    key = u'_'.join([unicode(param) for param in args])
    count = Comment.objects.filter(key=key).count()
    str_count = str(count)
    if count in [11, 12, 13, 14, 15, 16, 17, 18, 19]:
        label = 'комментариев'
    elif str_count[0] == '1':
        label = 'комментарий'
    elif str_count[-1:] in ['2', '3', '4']:
        label = 'комментария'
    else:
        label = 'комментариев'
    return {
        'count': count,
        'label': label
    }


@register.inclusion_tag('ucomment/count.html', takes_context=True)
def my_comments_count(context, *args):
    key = u'_'.join([unicode(param) for param in args])
    count = Comment.objects.filter(key=key, user=context['request'].user).count()
    str_count = str(count)
    if count in [11, 12, 13, 14, 15, 16, 17, 18, 19]:
        label = 'комментариев'
    elif str_count[0] == '1':
        label = 'комментарий'
    elif str_count[0] in ['2', '3', '4']:
        label = 'комментария'
    else:
        label = 'комментариев'
    return {
        'count': count,
        'label': label
    }