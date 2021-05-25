from django.contrib import admin
from vashdom.models import *


class TariffAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'price', 'town', 'main_base', 'vk_base', 'order', 'desc', 'hidden')
    list_filter = ('town', 'main_base', 'vk_base')
    list_per_page = 50

admin.site.register(Tariff, TariffAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'tel', 'total', 'tariff')
    list_per_page = 50

admin.site.register(Payment, PaymentAdmin)


class PasswordAdmin(admin.ModelAdmin):
    list_display = ('id', 'password', 'start_date', 'end_date', 'count', 'town')
    list_filter = ('town',)
    list_per_page = 50

admin.site.register(Password, PasswordAdmin)
