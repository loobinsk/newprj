# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, View, FormView, TemplateView
from gutils.views import BreadcrumbMixin, AjaxableResponseMixin, AjaxPageMixin
from main.models import Advert, VKAdvert, Town, Metro, District, Complain, Parser
from datetime import datetime, timedelta
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from annoying.decorators import ajax_request
from django.http import HttpResponseForbidden, HttpResponsePermanentRedirect, Http404, HttpResponseRedirect
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404
from vashdom.forms import AdvertForm, PaymentOrderForm
from django.utils.decorators import method_decorator
from datetime import datetime
from main.task import find_advert_clients
from mail_templated import send_mail
from vashdom.models import VashdomAdvert, Tariff, VashdomVKAdvert
from django.conf import settings


class Test_AdvertListView(BreadcrumbMixin, ListView):
    """
    Список объявлений
    """
    model = VashdomAdvert
    context_object_name = 'advert_list'
    paginate_by = 30
    template_name = 'vashdom/advert/page.html'
    template_name_ajax = 'vashdom/advert/page-ajax.html'
    district = None
    metro = None
    path_args = {}
    town = None
    company = None
    user = None

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax():
            self.template_name = self.template_name_ajax
        return super(Test_AdvertListView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        reqdict = dict(request.GET.dicts[0].lists())
        params = {}
        for key, value in reqdict.iteritems():
            if isinstance(value, list) and len(value) == 1:
                params[key] = value[0]
            else:
                params[key] = value
        params['town'] = request.current_town.id
        return HttpResponsePermanentRedirect(VashdomAdvert.get_catalog_url(params))

    def get(self, request, *args, **kwargs):
        if not request.current_town.main_base:
            return HttpResponseRedirect(reverse('advert:vklist'))
        else:
            return super(Test_AdvertListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        self.path_args = {}

        query = Q()

        self.path_args['type'] = Advert.TYPE_LEASE
        self.path_args['estate'] = Advert.ESTATE_LIVE

        if self.kwargs.has_key('town'):
            self.town = get_object_or_404(Town, slug=self.kwargs['town'])
            query &= Q(town=self.town)
            self.path_args['town'] = self.town.id
        else:
            self.town = self.request.current_town
            query &= Q(town=self.town)

        query &= VashdomAdvert.get_advert_query(self.town)

        district_arg = self.request.GET.getlist('district')
        if district_arg:
            try:
                district_list = District.objects.filter(id__in=district_arg if isinstance(district_arg, list) else [district_arg])
                if district_list:
                    query = query & Q(district_id__in=[district.id for district in district_list])
                    self.district = district_list[0]
            except:
                pass
        district_slug = self.kwargs.get('district', '')
        if district_slug:
            district_list = District.objects.filter(slug=district_slug)
            if district_list:
                query = query & Q(district=district_list[0])
                self.district = district_list[0]
                self.path_args['district'] = district_list[0].id
            else:
                raise Http404()

        try:
            metro_arg = self.request.GET.getlist('metro')
            if metro_arg:
                metro_list = Metro.objects.filter(id__in=metro_arg if isinstance(metro_arg, list) else [metro_arg])
                if metro_list:
                    query = query & Q(metro_id__in=[metro.id for metro in metro_list])
                    self.metro = metro_list[0]
        except:
            pass
        metro_slug = self.kwargs.get('metro', '')
        if metro_slug:
            metro_list = Metro.objects.filter(slug=metro_slug, town_id=self.path_args['town'])
            if metro_list:
                query = query & Q(metro=metro_list[0])
                self.metro = metro_list[0]
                self.path_args['metro'] = metro_list[0].id
            else:
                raise Http404()


        room_query = Q()
        room_list = self.request.GET.getlist('rooms')
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

        # цена
        try:
            min_price = int(self.request.GET.get('min_price'))
            if min_price:
                query = query & Q(price__gte=min_price)
        except:
            pass

        try:
            max_price = int(self.request.GET.get('max_price'))
            if max_price:
                query = query & Q(price__lte=max_price)
        except:
            pass

        # площадь
        try:
            min_square = int(self.request.GET.get('min_square'))
            if min_square:
                query = query & Q(square__gte=min_square)
        except:
            pass
        try:
            max_square = int(self.request.GET.get('max_square'))
            if max_square:
                query = query & Q(square__lte=max_square)
        except:
            pass

        if self.request.GET.get('tv') == 'on':
            query &= Q(tv=True)
        if self.request.GET.get('washer') == 'on':
            query &= Q(washer=True)
        if self.request.GET.get('refrigerator') == 'on':
            query &= Q(refrigerator=True)
        if self.request.GET.get('furniture') == 'on':
            query &= Q(furniture=True)

        # фильруем объвления на которые пользователь пожаловался
        if self.request.user.is_authenticated():
            query &= ~Q(complained__user=self.request.user)

        queryset = VashdomAdvert.objects.filter(query).select_related('metro', 'user', 'district', 'town')

        sort = self.request.GET.get('sort')
        if sort == 'date-asc':
            queryset = queryset.order_by('date_vashdom')
        elif sort == 'date-desc':
            queryset = queryset.order_by('-date_vashdom')
        elif sort == 'price-asc':
            queryset = queryset.order_by('price')
        elif sort == 'price-desc':
            queryset = queryset.order_by('-price')
        else:
            queryset = queryset.order_by('-date_vashdom')

            #  try:
            #     count = int(self.request.GET.get('count', 30))
            #   if count <= 60:
            #       self.paginate_by = count
            #  except:
            #     pass

        if self.request.GET.get('with_photo') == 'on':
            queryset = queryset.annotate(image_count=Count('images')).exclude(image_count=0)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(Test_AdvertListView, self).get_context_data(**kwargs)

        # if self.request.GET.get('type') == 'S':
        #     self.path_args['type'] =

        context['kwargs'] = self.path_args
        context['town'] = self.town
        context['date_order'] = 'asc' if self.request.GET.get('sort') == 'date-desc' else 'desc'
        context['price_order'] = 'asc' if self.request.GET.get('sort') == 'price-desc' else 'desc'
        context['sort'] = self.request.GET.get('sort')
        #  context['count'] = self.request.GET.get('count', '15')
        
        # Дополнительные ссылки
        ext_links = []
        ext_links2 = []
        params = {}
        town_str = u''
        if 'town' in self.path_args:
            params['town'] = self.path_args['town']
            t = Town.objects.get(id=params['town'])
            town_str = u' в %s' % t.title_d

        rooms = self.request.GET.getlist('rooms')
        if rooms:
            if rooms[0] == VashdomAdvert.LIVE_ROOM or rooms[0] == 'r':
                params['rooms'] = VashdomAdvert.LIVE_ROOM
                ext_links.append((VashdomAdvert.get_catalog_url(params), u'Снять комнату без посредников%s' % town_str))

                for price in [15000, 25000, 35000, 50000, 60000]:
                    ext_links2.append(((VashdomAdvert.get_catalog_url(params) + '&max_price=%s' % price, u'Снять комнату без посредников%s до %s руб.' % (town_str, price))))

                params['rooms'] = 1
                ext_links.append((VashdomAdvert.get_catalog_url(params), u'Снять 1-комнатную квартиру без посредников%s' % town_str))
                params['rooms'] = 2
                ext_links.append((VashdomAdvert.get_catalog_url(params), u'Снять 2-комнатную квартиру без посредников%s' % town_str))
            else:
                for price in [15000, 25000, 35000, 50000, 60000]:
                    ext_links2.append(((VashdomAdvert.get_catalog_url(params) + '?rooms=1&rooms=2&rooms=3&rooms=4&max_price=%s' % price, u'Снять квартиру без посредников%s до %s руб.' % (town_str, price))))

                room = int(rooms[0])
                if room-1 > 0:
                    params['rooms'] = room-1
                    ext_links.append((VashdomAdvert.get_catalog_url(params), u'Снять %s-комнатную квартиру без посредников%s' % (room-1, town_str)))
                if room+1 <= 4:
                    params['rooms'] = room+1
                    ext_links.append((VashdomAdvert.get_catalog_url(params), u'Снять %s-комнатную квартиру без посредников%s' % (room+1, town_str)))
                if room+2 <= 4:
                    params['rooms'] = room+2
                    ext_links.append((VashdomAdvert.get_catalog_url(params), u'Снять %s-комнатную квартиру без посредников%s' % (room+2, town_str)))

        else:
            for price in [15000, 25000, 35000, 50000, 60000]:
                ext_links2.append(((VashdomAdvert.get_catalog_url(params) + '?max_price=%s' % price, u'Снять жилье без посредников%s до %s руб.' % (town_str, price))))

            params['rooms'] = VashdomAdvert.LIVE_ROOM
            ext_links.append((VashdomAdvert.get_catalog_url(params), u'Снять комнату без посредников%s' % town_str))
            params['rooms'] = 1
            ext_links.append((VashdomAdvert.get_catalog_url(params), u'Снять 1-комнатную квартиру без посредников%s' % town_str))
            params['rooms'] = 2
            ext_links.append((VashdomAdvert.get_catalog_url(params), u'Снять 2-комнатную квартиру без посредников%s' % town_str))

        context['ext_links'] = ext_links
        context['ext_links2'] = ext_links2
        context['ext_town'] = town_str
        if self.path_args.get('metro'):
            metro = Metro.objects.get(id=self.path_args.get('metro'))
            context['ext_metro'] = u' у метро %s' % metro.title
        if self.path_args.get('district'):
            district = District.objects.get(id=self.path_args.get('district'))
            context['ext_district'] = u' в районе %s' % district.title
        if rooms:
            rooms_arr =[]
            for room in rooms:
                if room == VashdomAdvert.LIVE_ROOM or room == 'r':
                    rooms_arr.append( u'комнат')
                else:
                    rooms_arr.append(u'%s-комнатных квартир' % room)

            context['ext_room'] = u', '.join(rooms_arr)
        else:
            context['ext_room'] = u'комнат и квартир'
        return context
    
    def get_breadcrumbs(self):
        bread = []
        bread_params = {}
        if 'town' in self.path_args:
            bread_params['town'] = self.path_args['town']
            bread.append((self.town.title, VashdomAdvert.get_catalog_url(bread_params)))

            if 'estate' in self.path_args:
                bread_params['estate'] = self.path_args['estate']
                bread.append((VKAdvert.ESTATES[self.path_args['estate']], VashdomAdvert.get_catalog_url(bread_params)))

                if 'type' in self.path_args:
                    bread_params['type'] = self.path_args['type']
                    type_name = ''
                    if self.path_args['type'] == 'L':
                        type_name = 'Сдам'
                    elif self.path_args['type'] == 'S':
                        type_name = 'Продам'
                    elif self.path_args['type'] == 'LP':
                        type_name = 'Сдам посуточно'
                    bread.append((type_name, VashdomAdvert.get_catalog_url(bread_params)))

                    if self.path_args['estate'] == VKAdvert.ESTATE_LIVE:
                        if 'rooms' in self.path_args:
                            if self.path_args['rooms'] == 'R':
                                rooms_title = 'Комната'
                            else:
                                rooms_title = '%s-комнатная квартира' % self.path_args['rooms']
                            bread_params['rooms'] = self.path_args['rooms']
                            bread.append((rooms_title, VKAdvert.get_catalog_url(bread_params)))
                    elif self.path_args['estate'] == VashdomAdvert.ESTATE_COUNTRY:
                        if 'country' in self.path_args:
                            bread_params['country'] = self.path_args['country']
                            bread.append((VKAdvert.COUNTRIES[self.path_args['country']], VashdomAdvert.get_catalog_url(bread_params)))
                    elif self.path_args['estate'] == VashdomAdvert.ESTATE_COMMERCIAL:
                        if 'commercial' in self.path_args:
                            bread_params['commercial'] = self.path_args['commercial']
                            bread.append((VKAdvert.COMMERCIALS[self.path_args['commercial']], VashdomAdvert.get_catalog_url(bread_params)))
                    elif self.path_args['estate'] == VashdomAdvert.ESTATE_TERRITORY:
                        if 'territory' in self.path_args:
                            bread_params['territory'] = self.path_args['territory']
                            bread.append((VKAdvert.TERRITORIES[self.path_args['territory']], VashdomAdvert.get_catalog_url(bread_params)))

                    if 'metro' in self.path_args:
                        bread_params['metro'] = self.path_args['metro']
                        bread.append((u'метро ' + self.metro.title, VashdomAdvert.get_catalog_url(bread_params)))

                    if 'district' in self.path_args:
                        bread_params['district'] = self.path_args['district']
                        bread.append((u'район ' + self.district.title, VashdomAdvert.get_catalog_url(bread_params)))

        return super(Test_AdvertListView, self).get_breadcrumbs() + [('Каталог объявлений', reverse('advert:list'))] + bread


class AdvertMapView(Test_AdvertListView):
    template_name = 'vashdom/advert/map.html'
    template_name_ajax = 'vashdom/advert/map-ajax.html'

    def get_context_data(self, **kwargs):
        context = super(AdvertMapView, self).get_context_data(**kwargs)

        map_objects = []
        for advert in self.object_list[:2000]:
            if advert.longitude and advert.latitude:
                map_objects.append({
                    'x': advert.latitude,
                    'y': advert.longitude,
                    'desc': advert.title,
                    'id': advert.id,
                    'hint': advert.title,
                    'pointer': advert.rooms if advert.live == Advert.LIVE_FLAT else 'k'
                })
        context['map_objects'] = map_objects
        self.paginate_by = 0
        return context


class AdvertCreateView(BreadcrumbMixin, AjaxableResponseMixin, AjaxPageMixin, CreateView):
    model = VashdomAdvert
    form_class = AdvertForm
    template_name = 'vashdom/advert/create.html'
    template_name_ajax = 'vashdom/advert/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(AdvertCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('advert:create')

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
        form.instance.date = datetime.now()
        form.instance.estate = Advert.ESTATE_LIVE
        form.instance.adtype = Advert.TYPE_LEASE
        form.instance.need = Advert.NEED_SALE


        if form.cleaned_data['rooms_ext'] == 'R':
            form.instance.live = Advert.LIVE_ROOM
        for room in xrange(1, 5):
            if form.cleaned_data['rooms_ext'] == str(room):
                form.instance.live = Advert.LIVE_FLAT
                form.instance.rooms = room

        #это нужно чтобы обеспечить совместимость поиска клиентов м\д кол-вом комнат и флагами комнат
        if form.instance.need == Advert.NEED_DEMAND:
            form.instance.live_flat1 = form.instance.rooms == 1
            form.instance.live_flat2 = form.instance.rooms == 2
            form.instance.live_flat3 = form.instance.rooms == 3
            form.instance.live_flat4 = form.instance.rooms >= 4

        form.instance.parser = Parser.objects.get(title='smart')
        form.instance.check_owner()
        response = super(AdvertCreateView, self).form_valid(form)

        result = form.instance.check_spam(actions=True)
        if result:
            form.instance.status = Advert.STATUS_BLOCKED
            form.instance.save()
        else:
            find_advert_clients.delay(form.instance.id)
        # email
        if not self.request.user.is_authenticated():
            send_mail('vashdom/email/new-advert.html',{
                      'user': self.request.user,
                      'advert': form.instance,
                      'subject': 'Вы подали новое объявление №%s. Объявление отправлено на модерацию' % form.instance.id
                  },
                  recipient_list=[form.instance.owner_email], fail_silently=True)
        return response

    def get_model_dict(self):
        return {
            'url': reverse('advert:create'),
            'message': '<div class="success-advert"><p>Ваше объявление добавлено и отправлено на модерацию</p></div>'
        }

    def get_breadcrumbs(self):
        return [('Разместить объявление', reverse('advert:create'))]


class AdvertComplainView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AdvertComplainView, self).dispatch(request, *args, **kwargs)

    @method_decorator(ajax_request)
    def post(self, request, *args, **kwargs):
        try:
            advert = get_object_or_404(VashdomAdvert, id=kwargs['pk'])
            reason = request.POST.get('reason')
            complain_text = Complain.REASONS[reason]
            complain = Complain(user=request.user, content=advert, reason=reason, date=datetime.now())
            complain.save()

            send_mail('vashdom/email/complain.html',{
                'advert': advert,
                'complain': complain_text,
                'user': request.user,
                'subject': u'На объявление №%s отправлена жалоба: %s' % (advert.id, complain_text)
                },
                recipient_list=settings.NOTICE_COMPLAIN_EMAIL,
                fail_silently=True)

            return {
                'result': True,
                'id': advert.id,
                'message': u'На объявление №%s отправлена жалоба: %s<br>Это объявление больше не будет вам отображаться' % (advert.id, complain_text)
            }
        except Exception as ex:
            return {
                'result': False,
                'message': unicode(ex)
            }


class VKAdvertComplainView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(VKAdvertComplainView, self).dispatch(request, *args, **kwargs)

    @method_decorator(ajax_request)
    def post(self, request, *args, **kwargs):
        # try:
            advert = get_object_or_404(VashdomVKAdvert, id=kwargs['pk'])
            reason = request.POST.get('reason')
            complain_text = Complain.REASONS[reason]
            complain = Complain(user=request.user, content=advert, reason=reason, date=datetime.now())
            complain.save()

            send_mail('vashdom/email/vkcomplain.html',{
                'advert': advert,
                'complain': complain_text,
                'user': request.user,
                'subject': u'На объявление №%s отправлена жалоба: %s' % (advert.id, complain_text)
                },
                recipient_list=settings.NOTICE_COMPLAIN_EMAIL,
                fail_silently=True)

            return {
                'result': True,
                'id': advert.id,
                'message': u'На объявление №%s отправлена жалоба: %s<br>Это объявление больше не будет вам отображаться' % (advert.id, complain_text)
            }
        # except Exception as ex:
        #     return {
        #         'result': False,
        #         'message': unicode(ex)
        #     }


class AdvertDetailView(BreadcrumbMixin, DetailView):
    model = VashdomAdvert
    context_object_name = 'advert'
    template_name = 'vashdom/advert/detail.html'

    def get(self, request, *args, **kwargs):
        try:
            advert = self.get_object()
        except Http404 as ex:
            return HttpResponseRedirect(redirect_to='/%s/' % request.current_town.slug)
        advert.views += 1
        advert.save()
        return super(AdvertDetailView, self).get(request, *args, **kwargs)

    def get_breadcrumbs(self):
        bread = []
        bread_params = {}
        bread_params['town'] = self.object.town.id
        bread.append((self.object.town.title, VashdomAdvert.get_catalog_url(bread_params)))

        if self.object.estate:
            bread_params['estate'] = self.object.estate
            bread.append((Advert.ESTATES[self.object.estate], VashdomAdvert.get_catalog_url(bread_params)))

            if self.object.adtype:
                bread_params['type'] = self.object.adtype
                if self.object.adtype == Advert.TYPE_LEASE and self.object.limit == Advert.LIMIT_DAY:
                    type_name = 'Сдам посуточно'
                    bread_params['type'] = 'LP'
                elif self.object.adtype == Advert.TYPE_LEASE:
                    type_name = 'Сдам'
                else:
                    type_name = 'Продам'

                bread.append((type_name, VashdomAdvert.get_catalog_url(bread_params)))

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
                        bread.append((rooms_title, VashdomAdvert.get_catalog_url(bread_params)))
                elif self.object.estate == Advert.ESTATE_COUNTRY:
                    if self.object.country:
                        bread_params['country'] = self.object.country
                        bread.append((Advert.COUNTRIES[self.object.country], VashdomAdvert.get_catalog_url(bread_params)))
                elif self.object.estate == Advert.ESTATE_COMMERCIAL:
                    if self.object.commercial:
                        bread_params['commercial'] = self.object.commercial
                        bread.append((Advert.COMMERCIALS[self.object.commercial], VashdomAdvert.get_catalog_url(bread_params)))
                elif self.object.estate == Advert.ESTATE_TERRITORY:
                    if self.object.territory:
                        bread_params['territory'] = self.object.territory
                        bread.append((Advert.TERRITORIES[self.object.territory], VashdomAdvert.get_catalog_url(bread_params)))

                if self.object.metro:
                    bread_params['metro'] = self.object.metro.id
                    bread.append((u'метро ' + self.object.metro.title, VashdomAdvert.get_catalog_url(bread_params)))

                if self.object.district:
                    bread_params['district'] = self.object.district.id
                    bread.append((u'район ' + self.object.district.title, VashdomAdvert.get_catalog_url(bread_params)))

        return super(AdvertDetailView, self).get_breadcrumbs() + [('Каталог объявлений', reverse('advert:list'))] + bread

    def get_context_data(self, **kwargs):
        context = super(AdvertDetailView, self).get_context_data(**kwargs)
        md = self.object.metrodistance_set.filter(metro=self.object.metro)
        context['metro_distance'] = md[0] if md else None
        context['metro_distance_list'] = self.object.metrodistance_set.all().select_related('metro').order_by('duration_transport')
        if self.object.metro:
            query = Q(town=self.object.town,
                metro=self.object.metro,
                estate=self.object.estate,
                adtype=self.object.adtype,
                live=self.object.live,
                district=self.object.district,
                need=Advert.NEED_SALE,
                date__gte=datetime.now().date() - timedelta(days=30),
                limit=self.object.limit,
                status=Advert.STATUS_VIEW,
                company=None) & VashdomAdvert.get_advert_query(context['object'].town)
            context['similar_list'] = VashdomAdvert.objects.filter(query).exclude(id=self.object.id)[:4]
        return context

    def get_queryset(self):
        town_list = Town.objects.all()
        return super(AdvertDetailView, self).get_queryset().filter(VashdomAdvert.get_advert_query()).filter(town__in=town_list)


class AdvertBalloonView(AdvertDetailView):
    template_name = 'vashdom/advert/balloon.html'


class VKAdvertListView(BreadcrumbMixin, ListView):
    """
    Список объявлений
    """
    model = VashdomVKAdvert
    context_object_name = 'advert_list'
    paginate_by = 30
    template_name = 'vashdom/vkadvert/page.html'
    template_name_ajax = 'vashdom/vkadvert/page-ajax.html'
    district = None
    metro = None
    path_args = {}
    town = None
    company = None
    user = None

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax():
            self.template_name = self.template_name_ajax
        return super(VKAdvertListView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        reqdict = dict(request.GET.dicts[0].lists())
        params = {}
        for key, value in reqdict.iteritems():
            if isinstance(value, list) and len(value) == 1:
                params[key] = value[0]
            else:
                params[key] = value
        params['town'] = request.current_town.id
        params['estate'] = VKAdvert.ESTATE_LIVE
        params['type'] = VKAdvert.TYPE_LEASE
        return HttpResponsePermanentRedirect(VashdomVKAdvert.get_catalog_url(params))

    def get_queryset(self):
        self.path_args = {}

        query = Q(status=VKAdvert.STATUS_VIEW,
                  adtype=VKAdvert.TYPE_LEASE,
                  need=VKAdvert.NEED_SALE,
                  # date_vashdom__lte=datetime.now()
        )

        self.path_args['type'] = VKAdvert.TYPE_LEASE
        self.path_args['estate'] = VKAdvert.ESTATE_LIVE

        if self.kwargs.has_key('town'):
            self.town = get_object_or_404(Town, slug=self.kwargs['town'])
            query &= Q(town=self.town)
            self.path_args['town'] = self.town.id
        else:
            self.town = self.request.current_town
            query &= Q(town=self.town)

        # query &= get_roomas_VKAdvert_query(self.town)

        adtype = self.request.GET.get('type')
        if VKAdvert.TYPES.has_key(adtype):
            query = query & Q(adtype=adtype)
            self.path_args['type'] = adtype
        if self.request.GET.get('type') == VKAdvert.TYPE_LEASE:
            query &= Q(limit=VKAdvert.LIMIT_LONG)
        if self.request.GET.get('type') == 'LP':
            query &= Q(adtype=VKAdvert.TYPE_LEASE, limit=VKAdvert.LIMIT_DAY)
            self.path_args['type'] = 'LP'

        adtype_slug = self.kwargs.get('type', '')
        adtype = None
        for e, slug in VKAdvert.TYPES_SLUG.iteritems():
            if slug == adtype_slug:
                adtype = e
        if adtype and VKAdvert.TYPES.has_key(adtype):
            query = query & Q(adtype=adtype)
            self.path_args['type'] = adtype
        if self.kwargs.get('type', '') == 'sdam':
            query &= Q(limit=VKAdvert.LIMIT_LONG)
        if self.kwargs.get('type', '') == 'sdam-posutochno':
            adtype = 'LP'
            self.path_args['type'] = adtype
            query &= Q(adtype=VKAdvert.TYPE_LEASE, limit=VKAdvert.LIMIT_DAY)


        district_arg = self.request.GET.getlist('district')
        if district_arg:
            try:
                district_list = District.objects.filter(id__in=district_arg if isinstance(district_arg, list) else [district_arg])
                if district_list:
                    query = query & Q(district_id__in=[district.id for district in district_list])
                    self.district = district_list[0]
            except:
                pass
        district_slug = self.kwargs.get('district', '')
        if district_slug:
            district_list = District.objects.filter(slug=district_slug)
            if district_list:
                query = query & Q(district=district_list[0])
                self.district = district_list[0]
                self.path_args['district'] = district_list[0].id
            else:
                raise Http404()

        metro_arg = self.request.GET.getlist('metro')
        if metro_arg:
            metro_list = Metro.objects.filter(id__in=metro_arg if isinstance(metro_arg, list) else [metro_arg])
            if metro_list:
                query = query & Q(metro_id__in=[metro.id for metro in metro_list])
                self.metro = metro_list[0]
        metro_slug = self.kwargs.get('metro', '')
        if metro_slug:
            metro_list = Metro.objects.filter(slug=metro_slug)
            if metro_list:
                query = query & Q(metro=metro_list[0])
                self.metro = metro_list[0]
                self.path_args['metro'] = metro_list[0].id
            else:
                raise Http404()


        # estate = self.request.GET.get('estate')
        # if VKAdvert.ESTATES.has_key(estate):
        #     query = query & Q(estate=estate)
        # estate_slug = self.kwargs.get('estate', '')
        # estate = None
        # for e, slug in VKAdvert.ESTATES_SLUG.iteritems():
        #     if slug == estate_slug:
        #         estate = e
        # if estate and VKAdvert.ESTATES.has_key(estate):
        #     query = query & Q(estate=estate)
        #     self.path_args['estate'] = estate


        room_query = Q()
        room_list = self.request.GET.getlist('rooms')
        if 'R' in room_list:
            room_query &= Q(live=VKAdvert.LIVE_ROOM)
        for room in room_list:
            try:
                rooms = int(room)
                if rooms in [1, 2, 3]:
                    room_query |= Q(rooms=rooms, live=VKAdvert.LIVE_FLAT)
                elif rooms >= 4:
                    room_query |= Q(rooms__gt=3, live=VKAdvert.LIVE_FLAT)
            except:
                pass
        query &= room_query

        type2 = self.kwargs.get('type2', '')
        if type2:
            if type2 == 'komnata':
                query &= Q(live=VKAdvert.LIVE_ROOM)
                self.path_args['rooms'] = 'R'
            else:
                for r in xrange(1, 5):
                    if type2 == '%s-komnatnaya-kvartira' % r:
                        if r >= 4:
                            query &= Q(rooms__gt=4, live=VKAdvert.LIVE_FLAT)
                        else:
                            query &= Q(rooms=r, live=VKAdvert.LIVE_FLAT)
                        self.path_args['rooms'] = str(r)

        # цена
        try:
            min_price = int(self.request.GET.get('min_price'))
            if min_price:
                query = query & Q(price__gte=min_price)
        except:
            pass

        try:
            max_price = int(self.request.GET.get('max_price'))
            if max_price:
                query = query & Q(price__lte=max_price)
        except:
            pass

        # площадь
        try:
            min_square = int(self.request.GET.get('min_square'))
            if min_square:
                query = query & Q(square__gte=min_square)
        except:
            pass
        try:
            max_square = int(self.request.GET.get('max_square'))
            if max_square:
                query = query & Q(square__lte=max_square)
        except:
            pass

        # фильруем объвления на которые пользователь пожаловался
        if self.request.user.is_authenticated():
            query &= ~Q(complained__user=self.request.user)

        queryset = VashdomVKAdvert.objects.filter(query).select_related('metro', 'district')

        sort = self.request.GET.get('sort')
        if sort == 'date-asc':
            queryset = queryset.order_by('date_vashdom')
        elif sort == 'date-desc':
            queryset = queryset.order_by('-date_vashdom')
        elif sort == 'price-asc':
            queryset = queryset.order_by('price')
        elif sort == 'price-desc':
            queryset = queryset.order_by('-price')
        else:
            queryset = queryset.order_by('-date_vashdom')

        try:
            count = int(self.request.GET.get('count', 30))
            if count <= 60:
                self.paginate_by = count
        except:
            pass

        if self.request.GET.get('with_photo') == 'on':
            queryset = queryset.annotate(image_count=Count('images')).exclude(image_count=0)

        return queryset

    def get_breadcrumbs(self):
        bread = []
        bread_params = {}
        if 'town' in self.path_args:
            bread_params['town'] = self.path_args['town']
            bread.append((self.town.title, VashdomVKAdvert.get_catalog_url(bread_params)))

            if 'estate' in self.path_args:
                bread_params['estate'] = self.path_args['estate']
                bread.append((VKAdvert.ESTATES[self.path_args['estate']], VashdomVKAdvert.get_catalog_url(bread_params)))

                if 'type' in self.path_args:
                    bread_params['type'] = self.path_args['type']
                    type_name = ''
                    if self.path_args['type'] == 'L':
                        type_name = 'Сдам'
                    elif self.path_args['type'] == 'S':
                        type_name = 'Продам'
                    elif self.path_args['type'] == 'LP':
                        type_name = 'Сдам посуточно'
                    bread.append((type_name, VashdomVKAdvert.get_catalog_url(bread_params)))

                    if self.path_args['estate'] == VKAdvert.ESTATE_LIVE:
                        if 'rooms' in self.path_args:
                            if self.path_args['rooms'] == 'R':
                                rooms_title = 'Комната'
                            else:
                                rooms_title = '%s-комнатная квартира' % self.path_args['rooms']
                            bread_params['rooms'] = self.path_args['rooms']
                            bread.append((rooms_title, VKAdvert.get_catalog_url(bread_params)))
                    elif self.path_args['estate'] == VashdomVKAdvert.ESTATE_COUNTRY:
                        if 'country' in self.path_args:
                            bread_params['country'] = self.path_args['country']
                            bread.append((VKAdvert.COUNTRIES[self.path_args['country']], VashdomVKAdvert.get_catalog_url(bread_params)))
                    elif self.path_args['estate'] == VashdomVKAdvert.ESTATE_COMMERCIAL:
                        if 'commercial' in self.path_args:
                            bread_params['commercial'] = self.path_args['commercial']
                            bread.append((VKAdvert.COMMERCIALS[self.path_args['commercial']], VashdomVKAdvert.get_catalog_url(bread_params)))
                    elif self.path_args['estate'] == VashdomVKAdvert.ESTATE_TERRITORY:
                        if 'territory' in self.path_args:
                            bread_params['territory'] = self.path_args['territory']
                            bread.append((VKAdvert.TERRITORIES[self.path_args['territory']], VashdomVKAdvert.get_catalog_url(bread_params)))

                    if 'metro' in self.path_args:
                        bread_params['metro'] = self.path_args['metro']
                        bread.append((u'метро ' + self.metro.title, VashdomVKAdvert.get_catalog_url(bread_params)))

                    if 'district' in self.path_args:
                        bread_params['district'] = self.path_args['district']
                        bread.append((u'район ' + self.district.title, VashdomVKAdvert.get_catalog_url(bread_params)))

        return super(VKAdvertListView, self).get_breadcrumbs() + [('Каталог объявлений Вконтакте', reverse('advert:vklist'))] + bread

    def get_context_data(self, **kwargs):
        context = super(VKAdvertListView, self).get_context_data(**kwargs)

        # if self.request.GET.get('type') == 'S':
        #     self.path_args['type'] =

        context['kwargs'] = self.path_args
        context['town'] = self.town
        context['date_order'] = 'asc' if self.request.GET.get('sort') == 'date-desc' else 'desc'
        context['price_order'] = 'asc' if self.request.GET.get('sort') == 'price-desc' else 'desc'
        context['sort'] = self.request.GET.get('sort')
        context['count'] = self.request.GET.get('count', '15')

        return context
    
    
class VKAdvertDetailView(BreadcrumbMixin, DetailView):
    model = VashdomVKAdvert
    context_object_name = 'advert'
    template_name = 'vashdom/vkadvert/detail.html'

    def get(self, request, *args, **kwargs):
        advert = self.get_object()
        advert.views += 1
        advert.save()
        return super(VKAdvertDetailView, self).get(request, *args, **kwargs)

    def get_breadcrumbs(self):
        bread = []
        bread_params = {}
        bread_params['town'] = self.object.town.id
        bread.append((self.object.town.title, VashdomVKAdvert.get_catalog_url(bread_params)))

        if self.object.estate:
            bread_params['estate'] = self.object.estate
            bread.append((VKAdvert.ESTATES[self.object.estate], VashdomVKAdvert.get_catalog_url(bread_params)))

            if self.object.adtype:
                bread_params['type'] = self.object.adtype
                if self.object.adtype == VKAdvert.TYPE_LEASE and self.object.limit == VKAdvert.LIMIT_DAY:
                    type_name = 'Сдам посуточно'
                    bread_params['type'] = 'LP'
                elif self.object.adtype == VKAdvert.TYPE_LEASE:
                    type_name = 'Сдам'
                else:
                    type_name = 'Продам'

                bread.append((type_name, VashdomVKAdvert.get_catalog_url(bread_params)))

                if self.object.estate == VKAdvert.ESTATE_LIVE:
                    rooms_arg = None
                    if self.object.live == VKAdvert.LIVE_ROOM:
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
                        bread.append((rooms_title, VashdomVKAdvert.get_catalog_url(bread_params)))
                elif self.object.estate == VKAdvert.ESTATE_COUNTRY:
                    if self.object.country:
                        bread_params['country'] = self.object.country
                        bread.append((VKAdvert.COUNTRIES[self.object.country], VashdomVKAdvert.get_catalog_url(bread_params)))
                elif self.object.estate == VKAdvert.ESTATE_COMMERCIAL:
                    if self.object.commercial:
                        bread_params['commercial'] = self.object.commercial
                        bread.append((VKAdvert.COMMERCIALS[self.object.commercial], VashdomVKAdvert.get_catalog_url(bread_params)))
                elif self.object.estate == VKAdvert.ESTATE_TERRITORY:
                    if self.object.territory:
                        bread_params['territory'] = self.object.territory
                        bread.append((VKAdvert.TERRITORIES[self.object.territory], VashdomVKAdvert.get_catalog_url(bread_params)))

                if self.object.metro:
                    bread_params['metro'] = self.object.metro.id
                    bread.append((u'метро ' + self.object.metro.title, VashdomVKAdvert.get_catalog_url(bread_params)))

                if self.object.district:
                    bread_params['district'] = self.object.district.id
                    bread.append((u'район ' + self.object.district.title, VashdomVKAdvert.get_catalog_url(bread_params)))

        return super(VKAdvertDetailView, self).get_breadcrumbs() + [('Каталог объявлений Вконтакте', reverse('advert:vklist'))] + bread

    def get_context_data(self, **kwargs):
        context = super(VKAdvertDetailView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        town_list = Town.objects.all()
        return super(VKAdvertDetailView, self).get_queryset().filter(town__in=town_list, status=VKAdvert.STATUS_VIEW)


class AdvertGetAccessView(TemplateView):
    template_name = 'vashdom/advert/get-access.html'
    payment = None

    def get_context_data(self, **kwargs):
        context = super(AdvertGetAccessView, self).get_context_data(**kwargs)
        context['form'] = PaymentOrderForm(town=self.request.current_town)
        query = Q(hidden=False)
        if self.request.GET.get('vk') == 'true':
            query &= Q(vk_base=True)
            context['base'] = 'vk'
            context['advert'] = get_object_or_404(VashdomVKAdvert, id=self.request.GET.get('id'))
        else:
            query &= Q(main_base=True)
            context['base'] = 'main'
            context['advert'] = get_object_or_404(VashdomAdvert, id=self.request.GET.get('id'))
        context['tariff_list'] = Tariff.objects.filter(query).order_by('order')

        context['current_town'] = context['advert'].town

        if self.request.user.is_authenticated():
            if self.request.GET.get('vk') == 'true':
                password_list = self.request.user.vashdom_passwords.filter(end_date__gte=datetime.now(),
                                                                           count__gt=0,
                                                                           town=context['advert'].town,
                                                                           vk_base=True)
            else:
                password_list = self.request.user.vashdom_passwords.filter(end_date__gte=datetime.now(),
                                                                           count__gt=0,
                                                                           town=context['advert'].town,
                                                                           main_base=True)
            context['can_fast'] = len(password_list) > 0
        else:
            context['can_fast'] = False


        return context
