#-*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, View, FormView, TemplateView
from main.models import Advert, Metro, District, Company, clear_tel_list, Blacklist, Town, clear_tel, Parser, Complain
from uprofile.models import User, GlobalUser
from gutils.views import BreadcrumbMixin, AjaxableResponseMixin, AjaxPageMixin, AdminRequiredMixin
from django.core.urlresolvers import reverse
from django.db.models import Q, F
from main.form import FeedbackAdvertForm, RequestRemoveForm, AdvertForm, AdvertForm_Client, RequestForm, \
    SmartAdvertForm, BuyPayForm
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden, HttpResponsePermanentRedirect, Http404
from django.utils.decorators import method_decorator
from annoying.decorators import ajax_request
from mail_templated import send_mail_admins, send_mail
from django.db.transaction import atomic
from django.views.decorators.csrf import csrf_exempt
from main.task import find_advert_clients
from main.views.private import ClientPermMixin, ModerPermMixin
from django.conf import settings
from django.contrib.syndication.views import Feed
from uimg.models import UserImage


# ПРОВЕРКА ПРАВ
class AdvertUpdatePermMixin(object):
    """
    Проверка прав на редактирование объявления
    """
    def dispatch(self, request, *args, **kwargs):
        advert = self.get_object()
        if advert.user == request.user:
            return super(AdvertUpdatePermMixin, self).dispatch(request, *args, **kwargs)
        elif request.user.has_perm('main.change_advert'):
            if request.user.has_perm('main.view_all_advert'):
                return super(AdvertUpdatePermMixin, self).dispatch(request, *args, **kwargs)
            elif request.user.has_perm('main.view_advert_moderate') and (advert.status == Advert.STATUS_MODERATE):
                return super(AdvertUpdatePermMixin, self).dispatch(request, *args, **kwargs)
            elif request.user.has_perm('main.view_advert_moderate') and (advert.status == Advert.STATUS_VIEW) and (advert.moderator == request.user):
                return super(AdvertUpdatePermMixin, self).dispatch(request, *args, **kwargs)
        return HttpResponseForbidden()


class AdvertDeletePermMixin(object):
    """
    Проверка прав на удаление объявления
    """
    def dispatch(self, request, *args, **kwargs):
        advert = self.get_object()
        if advert.user == request.user:
            return super(AdvertDeletePermMixin, self).dispatch(request, *args, **kwargs)
        elif request.user.has_perm('main.del_advert'):
            if request.user.has_perm('main.view_all_advert'):
                return super(AdvertDeletePermMixin, self).dispatch(request, *args, **kwargs)
            elif request.user.has_perm('main.view_advert_moderate') and (advert.status == Advert.STATUS_MODERATE):
                return super(AdvertDeletePermMixin, self).dispatch(request, *args, **kwargs)
            elif request.user.has_perm('main.view_advert_moderate') and (advert.status == Advert.STATUS_VIEW) and (advert.moderator == request.user):
                return super(AdvertDeletePermMixin, self).dispatch(request, *args, **kwargs)
        return HttpResponseForbidden()


# ПРЕДСТАВЛЕНИЯ

class AdvertListView(BreadcrumbMixin, ListView):
    """
    Список объявлений
    """
    model = Advert
    context_object_name = 'advert_list'
    paginate_by = 15
    template_name = 'main/advert/page.html'
    template_name_ajax = 'main/advert/page-ajax.html'
    template_name_ajax_map = 'main/advert/business-map.html'
    district = None
    metro = None
    path_args = {}
    town = None
    company = None
    user = None

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax():
            if request.REQUEST.get('map') == '1':
                self.template_name = self.template_name_ajax_map
                self.paginate_by = 0
            else:
                self.template_name = self.template_name_ajax
        return super(AdvertListView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        reqdict = dict(request.REQUEST.dicts[0].lists())
        params = {}
        for key, value in reqdict.iteritems():
            if isinstance(value, list) and len(value) == 1:
                params[key] = value[0]
            else:
                params[key] = value
        params['town'] = request.current_town.id
        return HttpResponsePermanentRedirect(Advert.get_catalog_url(params))

    def get_queryset(self):
        self.path_args = {}

        query = Q(status=Advert.STATUS_VIEW, need=Advert.NEED_SALE)
        if self.kwargs.has_key('town'):
            self.town = get_object_or_404(Town, slug=self.kwargs['town'])
            query &= Q(town=self.town)
            self.path_args['town'] = self.town.id
        else:
            query &= Q(town=self.request.current_town)

        adtype = self.request.REQUEST.get('type')
        if Advert.TYPES.has_key(adtype):
            query = query & Q(adtype=adtype)
            self.path_args['type'] = adtype
        if self.request.REQUEST.get('type') == Advert.TYPE_LEASE:
            query &= Q(limit=Advert.LIMIT_LONG)
        if self.request.REQUEST.get('type') == 'LP':
            query &= Q(adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_DAY)
            self.path_args['type'] = 'LP'

        adtype_slug = self.kwargs.get('type', '')
        adtype = None
        for e, slug in Advert.TYPES_SLUG.iteritems():
            if slug == adtype_slug:
                adtype = e
        if adtype and Advert.TYPES.has_key(adtype):
            query = query & Q(adtype=adtype)
            self.path_args['type'] = adtype
        if self.kwargs.get('type', '') == 'sdam':
            query &= Q(limit=Advert.LIMIT_LONG)
        if self.kwargs.get('type', '') == 'sdam-posutochno':
            adtype = 'LP'
            self.path_args['type'] = adtype
            query &= Q(adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_DAY)

        # need = self.request.REQUEST.get('need')
        # if Advert.NEEDS.has_key(need):
        #     query = query & Q(need=need)


        if self.request.REQUEST.get('district'):
            try:
                district_list = District.objects.filter(id=self.request.REQUEST.get('district'))
                if district_list:
                    query = query & Q(district=district_list[0])
                    self.district = district_list[0]
            except:
                pass
        district_slug = self.kwargs.get('district', '')
        if district_slug:
            district_list = District.objects.filter(slug=district_slug, town_id=self.path_args['town'])
            if district_list:
                query = query & Q(district=district_list[0])
                self.district = district_list[0]
                self.path_args['district'] = district_list[0].id
            else:
                raise Http404()

        metro_arg = self.request.REQUEST.getlist('metro')
        if metro_arg:
            metro_list = Metro.objects.filter(id__in=metro_arg if isinstance(metro_arg, list) else [metro_arg])
            if metro_list:
                query = query & Q(metro_id__in=[metro.id for metro in metro_list])
                self.metro = metro_list[0]
        metro_slug = self.kwargs.get('metro', '')
        if metro_slug:
            metro_list = Metro.objects.filter(slug=metro_slug, town_id=self.path_args['town'])
            if metro_list:
                query = query & Q(metro=metro_list[0])
                self.metro = metro_list[0]
                self.path_args['metro'] = metro_list[0].id
            else:
                raise Http404()


        estate = self.request.REQUEST.get('estate')
        if Advert.ESTATES.has_key(estate):
            query = query & Q(estate=estate)
        estate_slug = self.kwargs.get('estate', '')
        estate = None
        for e, slug in Advert.ESTATES_SLUG.iteritems():
            if slug == estate_slug:
                estate = e
        if estate and Advert.ESTATES.has_key(estate):
            query = query & Q(estate=estate)
            self.path_args['estate'] = estate


        room_query = Q()
        room_list = self.request.REQUEST.getlist('rooms')
        if 'R' in room_list:
            room_query &= Q(live=Advert.LIVE_ROOM)
        for room in room_list:
            try:
                rooms = int(room)
                if rooms in [1, 2, 3]:
                    room_query |= Q(rooms=rooms, live=Advert.LIVE_FLAT)
                elif rooms >= 4:
                    room_query |= Q(rooms__gt=3, live=Advert.LIVE_FLAT)
            except:
                pass
        query &= room_query

        type2 = self.kwargs.get('type2', '')
        if type2:
            if estate == Advert.ESTATE_LIVE:
                if type2 == 'komnata':
                    query &= Q(live=Advert.LIVE_ROOM)
                    self.path_args['rooms'] = 'R'
                else:
                    for r in xrange(1, 5):
                        if type2 == '%s-komnatnaya-kvartira' % r:
                            if r >= 4:
                                query &= Q(rooms__gt=4, live=Advert.LIVE_FLAT)
                            else:
                                query &= Q(rooms=r, live=Advert.LIVE_FLAT)
                            self.path_args['rooms'] = str(r)
            if estate == Advert.ESTATE_COUNTRY:
                for e, slug in Advert.COUNTRIES_SLUG.iteritems():
                    if slug == type2:
                        query = query & Q(country=e)
                        self.path_args['country'] = e
            if estate == Advert.ESTATE_COMMERCIAL:
                for e, slug in Advert.COMMERCIALS_SLUG.iteritems():
                    if slug == type2:
                        query = query & Q(commercial=e)
                        self.path_args['commercial'] = e
            if estate == Advert.ESTATE_TERRITORY:
                for e, slug in Advert.TERRITORIES_SLUG.iteritems():
                    if slug == type2:
                        query = query & Q(territory=e)
                        self.path_args['territory'] = e

        # тип загородное недвижимости
        country = self.request.REQUEST.getlist('country')
        if country and estate == Advert.ESTATE_COUNTRY:
            query = query & Q(country__in=country)

        # тип загородное недвижимости
        commercial = self.request.REQUEST.getlist('commercial')
        if commercial and estate == Advert.ESTATE_COMMERCIAL:
            query = query & Q(commercial__in=commercial)

        # тип земли
        territory = self.request.REQUEST.getlist('territory')
        if territory and estate == Advert.ESTATE_TERRITORY:
            query = query & Q(territory__in=territory)

        # цена
        try:
            min_price = int(self.request.REQUEST.get('min_price'))
            if min_price:
                query = query & Q(price__gte=min_price)
        except:
            pass

        try:
            max_price = int(self.request.REQUEST.get('max_price'))
            if max_price:
                query = query & Q(price__lte=max_price)
        except:
            pass

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

        if self.request.REQUEST.get('company'):
            self.company = get_object_or_404(Company, id=self.request.REQUEST.get('company'))
            query = query & Q(company=self.company)

        if self.request.REQUEST.get('user'):
            self.user = get_object_or_404(User, id=self.request.REQUEST.get('user'))
            query = query & Q(user=self.user)

        if not self.request.REQUEST.get('company'):
            if self.request.REQUEST.get('date'):
                try:
                    days = int(self.request.REQUEST.get('date', 0))
                    if days != 0:
                        query = query & Q(date__gte=datetime.now().date() - timedelta(days=days))
                except:
                    pass
            # else:
            #     query = query & Q(date__gte=datetime.now() - timedelta(days=30))


        queryset = Advert.objects.filter(query).select_related('metro', 'user', 'district')
        # queryset = queryset.exclude(company=None)

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
            count = int(self.request.GET.get('count', 15))
            if count <= 60:
                self.paginate_by = count
        except:
            pass

        return queryset

    def get_breadcrumbs(self):
        bread = []
        bread_params = {}
        if 'town' in self.path_args:
            bread_params['town'] = self.path_args['town']
            bread.append((self.town.title, Advert.get_catalog_url(bread_params)))

            if 'estate' in self.path_args:
                bread_params['estate'] = self.path_args['estate']
                bread.append((Advert.ESTATES[self.path_args['estate']], Advert.get_catalog_url(bread_params)))

                if 'type' in self.path_args:
                    bread_params['type'] = self.path_args['type']
                    type_name = ''
                    if self.path_args['type'] == 'L':
                        type_name = 'Сдам'
                    elif self.path_args['type'] == 'S':
                        type_name = 'Продам'
                    elif self.path_args['type'] == 'LP':
                        type_name = 'Сдам посуточно'
                    bread.append((type_name, Advert.get_catalog_url(bread_params)))

                    if self.path_args['estate'] == Advert.ESTATE_LIVE:
                        if 'rooms' in self.path_args:
                            if self.path_args['rooms'] == 'R':
                                rooms_title = 'Комната'
                            else:
                                rooms_title = '%s-комнатная квартира' % self.path_args['rooms']
                            bread_params['rooms'] = self.path_args['rooms']
                            bread.append((rooms_title, Advert.get_catalog_url(bread_params)))
                    elif self.path_args['estate'] == Advert.ESTATE_COUNTRY:
                        if 'country' in self.path_args:
                            bread_params['country'] = self.path_args['country']
                            bread.append((Advert.COUNTRIES[self.path_args['country']], Advert.get_catalog_url(bread_params)))
                    elif self.path_args['estate'] == Advert.ESTATE_COMMERCIAL:
                        if 'commercial' in self.path_args:
                            bread_params['commercial'] = self.path_args['commercial']
                            bread.append((Advert.COMMERCIALS[self.path_args['commercial']], Advert.get_catalog_url(bread_params)))
                    elif self.path_args['estate'] == Advert.ESTATE_TERRITORY:
                        if 'territory' in self.path_args:
                            bread_params['territory'] = self.path_args['territory']
                            bread.append((Advert.TERRITORIES[self.path_args['territory']], Advert.get_catalog_url(bread_params)))

                    if 'metro' in self.path_args:
                        bread_params['metro'] = self.path_args['metro']
                        bread.append((u'метро ' + self.metro.title, Advert.get_catalog_url(bread_params)))

                    if 'district' in self.path_args:
                        bread_params['district'] = self.path_args['district']
                        bread.append((u'район ' + self.district.title, Advert.get_catalog_url(bread_params)))

        if self.company:
            bread.append((self.company.title, self.company.get_absolute_url()))
            bread.append((u'Объявления агентства', reverse('advert:list') + '?company=%s' % self.company.id))

        if self.user:
            bread.append((self.user.get_full_name(), self.user.get_absolute_url()))
            bread.append((u'Объявления агента', reverse('advert:list') + '?user=%s' % self.user.id))

        return super(AdvertListView, self).get_breadcrumbs() + [('Каталог объявлений', reverse('advert:list'))] + bread

    def get_context_data(self, **kwargs):
        context = super(AdvertListView, self).get_context_data(**kwargs)

        # if self.request.GET.get('type') == 'S':
        #     self.path_args['type'] =

        context['kwargs'] = self.path_args
        context['town'] = self.town
        context['date_order'] = 'asc' if self.request.GET.get('sort') == 'date-desc' else 'desc'
        context['price_order'] = 'asc' if self.request.GET.get('sort') == 'price-desc' else 'desc'
        context['sort'] = self.request.GET.get('sort')
        context['count'] = self.request.GET.get('count', '15')
        context['company'] = self.company
        context['agent'] = self.user

        if self.request.REQUEST.get('map') == '1':
            context['map'] = True
            map_objects = []
            for advert in self.object_list[:2000]:
                if advert.longitude and advert.latitude:
                    map_objects.append({
                        'x': advert.latitude,
                        'y': advert.longitude,
                        'desc': advert.title,
                        'id': advert.id,
                        'hint': advert.title
                    })
            context['map_objects'] = map_objects
            self.paginate_by = 0

        # премиум объявления
        query = Q(
            town=self.request.current_town,
            company=None,
            need=Advert.NEED_SALE,
            date__gte=datetime.now().date() - timedelta(days=30),
            status=Advert.STATUS_VIEW
        )
        need = self.request.REQUEST.get('need')
        if Advert.NEEDS.has_key(need):
            query = query & Q(need=need)

        adtype = self.request.REQUEST.get('type')
        if Advert.TYPES.has_key(adtype):
            query = query & Q(adtype=adtype)
        if self.request.REQUEST.get('type') == 'LP':
            query &= Q(adtype=Advert.TYPE_LEASE, limit=Advert.LIMIT_DAY)

        estate = self.request.REQUEST.get('estate')
        if Advert.ESTATES.has_key(estate):
            query &= Q(estate=estate)

        if self.district:
            query = query & Q(district=self.district)
        if self.metro:
            query = query & Q(metro=self.metro)

        # context['vip_list'] = Advert.objects.filter(query).exclude(images__id=None).order_by('-date')[:3]
        context['actual_count'] = self.get_queryset().filter(Advert.ARCHIVE_NO_QUERY).count()

        # для описания
        GET = self.request.GET

        page_desc = {}
        if self.path_args.get('type', None) == 'L':
            page_desc['type'] = 'Снять'
            page_desc['type_l'] = 'снять'
            page_desc['oper'] = 'Аренда'
            page_desc['oper_r'] = 'аренды'
            page_desc['variant1'] = 'в аренду'
        elif self.path_args.get('type', None) == 'S':
            page_desc['type'] = 'Купить'
            page_desc['type_l'] = 'купить'
            page_desc['oper'] = 'Покупка'
            page_desc['oper_r'] = 'покупки'
            page_desc['variant1'] = 'на продажу'
        elif self.path_args.get('type', None) == 'LP':
            page_desc['type'] = 'Снять посуточно'
            page_desc['type_l'] = 'снять посуточно'
            page_desc['oper'] = 'Аренда'
            page_desc['oper_r'] = 'аренды'
            page_desc['variant1'] = 'в аренду'
        else:
            page_desc['type'] = 'Купить или снять'
            page_desc['type_l'] = 'снять или купить'
            page_desc['oper'] = 'Аренда'
            page_desc['oper_r'] = 'аренды'
            page_desc['variant1'] = 'в аренду'

        if self.path_args.get('rooms', None) == 'R' or GET.get('rooms') == 'R':
            page_desc['rooms'] = 'комнату'
            page_desc['variant2'] = 'комнаты'
        elif self.path_args.get('rooms', None) == '1' or '1' in GET.getlist('rooms'):
            page_desc['rooms'] = '1-комнатную квартиру'
            page_desc['variant2'] = 'квартиры'
        elif self.path_args.get('rooms', None) == '2' or '2' in GET.getlist('rooms'):
            page_desc['rooms'] = '2-комнатную квартиру'
            page_desc['variant2'] = 'квартиры'
        elif self.path_args.get('rooms', None) == '3' or '3' in GET.getlist('rooms'):
            page_desc['rooms'] = '3-комнатную квартиру'
            page_desc['variant2'] = 'квартиры'
        elif self.path_args.get('rooms', None) == '4' or '4' in GET.getlist('rooms'):
            page_desc['rooms'] = '4-комнатную квартиру'
            page_desc['variant2'] = 'квартиры'
        else:
            page_desc['rooms'] = 'комнату или квартиру'
            page_desc['variant2'] = 'квартиры'

        if page_desc.get('variant1') and page_desc.get('variant2'):
            page_desc['variant'] = '%s %s' % (page_desc['variant2'], page_desc['variant1'])

        context['page_desc'] = page_desc
        return context


class AdvertDetailView(BreadcrumbMixin, DetailView):
    model = Advert
    context_object_name = 'advert'
    template_name = 'main/advert/detail.html'

    def get(self, request, *args, **kwargs):
        advert = self.get_object()
        advert.views += 1
        advert.save()
        return super(AdvertDetailView, self).get(request, *args, **kwargs)

    def get_breadcrumbs(self):
        bread = []
        bread_params = {}
        bread_params['town'] = self.object.town.id
        bread.append((self.object.town.title, Advert.get_catalog_url(bread_params)))

        if self.object.estate:
            bread_params['estate'] = self.object.estate
            bread.append((Advert.ESTATES[self.object.estate], Advert.get_catalog_url(bread_params)))

            if self.object.adtype:
                bread_params['type'] = self.object.adtype
                if self.object.adtype == Advert.TYPE_LEASE and self.object.limit == Advert.LIMIT_DAY:
                    type_name = 'Сдам посуточно'
                    bread_params['type'] = 'LP'
                elif self.object.adtype == Advert.TYPE_LEASE:
                    type_name = 'Сдам'
                else:
                    type_name = 'Продам'

                bread.append((type_name, Advert.get_catalog_url(bread_params)))

                if self.object.estate == Advert.ESTATE_LIVE:
                    rooms_arg = None
                    if self.object.live == Advert.LIVE_ROOM:
                        rooms_title = 'Комната'
                        rooms_arg = 'R'
                    else:
                        if self.object.rooms:
                            rooms_title = '%s-комнатная квартира' % self.object.rooms
                            rooms_arg = str(self.object.rooms)
                        else:
                            rooms_title = 'Квартира'
                    if rooms_arg:
                        bread_params['rooms'] = rooms_arg
                        bread.append((rooms_title, Advert.get_catalog_url(bread_params)))
                elif self.object.estate == Advert.ESTATE_COUNTRY:
                    if self.object.country:
                        bread_params['country'] = self.object.country
                        bread.append((Advert.COUNTRIES[self.object.country], Advert.get_catalog_url(bread_params)))
                elif self.object.estate == Advert.ESTATE_COMMERCIAL:
                    if self.object.commercial:
                        bread_params['commercial'] = self.object.commercial
                        bread.append((Advert.COMMERCIALS[self.object.commercial], Advert.get_catalog_url(bread_params)))
                elif self.object.estate == Advert.ESTATE_TERRITORY:
                    if self.object.territory:
                        bread_params['territory'] = self.object.territory
                        bread.append((Advert.TERRITORIES[self.object.territory], Advert.get_catalog_url(bread_params)))

                if self.object.metro:
                    bread_params['metro'] = self.object.metro.id
                    bread.append((u'метро ' + self.object.metro.title, Advert.get_catalog_url(bread_params)))

                if self.object.district:
                    bread_params['district'] = self.object.district.id
                    bread.append((u'район ' + self.object.district.title, Advert.get_catalog_url(bread_params)))

        return super(AdvertDetailView, self).get_breadcrumbs() + [('Каталог объявлений', reverse('advert:list'))] + bread

    def get_context_data(self, **kwargs):
        context = super(AdvertDetailView, self).get_context_data(**kwargs)
        md = self.object.metrodistance_set.filter(metro=self.object.metro)
        context['metro_distance'] = md[0] if md else None
        context['metro_distance_list'] = self.object.metrodistance_set.all().select_related('metro').order_by('duration_transport')
        context['metro_distance_array'] = {'count': len(context['metro_distance_list']), 'obj':[]}
        for md in context['metro_distance_list']:
            context['metro_distance_array']['obj'].append({'title': md.metro.title,
                                                           'category': u'Метро',
                                                           'address': '',
                                                           'lat': md.latitude,
                                                           'lon': md.longitude})
        if self.object.metro:
            context['similar_list'] = Advert.objects.filter(
                town=self.object.town,
                metro=self.object.metro,
                estate=self.object.estate,
                adtype=self.object.adtype,
                live=self.object.live,
                district=self.object.district,
                need=Advert.NEED_SALE,
                date__gte=datetime.now() - timedelta(days=30),
                limit=self.object.limit,
                status=Advert.STATUS_VIEW
            ).exclude(id=self.object.id)[:4]
        if self.object.company:
            context['similar_company_list'] = Advert.objects.filter(town=self.object.town, company=self.object.company).exclude(id=self.object.id)[:4]

        context['feedback_form'] = FeedbackAdvertForm()

        # context['vip_list'] = Advert.objects.filter(
        #         estate=self.object.estate,
        #         adtype=self.object.adtype,
        #         live=self.object.live,
        #         district=self.object.district,
        #         town=self.object.town,
        #         company=None,
        #         need=Advert.NEED_SALE,
        #         date__gte=datetime.now() - timedelta(days=30),
        #         limit=self.object.limit,
        #         status=Advert.STATUS_VIEW
        #     ).exclude(images__id=None).order_by('?')[:3]
        return context

    def get_queryset(self):
        town_list = Town.objects.all()
        return super(AdvertDetailView, self).get_queryset().filter(status=Advert.STATUS_VIEW, town__in=town_list)


class AdvertBalloonView(AdvertDetailView):
    template_name = 'main/advert/balloon.html'


class AdvertAddressMapView(AdvertDetailView):
    template_name = 'main/advert/address-map.html'

    def get_context_data(self, **kwargs):
        context = super(AdvertAddressMapView, self).get_context_data(**kwargs)
        map_objects = []
        if self.object.longitude and self.object.latitude:
            map_objects.append({
                'x': self.object.latitude,
                'y': self.object.longitude,
                'desc': self.object.title,
                'id': self.object.id,
                'hint': self.object.title
            })

        map_list = Advert.objects.filter(
            estate=self.object.estate,
            adtype=self.object.adtype,
            live=self.object.live,
            district=self.object.district,
            town=self.object.town,
            need=Advert.NEED_SALE,
            date__gte=datetime.now() - timedelta(days=30),
            limit=self.object.limit,
            status=Advert.STATUS_VIEW
        ).exclude(id=self.object.id)

        for advert in map_list:
            if advert.longitude and advert.latitude:
                map_objects.append({
                    'x': advert.latitude,
                    'y': advert.longitude,
                    'desc': advert.title,
                    'id': advert.id,
                    'hint': advert.title
                })
        context['map_objects'] = map_objects
        return context


class HomeView_Client(ClientPermMixin, BreadcrumbMixin, ListView):
    """
    Список объявлений клиентская часть
    """
    model = Advert
    context_object_name = 'advert_list'
    paginate_by = 50
    template_name = 'main/client/home.html'
    template_name_ajax = 'main/client/home-ajax.html'
    template_name_ajax_map = 'main/client/advert/business-map.html'

    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax():
            if request.REQUEST.get('map') == '1':
                self.template_name = self.template_name_ajax_map
                self.paginate_by = 0
            else:
                self.template_name = self.template_name_ajax
        return super(HomeView_Client, self).dispatch(request, *args, **kwargs)

    def get_breadcrumbs(self):
        return super(HomeView_Client, self).get_breadcrumbs() + [('Каталог объявлений', reverse('client:home'))]

    def get_context_data(self, **kwargs):
        context = super(HomeView_Client, self).get_context_data(**kwargs)
        context['favorites'] = [advert.id for advert in self.request.user.favorites.all()]
        if self.request.REQUEST.get('map') == '1':
            context['map'] = True
            company = self.request.user.company
            if company and not self.request.user.is_staff:
                context['current_town'] = company.town

            map_objects = []
            for advert in self.object_list[:2000]:
                if advert.longitude and advert.latitude:
                    map_objects.append({
                        'x': advert.latitude,
                        'y': advert.longitude,
                        'desc': advert.title,
                        'id': advert.id,
                        'hint': advert.title
                    })
            context['map_objects'] = map_objects

        context['folded'] = [advert.id for advert in self.request.user.folded.filter(id__in = [a.id for a in context['advert_list']])]

        return context

    def get_queryset(self):
        query = Q()

        if self.request.user.is_staff:
            query &= Q(town=self.request.current_town)
        else:
            if self.request.is_moder:
                if self.request.user.town:
                    query &= Q(town=self.request.user.town)
                # if not self.request.user.has_perm('main.view_all_advert'):
                query &= Q(need=Advert.NEED_SALE, adtype=Advert.TYPE_LEASE)
            else:
                company = self.request.user.company
                if company:
                    town = company.town
                else:
                    town = self.request.current_town
                query &= Q(town=town)

        if self.request.REQUEST.get('id'):
            query = query & Q(id=self.request.REQUEST.get('id'))

        if self.request.REQUEST.get('owner_tel'):
            query = query & Q(owner_tel__icontains=clear_tel(self.request.REQUEST.get('owner_tel')))

        adtype = self.request.REQUEST.get('type')
        if Advert.TYPES.has_key(adtype):
            query = query & Q(adtype=adtype)

        type_query = Q()

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
        #     type_query = type_query | Q(adtype=Advert.TYPE_LEASE, need=Advert.NEED_SALE)
        # # сниму
        # elif 'LD' == type2:
        #     type_query = type_query | Q(adtype=Advert.TYPE_LEASE, need=Advert.NEED_DEMAND)
        # # Продам
        # elif 'SS' == type2:
        #     type_query = type_query | Q(adtype=Advert.TYPE_SALE, need=Advert.NEED_SALE)
        # # Куплю
        # elif 'SD' == type2:
        #     type_query = type_query | Q(adtype=Advert.TYPE_SALE, need=Advert.NEED_DEMAND)

        type_query = Q(adtype=Advert.TYPE_LEASE, need=Advert.NEED_SALE)

        query = query & type_query

        if not self.request.is_moder:
            if self.request.REQUEST.get('limit_day'):
                query = query & Q(limit=Advert.LIMIT_DAY)
            else:
                query = query & Q(limit=Advert.LIMIT_LONG)

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
        if estate == Advert.ESTATE_LIVE:
            query = query & Q(estate=Advert.ESTATE_LIVE)
        elif estate == Advert.ESTATE_COUNTRY:
            query = query & Q(estate=Advert.ESTATE_COUNTRY)
        elif estate == Advert.ESTATE_COMMERCIAL:
            query = query & Q(estate=Advert.ESTATE_COMMERCIAL)
        elif estate == Advert.ESTATE_TERRITORY:
            query = query & Q(estate=Advert.ESTATE_TERRITORY)

        # кол-во комнат
        try:
            room_query = Q()
            room_arg = self.request.REQUEST.getlist('rooms')
            if room_arg:
                for room in room_arg:
                    if room == 'R':
                        room_query |= Q(live=Advert.LIVE_ROOM)
                    else:
                        if int(room) in [1, 2, 3]:
                            room_query |= Q(rooms=int(room), live=Advert.LIVE_FLAT)
                        elif int(room) >= 4:
                            room_query |= Q(rooms__gt=3, live=Advert.LIVE_FLAT)
                query &= room_query
        except:
            pass

        # тип загородное недвижимости
        country = self.request.REQUEST.get('country')
        if Advert.COUNTRIES.has_key(country):
            query = query & Q(country=country)

        # тип загородное недвижимости
        commercial = self.request.REQUEST.get('commercial')
        if Advert.COMMERCIALS.has_key(commercial):
            query = query & Q(commercial=commercial)

        # тип земли
        territory = self.request.REQUEST.get('territory')
        if Advert.TERRITORIES.has_key(territory):
            query = query & Q(territory=territory)

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
        owner_query = Q()
        if self.request.REQUEST.get('owner_agent'):
            owner_query = owner_query | ~Q(company=None)
        if self.request.REQUEST.get('owner_owner'):
            owner_query = owner_query | Q(company=None)
        query = query & owner_query

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

        if self.request.REQUEST.get('company'):
            company = get_object_or_404(Company, id=self.request.REQUEST.get('company'))
            query = query & Q(company=company)

        if self.request.REQUEST.get('user'):
            user = get_object_or_404(User, id=self.request.REQUEST.get('user'))
            query = query & Q(user=user)

        if not self.request.REQUEST.get('archive'):
            if self.request.REQUEST.get('date'):
                try:
                    days = int(self.request.REQUEST.get('date', 30))
                    if days != 0:
                        query = query & Q(date__gte=datetime.now().date() - timedelta(days=days))
                except:
                    pass
            else:
                query = query & Q(date__gte=datetime.now().date() - timedelta(days=30))
        else:
            query = query & Advert.ARCHIVE_YES_QUERY

        if self.request.is_moder:
            if self.request.user.has_perm('main.view_advert_moderate'):
                if not self.request.user.has_perm('main.view_all_advert'):
                    query &= Q(status=Advert.STATUS_MODERATE, blocked=False, not_answer=False)
        else:
            query &= Q(status=Advert.STATUS_VIEW)
            # if not self.request.user.is_staff:
            #     query &= ~Q(company=None) | (Q(company=None) & self.request.user.company.get_access_query())

        queryset = Advert.objects.filter(query).select_related('metro', 'user', 'district', 'company', 'moderator')

        return queryset


class MyAdvertView_Client(ClientPermMixin, AdvertListView):
    template_name = 'main/client/advert/my-advert-page.html'

    def get_breadcrumbs(self):
        return super(AdvertListView, self).get_breadcrumbs() + [('Мои объявления', reverse('client:advert:my'))]

    def get_queryset(self):
        is_archive = self.request.GET.get('archive', False)
        query = Q(user=self.request.user)
        if is_archive:
            query &= Advert.ARCHIVE_YES_QUERY
        else:
            query &= Advert.ARCHIVE_NO_QUERY

        return Advert.objects.filter(query).select_related('company', 'user')

    def get_context_data(self, **kwargs):
        context = super(MyAdvertView_Client, self).get_context_data(**kwargs)
        context['folded'] = [advert.id for advert in self.request.user.folded.filter(id__in = [a.id for a in context['advert_list']])]
        context['archive_no_count'] = Advert.objects.filter(user=self.request.user).filter(Advert.ARCHIVE_NO_QUERY).count()
        context['archive_yes_count'] = Advert.objects.filter(user=self.request.user).filter(Advert.ARCHIVE_YES_QUERY).count()
        return context


class MyModerateAdvertView_Client(ModerPermMixin, MyAdvertView_Client):

    def get_queryset(self):
        return Advert.objects.filter(moderator=self.request.user, status=Advert.STATUS_VIEW)


class AdvertNotAnswerListView_Client(ModerPermMixin, AdvertListView):
    template_name = 'main/client/advert/not-answer-page.html'

    def get_breadcrumbs(self):
        return super(AdvertListView, self).get_breadcrumbs() + [('Не берет трубку', reverse('client:advert:not_answer'))]

    def get_queryset(self):
        query = Q(not_answer=True, status=Advert.STATUS_MODERATE)
        if self.request.user.is_staff:
            query &= Q(town=self.request.current_town)
        else:
            if self.request.is_moder:
                if self.request.user.town:
                    query &= Q(town=self.request.user.town)
            else:
                company = self.request.user.company
                if company:
                    town = company.town
                else:
                    town = self.request.current_town
                query &= Q(town=town)
        return Advert.objects.filter(query)

    def get_context_data(self, **kwargs):
        context = super(AdvertNotAnswerListView_Client, self).get_context_data(**kwargs)
        context['folded'] = [advert.id for advert in self.request.user.folded.filter(id__in = [a.id for a in context['advert_list']])]
        return context


class FavoritesView_Client(ClientPermMixin, ListView):
    model = Advert
    context_object_name = 'advert_list'
    paginate_by = 15
    template_name = 'main/client/advert/favorites.html'

    def get_queryset(self):
        return self.request.user.favorites.all()

    def get_context_data(self, **kwargs):
        context = super(FavoritesView_Client, self).get_context_data(**kwargs)
        context['favorites'] = [advert.id for advert in self.object_list]
        context['folded'] = [advert.id for advert in self.request.user.folded.filter(id__in = [a.id for a in context['advert_list']])]
        return context


class AdvertBuyedView_Client(ClientPermMixin, ListView):
    model = Advert
    context_object_name = 'advert_list'
    paginate_by = 15
    template_name = 'main/client/advert/buyed.html'

    def get_queryset(self):
        return self.request.user.buy_adverts.all()

    def get_context_data(self, **kwargs):
        context = super(AdvertBuyedView_Client, self).get_context_data(**kwargs)
        context['folded'] = [advert.id for advert in self.request.user.folded.filter(id__in = [a.id for a in context['advert_list']])]
        return context


class AdvertPreviewView_Client(ClientPermMixin, DetailView):
    model = Advert
    context_object_name = 'advert'
    template_name = 'main/client/advert/preview.html'

    def get_queryset(self):
        # query = Q()
        # if not self.request.user.has_perm('uprofile.view_moderate'):
        #     query &= ~Q(company=None) | (Q(company=None) & self.request.user.company.get_access_query())
        return super(AdvertPreviewView_Client, self).get_queryset()


class AdvertBalloonView_Client(AdvertPreviewView_Client):
    template_name = 'main/client/advert/balloon.html'

class AdvertAddressMapView_Client(AdvertPreviewView_Client):
    template_name = 'main/client/advert/address-map.html'

    def get_context_data(self, **kwargs):
        context = super(AdvertAddressMapView_Client, self).get_context_data(**kwargs)
        map_objects = []
        if self.object.longitude and self.object.latitude:
            map_objects.append({
                'x': self.object.latitude,
                'y': self.object.longitude,
                'desc': self.object.title,
                'id': self.object.id,
                'hint': self.object.title
            })

        map_list = Advert.objects.filter(
            estate=self.object.estate,
            adtype=self.object.adtype,
            live=self.object.live,
            district=self.object.district,
            town=self.object.town,
            need=Advert.NEED_SALE,
            date__gte=datetime.now() - timedelta(days=30),
            limit=self.object.limit,
            status=Advert.STATUS_VIEW
        ).exclude(id=self.object.id)

        for advert in map_list:
            if advert.longitude and advert.latitude:
                map_objects.append({
                    'x': advert.latitude,
                    'y': advert.longitude,
                    'desc': advert.title,
                    'id': advert.id,
                    'hint': advert.title
                })
        context['map_objects'] = map_objects
        return context


class AdvertClientsView_Client(ClientPermMixin, ListView):
    template_name = 'main/client/advert/list-clients.html'
    model = Advert
    advert = None
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        self.advert = get_object_or_404(Advert, id=kwargs['pk'])
        return super(AdvertClientsView_Client, self).get(request, *args, **kwargs)

    def get_queryset(self):
        query = Q()
        if self.request.GET.get('owner') == 'owner':
            query = Q(company=None)
        elif self.request.GET.get('owner') == 'company':
            query = ~Q(company=None)
        return self.advert.clients.filter(query).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(AdvertClientsView_Client, self).get_context_data(**kwargs)
        context['parent_advert'] = self.advert
        if self.advert.user == self.request.user:
            if self.advert.last_viewed_count != len(context['object_list']):
                self.advert.last_viewed_count = len(context['object_list'])
                self.advert.save()
                self.advert.clear_cache()
        if self.request.GET.get('owner') in ['owner', 'company']:
            context['owner'] = self.request.GET.get('owner')
        else:
            context['owner'] = 'all'
        return context


class AdvertComplainsView_Client(AdminRequiredMixin, ListView):
    template_name = 'main/client/advert/list-complains.html'
    model = Complain
    advert = None
    context_object_name = 'complain_list'

    def get(self, request, *args, **kwargs):
        self.advert = get_object_or_404(Advert, id=kwargs['pk'])
        return super(AdvertComplainsView_Client, self).get(request, *args, **kwargs)

    def get_queryset(self):

        return self.advert.complained.all().order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(AdvertComplainsView_Client, self).get_context_data(**kwargs)
        context['advert'] = self.advert
        return context


class AdvertImageGalleryView_Client(ClientPermMixin, DetailView):
    model = Advert
    context_object_name = 'advert'
    template_name = 'main/client/advert/image-gallery.html'


class AdvertCreateView(BreadcrumbMixin, AjaxableResponseMixin, AjaxPageMixin, CreateView):
    model = Advert
    form_class = AdvertForm
    template_name = 'main/advert/create.html'
    template_name_ajax = 'main/advert/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(AdvertCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('advert:create')
        context['remove_form'] = RequestRemoveForm()

        context['towns'] = [{
                                'id': town.id,
                                'name': town.title,
                                'x': town.longitude,
                                'y': town.latitude,
                                'metro': [{
                                    'id': metro.id,
                                    'name': metro.title
                                } for metro in town.metro_set.all()],
                                'district': [{
                                              'id': district.id,
                                              'name': district.title
                                          } for district in town.district_set.all()]
                            } for town in Town.objects.all()]
        return context

    def get_form_kwargs(self):
        kwargs = super(AdvertCreateView, self).get_form_kwargs()
        kwargs['filter_town'] = self.request.current_town
        return kwargs

    def form_valid(self, form):
        form.instance.status = Advert.STATUS_MODERATE
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            form.instance.company = self.request.user.company
            if form.instance.company:
                if form.instance.company.status == Company.STATUS_ACTIVE:
                    form.instance.status = Advert.STATUS_VIEW
        form.instance.date = datetime.now()

        if form.cleaned_data['type'] == 'LS':
            form.instance.adtype = Advert.TYPE_LEASE
            form.instance.need = Advert.NEED_SALE
        elif form.cleaned_data['type'] == 'SS':
            form.instance.adtype = Advert.TYPE_SALE
            form.instance.need = Advert.NEED_SALE
        elif form.cleaned_data['type'] == 'LD':
            form.instance.adtype = Advert.TYPE_LEASE
            form.instance.need = Advert.NEED_DEMAND
        elif form.cleaned_data['type'] == 'SD':
            form.instance.adtype = Advert.TYPE_SALE
            form.instance.need = Advert.NEED_DEMAND

        #это нужно чтобы обеспечить совместимость поиска клиентов м\д кол-вом комнат и флагами комнат
        if form.instance.need == Advert.NEED_DEMAND:
            form.instance.live_flat1 = form.instance.rooms == 1
            form.instance.live_flat2 = form.instance.rooms == 2
            form.instance.live_flat3 = form.instance.rooms == 3
            form.instance.live_flat4 = form.instance.rooms >= 4

        form.instance.parse_tags(form.instance.body)
        form.instance.parser = Parser.objects.get(title='public')
        form.instance.check_owner()
        response = super(AdvertCreateView, self).form_valid(form)
        find_advert_clients.delay(form.instance.id)
        # email
        if not self.request.user.is_authenticated():
            send_mail('main/email/new-advert.html',{
                      'user': self.request.user,
                      'advert': form.instance,
                      'subject': 'Вы подали новое объявление №%s. Объявление отправлено на модерацию' % form.instance.id
                  },
                  recipient_list=[form.instance.owner_email], fail_silently=True)
        return response

    def get_model_dict(self):
        return {
            'url': reverse('advert:create'),
            'message': '<div class="success-advert"><img src="/static/img/ok.png"><p>Ваше объявление добавлено<br> и ему присвоен номер %s</p></div>' %self.object.id
        }

    def get_breadcrumbs(self):
        return [('Создать объявление', reverse('advert:create'))]


class AdvertCreateView_Client(ClientPermMixin, BreadcrumbMixin, AjaxableResponseMixin, CreateView):
    model = Advert
    form_class = AdvertForm_Client
    template_name = 'main/client/advert/create.html'
    success_url = '/'
    not_answer = False

    def get_context_data(self, **kwargs):
        context = super(AdvertCreateView_Client, self).get_context_data(**kwargs)
        context['action'] = reverse('client:advert:create')
        context['map_town'] = self.request.current_town
        return context

    def get_form_kwargs(self):
        kwargs = super(AdvertCreateView_Client, self).get_form_kwargs()
        kwargs['filter_town'] = self.request.current_town
        kwargs['check_tel'] = self.request.user.has_perm('main.view_blacklist') and self.request.is_moder
        return kwargs

    def get_initial(self):
        initial = super(AdvertCreateView_Client, self).get_initial()
        if not self.request.is_moder:
            initial['owner_name'] = self.request.user.get_full_name()
            initial['owner_tel'] = self.request.user.tel
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.company = self.request.user.company
        form.instance.moderator = self.request.user
        form.instance.moderate_date = datetime.now()

        if form.cleaned_data['type2'] == 'LS':
            form.instance.adtype = Advert.TYPE_LEASE
            form.instance.need = Advert.NEED_SALE
        elif form.cleaned_data['type2'] == 'SS':
            form.instance.adtype = Advert.TYPE_SALE
            form.instance.need = Advert.NEED_SALE
        elif form.cleaned_data['type2'] == 'LD':
            form.instance.adtype = Advert.TYPE_LEASE
            form.instance.need = Advert.NEED_DEMAND
        elif form.cleaned_data['type2'] == 'SD':
            form.instance.adtype = Advert.TYPE_SALE
            form.instance.need = Advert.NEED_DEMAND

        if form.cleaned_data['need_metro']:
            form.instance.metro = form.cleaned_data['need_metro'][0]

        form.instance.date = datetime.now()
        form.instance.town = self.request.current_town
        form.instance.parser = Parser.objects.get(title='client')

        # функционал для модераторов
        if self.request.user.has_perm('main.change_advert_status') and \
                (self.request.user.has_perm('main.view_advert_moderate') and (form.instance.status == Advert.STATUS_MODERATE or not form.instance.id) \
                     or self.request.user.has_perm('main.view_all_advert')):

            if self.request.POST.get('not_answer'):
                form.instance.status = Advert.STATUS_MODERATE
                form.instance.moderator = self.request.user
                form.instance.moderate_date = datetime.now()
                form.instance.not_answer = True
                self.not_answer = True

        if self.request.is_moder:
            duplicates = Advert.get_duplicates(form.instance.adtype, form.instance.estate, form.instance.need, exclude_id=form.instance.id, metro=form.instance.metro_id, tel=form.instance.owner_tel)
            if duplicates:
                raise Exception(u'Есть совпадения с объявлением № ' + u', '.join([u'%s тел:%s' % (unicode(a.id), a.owner_tel) for a in duplicates]))

        form.instance.parse_tags(form.instance.body)
        result = super(AdvertCreateView_Client, self).form_valid(form)
        find_advert_clients.delay(form.instance.id)
        # form.instance.find_search_request()
        form.instance.publish()
        return result

    def get_model_dict(self):
        url = reverse('client:advert:create')
        message = '<div class="success-advert"><img src="/static/img/ok.png"><p>Ваше объявление добавлено<br> и ему присвоен номер %s</p></div>' %self.object.id
        if self.not_answer:
            #получение следующего объявления на модерацию
            query = Q(status=Advert.STATUS_MODERATE, blocked=False, not_answer=False, need=Advert.NEED_SALE, adtype=Advert.TYPE_LEASE)
            if self.request.user.town:
                query &= Q(town=self.request.user.town)
            advert_list = Advert.objects.filter(query).exclude(id=self.object.id).order_by('date')
            url = reverse('client:advert:edit', kwargs={'pk': advert_list[0].id}) if advert_list else reverse('client:advert:moderated'),
            message = '<div class="success-advert"><img src="/static/img/ok.png"><p>Объявление №%s отправлено на модерацию.</p></div>' % self.object.id

        return {
            'url': url,
            'message': message
        }

    def get_breadcrumbs(self):
        return [('Создать объявление', reverse('client:advert:create'))]


class AdvertUpdateView_Client(ClientPermMixin, AdvertUpdatePermMixin, AjaxableResponseMixin, UpdateView):
    model = Advert
    form_class = AdvertForm_Client
    template_name = 'main/client/advert/edit.html'
    context_object_name = 'advert'
    success_url = '/'
    not_answer = False

    def get_context_data(self, **kwargs):
        context = super(AdvertUpdateView_Client, self).get_context_data(**kwargs)
        context['action'] = reverse('client:advert:edit', kwargs={'pk': self.object.id})
        context['map_town'] = self.object.town
        if not self.object.blocked:
            self.object.blocked = True
            self.object.block_date = datetime.now()
            self.object.block_user = self.request.user
            self.object.save()
            self.object.clear_cache()
        return context

    def form_valid(self, form):
        if form.instance.blocked:
            if form.instance.block_user != self.request.user:
                raise Exception(u'Объявление заблокировано другим пользователем')
            form.instance.blocked = False
            form.instance.block_user = None
            form.instance.block_date = None

        if form.cleaned_data['type2'] == 'LS':
            form.instance.adtype = Advert.TYPE_LEASE
            form.instance.need = Advert.NEED_SALE
        elif form.cleaned_data['type2'] == 'SS':
            form.instance.adtype = Advert.TYPE_SALE
            form.instance.need = Advert.NEED_SALE
        elif form.cleaned_data['type2'] == 'LD':
            form.instance.adtype = Advert.TYPE_LEASE
            form.instance.need = Advert.NEED_DEMAND
        elif form.cleaned_data['type2'] == 'SD':
            form.instance.adtype = Advert.TYPE_SALE
            form.instance.need = Advert.NEED_DEMAND

        if form.cleaned_data['need_metro']:
            form.instance.metro = form.cleaned_data['need_metro'][0]

        form.instance.date = datetime.now()

        # функционал для модераторов
        if self.request.user.has_perm('main.change_advert_status') and  \
                (self.request.user.has_perm('main.view_advert_moderate') and (form.instance.status == Advert.STATUS_MODERATE or not form.instance.id) \
                    or self.request.user.has_perm('main.view_all_advert')):

            if self.request.POST.get('not_answer'):
                form.instance.status = Advert.STATUS_MODERATE
                form.instance.moderator = self.request.user
                form.instance.moderate_date = datetime.now()
                form.instance.not_answer = True
                self.not_answer = True

        if self.request.is_moder:
            duplicates = Advert.get_duplicates(form.instance.adtype, form.instance.estate, form.instance.need, exclude_id=form.instance.id, metro=form.instance.metro_id, tel=form.instance.owner_tel)
            if duplicates:
                raise Exception(u'Есть совпадения с объявленияем № ' + u', '.join([u'%s тел:%s' % (unicode(a.id), a.owner_tel) for a in duplicates]))

        form.instance.parse_tags(form.instance.body)
        form.instance.clear_description()
        result = super(AdvertUpdateView_Client, self).form_valid(form)
        find_advert_clients.delay(form.instance.id)
        # form.instance.find_clients()
        form.instance.clear_cache()
        return result

    def get_model_dict(self):
        url = reverse('client:advert:edit', kwargs={'pk': self.object.id})
        message = '<div class="success-advert"><img src="/static/img/ok.png"><p>Ваше объявление №%s сохранено</p></div>' % self.object.id
        if self.not_answer:
            #получение следующего объявления на модерацию
            query = Q(status=Advert.STATUS_MODERATE, blocked=False, not_answer=False, need=Advert.NEED_SALE, adtype=Advert.TYPE_LEASE)
            if self.request.user.town:
                query &= Q(town=self.request.user.town)
            for days in xrange(1, 10):
                advert_list = Advert.objects.filter(query).exclude(id=self.object.id).filter(date__gte=datetime.now()-timedelta(days=days)).order_by('-parser__priority', '-date')[:1]
                if advert_list:
                    break
            url = reverse('client:advert:edit', kwargs={'pk': advert_list[0].id}) if advert_list else reverse('client:advert:moderated'),
            message = '<div class="success-advert"><img src="/static/img/ok.png"><p>Объявление №%s отправлено на модерацию.</p></div>' % self.object.id

        return {
            'url': url,
            'message': message
        }

    def get_form_kwargs(self):
        kwargs = super(AdvertUpdateView_Client, self).get_form_kwargs()
        kwargs['filter_town'] = self.object.town
        kwargs['check_tel'] = self.request.user.has_perm('main.view_blacklist') and self.request.is_moder
        if kwargs['instance'].adtype == Advert.TYPE_LEASE and kwargs['instance'].need == Advert.NEED_SALE:
            kwargs['initial']['type2'] = 'LS'
        elif kwargs['instance'].adtype == Advert.TYPE_SALE and kwargs['instance'].need == Advert.NEED_SALE:
            kwargs['initial']['type2'] = 'SS'
        elif kwargs['instance'].adtype == Advert.TYPE_LEASE and kwargs['instance'].need == Advert.NEED_DEMAND:
            kwargs['initial']['type2'] = 'LD'
        elif kwargs['instance'].adtype == Advert.TYPE_SALE and kwargs['instance'].need == Advert.NEED_DEMAND:
            kwargs['initial']['type2'] = 'SD'
        return kwargs


class AdvertDeleteView_Client(ClientPermMixin, AdvertDeletePermMixin, AjaxableResponseMixin, DeleteView):
    model = Advert
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super(AdvertDeleteView_Client, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return {
            'url': reverse('client:home')
        }


class AddFavoriteView_Client(ClientPermMixin, View):
    @method_decorator(ajax_request)
    def post(self, request, *args, **kwargs):
        advert = get_object_or_404(Advert, id=int(request.POST.get('id')))
        if advert.favorites.filter(id=request.user.id).count() > 0:
            advert.favorites.remove(request.user)
            return {
                'result': False,
                'id': advert.id
            }
        else:
            advert.favorites.add(request.user)
            return {
                'result': True,
                'id': advert.id
            }


class AdvertBuyView_Client(AjaxableResponseMixin, ClientPermMixin, FormView):
    form_class = BuyPayForm
    success_url = '/'
    template_name = 'main/client/advert/buy-form.html'
    advert = None

    def get_context_data(self, **kwargs):
        context = super(AdvertBuyView_Client, self).get_context_data(**kwargs)
        context['action'] = reverse('client:advert:buy')
        context['id'] = self.request.GET.get('id')
        context['count_buys'] = self.request.user.buys
        return context

    def get_initial(self):
        return {
            'advert_id': self.request.GET.get('id'),
            'count': 1
        }

    def form_valid(self, form):
        company = self.request.user.company

        query = Q(id=form.cleaned_data['advert_id'])
        query &= ~Q(company=None) | (Q(company=None) & self.request.user.get_access_query())
        advert_list = Advert.objects.filter(query)
        if not advert_list:
            raise Exception(u'Нет прав')
        self.advert = advert_list[0]

        if not company and not self.request.user.is_staff:
            raise Exception(u'Нельзя выкупить')
        buys_count = int(form.cleaned_data['days'])
        if self.request.user.buys - buys_count < 0:
            raise Exception(u'У вас не хватает выкупов')
        self.request.user.buys -= buys_count
        self.request.user.save()
        if company:
            self.advert.buy_company.add(company)
        self.advert.buy_users.add(self.request.user)
        self.advert.buy_date = datetime.now() + timedelta(days=buys_count)
        self.advert.save()
        return super(AdvertBuyView_Client, self).form_valid(form)

    def get_model_dict(self):
        from main.templatetags.main_tags import fmt_date
        return {
            'result': True,
            'id': self.advert.id,
            'message': 'Объявление %s выкуплено до %s' % (self.advert.id, fmt_date(self.advert.buy_date))
        }


class AdvertSendFriendView(AjaxableResponseMixin, FormView):
    form_class = FeedbackAdvertForm
    advert = None
    success_url = '/'

    def post(self, request, *args, **kwargs):
        self.advert = get_object_or_404(Advert, id=kwargs['pk'])
        return super(AdvertSendFriendView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        send_mail('main/email/send-advert.html',{
            'email': form.cleaned_data['email'],
            'friend_email': form.cleaned_data['friend_email'],
            'subject': u'Ваш друг (%s) отправил вам объявление' % form.cleaned_data['email'],
            'advert': self.advert
            },
            recipient_list=[form.cleaned_data['friend_email']],
            fail_silently=True)
        return super(AdvertSendFriendView, self).form_valid(form)

    def get_model_dict(self):
        return {
            'message': 'Объявление отправлено'
        }


class RequestView(AjaxableResponseMixin, CreateView):
    form_class = RequestForm
    model = Advert
    template_name = 'main/advert/request.html'
    success_url = '/'
    source_advert = None

    def get(self, request, *args, **kwargs):
        if request.GET.get('id'):
            advert_list = Advert.objects.filter(id=request.GET.get('id'))
            if advert_list:
                self.source_advert = advert_list[0]
        return super(RequestView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RequestView, self).get_context_data(**kwargs)
        return context

    def get_form_kwargs(self):
        kwargs = super(RequestView, self).get_form_kwargs()
        kwargs['filter_town'] = self.request.current_town
        if self.source_advert:
            kwargs['initial'] = {}
            kwargs['initial']['estate'] = self.source_advert.estate
            if self.source_advert.estate == Advert.ESTATE_LIVE:
                kwargs['initial']['live'] = self.source_advert.live
            elif self.source_advert.estate == Advert.ESTATE_COUNTRY:
                kwargs['initial']['country'] = self.source_advert.country
            elif self.source_advert.estate == Advert.ESTATE_COMMERCIAL:
                kwargs['initial']['commercial'] = self.source_advert.commercial
            elif self.source_advert.estate == Advert.ESTATE_TERRITORY:
                kwargs['initial']['territory'] = self.source_advert.territory
            kwargs['initial']['adtype2'] = self.source_advert.adtype
            if self.source_advert.limit == Advert.LIMIT_DAY:
                kwargs['initial']['adtype2'] = 'LP'
            if self.source_advert.metro:
                kwargs['initial']['need_metro'] = [str(self.source_advert.metro_id)]
            kwargs['initial']['district'] = self.source_advert.district_id
            kwargs['initial']['price'] = self.source_advert.price
        return kwargs

    @method_decorator(atomic)
    def form_valid(self, form):
        form.instance.date = datetime.now()
        form.instance.town = self.request.current_town
        form.instance.need = Advert.NEED_DEMAND
        form.instance.parser = Parser.objects.get(title='request')
        adtype = form.cleaned_data['adtype2']
        if Advert.TYPES.has_key(adtype):
            form.instance.adtype = adtype
        if adtype == 'LP':
            form.instance.adtype = Advert.TYPE_LEASE
            form.instance.limit = Advert.LIMIT_DAY
        if form.cleaned_data['need_metro']:
            form.instance.metro = form.cleaned_data['need_metro'][0]
        response = super(RequestView, self).form_valid(form)
        find_advert_clients.delay(form.instance.id)
        # email
        send_mail('main/email/new-request.html',{
            'user': self.request.user,
            'advert': form.instance,
            'subject': 'Вы подали новый запрос на поиск №%s' % form.instance.id
            },
            recipient_list=[form.instance.owner_email], fail_silently=True)
        return response

    def get_model_dict(self):
        return {
            'message': '<div class="success-advert"><img src="/static/img/ok.png"><p>Ваше заявка принята<br> и ей присвоен номер %s</p></div>' %self.object.id
        }


class AdvertRequestRemoveView(AjaxableResponseMixin, FormView):
    form_class = RequestRemoveForm
    success_url = '/'

    def form_valid(self, form):
        send_mail('main/email/new-request-remove.html',{
            'id': form.cleaned_data['nomer'],
            'tel': form.cleaned_data['tel'],
            'subject': u'Подан запрос на удаление объявления №%s' % form.cleaned_data['nomer']
            },
            recipient_list=settings.NOTICE_REMOVE_EMAIL,
            fail_silently=True)
        return super(AdvertRequestRemoveView, self).form_valid(form)

    def get_model_dict(self):
        return {
            'message': u'Ваша заявка на удаление отправлена'
        }


class AdvertComplainView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AdvertComplainView, self).dispatch(request, *args, **kwargs)

    @method_decorator(ajax_request)
    def post(self, request, *args, **kwargs):
        try:
            advert = get_object_or_404(Advert, id=kwargs['pk'])
            complain_text = request.POST.get('complain')
            reason = request.POST.get('reason')
            complain = Complain(user=request.user, content=advert, reason=reason, date=datetime.now())
            complain.save()

            send_mail('main/email/complain.html',{
                'user': request.user,
                'advert': advert,
                'complain': complain_text,
                'subject': u'На объявление №%s отправлена жалоба: %s' % (advert.id, complain_text)
                },
                recipient_list=settings.NOTICE_COMPLAIN_EMAIL,
                fail_silently=True)

            return {
                'result': True,
                'id': advert.id,
                'message': u'На объявление №%s отправлена жалоба: %s' % (advert.id, complain_text)
            }
        except Exception as ex:
            return {
                'result': False,
                'message': unicode(ex)
            }


class AdvertFoldView_Client(ClientPermMixin, View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AdvertFoldView_Client, self).dispatch(request, *args, **kwargs)

    @method_decorator(ajax_request)
    def post(self, request, *args, **kwargs):
        try:
            query = Q(id=kwargs['pk'])
            # if not request.user.has_perm('uprofile.view_client') and not request.user.has_perm('uprofile.view_moderate'):
            #     query &= ~Q(company=None) | (Q(company=None) & request.user.company.get_access_query())
            advert_list = Advert.objects.filter(query)
            if not advert_list:
                raise Exception(u'Нет прав')
            advert = advert_list[0]

            folded = request.POST.get('fold', False)
            if folded == 'true':
                advert.folded.add(request.user)
            else:
                advert.folded.remove(request.user)

            return {
                'result': True,
                'id': advert.id,
                'fold': folded
            }
        except Exception as ex:
            return {
                'result': False,
                'message': unicode(ex)
            }


class AdvertApproveView_Client(ModerPermMixin, AdvertUpdateView_Client):

    def form_valid(self, form):
        if not self.request.user.has_perm('main.change_advert_status'):
            raise Exception(u'Нет прав')
        if not ((self.request.user.has_perm('main.view_advert_moderate') and form.instance.status == Advert.STATUS_MODERATE) \
            or self.request.user.has_perm('main.view_all_advert')):
            raise Exception(u'Нет прав')

        if form.instance.blocked:
            if form.instance.block_user != self.request.user:
                raise Exception(u'Объявление заблокировано другим пользователем')
        prev_status = form.instance.status
        form.instance.status = Advert.STATUS_VIEW
        form.instance.blocked = False
        form.instance.block_user = None
        form.instance.block_date = None
        form.instance.moderator = self.request.user
        form.instance.moderate_date = datetime.now()
        form.instance.date = datetime.now()
        form.instance.not_answer = False

        result = super(AdvertApproveView_Client, self).form_valid(form)

        if prev_status != Advert.STATUS_VIEW:
            form.instance.publish()
        return result

    def get_model_dict(self):
        #получение следующего объявления на модерацию
        query = Q(status=Advert.STATUS_MODERATE, blocked=False, not_answer=False, need=Advert.NEED_SALE, adtype=Advert.TYPE_LEASE)
        if self.request.user.town:
            query &= Q(town=self.request.user.town)
        for days in xrange(1, 10):
            advert_list = Advert.objects.filter(query).filter(date__gte=datetime.now()-timedelta(days=days)).order_by('-parser__priority', '-date')[:1]
            if advert_list:
                break

        return {
            'result': True,
            'id': self.object.id,
            'message': '<div class="success-advert"><img src="/static/img/ok.png"><p>Объявление №%s размещено</p></div>' % self.object.id,
            'url': reverse('client:advert:edit', kwargs={'pk': advert_list[0].id}) if advert_list else reverse('client:advert:moderated'),
        }


class AdvertIsAgentView_Client(ModerPermMixin, View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AdvertIsAgentView_Client, self).dispatch(request, *args, **kwargs)

    @method_decorator(ajax_request)
    @atomic
    def post(self, request, *args, **kwargs):
        try:
            advert = get_object_or_404(Advert, id=kwargs['pk'])

            if not request.user.has_perm('main.change_advert_status'):
                raise Exception(u'Нет прав')
            if not ((request.user.has_perm('main.view_advert_moderate') and advert.status == Advert.STATUS_MODERATE) \
                or request.user.has_perm('main.view_all_advert')):
                raise Exception(u'Нет прав')

            if advert.blocked:
                if advert.block_user != request.user:
                    raise Exception(u'Объявление заблокировано пользователем')

            tel = clear_tel_list(advert.owner_tel)
            blacklist = Blacklist.objects.filter(tel__icontains=tel)
            if not blacklist:
                Blacklist.add_tel(tel, 'Определен как агент по объявлению %s' % advert.id)

            advert.status = Advert.STATUS_BLOCKED
            advert.save()

            deleted_adverts = Advert.block_by_tel(advert.owner_tel)

            #получение следующего объявления на модерацию
            query = Q(status=Advert.STATUS_MODERATE, blocked=False, not_answer=False, need=Advert.NEED_SALE, adtype=Advert.TYPE_LEASE)
            if request.user.town:
                query &= Q(town=request.user.town)
            for days in xrange(1, 10):
                advert_list = Advert.objects.filter(query).exclude(id=advert.id).filter(date__gte=datetime.now()-timedelta(days=days)).order_by('-parser__priority', '-date')[:1]
                if advert_list:
                    break

            return {
                'result': True,
                'id': advert.id,
                'message': '<div class="success-advert"><img src="/static/img/delete.png"><p>Объявление №%s удалено. <br>Номер телефона отправлен в черный список%s</p></div>' % (advert.id, \
                    '<br>Удалено ' + str(deleted_adverts) + ' объявлений с таким телефоном' if deleted_adverts else ''),
                'url': reverse('client:advert:edit', kwargs={'pk': advert_list[0].id}) if advert_list else reverse('client:advert:moderated'),
            }
        except Exception as ex:
            return {
                'result': False,
                'message': unicode(ex)
            }


class AdvertIrrelevantView_Client(ModerPermMixin, View):
    """
    Отметить как неактуальное
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AdvertIrrelevantView_Client, self).dispatch(request, *args, **kwargs)

    @method_decorator(ajax_request)
    @atomic
    def post(self, request, *args, **kwargs):
        try:
            advert = get_object_or_404(Advert, id=kwargs['pk'])

            if not request.user.has_perm('main.change_advert_status'):
                raise Exception(u'Нет прав')
            if not ((request.user.has_perm('main.view_advert_moderate') and advert.status == Advert.STATUS_MODERATE) \
                or request.user.has_perm('main.view_all_advert')):
                raise Exception(u'Нет прав')

            if advert.blocked:
                if advert.block_user != request.user:
                    raise Exception(u'Объявление заблокировано пользователем')

            advert.status = Advert.STATUS_BLOCKED
            advert.save()

            #получение следующего объявления на модерацию
            query = Q(status=Advert.STATUS_MODERATE, blocked=False, not_answer=False, need=Advert.NEED_SALE, adtype=Advert.TYPE_LEASE)
            if request.user.town:
                query &= Q(town=request.user.town)
            for days in xrange(1, 10):
                advert_list = Advert.objects.filter(query).exclude(id=advert.id).filter(date__gte=datetime.now()-timedelta(days=days)).order_by('-parser__priority', '-date')[:1]
                if advert_list:
                    break

            return {
                'result': True,
                'id': advert.id,
                'message': '<div class="modal-icon"><img src="/static/img/delete.png"><p>Объявление №%s удалено.</p></div>' % advert.id,
                'url': reverse('client:advert:edit', kwargs={'pk': advert_list[0].id}) if advert_list else reverse('client:advert:moderated'),
                }
        except Exception as ex:
            return {
                'result': False,
                'message': unicode(ex)
            }


class AdvertSearchDuplicateView_Client(ModerPermMixin, View):
    """
    Поиск дублей
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AdvertSearchDuplicateView_Client, self).dispatch(request, *args, **kwargs)

    @method_decorator(ajax_request)
    def post(self, request, *args, **kwargs):
        try:
            if request.POST.get('type2') == 'LS':
                adtype = Advert.TYPE_LEASE
                need = Advert.NEED_SALE
            elif request.POST.get('type2') == 'SS':
                adtype = Advert.TYPE_SALE
                need = Advert.NEED_SALE
            elif request.POST.get('type2') == 'LD':
                adtype = Advert.TYPE_LEASE
                need = Advert.NEED_DEMAND
            elif request.POST.get('type2') == 'SD':
                adtype = Advert.TYPE_SALE
                need = Advert.NEED_DEMAND
            else:
                adtype = None
                need = None

            duplicate_list = Advert.get_duplicates(adtype, request.POST.get('estate'), need, exclude_id=request.POST.get('id'), metro=request.POST.get('metro'), tel=clear_tel(request.POST.get('owner_tel')))
            if duplicate_list:
                message = u'<div class="modal-icon"><img src="/static/img/copy.png"><p>Есть совпадения с объявлением № ' + u', '.join([u'%s тел:%s' % (unicode(a.id), a.owner_tel) for a in duplicate_list]) + '</p>'
                result = True
            else:
                message = ''
                result = False

            return {
                'result': True,
                'exists': result,
                'id': [a.id for a in duplicate_list],
                'message': message
                }
        except Exception as ex:
            return {
                'result': False,
                'message': unicode(ex)
            }


class AdvertSetBlockView_Client(ModerPermMixin, View):
    """
    Блокировка объявления
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AdvertSetBlockView_Client, self).dispatch(request, *args, **kwargs)

    @method_decorator(ajax_request)
    def post(self, request, *args, **kwargs):
        result = True
        advert = get_object_or_404(Advert, id=kwargs['pk'])
        if advert.blocked:
            if advert.block_user != request.user:
                result = False
            advert.blocked = True
            advert.block_user = request.user
            advert.block_date = datetime.now()
            advert.save()
        else:
            result = False

        return {
            'result': result,
            'id': advert.id
        }


class AdvertSetArchiveView_Client(ClientPermMixin, View):
    """
    Сдача объявления в архив
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AdvertSetArchiveView_Client, self).dispatch(request, *args, **kwargs)

    @method_decorator(ajax_request)
    def post(self, request, *args, **kwargs):
        result = True
        advert = get_object_or_404(Advert, id=request.POST.get('id'))
        if advert.user == request.user:
            if request.POST.get('archive') == '1':
                advert.archive = Advert.ARCHIVE_YES
            elif request.POST.get('archive') == '0':
                advert.archive = Advert.ARCHIVE_NO
            advert.save()
        else:
            result = False

        return {
            'result': result,
            'id': advert.id
        }




class AdvertViewByUsersView(AdminRequiredMixin, BreadcrumbMixin, ListView):
    model = Advert
    template_name = 'main/client/advert/stat/users.html'
    context_object_name = 'user_list'
    advert = None
    paginate_by = 50

    def get(self, request, *args, **kwargs):
        self.advert = get_object_or_404(Advert, id=kwargs['pk'])
        return super(AdvertViewByUsersView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.advert.viewed.all()

    def get_context_data(self, **kwargs):
        context = super(AdvertViewByUsersView, self).get_context_data(**kwargs)
        context['advert'] = self.advert
        return context

    def get_breadcrumbs(self):
        return super(AdvertViewByUsersView, self).get_breadcrumbs() + [
            ('Пользователи смотревшие объявление %s' % self.advert.id, reverse('client:advert:stat:users', kwargs={'pk': self.advert.id})),
            ]


class AdvertViewByVashdomPasswordView(AdminRequiredMixin, BreadcrumbMixin, ListView):
    model = Advert
    template_name = 'main/client/advert/stat/password-vashdom.html'
    context_object_name = 'password_list'
    advert = None
    paginate_by = 50

    def get(self, request, *args, **kwargs):
        self.advert = get_object_or_404(Advert, id=kwargs['pk'])
        return super(AdvertViewByVashdomPasswordView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.advert.password_set.all()

    def get_context_data(self, **kwargs):
        context = super(AdvertViewByVashdomPasswordView, self).get_context_data(**kwargs)
        context['advert'] = self.advert
        return context

    def get_breadcrumbs(self):
        return super(AdvertViewByVashdomPasswordView, self).get_breadcrumbs() + [
            ('Пароли открывшие объявление %s' % self.advert.id, reverse('client:advert:stat:password-vashdom', kwargs={'pk': self.advert.id})),
            ]
