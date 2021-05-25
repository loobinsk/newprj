#-*- coding: utf-8 -*-
from django import template
from uprofile.models import User

register = template.Library()

@register.inclusion_tag('uprofile/avatar.html', takes_context=True)
def user_avatar(context, user):
    return {
        'user': user
    }
