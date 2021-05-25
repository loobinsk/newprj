from django.contrib import admin
from uprofile.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'tel', 'is_active', 'independent', 'site')
    list_filter = ('site', 'is_active', 'status')
    list_per_page = 50

admin.site.register(User, UserAdmin)
