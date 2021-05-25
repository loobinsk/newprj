#-*- coding: utf-8 -*-
from django.views.generic import View
from main.models import Advert, VKAdvert, RegViewed
from main.templatetags.main_tags import fmt_tel
from django.http import HttpResponse
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from django.db.models import Q
from vashdom.models import Tariff, Password, VashdomAdvert
from django.db.models import Sum
from main.templatetags.main_tags import is_advert_viewed


def tel2img(tel_list):
    im = Image.new('RGB', (200, 25 * len(tel_list)-5))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('/usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono.ttf', size=18)
    draw.rectangle([(0, 0), (200, 25 * len(tel_list)-5)], fill="#FFFFFF")
    n = 0
    for tel in tel_list:
        draw.text((0, n * 25), tel.strip(), fill=(0, 0, 0), font=font)
        n += 1
    del draw
    return im


class AdvertPhoneView(View):
    def get(self, request, *args, **kwargs):

        query = Q(id=request.GET.get('id'), company=None) & VashdomAdvert.get_advert_query(request.current_town)
        advert_list = Advert.objects.filter(query)
        if not advert_list:
            # если объявление не найдено значит у пользователя не прав на его просмотр
            im = tel2img([u'Не найдено'])
            response = HttpResponse(content_type="image/png")
            im.save(response, 'PNG')
        else:
            advert = advert_list[0]
            is_viewed = is_advert_viewed(advert, request.user) if request.user.is_authenticated() else False

            if not request.GET.get('password') and request.user.is_authenticated():
                password = self.request.user.vashdom_passwords.filter(end_date__gte=datetime.now(),
                                                                           count__gt=0,
                                                                           town=advert.town,
                                                                           main_base=True)
            else:
                password = Password.objects.filter(password=request.GET.get('password'),
                                    start_date__lte=datetime.now(),
                                    end_date__gte=datetime.now(),
                                    count__gt=0,
                                    town=advert.town,
                                    main_base=True)

            if password:
                #открытие телефона
                if advert.owner_tel:
                    text = fmt_tel(advert.owner_tel)
                else:
                    text = fmt_tel(advert.user.tel if advert.user and advert.user.tel else '')
                tel_list = text.split(',')

                im = tel2img(tel_list)

                response = HttpResponse(content_type="image/png")
                im.save(response, 'PNG')

                if password[0].adverts.filter(id=advert.id).count() == 0:
                    password[0].count -= 1
                    password[0].save()
                    password[0].adverts.add(advert)

                if not is_viewed:
                    advert.views_tel += 1
                    advert.save()
                    if request.user.is_authenticated():
                        try:
                            RegViewed.add(advert, request.user)
                        except:
                            pass

            else:
                im = tel2img([u'Неверный пароль'])
                response = HttpResponse(content_type="image/png")
                im.save(response, 'PNG')
        return response


class VKAdvertPhoneView(View):
    def get(self, request, *args, **kwargs):

        query = Q(id=request.GET.get('id'))
        advert_list = VKAdvert.objects.filter(query)
        if not advert_list:
            # если объявление не найдено значит у пользователя не прав на его просмотр
            im = tel2img([u'Не найдено'])
            response = HttpResponse(content_type="image/png")
            im.save(response, 'PNG')
        else:
            advert = advert_list[0]
            if not request.GET.get('password') and request.user.is_authenticated():
                password = self.request.user.vashdom_passwords.filter(end_date__gte=datetime.now(),
                                                                           count__gt=0,
                                                                           town=advert.town,
                                                                           vk_base=True)
            else:
                password = Password.objects.filter(password=request.GET.get('password'),
                                    start_date__lte=datetime.now(),
                                    end_date__gte=datetime.now(),
                                    count__gt=0,
                                    town=advert.town,
                                    vk_base=True)

            if password:
                #открытие телефона
                if advert.owner_tel:
                    text = fmt_tel(advert.owner_tel)
                else:
                    text = u'Телефон не указан'
                tel_list = text.split(',')

                im = tel2img(tel_list)

                response = HttpResponse(content_type="image/png")
                im.save(response, 'PNG')

                if password[0].vkadverts.filter(id=advert.id).count() == 0:
                    password[0].count -= 1
                    password[0].save()
                    try:
                        password[0].vkadverts.add(advert)
                    except:
                        pass
            else:
                im = tel2img([u'Неверный пароль'])
                response = HttpResponse(content_type="image/png")
                im.save(response, 'PNG')
        return response


class VKAdvertLinkView(View):
    def get(self, request, *args, **kwargs):

        query = Q(id=request.GET.get('id'))
        advert_list = VKAdvert.objects.filter(query)
        if not advert_list:
            # если объявление не найдено значит у пользователя не прав на его просмотр
            response = HttpResponse(u'Не найдено')
        else:
            advert = advert_list[0]
            if not request.GET.get('password') and request.user.is_authenticated():
                password = self.request.user.vashdom_passwords.filter(end_date__gte=datetime.now(),
                                                                           count__gt=0,
                                                                           town=advert.town,
                                                                           vk_base=True)
            else:
                password = Password.objects.filter(password=request.GET.get('password'),
                                    start_date__lte=datetime.now(),
                                    end_date__gte=datetime.now(),
                                    count__gt=0,
                                    town=advert.town,
                                    vk_base=True)

            if password:
                #открытие ссылки
                if advert.owner_vkid:
                    text = '<a href="https://vk.com/id%s" target="_blank">https://vk.com/id%s</a>' % (advert.owner_vkid, advert.owner_vkid)
                else:
                    text = '<a href="#">Не указан</a>'
                response = HttpResponse(text)
            else:
                response = HttpResponse(u'Неправильный пароль')
        return response