#-*- coding: utf-8 -*-
from .models import VashdomAdvert, Town, Metro, District, VashdomVKAdvert
from uimg.models import UserImage
from rest_framework import routers, serializers, viewsets
from rest_framework import generics
from datetime import datetime, timedelta
from django.db.models import Q
import json
from .templatetags.vashdom_tags import fmt_vashdom_date
from sorl.thumbnail import get_thumbnail
from datetime import datetime


class VashdomDateField(serializers.DateTimeField):

    def to_representation(self, value):
        try:
            return value.strftime('%d.%m.%y')
        except:
            return ''


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = ('image', )


class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = ('id',
                  'title',
                  'title_d',
        )


class MetroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metro
        fields = ('id',
                  'title',
        )


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id',
                  'title',
        )


class AdvertSerializer(serializers.HyperlinkedModelSerializer):
    date = VashdomDateField()
    images = ImageSerializer(many=True)
    town = TownSerializer()
    metro = MetroSerializer()
    district = DistrictSerializer()
    url = serializers.CharField(source='get_absolute_url')
    tags = serializers.SerializerMethodField()

    class Meta:
        model = VashdomAdvert
        fields = ('id',
                  'date',
                  'title',
                  'short_title',
                  'description',
                  'images',
                  'adtype',
                  'need',
                  'estate',
                  'live',
                  'limit',
                  'address',
                  'town',
                  'metro',
                  'district',
                  'square',
                  'living_square',
                  'kitchen_square',
                  'rooms',
                  'price',
                  'owner_name',
                  'owner_tel',
                  'longitude',
                  'latitude',
                  'url',
                  'tags',
        )

    def get_tags(self, advert):
        tags = []
        for field in advert.comfort_list:
            if field[1]:
                tags.append(field[2])
        return tags


class Advert2Serializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    tags = serializers.SerializerMethodField()

    class Meta:
        model = VashdomAdvert
        fields = ('id',
                  'date',
                  'title',
                  'short_title',
                  'description',
                  'images',
                  'adtype',
                  'need',
                  'estate',
                  'live',
                  'limit',
                  'address',
                  'town',
                  'metro',
                  'district',
                  'square',
                  'living_square',
                  'kitchen_square',
                  'rooms',
                  'price',
                  'owner_name',
                  'owner_tel',
                  'longitude',
                  'latitude',
                  'tags',
                  'refrigerator',
                  'tv',
                  'washer',
                  'phone',
                  'internet',
                  'conditioner',
                  'furniture',
                  'separate_wc',
                  'balcony',
                  'euroremont',
                  'redecoration',
                  'no_remont',
                  'need_remont',
                  'electric',
                  'gas',
                  'water',
                  'sewage'
        )

    def get_tags(self, advert):
        tags = []
        for field in advert.comfort_list:
            if field[1]:
                tags.append(field[2])
        return tags


class AdvertVkSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    tags = serializers.SerializerMethodField()

    class Meta:
        model = VashdomVKAdvert
        fields = ('id',
                  'date',
                  'title',
                  'short_title',
                  'body',
                  'images',
                  'adtype',
                  'need',
                  'estate',
                  'live',
                  'limit',
                  'address',
                  'town',
                  'metro',
                  'district',
                  'square',
                  'living_square',
                  'kitchen_square',
                  'rooms',
                  'price',
                  'owner_name',
                  'owner_tel',
                  'longitude',
                  'latitude',
                  'tags',
        )

    def get_tags(self, advert):
        tags = []
        for field in advert.comfort_list:
            if field[1]:
                tags.append(field[2])
        return tags


class AdvertList(generics.ListAPIView):
    serializer_class = AdvertSerializer
    paginate_by = 30

    def get_queryset(self):
        query = Q()
        query = Q(date__lte=datetime.now())

        query &= VashdomAdvert.get_advert_query()

        town_id = self.request.GET.get('town')
        if town_id:
            query &= Q(town_id=town_id)
        else:
            query &= Q(town_id__in=[1, 2])

        ids = self.request.GET.getlist('ids')
        if ids:
            query &= Q(id__in=ids)

        if self.request.GET.get('district'):
            try:
                district_list = District.objects.filter(id=self.request.GET.get('district'))
                if district_list:
                    query = query & Q(district=district_list[0])
                    self.district = district_list[0]
            except:
                pass

        try:
            metro_arg = self.request.GET.getlist('metro')
            if metro_arg:
                metro_list = Metro.objects.filter(id__in=metro_arg if isinstance(metro_arg, list) else [metro_arg])
                if metro_list:
                    query = query & Q(metro_id__in=[metro.id for metro in metro_list])
                    self.metro = metro_list[0]
        except:
            pass

        room_query = Q()
        room_list = self.request.GET.getlist('rooms')
        if 'R' in room_list or 'r' in room_list:
            room_query &= Q(live=VashdomAdvert.LIVE_ROOM)
        for room in room_list:
            try:
                rooms = int(room)
                if rooms in [1, 2, 3]:
                    room_query |= Q(rooms=rooms, live=VashdomAdvert.LIVE_FLAT)
                elif rooms >= 4:
                    room_query |= Q(rooms__gt=3, live=VashdomAdvert.LIVE_FLAT)
            except:
                pass
        query &= room_query

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
        if self.request.GET.get('internet') == 'on':
            query &= Q(internet=True)
        if self.request.GET.get('phone') == 'on':
            query &= Q(phone=True)
        if self.request.GET.get('balcony') == 'on':
            query &= Q(balcony=True)

        # фильруем объвления на которые пользователь пожаловался
        if self.request.user.is_authenticated():
            query &= ~Q(complained__user=self.request.user)

        query &= Q(date__gte=datetime.now() - timedelta(days=30))

        queryset = VashdomAdvert.objects.filter(query).select_related('metro', 'user', 'district')

        sort = self.request.GET.get('sort')
        if sort == 'date-asc':
            queryset = queryset.order_by('date')
        elif sort == 'date-desc':
            queryset = queryset.order_by('-date')
        elif sort == 'price-asc':
            queryset = queryset.order_by('price')
        elif sort == 'price-desc':
            queryset = queryset.order_by('-price')
        else:
            queryset = queryset.order_by('-date')

        return queryset


class Advert2List(generics.ListAPIView):
    serializer_class = Advert2Serializer
    paginate_by = 30

    def get_queryset(self):
        query = Q()

        query &= VashdomAdvert.get_advert_query()

        town_id = self.request.GET.get('town')
        if town_id:
            query &= Q(town_id=town_id)
        else:
            query &= Q(town_id__in=[1, 2, 10, 6])

        ids = self.request.GET.getlist('ids')
        if ids:
            query &= Q(id__in=ids)

        if self.request.GET.get('district'):
            try:
                district_list = District.objects.filter(id=self.request.GET.get('district'))
                if district_list:
                    query = query & Q(district=district_list[0])
                    self.district = district_list[0]
            except:
                pass

        try:
            metro_arg = self.request.GET.getlist('metro')
            if metro_arg:
                metro_list = Metro.objects.filter(id__in=metro_arg if isinstance(metro_arg, list) else [metro_arg])
                if metro_list:
                    query = query & Q(metro_id__in=[metro.id for metro in metro_list])
                    self.metro = metro_list[0]
        except:
            pass

        room_query = Q()
        room_list = self.request.GET.getlist('rooms')
        if 'R' in room_list or 'r' in room_list:
            room_query &= Q(live=VashdomAdvert.LIVE_ROOM)
        for room in room_list:
            try:
                rooms = int(room)
                if rooms in [1, 2, 3]:
                    room_query |= Q(rooms=rooms, live=VashdomAdvert.LIVE_FLAT)
                elif rooms >= 4:
                    room_query |= Q(rooms__gt=3, live=VashdomAdvert.LIVE_FLAT)
            except:
                pass
        query &= room_query

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
        if self.request.GET.get('internet') == 'on':
            query &= Q(internet=True)
        if self.request.GET.get('phone') == 'on':
            query &= Q(phone=True)
        if self.request.GET.get('balcony') == 'on':
            query &= Q(balcony=True)

        # фильруем объвления на которые пользователь пожаловался
        if self.request.user.is_authenticated():
            query &= ~Q(complained__user=self.request.user)

        queryset = VashdomAdvert.objects.filter(query).select_related('metro', 'user', 'district')

        sort = self.request.GET.get('sort')
        if sort == 'date-asc':
            queryset = queryset.order_by('date')
        elif sort == 'date-desc':
            queryset = queryset.order_by('-date')
        elif sort == 'price-asc':
            queryset = queryset.order_by('price')
        elif sort == 'price-desc':
            queryset = queryset.order_by('-price')
        else:
            queryset = queryset.order_by('-date')

        return queryset


class LoadAdvert(generics.ListAPIView):
    serializer_class = Advert2Serializer
    paginate_by = 30

    def get_queryset(self):
        page = self.request.GET.get('page') or '1'
        page = int(page)
        start_offset = (page - 1) * 30
        end_offset = page * 30

        query = Q(date__gte=datetime(2019, 1, 1))
        query &= VashdomAdvert.get_advert_query()
        queryset = VashdomAdvert.objects.filter(query).select_related('metro', 'user', 'district').order_by('date')
        return queryset


class AdvertDetail(generics.RetrieveAPIView):
    serializer_class = AdvertSerializer
    queryset = VashdomAdvert.objects.all()


class AdvertVkList(generics.ListAPIView):
    serializer_class = AdvertVkSerializer
    paginate_by = 30

    def get_queryset(self):
        query = Q()

        town_id = self.request.GET.get('town')
        if town_id:
            query &= Q(town_id=town_id)
        else:
            query &= Q(town_id__in=[1, 2, 10, 6])

        ids = self.request.GET.getlist('ids')
        if ids:
            query &= Q(id__in=ids)

        if self.request.GET.get('district'):
            try:
                district_list = District.objects.filter(id=self.request.GET.get('district'))
                if district_list:
                    query = query & Q(district=district_list[0])
                    self.district = district_list[0]
            except:
                pass

        try:
            metro_arg = self.request.GET.getlist('metro')
            if metro_arg:
                metro_list = Metro.objects.filter(id__in=metro_arg if isinstance(metro_arg, list) else [metro_arg])
                if metro_list:
                    query = query & Q(metro_id__in=[metro.id for metro in metro_list])
                    self.metro = metro_list[0]
        except:
            pass

        room_query = Q()
        room_list = self.request.GET.getlist('rooms')
        if 'R' in room_list or 'r' in room_list:
            room_query &= Q(live=VashdomVKAdvert.LIVE_ROOM)
        for room in room_list:
            try:
                rooms = int(room)
                if rooms in [1, 2, 3]:
                    room_query |= Q(rooms=rooms, live=VashdomVKAdvert.LIVE_FLAT)
                elif rooms >= 4:
                    room_query |= Q(rooms__gt=3, live=VashdomVKAdvert.LIVE_FLAT)
            except:
                pass
        query &= room_query

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
        if self.request.GET.get('internet') == 'on':
            query &= Q(internet=True)
        if self.request.GET.get('phone') == 'on':
            query &= Q(phone=True)
        if self.request.GET.get('balcony') == 'on':
            query &= Q(balcony=True)

        # фильруем объвления на которые пользователь пожаловался
        if self.request.user.is_authenticated():
            query &= ~Q(complained__user=self.request.user)

        queryset = VashdomVKAdvert.objects.filter(query).select_related('metro', 'district')

        sort = self.request.GET.get('sort')
        if sort == 'date-asc':
            queryset = queryset.order_by('date')
        elif sort == 'date-desc':
            queryset = queryset.order_by('-date')
        elif sort == 'price-asc':
            queryset = queryset.order_by('price')
        elif sort == 'price-desc':
            queryset = queryset.order_by('-price')
        else:
            queryset = queryset.order_by('-date')

        return queryset