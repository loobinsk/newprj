from django.contrib import admin
from ucomment.models import *
from feincms.admin import tree_editor


class CommentAdmin(tree_editor.TreeEditor):
    list_display = ('user', 'text')
    list_per_page = 50

admin.site.register(Comment, CommentAdmin)
