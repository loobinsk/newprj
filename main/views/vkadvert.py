# -*- coding: utf-8 -*-
from django.views.generic import ListView, View, DetailView
from main.models import VKAdvert, Metro, Town, District, clear_tel, clear_tel_list, Blacklist, VKBlacklist, Complain
from gutils.views import BreadcrumbMixin
from main.views.private import ModerPermMixin, ClientPermMixin
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.db.transaction import atomic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from annoying.decorators import ajax_request
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from mail_templated import send_mail
from django.conf import settings


class VKAdvertListView_Client(ClientPermMixin, BreadcrumbMixin, ListView):
    """
    Список объявлений
    """
    model = VKAdvert
    context_object_name = 'advert_list'
    paginate_by = 30
    template_name = 'main/client/vkadvert/page.html'
    template_name_ajax = 'main/client/vkadvert/page-ajax.html'
    district = None
    metro = None
    path_args = {}
    town = None
    company = None
    user = None

    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax():
            self.template_name = self.template_name_ajax
        return super(VKAdvertListView_Client, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        self.path_args = {}

        query = Q()
        if self.request.is_moder:
            if self.request.REQUEST.get('town'):
                town_list = Town.admin_objects.filter(id=self.request.REQUEST.get('town'))
                if town_list:
                    query = query & Q(town=town_list[0])
        else:
            query = query & Q(town=self.request.current_town, status=VKAdvert.STATUS_VIEW)

        if self.request.REQUEST.get('id'):
            query = query & Q(id=self.request.REQUEST.get('id'))

        if self.request.REQUEST.get('owner_vkid'):
            query = query & Q(owner_vkid=self.request.REQUEST.get('owner_vkid'))

        adtype = self.request.REQUEST.get('type')
        if VKAdvert.TYPES.has_key(adtype):
            query = query & Q(adtype=adtype)

        # type_query = Q()
        #
        # type2 = self.request.REQUEST.get('type2')
        # if not type2:
        #     if self.request.REQUEST.get('type') == 'L':
        #         type2 = 'LS'
        #     elif self.request.REQUEST.get('type') == 'S':
        #         type2 = 'SS'
        #     elif self.request.REQUEST.get('estate') in ['H', 'C', 'T']:
        #         type2 = 'LS'
        # # сдам
        # if 'LS' == type2:
        #     type_query = type_query | Q(adtype=VKAdvert.TYPE_LEASE, need=VKAdvert.NEED_SALE)
        # # сниму
        # elif 'LD' == type2:
        #     type_query = type_query | Q(adtype=VKAdvert.TYPE_LEASE, need=VKAdvert.NEED_DEMAND)
        # # Продам
        # elif 'SS' == type2:
        #     type_query = type_query | Q(adtype=VKAdvert.TYPE_SALE, need=VKAdvert.NEED_SALE)
        # # Куплю
        # elif 'SD' == type2:
        #     type_query = type_query | Q(adtype=VKAdvert.TYPE_SALE, need=VKAdvert.NEED_DEMAND)
        # else:
        #     # по умолчанию сдам квартиру
        #     type_query = type_query | Q(adtype=VKAdvert.TYPE_LEASE, need=VKAdvert.NEED_SALE)

        type_query = Q(adtype=VKAdvert.TYPE_LEASE, need=VKAdvert.NEED_SALE)

        query = query & type_query

        if not self.request.is_moder:
            if self.request.REQUEST.get('limit_day'):
                query = query & Q(limit=VKAdvert.LIMIT_DAY)
            else:
                query = query & Q(limit=VKAdvert.LIMIT_LONG)

        # район
        district_list = District.objects.filter(id=self.request.REQUEST.get('district'))
        if district_list:
            query = query & Q(district=district_list[0])

        # метро
        metro_arg = self.request.REQUEST.getlist('metro')
        if metro_arg:
            metro_list = Metro.objects.filter(id__in=metro_arg if isinstance(metro_arg, list) else [metro_arg])
            if metro_list:
                query = query & Q(metro_id__in=[metro.id for metro in metro_list])

        # тип недвижимости
        estate = self.request.REQUEST.get('estate')
        if estate == VKAdvert.ESTATE_LIVE:
            query = query & Q(estate=VKAdvert.ESTATE_LIVE)
        # elif estate == Advert.ESTATE_COUNTRY:
        #     query = query & Q(estate=Advert.ESTATE_COUNTRY)
        # elif estate == Advert.ESTATE_COMMERCIAL:
        #     query = query & Q(estate=Advert.ESTATE_COMMERCIAL)
        # elif estate == Advert.ESTATE_TERRITORY:
        #     query = query & Q(estate=Advert.ESTATE_TERRITORY)

        # кол-во комнат
        try:
            room_query = Q()
            room_arg = self.request.REQUEST.getlist('rooms')
            if room_arg:
                for room in room_arg:
                    if room == 'R':
                        room_query |= Q(live=VKAdvert.LIVE_ROOM)
                    else:
                        if int(room) in [1, 2, 3]:
                            room_query |= Q(rooms=int(room), live=VKAdvert.LIVE_FLAT)
                        elif int(room) >= 4:
                            room_query |= Q(rooms__gt=3, live=VKAdvert.LIVE_FLAT)
                query &= room_query
        except:
            pass

        # # тип загородное недвижимости
        # country = self.request.REQUEST.get('country')
        # if Advert.COUNTRIES.has_key(country):
        #     query = query & Q(country=country)
        #
        # # тип загородное недвижимости
        # commercial = self.request.REQUEST.get('commercial')
        # if Advert.COMMERCIALS.has_key(commercial):
        #     query = query & Q(commercial=commercial)
        #
        # # тип земли
        # territory = self.request.REQUEST.get('territory')
        # if Advert.TERRITORIES.has_key(territory):
        #     query = query & Q(territory=territory)

        # мин цена
        try:
            min_price = int(self.request.REQUEST.get('min_price'))
            if min_price:
                query = query & Q(price__gte=min_price)
        except:
            pass

        # макс цена
        try:
            max_price = int(self.request.REQUEST.get('max_price'))
            if max_price:
                query = query & Q(price__lte=max_price)
        except:
            pass

        #владелец
        # owner_query = Q()
        # if self.request.REQUEST.get('owner_agent'):
        #     owner_query = owner_query | ~Q(company=None)
        # if self.request.REQUEST.get('owner_owner'):
        #     owner_query = owner_query | Q(company=None)
        # query = query & owner_query

        # этаж
        try:
            min_floor = int(self.request.REQUEST.get('min_floor'))
            if min_floor:
                query = query & Q(floor__gte=min_floor)
        except:
            pass
        try:
            max_floor = int(self.request.REQUEST.get('max_floor'))
            if max_floor:
                query = query & Q(floor__lte=max_floor)
        except:
            pass
        if self.request.REQUEST.get('not_first_floor'):
            query = query & ~Q(floor=1)

        # площадь
        try:
            min_square = int(self.request.REQUEST.get('min_square'))
            if min_square:
                query = query & Q(square__gte=min_square)
        except:
            pass
        try:
            max_square = int(self.request.REQUEST.get('max_square'))
            if max_square:
                query = query & Q(square__lte=max_square)
        except:
            pass

        # удобства
        if self.request.REQUEST.get('refrigerator'):
            query = query & Q(refrigerator=self.request.REQUEST.get('refrigerator'))
        if self.request.REQUEST.get('tv'):
            query = query & Q(tv=self.request.REQUEST.get('tv'))
        if self.request.REQUEST.get('washer'):
            query = query & Q(washer=self.request.REQUEST.get('washer'))
        if self.request.REQUEST.get('phone'):
            query = query & Q(phone=self.request.REQUEST.get('phone'))
        if self.request.REQUEST.get('internet'):
            query = query & Q(internet=self.request.REQUEST.get('internet'))
        if self.request.REQUEST.get('furniture'):
            query = query & Q(furniture=self.request.REQUEST.get('firniture'))
        if self.request.REQUEST.get('euroremont'):
            query = query & Q(euroremont=self.request.REQUEST.get('euroremont'))
        if self.request.REQUEST.get('separate_wc'):
            query = query & Q(separate_wc=self.request.REQUEST.get('separate_wc'))
        if self.request.REQUEST.get('balcony'):
            query = query & Q(balcony=self.request.REQUEST.get('balcony'))
        if self.request.REQUEST.get('lift'):
            query = query & Q(lift=self.request.REQUEST.get('lift'))
        if self.request.REQUEST.get('parking'):
            query = query & Q(parking=self.request.REQUEST.get('parking'))
        if self.request.REQUEST.get('conditioner'):
            query = query & Q(conditioner=self.request.REQUEST.get('conditioner'))
        if self.request.REQUEST.get('redecoration'):
            query = query & Q(redecoration=self.request.REQUEST.get('redecoration'))
        if self.request.REQUEST.get('no_remont'):
            query = query & Q(no_remont=self.request.REQUEST.get('no_remont'))
        if self.request.REQUEST.get('need_remont'):
            query = query & Q(need_remont=self.request.REQUEST.get('need_remont'))
        if self.request.REQUEST.get('electric'):
            query = query & Q(electric=self.request.REQUEST.get('electric'))
        if self.request.REQUEST.get('gas'):
            query = query & Q(gas=self.request.REQUEST.get('gas'))
        if self.request.REQUEST.get('water'):
            query = query & Q(water=self.request.REQUEST.get('water'))
        if self.request.REQUEST.get('sewage'):
            query = query & Q(sewage=self.request.REQUEST.get('sewage'))
        if self.request.REQUEST.get('brick_building'):
            query = query & Q(brick_building=self.request.REQUEST.get('brick_building'))
        if self.request.REQUEST.get('wood_building'):
            query = query & Q(wood_building=self.request.REQUEST.get('wood_building'))
        if self.request.REQUEST.get('live_one'):
            query = query & Q(live_one=self.request.REQUEST.get('live_one'))
        if self.request.REQUEST.get('live_two'):
            query = query & Q(live_two=self.request.REQUEST.get('live_two'))
        if self.request.REQUEST.get('live_pare'):
            query = query & Q(live_pare=self.request.REQUEST.get('live_pare'))
        if self.request.REQUEST.get('live_more'):
            query = query & Q(live_more=self.request.REQUEST.get('live_more'))
        if self.request.REQUEST.get('live_child'):
            query = query & Q(live_child=self.request.REQUEST.get('live_child'))
        if self.request.REQUEST.get('live_animal'):
            query = query & Q(live_animal=self.request.REQUEST.get('live_animal'))
        if self.request.REQUEST.get('live_girl'):
            query = query & Q(live_girl=self.request.REQUEST.get('live_girl'))
        if self.request.REQUEST.get('live_man'):
            query = query & Q(live_man=self.request.REQUEST.get('live_man'))
        if self.request.REQUEST.get('concierge'):
            query = query & Q(concierge=self.request.REQUEST.get('concierge'))
        if self.request.REQUEST.get('guard'):
            query = query & Q(guard=self.request.REQUEST.get('guard'))
        if self.request.REQUEST.get('garage'):
            query = query & Q(garage=self.request.REQUEST.get('garage'))

        if not self.request.REQUEST.get('archive'):
            if self.request.REQUEST.get('date'):
                try:
                    days = int(self.request.REQUEST.get('date', 30))
                    if days != 0:
                        query = query & Q(date__gte=datetime.now() - timedelta(days=days))
                except:
                    pass
            else:
                query = query & Q(date__gte=datetime.now() - timedelta(days=30))
        else:
            query = query & VKAdvert.ARCHIVE_YES_QUERY

        # фильтрую объявления на которые пожаловались
        query &= ~Q(complained__user=self.request.user)

        queryset = VKAdvert.objects.filter(query).select_related('metro', 'district', 'town')

        sort = self.request.GET.get('sort')
        if sort == 'date-asc':
            queryset = queryset.order_by('date')
        elif sort == 'date-desc':
            queryset = queryset.order_by('-date')
        elif sort == 'price-asc':
            queryset = queryset.order_by('price')
        elif sort == 'price-desc':
            queryset = queryset.order_by('-price')

        try:
            count = int(self.request.GET.get('count', 30))
            if count <= 60:
                self.paginate_by = count
        except:
            pass

        return queryset

    def get_breadcrumbs(self):
        return super(VKAdvertListView_Client, self).get_breadcrumbs() + [('Каталог объявлений', reverse('client:advert:vk:list'))]

    def get_context_data(self, **kwargs):
        context = super(VKAdvertListView_Client, self).get_context_data(**kwargs)
        return context


class VKAdvertPreview_Client(ClientPermMixin, DetailView):
    model = VKAdvert
    template_name = 'main/client/vkadvert/preview.html'
    context_object_name = 'advert'


class VKAdvertImageGalleryView_Client(ClientPermMixin, DetailView):
    model = VKAdvert
    context_object_name = 'advert'
    template_name = 'main/client/advert/image-gallery.html'


class VKAdvertIsAgentView_Client(ModerPermMixin, View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(VKAdvertIsAgentView_Client, self).dispatch(request, *args, **kwargs)

    @method_decorator(ajax_request)
    @atomic
    def post(self, request, *args, **kwargs):
        try:
            advert = get_object_or_404(VKAdvert, id=kwargs['pk'])

            if not request.user.has_perm('main.change_advert_status'):
                raise Exception(u'Нет прав')
            # if not ((request.user.has_perm('main.view_advert_moderate') and advert.status == Advert.STATUS_MODERATE) \
            #     or request.user.has_perm('main.view_all_advert')):
            #     raise Exception(u'Нет прав')

            tel_list = clear_tel_list(advert.owner_tel)
            if not Blacklist.check_list(tel_list):
                Blacklist.add_tel(tel_list, 'Определен как агент по объявлению вконтакте %s' % advert.id)

            if not VKBlacklist.check_vkid(advert.owner_vkid):
                VKBlacklist.add_vkid(advert.owner_vkid, 'Определен как агент по объявлению вконтакте %s' % advert.id)

            advert.status = VKAdvert.STATUS_BLOCKED
            advert.save()

            if advert.owner_vkid:
                deleted_adverts = VKAdvert.block_by_vkid(advert.owner_vkid)

            return {
                'result': True,
                'id': advert.id,
                'message': '<div class="success-advert"><img src="/static/img/delete.png"><p>Объявление №%s удалено. <br>Номер телефона отправлен в черный список%s</p></div>' % (advert.id, \
                    '<br>Удалено ' + str(deleted_adverts) + ' объявлений с таким телефоном' if deleted_adverts else ''),
            }
        except Exception as ex:
            return {
                'result': False,
                'message': unicode(ex)
            }


class VKAdvertIrrelevantView_Client(ModerPermMixin, View):
    """
    Отметить как неактуальное
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(VKAdvertIrrelevantView_Client, self).dispatch(request, *args, **kwargs)

    @method_decorator(ajax_request)
    @atomic
    def post(self, request, *args, **kwargs):
        try:
            advert = get_object_or_404(VKAdvert, id=kwargs['pk'])

            if not request.user.has_perm('main.change_advert_status'):
                raise Exception(u'Нет прав')
            # if not ((request.user.has_perm('main.view_advert_moderate') and advert.status == Advert.STATUS_MODERATE) \
            #     or request.user.has_perm('main.view_all_advert')):
            #     raise Exception(u'Нет прав')

            advert.status = VKAdvert.STATUS_BLOCKED
            advert.save()

            return {
                'result': True,
                'id': advert.id,
                'message': '<div class="modal-icon"><img src="/static/img/delete.png"><p>Объявление №%s удалено.</p></div>' % advert.id,
                }
        except Exception as ex:
            return {
                'result': False,
                'message': unicode(ex)
            }


class VKAdvertComplainView_Client(ClientPermMixin, View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(VKAdvertComplainView_Client, self).dispatch(request, *args, **kwargs)

    @method_decorator(ajax_request)
    def post(self, request, *args, **kwargs):
        try:
            advert = get_object_or_404(VKAdvert, id=kwargs['pk'])
            complain_text = request.POST.get('complain')
            reason = request.POST.get('reason')
            complain = Complain(user=request.user, content=advert, reason=reason, date=datetime.now())
            complain.save()

            send_mail('main/email/complain.html',{
                'advert': advert,
                'complain': complain_text,
                'user': request.user,
                'subject': u'На объявление №%s отправлена жалоба: %s' % (advert.id, complain)
                },
                recipient_list=settings.NOTICE_COMPLAIN_EMAIL,
                fail_silently=True)

            return {
                'result': True,
                'id': advert.id,
                'message': u'На объявление №%s отправлена жалоба: %s<br>Это объявление больше не будет вам отображаться' % (advert.id, complain)
            }
        except Exception as ex:
            return {
                'result': False,
                'message': unicode(ex)
            }