from django.contrib import admin
from social_auth.admin import UserSocialAuthOption


UserSocialAuthOption.list_display += ('site',)