# -*- coding: utf-8 -*-
from django import template
from vashdom.forms import FilterAdvertForm, FilterVKAdvertForm
from main.models import Town
from django.core.urlresolvers import reverse
import re
from django.utils.html import mark_safe
from django.template.defaultfilters import linebreaksbr
from datetime import datetime, timedelta
from vashdom.models import VashdomAdvert, VashdomVKAdvert
import random, string
from django.conf import settings

register = template.Library()

@register.inclusion_tag('vashdom/block/filter_advert.html', takes_context=True)
def vashdom_filter_advert_block(context, url=None, kwargs={}):
    form_data = {}
    for key, value in context['request'].GET.lists():
        if isinstance(value, list) and len(value) > 1:
            form_data[key] = value
        else:
            form_data[key] = value[0]
    form_data.update(kwargs)
    form = FilterAdvertForm(town=context['request'].current_town, data=form_data)
    if not url:
        url = '/%s/' % context['request'].current_town.slug
    return {
        'form': form,
        'url': url,
        'current_town': context['current_town'],
        'user': context['user'],
        'request': context['request'],
        'random_id': ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(10))
    }

@register.inclusion_tag('vashdom/block/filter_vkadvert.html', takes_context=True)
def vashdom_filter_vkadvert_block(context, url=None, kwargs={}):
    form_data = {}
    for key, value in context['request'].GET.lists():
        if isinstance(value, list) and len(value) > 1:
            form_data[key] = value
        else:
            form_data[key] = value[0]
    form_data.update(kwargs)
    form = FilterVKAdvertForm(town=context['request'].current_town, data=form_data)
    url = '/vk/%s/' % context['request'].current_town.slug
    return {
        'form': form,
        'url': url,
        'current_town': context['current_town'],
        'user': context['user'],
        'request': context['request'],
        'random_id': ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(10))
    }

@register.inclusion_tag('vashdom/block/filter_advert_map.html', takes_context=True)
def vashdom_filter_advert_map_block(context, url=None):
    form = FilterAdvertForm(town=context['request'].current_town)
    if not url:
        url = reverse('advert:map')
    return {
        'form': form,
        'url': url,
        'current_town': context['current_town'],
        'user': context['user'],
        'request': context['request'],
    }


@register.inclusion_tag('vashdom/block/image-detail.html')
def vashdom_image_detail(advert):
    return {
        'image_list': advert.images.all(),
        'id': id,
        'title': advert.title,
    }

@register.inclusion_tag('vashdom/block/image-preview.html')
def vashdom_image_preview(advert):
    return {
        'image_list': advert.images.all(),
        'id': advert.id,
        'title': advert.title,
        'url': advert.get_absolute_url(),
        'advert': advert
    }


@register.filter
def fmt_vashdom_date(advert):
    try:
        now = datetime.now()
        yesterday = now - timedelta(days=1)
        if advert.date_vashdom.date() == now.date():
            is_hot = VashdomAdvert.is_hot(advert)
            hot_text = '<span class="fire" title="Цена объекта ниже среднерыночной"></span> ' if is_hot else ''
            hot_class = 'red' if is_hot else ''
            return mark_safe(hot_text + '<span class="value %s">Сегодня</span>' % hot_class)
        if advert.date_vashdom.date() == yesterday.date():
            return mark_safe('Вчера')
        archive = 'archive' if VashdomAdvert.is_archive else ''
        return mark_safe('<span class="value %s">%s</span>' % (archive, advert.date_vashdom.strftime('%d.%m.%y')))
    except:
        return ''


@register.filter
def fmt_vashdom_tel(tel):
    from main.templatetags.main_tags import fmt_tel

    result = []
    if tel:
        for t in tel.split(','):
            t = t.strip()
            if t:
                full_tel = fmt_tel(t)
                if full_tel.startswith('+7') or full_tel.startswith('+8'):
                    result.append(full_tel[:9] + re.sub('\d', 'X', full_tel[9:]))
                else:
                    result.append(full_tel[:4] + re.sub('\d', 'X', full_tel[4:]))
    return mark_safe('<br>'.join(result))

@register.filter
def fmt_vashdom_advert_body(advert):
    text = advert.body
    text = text.replace(u' ', u'\u00ad' + u' ')
    text = text.replace(u'[phone]', mark_safe(u'<strong class="hidden-phone">Скрыто</strong>'))
    text = linebreaksbr(text, autoescape=False)
    return text


@register.inclusion_tag('vashdom/payment/w1payment-form.html')
def vashdom_w1payment_form(payment):
    from walletone.forms import WalletOnePaymentForm
    import requests

    w1_form = WalletOnePaymentForm(initial={
        'WMI_PAYMENT_AMOUNT': unicode(payment.total),
        'WMI_PAYMENT_NO': unicode(payment.id),
        'WMI_DESCRIPTION': payment.description,
        'WMI_CULTURE_ID': 'ru-RU',
        'WMI_SUCCESS_URL': settings.DJANGO_W1_SUCCESS_URL + '?PAYMENT_NO=%s' % payment.id,
        'WMI_FAIL_URL': settings.DJANGO_W1_FAIL_URL + '?PAYMENT_NO=%s' % payment.id
    })

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset':'windows-1251,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding':'gzip,deflate,sdch',
        'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
        'Content-Type':'application/x-www-form-urlencoded',
        'Host': 'wl.walletone.com',
        'Referer': 'wl.walletone.com',
        'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.11 (KHTML, like Gecko) Ubuntu/12.04 Chromium/20.0.1132.47 Chrome/20.0.1132.47 Safari/536.11)'
    }

    data = {k:w1_form.fields[k].initial for k in w1_form.fields}

    r = requests.post(w1_form.action_url, data=data, headers=headers, allow_redirects=True)

    return {
        'payment': payment,
        'w1_form': w1_form,
        'w1_url': r.url if r.status_code == 200 else ''
    }

@register.inclusion_tag('vashdom/payment/payment-form.html')
def vashdom_payment_form(payment):
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


@register.inclusion_tag('vashdom/payment/promocode-form.html')
def vashdom_promocode_form(payment):
    from main.form import PromoForm
    form = PromoForm(initial={'payment': payment.id})
    return {
        'payment': payment,
        'form': form
    }


@register.inclusion_tag('vashdom/block/choose_town.html', takes_context=True)
def vashdom_choose_town_block(context):
    return {
        'town_list': Town.objects.all().order_by('order'),
        'current_town': context['request'].current_town,
    }

@register.inclusion_tag('vashdom/block/offcanvas_town.html', takes_context=True)
def vashdom_offcanvas_town_block(context):
    return {
        'town_list': Town.objects.all().order_by('order'),
        'current_town': context['request'].current_town,
    }


@register.inclusion_tag('vashdom/block/pagination.html', takes_context=True)
def vashdom_pagination(context, page_number):
    from bootstrap_pagination.templatetags.bootstrap_pagination import get_page_url

    url_view_name = None
    url_param_name = "page"
    url_extra_args = []
    url_extra_kwargs = []
    url_get_params = context['request'].GET

    try: 
        page = int(page_number)
    except:
        page = 1

    next_page_url = get_page_url(page+1, context.current_app, url_view_name, url_extra_args, url_extra_kwargs, url_param_name, url_get_params)
    prev_page_url = get_page_url(page-1, context.current_app, url_view_name, url_extra_args, url_extra_kwargs, url_param_name, url_get_params) \
                        if page > 1 else None

    return {
        'request': context['request'],
        'next_page_url': next_page_url,
        'prev_page_url': prev_page_url
    }


@register.inclusion_tag('vashdom/payment/detail-success.html')
def vashdom_payment_by_id(id):
    from vashdom.models import Payment
    payments = Payment.objects.filter(id=id)
    if payments:
        payment = payments[0]
    else:
        payment = None
    return {
        'payment': payment
    }


@register.filter
def vashdom_catalog_title(args, request):
    return VashdomAdvert.get_catalog_title(args, request)

@register.filter
def vashdom_catalog_description(args, request):
    return VashdomAdvert.get_catalog_description(args, request)

@register.filter
def vashdom_vkcatalog_title(args, request):
    return VashdomVKAdvert.get_catalog_title(args, request)


@register.simple_tag
def random_preview_image():
    images = ['/static/img/noimage.jpg', '/static/img/noimage1.jpg', '/static/img/noimage2.jpg']
    return random.choice(images)