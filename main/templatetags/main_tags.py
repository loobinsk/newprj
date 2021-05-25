#-*- coding: utf-8 -*-
from django import template
from django.core.urlresolvers import reverse
from django.utils.html import mark_safe
from datetime import datetime, timedelta
from main.form import FilterAdvertForm, FilterAdvertClientForm, FeedbackForm_Client, FilterVKAdvertClientForm
from main.models import Advert, Town, VKAdvert
from uprofile.models import User
from django.template import Node, resolve_variable, TemplateSyntaxError
import json
from django.db.models import Avg, Q
import re
from random import randint
from django.http import QueryDict


register = template.Library()

# FILTER

@register.simple_tag
def nav_active(request, urls):
    if request.path in (reverse(url) for url in urls.split()):
        return "active"
    return ""


@register.filter
def nav_url(request, url):
    return url in request.path


@register.filter
def add_class(value, arg):
    cls = value.field.widget.attrs.get('class')
    return value.as_widget(attrs={'class': cls + ' ' + arg if cls else '' + arg})


@register.filter
def fmt_date(date):
    try:
        now = datetime.now()
        yesterday = now - timedelta(days=1)
        if date.date() == now.date():
            return 'Сегодня в '+str(date.strftime('%H:%M'))
        if date.date() == yesterday.date():
            return 'Вчера в '+str(date.strftime('%H:%M'))
        return date.strftime('%d.%m.%y в %H:%M')
    except:
        return ''


@register.filter
def fmt_date_dp(date):
    if isinstance(date, str):
        return date
    if isinstance(date, datetime):
        return date.strftime('%d.%m.%Y')
    return date


@register.filter
def fmt_tel(tel):
    result = []
    if tel:
        for t in tel.split(','):
            t = t.strip()
            if t:
                if len(t) == 11: #стандартный мобильник
                    result.append('+%s (%s) %s-%s-%s' % (t[0], t[1:4], t[4:7], t[7:9], t[9:11]))
                elif len(t) == 11:
                    result.append('+7 (%s) %s-%s-%s' % (t[0:3], t[3:6], t[6:8], t[8:10]))
                elif len(t) == 7:
                    result.append('%s-%s-%s' % (t[0:3], t[3:5], t[5:7]))
                else:
                    result.append(t)
    return ', '.join(result)


@register.filter
def fmt_price(price):
    if price:
        return mark_safe('{0:,.0f}'.format(price).replace(',', ' ').replace(' ', '&nbsp;'))
    else:
         return ''


@register.filter
def user_status(status):
    if status in User.STATUSES:
        return User.STATUSES[status]
    else:
        return ''


@register.filter
def advert_limit(limit):
    return Advert.LIMITS[limit]


@register.filter
def advert_status(status):
    if status == Advert.STATUS_VIEW:
        return mark_safe('<span class="text-primary">%s</span>' % Advert.STATUSES[status])
    elif status == Advert.STATUS_MODERATE:
        return mark_safe('<span class="text-danger">%s</span>' % Advert.STATUSES[status])
    return Advert.STATUSES[status]


@register.filter
def to_str(value):
    return str(value)


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


class AddParameter(Node):
    def __init__(self, varname, value, param):
        self.varname = varname
        self.value = value
        self.param = param

    def render(self, context):
        req = resolve_variable('request', context)
        params = req.GET.copy()
        if self.param:
            params[self.varname] = context[self.param]
        else:
            params[self.varname] = self.value
        return '%s?%s' % (req.path, params.urlencode())

@register.tag
def addurlparameter(parser, token):
    from re import split
    bits = split(r'\s+', token.contents, 2)
    if len(bits) < 2:
        raise TemplateSyntaxError, "'%s' tag requires two arguments" % bits[0]
    param = None
    if 'param=' in bits[2]:
        param_name, param = bits[2].split('=')
    return AddParameter(bits[1], bits[2], param)


# BLOCK
@register.inclusion_tag('main/block/filter_advert.html', takes_context=True)
def filter_advert_block(context, url=None, kwargs={}):
    form_data = {}
    for key, value in context['request'].GET.lists():
        if isinstance(value, list) and len(value) > 1:
            form_data[key] = value
        else:
            form_data[key] = value[0]
    form_data.update(kwargs)
    form = FilterAdvertForm(town=context['request'].current_town, data=form_data)
    if not url:
        url = reverse('advert:list')
    return {
        'form': form,
        'url': url,
        'current_town': context['current_town'],
        'user': context['user']
    }

@register.inclusion_tag('main/block/filter_advert_client.html', takes_context=True)
def filter_advert_client_block(context, action=None):
    form = FilterAdvertClientForm(town=context['request'].current_town, data=context['request'].REQUEST, adtype=context['request'].GET.get('type'))
    url = action if action else reverse('client:home')
    company = context['user'].company
    return {
        'form': form,
        'url': url,
        'current_town': company.town if company else context['current_town'],
        'user': context['user'],
        'is_moder': context['request'].is_moder
    }

@register.inclusion_tag('main/block/filter_vkadvert_client.html', takes_context=True)
def filter_vkadvert_client_block(context, action=None):
    form = FilterVKAdvertClientForm(town=context['request'].current_town, data=context['request'].REQUEST,
                                    adtype=context['request'].GET.get('type'))
    url = reverse('client:advert:vk:list')
    return {
        'form': form,
        'url': url,
        'current_town': context['current_town'],
        'user': context['user'],
        'is_moder': context['request'].is_moder
    }


@register.inclusion_tag('main/block/choose_town.html', takes_context=True)
def choose_town_block(context):
    return {
        'town_list': Town.objects.all().order_by('order'),
        'current_town': context['request'].current_town
    }


@register.inclusion_tag('main/block/advert-map.html')
def advert_map(advert):
    return {
        'advert': advert
    }


@register.inclusion_tag('main/client/advert/business-map.html', takes_context=True)
def business_map(context):
    town = context['current_town']
    advert_list = Advert.objects.filter(town=town).exclude(latitude=None, longitude=None).order_by('-date').select_related('metro','user')[:500]
    return {
        'advert_list': advert_list,
        'current_town': town
    }

@register.filter
def jsonify(o):
    return mark_safe(json.dumps(o))

@register.inclusion_tag('main/block/login.html', takes_context=True)
def login_block(context):
    from main.form import AuthForm

    return {
        'STATIC_URL': context['STATIC_URL'],
        'user': context['user'],
        'form': AuthForm(),
        'is_moder': context['is_moder']
    }

@register.inclusion_tag('main/block/stat-arenda.html', takes_context=True)
def stat_arenda_block(context, adtype=Advert.TYPE_LEASE):
    # комнаты
    avg_room = Advert.objects.filter(
        town=context['current_town'],
        status=Advert.STATUS_VIEW,
        adtype=adtype,
        estate=Advert.ESTATE_LIVE,
        live=Advert.LIVE_ROOM,
        limit=Advert.LIMIT_LONG,
        need=Advert.NEED_SALE,
        date__gte=datetime.now() - timedelta(days=30)
        ).aggregate(Avg('price'))

    # квартиры
    avg_flat3 = Advert.objects.filter(
        town=context['current_town'],
        status=Advert.STATUS_VIEW,
        adtype=adtype,
        estate=Advert.ESTATE_LIVE,
        live=Advert.LIVE_FLAT,
        rooms=3,
        limit=Advert.LIMIT_LONG,
        need=Advert.NEED_SALE,
        price__gt=10000,
        date__gte=datetime.now() - timedelta(days=30)
    ).aggregate(Avg('price'))

    # квартиры 1
    avg_flat1 = Advert.objects.filter(
        town=context['current_town'],
        status=Advert.STATUS_VIEW,
        adtype=adtype,
        estate=Advert.ESTATE_LIVE,
        live=Advert.LIVE_FLAT,
        rooms=1,
        limit=Advert.LIMIT_LONG,
        need=Advert.NEED_SALE,
        price__gt=10000,
        date__gte=datetime.now() - timedelta(days=30)
    ).aggregate(Avg('price'))

    # квартиры 2
    avg_flat2 = Advert.objects.filter(
        town=context['current_town'],
        status=Advert.STATUS_VIEW,
        adtype=adtype,
        estate=Advert.ESTATE_LIVE,
        live=Advert.LIVE_FLAT,
        rooms=2,
        limit=Advert.LIMIT_LONG,
        need=Advert.NEED_SALE,
        price__gt=10000,
        date__gte=datetime.now() - timedelta(days=30)
    ).aggregate(Avg('price'))

    # коттеджи
    avg_house = Advert.objects.filter(
        town=context['current_town'],
        status=Advert.STATUS_VIEW,
        adtype=adtype,
        estate=Advert.ESTATE_COUNTRY,
        country=Advert.COUNTRY_HOUSE,
        limit=Advert.LIMIT_LONG,
        need=Advert.NEED_SALE,
        price__gt=10000,
        date__gte=datetime.now() - timedelta(days=30)
    ).aggregate(Avg('price'))

    return {
        'town': context['current_town'],
        'room': avg_room['price__avg'],
        'flat3': avg_flat3['price__avg'],
        'flat1': avg_flat1['price__avg'],
        'flat2': avg_flat2['price__avg'],
        'house': avg_house['price__avg'],
        'adtype': adtype
    }


class BreaklessNode(Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        from django.utils.html import strip_spaces_between_tags
        return strip_spaces_between_tags(re.sub(r'(\ +)', ' ', self.nodelist.render(context).strip().replace('\n', '')))

@register.tag
def breakless(parser, token):
    nodelist = parser.parse(('endbreakless',))
    parser.delete_first_token()
    return BreaklessNode(nodelist)


class BreaklessPointNode(Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        from django.utils.html import strip_spaces_between_tags
        return strip_spaces_between_tags(re.sub(r'(\ +)', ' ', self.nodelist.render(context).strip().replace('\n', ', ')))

@register.tag
def breakless_point(parser, token):
    nodelist = parser.parse(('endbreakless_point',))
    parser.delete_first_token()
    return BreaklessPointNode(nodelist)


@register.filter
def catalog_title(args, request):
    return Advert.get_catalog_title(args, request)

@register.filter
def vkcatalog_title(args, request):
    return VKAdvert.get_catalog_title(args, request)


@register.filter
def is_advert_viewed(advert, user):
    return advert.viewed.filter(id=user.id).count() > 0

@register.simple_tag
def random_number(length=5):
    return randint(10**(length-1), (10**(length)-1))


@register.inclusion_tag('main/client/block/client-feedback-block.html', takes_context=True)
def client_feedback_block(context):
    return {
        'form': FeedbackForm_Client(),
        'is_moder': context['request'].is_moder,
        'current_town': context['request'].current_town
    }


@register.filter
def news_preview(text):
    from django.template.defaultfilters import truncatewords_html

    pos = text.find(u'<hr />')
    if pos == -1:
        return truncatewords_html(text, 30)
    else:
        return text[:pos]


@register.inclusion_tag('main/client/payment/payment-form.html')
def payment_form(payment):
    from robokassa.forms import RobokassaForm

    robokassa_form = RobokassaForm(initial={
        'OutSum': payment.total,
        'InvId': payment.id,
        'Desc': payment.description
    })
    return {
        'payment': payment,
        'robokassa_form': robokassa_form
    }


@register.inclusion_tag('main/client/payment/promocode-form.html')
def promocode_form(payment):
    from main.form import PromoForm
    form = PromoForm(initial={'payment': payment.id})
    return {
        'payment': payment,
        'form': form
    }


@register.inclusion_tag('main/client/payment/detail-ajax.html')
def payment_by_id(id):
    from main.models import Payment
    payment = Payment.objects.get(id=id)
    return {
        'payment': payment
    }


@register.filter
def agent24_has_perm(user, perm):
    return perm in user.get_agent24_active_perms()


@register.filter
def rating_score(rating):
    return '%.2f' % rating

@register.filter
def rating_pixels(rating, width):
    return "%.0f" % round(width / 100.0 * rating * 10.0, 0)

@register.filter
def fmt_seconds(sec):
    from math import ceil
    if sec:
        return "~%.0f мин." % ceil(sec/60)
    else:
        return ''

@register.filter
def fmt_meters(meter):
    if meter:
        return "%.1f км." % (meter/1000, )
    else:
        return ''

@register.filter
def fmt_buys_declination(count):
    if count in [11, 12, 13, 14]:
        return 'выкупов'
    elif count == 1:
        return 'выкуп'
    elif str(count)[-1:] in ['2', '3', '4']:
        return 'выкупа'
    else:
        return 'выкупов'


@register.inclusion_tag('main/client/block/tariff-stats.html', takes_context=True)
def tariff_stats(context):
    from main.models import ConnectedService

    if context['user'].independent:
        # если агент независимый
        service_query = Q(user=context['user'])
    else:
        # если агент под агентством
        service_query = Q(company=context['user'].company)
    list_objects = ConnectedService.objects.filter(service_query).\
                                            filter(perm__need=Advert.NEED_SALE,
                                                       active=True). \
                                            order_by('-end_date')

    list_clients = ConnectedService.objects.filter(service_query).\
                                            filter(perm__need=Advert.NEED_DEMAND,
                                                       active=True). \
                                            order_by('-end_date')

    list_vk = ConnectedService.objects.filter(service_query).\
                                            filter(perm__base_vk=True,
                                                       active=True). \
                                            order_by('-end_date')
    return {
        'user': context['user'],
        'service_objects': list_objects[0].elapsed_time if list_objects else 'Не подключен',
        'service_clients': list_clients[0].elapsed_time if list_clients else 'Не подключен',
        'service_vk': list_vk[0].elapsed_time if list_vk else 'Не подключен'
    }

@register.inclusion_tag('main/block/pagination.html', takes_context=True)
def pagination(context, page_obj):
    from bootstrap_pagination.templatetags.bootstrap_pagination import get_page_url

    url_view_name = None
    url_param_name = "page"
    url_extra_args = []
    url_extra_kwargs = []
    url_get_params = context['request'].GET

    next_page_url = None
    if page_obj.has_next():
        next_page_url = get_page_url(page_obj.next_page_number(), context.current_app, url_view_name, url_extra_args, url_extra_kwargs, url_param_name, url_get_params)

    return {
        'page_obj': page_obj,
        'request': context['request'],
        'next_page_url': next_page_url,
        'is_client': context['is_client']
    }
