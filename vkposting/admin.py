from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'login')

admin.site.register(Profile, ProfileAdmin)


class CanalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'code')

admin.site.register(Canal, CanalAdmin)
