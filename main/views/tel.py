#-*- coding: utf-8 -*-
from django.views.generic import View
from main.models import Company, Advert, VKAdvert, RegViewed
from main.templatetags.main_tags import fmt_tel
from uprofile.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from django.db.models import Q
from django.http import Http404
from main.templatetags.main_tags import is_advert_viewed


def tel2img(tel_list):
    im = Image.new('RGB', (200, 25 * len(tel_list)-5))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('/usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono.ttf', size=16)
    draw.rectangle([(0, 0), (200, 25 * len(tel_list)-5)], fill="#FFFFFF")
    n = 0
    for tel in tel_list:
        draw.text((0, n * 25), tel.strip(), fill=(0, 0, 0), font=font)
        n += 1
    del draw
    return im


class CompanyPhoneView(View):
    def get(self, request, *args, **kwargs):
        time = int(request.session.get('phone_open_time', 0))
        now = int(datetime.now().strftime('%s'))
        if now - time > 30:
            company = get_object_or_404(Company, id=self.request.GET.get('id'))

            text = fmt_tel(company.tel)
            tel_list = text.split(',')

            im = tel2img(tel_list)

            response = HttpResponse(content_type="image/png")
            im.save(response, 'PNG')

            request.session['phone_open_time'] = datetime.now().strftime('%s')
            request.session.modified = True
        else:
            im = tel2img([u'Ждите %s сек...' % (30 - (now - time))])
            response = HttpResponse(content_type="image/png")
            im.save(response, 'PNG')
        return response


class UserPhoneView(View):
    def get(self, request, *args, **kwargs):
        time = int(request.session.get('phone_open_time', 0))
        now = int(datetime.now().strftime('%s'))
        if now - time > 30:
            user = get_object_or_404(User, id=self.request.GET.get('id'))

            text = fmt_tel(user.tel)
            tel_list = text.split(',')

            im = tel2img(tel_list)

            response = HttpResponse(content_type="image/png")
            im.save(response, 'PNG')

            request.session['phone_open_time'] = datetime.now().strftime('%s')
            request.session.modified = True
        else:
            im = tel2img([u'Ждите %s сек...' % (30 - (now - time))])
            response = HttpResponse(content_type="image/png")
            im.save(response, 'PNG')
        return response


class AdvertPhoneView(View):
    def get(self, request, *args, **kwargs):

        query = Q(id=request.GET.get('id'))
        if request.user.is_authenticated():
            if not request.user.has_perm('uprofile.view_moderate'):
                query &= ~Q(company=None) | (Q(company=None) & request.user.get_access_query()) | Q(viewed__id=request.user.id)
        else:
            query &= ~Q(company=None)
        advert_list = Advert.objects.filter(query)
        if not advert_list:
            # если объявление не найдено значит у пользователя не прав на его просмотр
            im = tel2img([u'Нет доступа'])
            response = HttpResponse(content_type="image/png")
            im.save(response, 'PNG')
        else:
            advert = advert_list[0]
            is_viewed = is_advert_viewed(advert, request.user)

            if request.user.is_authenticated():
                buyed = request.user.buy_adverts.filter(id=advert.id, buy_date__gte=datetime.now()).count()
            else:
                buyed = []

            if advert.is_buyed and not buyed:
                # если объявление выкуплено
                im = tel2img([u'Выкуплено'])
                response = HttpResponse(content_type="image/png")
                im.save(response, 'PNG')
            else:
                time = int(request.session.get('phone_open_time', 0))
                now = int(datetime.now().strftime('%s'))
                if now - time > 3 or is_viewed:
                    #открытие телефона
                    if advert.owner_tel:
                        text = fmt_tel(advert.owner_tel)
                    else:
                        text = fmt_tel(advert.user.tel if advert.user and advert.user.tel else '')
                    tel_list = text.split(',')

                    im = tel2img(tel_list)

                    response = HttpResponse(content_type="image/png")
                    im.save(response, 'PNG')

                    if not is_viewed:
                        advert.views_tel += 1
                        advert.save()
                        if request.user.is_authenticated():
                            try:
                                RegViewed.add(advert, request.user)
                            except:
                                pass
                            advert.clear_user_cache(request.user)

                    if not is_viewed:
                        # если телефон открывается в первый раз то ставим таймер на открытие следующего телефона
                        request.session['phone_open_time'] = datetime.now().strftime('%s')
                        request.session.modified = True
                else:
                    im = tel2img([u'Ждите %s сек...' % (3 - (now - time))])
                    response = HttpResponse(content_type="image/png")
                    im.save(response, 'PNG')
        return response


class VKAdvertPhoneView(View):
    def get(self, request, *args, **kwargs):

        query = Q(id=request.GET.get('id'))
        if request.user.is_authenticated():
            if not request.user.has_perm('uprofile.view_moderate'):
                query &= Q(id=None) | (request.user.get_access_query(base='vk')) | Q(viewed__id=request.user.id)
        else:
            query &= Q(id=None)
        advert_list = VKAdvert.objects.filter(query)
        if not advert_list or not request.user.is_authenticated():
            # если объявление не найдено значит у пользователя не прав на его просмотр
            im = tel2img([u'Нет доступа'])
            response = HttpResponse(content_type="image/png")
            im.save(response, 'PNG')
        else:
            advert = advert_list[0]
            is_viewed = is_advert_viewed(advert, request.user)

            time = int(request.session.get('phone_open_time', 0))
            now = int(datetime.now().strftime('%s'))
            if now - time > 3 or is_viewed:
                #открытие телефона
                if advert.owner_tel:
                    text = fmt_tel(advert.owner_tel)
                else:
                    text = u'Телефон не указан'
                tel_list = text.split(',')

                im = tel2img(tel_list)

                response = HttpResponse(content_type="image/png")
                im.save(response, 'PNG')

                if not is_viewed:
                    advert.views_tel += 1
                    advert.save()
                    if request.user.is_authenticated():
                        try:
                            advert.viewed.add(request.user)
                        except:
                            pass
                        advert.clear_user_cache(request.user)

                if not is_viewed:
                    # если телефон открывается в первый раз то ставим таймер на открытие следующего телефона
                    request.session['phone_open_time'] = datetime.now().strftime('%s')
                    request.session.modified = True
            else:
                im = tel2img([u'Ждите %s сек...' % (3 - (now - time))])
                response = HttpResponse(content_type="image/png")
                im.save(response, 'PNG')
        return response


class VKAdvertLinkView(View):
    def get(self, request, *args, **kwargs):

        query = Q(id=request.GET.get('id'))
        if request.user.is_authenticated():
            if not request.user.has_perm('uprofile.view_moderate'):
                query &= Q(id=None) | (request.user.get_access_query(base='vk')) | Q(viewed__id=request.user.id)
        else:
            query &= Q(id=None)
        advert_list = VKAdvert.objects.filter(query)
        if not advert_list or not request.user.is_authenticated():
            # если объявление не найдено значит у пользователя не прав на его просмотр
            response = HttpResponse(u'<a href="javascript: return false;" class="owner-vkid">Не подключен тариф</a>')
        else:
            advert = advert_list[0]
            is_viewed = is_advert_viewed(advert, request.user)

            time = int(request.session.get('phone_open_time', 0))
            now = int(datetime.now().strftime('%s'))
            if now - time > 3 or is_viewed:
                #открытие телефона
                text = '<a href="https://vk.com/id%s" target="_blank" rel="nofollow" class="owner-vkid">https://vk.com/id%s</a>' % (advert.owner_vkid, advert.owner_vkid)
                response = HttpResponse(text)
                if not is_viewed:
                    advert.views_tel += 1
                    advert.save()
                    if request.user.is_authenticated():
                        try:
                            advert.viewed.add(request.user)
                        except:
                            pass
                        advert.clear_user_cache(request.user)

                if not is_viewed:
                    # если телефон открывается в первый раз то ставим таймер на открытие следующего телефона
                    request.session['phone_open_time'] = datetime.now().strftime('%s')
                    request.session.modified = True
            else:
                response = HttpResponse(u"")
        return response