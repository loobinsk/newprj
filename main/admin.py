from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django import forms
from ckeditor.fields import CKEditorWidget
from main.models import *


class LocalFlatPageForm(FlatpageForm):
    content = forms.CharField(widget=CKEditorWidget)


class LocalFlatPageAdmin(FlatPageAdmin):
    form = LocalFlatPageForm

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, LocalFlatPageAdmin)


class TownAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order')
    list_per_page = 50

    def get_queryset(self, request):
        """
        Returns a QuerySet of all model instances that can be edited by the
        admin site. This is used by changelist_view.
        """
        qs = self.model.admin_objects.get_queryset()
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

admin.site.register(Town, TownAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('title', 'town', 'slug')
    list_filter = ('town',)
    list_per_page = 50

admin.site.register(District, DistrictAdmin)


class MetroAdmin(admin.ModelAdmin):
    list_display = ('title', 'town', 'slug', 'x', 'y', 'x1', 'y1', 'color', 'centr')
    list_filter = ('town', 'centr')
    list_per_page = 50

admin.site.register(Metro, MetroAdmin)


class AdvertAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'user', 'town', 'company')
    list_filter = ('town', 'user', 'adtype', 'estate', 'need', 'live')
    list_per_page = 50

admin.site.register(Advert, AdvertAdmin)


class VKAdvertAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'town', 'extnum', 'body')
    list_filter = ('town', 'adtype', 'estate', 'need', 'live')
    list_per_page = 50

admin.site.register(VKAdvert, VKAdvertAdmin)


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'user')
    list_filter = ('user', )
    list_per_page = 50

admin.site.register(Vacancy, VacancyAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('body', 'answer', 'date')
    list_per_page = 50

admin.site.register(Question, QuestionAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tel', 'email', 'address', 'town')
    list_per_page = 20

admin.site.register(Company, CompanyAdmin)


class BlacklistAdmin(admin.ModelAdmin):
    list_display = ('tel', 'body', 'tag', 'town')
    list_filter = ('town',)
    list_per_page = 50

admin.site.register(Blacklist, BlacklistAdmin)


class VKBlacklistAdmin(admin.ModelAdmin):
    list_display = ('vkid', 'body')
    list_per_page = 50

admin.site.register(VKBlacklist, VKBlacklistAdmin)


class TariffAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'desc', 'price', 'order')
    list_per_page = 20

admin.site.register(Tariff, TariffAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'status', 'total')
    list_per_page = 20

admin.site.register(Payment, PaymentAdmin)


class PaymentItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'tariff', 'total')
    list_per_page = 20

admin.site.register(PaymentItem, PaymentItemAdmin)


class ConnectedServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'active', 'company', 'user', 'perm', 'months', 'start_date', 'end_date')
    list_filter = ('company', 'user', 'perm')
    list_per_page = 20

admin.site.register(ConnectedService, ConnectedServicesAdmin)


class PermsAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'adtype', 'need', 'estate', 'live', 'base_main', 'base_vk', 'day_limit')
    list_per_page = 20

admin.site.register(Perm, PermsAdmin)


class ParserAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'priority')
    list_per_page = 20

admin.site.register(Parser, ParserAdmin)


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('code', 'title')
    list_per_page = 20

admin.site.register(Subscribe, SubscribeAdmin)


class SubscribeCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'subscribe', 'user')
    list_per_page = 20

admin.site.register(SubscribeCode, SubscribeCodeAdmin)


class SyncFilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'server', 'files')
    list_per_page = 20

admin.site.register(SyncFiles, SyncFilesAdmin)


class PromotionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'site', 'discount', 'code')
    list_filter = ('site', )
    list_per_page = 20

admin.site.register(Promotion, PromotionAdmin)


class PromocodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'promotion', 'user')
    list_filter = ('promotion', 'user')
    list_per_page = 20

admin.site.register(Promocode, PromocodeAdmin)


class MetatagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'site', 'path')
    list_filter = ('site',)
    search_fields = ('name', 'path', )
    list_per_page = 20
admin.site.register(Metatag, MetatagAdmin)