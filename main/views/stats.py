#-*- coding: utf-8 -*-
from django.views.generic import ListView, TemplateView
from gutils.views import AdminRequiredMixin, BreadcrumbMixin
from django.core.urlresolvers import reverse
from datetime import datetime
from main.form import ModeratorStatFilterForm, ParserStatFilterForm
from uprofile.models import User
from main.models import Parser, Town
from django.db.models import Q
import caching


class ModeratorStatView(AdminRequiredMixin, BreadcrumbMixin, ListView):
    template_name = 'main/client/stat/moderator.html'
    model = User
    context_object_name = 'moderator_list'

    def get_breadcrumbs(self):
        return [('Статистика модераторов', reverse('client:stat:moderator'))]

    def get_context_data(self, **kwargs):
        context = super(ModeratorStatView, self).get_context_data(**kwargs)
        context['form'] = ModeratorStatFilterForm(self.request.GET)
        return context

    def get_queryset(self):
        start_date = datetime.now().strftime('%Y-%m-%d')
        if self.request.GET.get('start_date'):
            start_date = datetime.strptime(self.request.GET.get('start_date'), '%d.%m.%Y').strftime('%Y-%m-%d')
        end_date = '9999-01-01'
        if self.request.GET.get('end_date'):
            end_date = datetime.strptime(self.request.GET.get('end_date'), '%d.%m.%Y').strftime('%Y-%m-%d')
        return User.objects.raw(u'select '
                                u'usr.*,'
                                u'(select COUNT(advert.id) from main_advert as advert '
                                    u'where advert.moderator_id=usr.id and advert.status=\'v\' and advert.date between %(start_date)s and %(end_date)s) count_view, '
                                u'(select COUNT(advert.id) '
                                    u'from main_advert as advert '
                                    u'where advert.moderator_id=usr.id and advert.status=\'v\' and advert.date between %(start_date)s and %(end_date)s and'
                                    u'(select count(adv.id) from main_advert as adv inner join main_advert_images as img on adv.id=img.advert_id where advert.id=adv.id) > 0) count_view_images, '
                                u'(select COUNT(advert.id) from main_advert as advert '
                                    u'where advert.moderator_id=usr.id and advert.status=\'m\' and advert.not_answer=true and advert.date between %(start_date)s and %(end_date)s) count_na, '
                                u'(select COUNT(advert.id) from main_advert as advert '
                                    u'where advert.moderator_id=usr.id and advert.status=\'b\' and advert.date between %(start_date)s and %(end_date)s) count_agent '

                                u'from uprofile_user as usr '

                                u'left join uprofile_user_groups as gr on gr.user_id=usr.id '
                                u'left join auth_group as grp on gr.group_id=grp.id '
                                u'where grp.name=%(grp1)s or usr.is_superuser=True '
                                u'group by usr.id '
                                u'order by usr.username ',
            {u'grp1': u'Модератор', u'start_date': start_date, u'end_date': end_date})


class ParserStatView(AdminRequiredMixin, BreadcrumbMixin, ListView):
    template_name = 'main/client/stat/parser.html'
    model = Parser
    context_object_name = 'parser_list'

    def get_breadcrumbs(self):
        return [('Статистика парсеров', reverse('client:stat:parser'))]

    def get_context_data(self, **kwargs):
        start_date = datetime.now().strftime('%Y-%m-%d')
        if self.request.GET.get('start_date'):
            start_date = datetime.strptime(self.request.GET.get('start_date'), '%d.%m.%Y').strftime('%Y-%m-%d')
        end_date = '9999-01-01'
        if self.request.GET.get('end_date'):
            end_date = datetime.strptime(self.request.GET.get('end_date'), '%d.%m.%Y').strftime('%Y-%m-%d')

        context = super(ParserStatView, self).get_context_data(**kwargs)
        context['form'] = ParserStatFilterForm(self.request.GET)

        context['towns'] = Town.objects.raw(u'select '
                                   u'town.*, '
                                   u'(select count(advert.id) from main_advert as advert where advert.town_id=town.id and advert.date between %(start_date)s and %(end_date)s) as count_parsed, '
                                   u'(select count(advert.id) from main_advert as advert where advert.town_id=town.id and advert.date between %(start_date)s and %(end_date)s and advert.status=\'v\') as count_view, '
                                   u'(select count(advert.id) from main_advert as advert where advert.town_id=town.id and advert.date between %(start_date)s and %(end_date)s and advert.status=\'m\' and advert.not_answer=True) as count_na, '
                                   u'(select count(advert.id) from main_advert as advert where advert.town_id=town.id and advert.date between %(start_date)s and %(end_date)s and advert.status=\'b\') as count_blocked '

                                   u'from main_town as town '

                                   u'order by town.title ',
                                   {u'start_date': start_date, u'end_date': end_date})
        context['towns'].timeout = caching.config.NO_CACHE

        context['towns_vk'] = Town.objects.raw(u'select '
                                   u'town.*, '
                                   u'(select count(advert.id) from main_vkadvert as advert where advert.town_id=town.id and advert.date between %(start_date)s and %(end_date)s) as count_parsed, '
                                   u'(select count(advert.id) from main_vkadvert as advert where advert.town_id=town.id and advert.date between %(start_date)s and %(end_date)s and advert.status=\'v\') as count_view, '
                                   u'(select count(advert.id) from main_vkadvert as advert where advert.town_id=town.id and advert.date between %(start_date)s and %(end_date)s and advert.status=\'b\') as count_blocked '

                                   u'from main_town as town '

                                   u'order by town.title ',
                                   {u'start_date': start_date, u'end_date': end_date})
        context['towns_vk'].timeout = caching.config.NO_CACHE

        context['towns_public'] = Town.objects.raw(u'select '
                                            u'town.*, '
                                            u'(select count(advert.id) from main_advert as advert where advert.town_id=town.id and advert.parser_id=9 and advert.date between %(start_date)s and %(end_date)s) as count_parsed, '
                                            u'(select count(advert.id) from main_advert as advert where advert.town_id=town.id and advert.parser_id=9 and advert.date between %(start_date)s and %(end_date)s and advert.status=\'v\') as count_view, '
                                            u'(select count(advert.id) from main_advert as advert where advert.town_id=town.id and advert.parser_id=9 and advert.date between %(start_date)s and %(end_date)s and advert.status=\'m\' and advert.not_answer=True) as count_na, '
                                            u'(select count(advert.id) from main_advert as advert where advert.town_id=town.id and advert.parser_id=9 and advert.date between %(start_date)s and %(end_date)s and advert.status=\'b\') as count_blocked '

                                            u'from main_town as town '

                                            u'order by town.title ',
                                            {u'start_date': start_date, u'end_date': end_date})
        context['towns_public'].timeout = caching.config.NO_CACHE

        context['towns_request'] = Town.objects.raw(u'select '
                                                   u'town.*, '
                                                   u'(select count(advert.id) from main_advert as advert where advert.town_id=town.id and advert.parser_id=10 and advert.date between %(start_date)s and %(end_date)s) as count_parsed, '
                                                   u'(select count(advert.id) from main_advert as advert where advert.town_id=town.id and advert.parser_id=10 and advert.date between %(start_date)s and %(end_date)s and advert.status=\'v\') as count_view, '
                                                   u'(select count(advert.id) from main_advert as advert where advert.town_id=town.id and advert.parser_id=10 and advert.date between %(start_date)s and %(end_date)s and advert.status=\'m\' and advert.not_answer=True) as count_na, '
                                                   u'(select count(advert.id) from main_advert as advert where advert.town_id=town.id and advert.parser_id=10 and advert.date between %(start_date)s and %(end_date)s and advert.status=\'b\') as count_blocked '

                                                   u'from main_town as town '

                                                   u'order by town.title ',
                                                   {u'start_date': start_date, u'end_date': end_date})
        context['towns_request'].timeout = caching.config.NO_CACHE

        context['vk_parser'] = Parser.objects.raw(u'select '
                                u'parser.*, '
                                u'(select count(advert.id) from main_vkadvert as advert where advert.date between %(start_date)s and %(end_date)s) as count_parsed, '
                                u'(select count(advert.id) from main_vkadvert as advert where advert.date between %(start_date)s and %(end_date)s and advert.status=\'v\') as count_view, '
                                u'(select count(advert.id) from main_vkadvert as advert where advert.date between %(start_date)s and %(end_date)s and advert.status=\'b\') as count_blocked '

                                u'from main_parser as parser '
                                u'where parser.title=\'vk\' '
                                u'order by parser.title ',
                                {u'start_date': start_date, u'end_date': end_date})

        return context

    def get_queryset(self):
        start_date = datetime.now().strftime('%Y-%m-%d')
        if self.request.GET.get('start_date'):
            start_date = datetime.strptime(self.request.GET.get('start_date'), '%d.%m.%Y').strftime('%Y-%m-%d')
        end_date = '9999-01-01'
        if self.request.GET.get('end_date'):
            end_date = datetime.strptime(self.request.GET.get('end_date'), '%d.%m.%Y').strftime('%Y-%m-%d')
        return Parser.objects.raw(u'select '
                                u'parser.*, '
                                u'(select count(advert.id) from main_advert as advert where advert.parser_id=parser.id and advert.date between %(start_date)s and %(end_date)s) as count_parsed, '
                                u'(select count(advert.id) from main_advert as advert where advert.parser_id=parser.id and advert.date between %(start_date)s and %(end_date)s and advert.status=\'v\') as count_view, '
                                u'(select count(advert.id) from main_advert as advert where advert.parser_id=parser.id and advert.date between %(start_date)s and %(end_date)s and advert.status=\'m\' and advert.not_answer=True) as count_na, '
                                u'(select count(advert.id) from main_advert as advert where advert.parser_id=parser.id and advert.date between %(start_date)s and %(end_date)s and advert.status=\'b\') as count_blocked '

                                u'from main_parser as parser '

                                u'order by parser.title ',
                                {u'start_date': start_date, u'end_date': end_date})

