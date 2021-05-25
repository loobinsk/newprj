#-*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from registration.forms import RegistrationForm
from main.models import Advert, Town, Metro, District, News, Vacancy, Question, Blacklist, Company, clear_tel_list, \
    clear_tel, Tariff, Abbr, ConnectedService, SearchRequest, Perm, Promotion, Promocode, Referral
from gutils.forms import BootstrapFormMixin
from uimg.forms import MultiUploadImageWidget
from uvideo.forms import UploadVideoWidget
from uprofile.models import User
from django.template import loader, Context
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from registration.users import UserModel
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.sites.models import Site


class AuthForm(BootstrapFormMixin, AuthenticationForm):
    """
    Форма авторизации
    """
    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].error_messages = {
            'required': 'Заполните имя пользователя',
            'invalid': 'Неправильное значение имени пользователя'
        }
        self.fields['username'].widget.attrs['placeholder'] = 'Электронная почта'
        self.fields['password'].error_messages = {
            'required': 'Заполните пароль',
            'invalid': 'Неправильное значение пароля'
        }
        self.fields['password'].widget.attrs['placeholder'] = 'Пароль'



class RadioButtonWidget(forms.Select):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/radiobutton-widget.html')
        return tmpl.render(Context({
            'id': name,
            'choices': self.choices,
            'value': value,
            'attrs': attrs
            }))


class CheckListButtonWidget(forms.SelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/checklistbutton-widget.html')
        return tmpl.render(Context({
            'id': name,
            'choices': self.choices,
            'value': value
        }))


class AdvertTypeButtonWidget(forms.Select):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/adverttype-widget.html')
        return tmpl.render(Context({
            'id': name,
            'choices': self.choices,
            'value': value
        }))


class Btn8RadioButtonWidget(forms.Select):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/btn8-radiobutton-widget.html')
        return tmpl.render(Context({
            'id': name,
            'choices': self.choices,
            'value': value
        }))


class Btn8CheckButtonWidget(forms.SelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/btn8-checkbutton-widget.html')
        return tmpl.render(Context({
            'id': name,
            'choices': self.choices,
            'value': value
        }))


class AdvertEstateCheckButtonWidget(forms.Select):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/estate-widget.html')
        return tmpl.render(Context({
            'id': name,
            'choices': FilterAdvertForm.ESTATES,
            'value': value,
            'type': 'checkbox'
        }))


class AdvertEstateRadioButtonWidget(forms.Select):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/estate-widget.html')
        return tmpl.render(Context({
            'id': name,
            'choices': FilterAdvertForm.ESTATES,
            'value': value,
            'type': 'radio'
        }))


class RoomMultipleWidget(forms.SelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/room-multiple-widget.html')
        return tmpl.render(Context({
            'id': name,
            'choices': self.choices,
            'value': value
        }))


class RadioSelectWidget(forms.Select):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/radio-select-widget.html')
        return tmpl.render(Context({
            'id': attrs['id'],
            'name': name,
            'choices': self.choices,
            'value': str(value),
        }))


class RadioMultipleSelectWidget(forms.SelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/radio-multiple-select-widget.html')
        return tmpl.render(Context({
            'id': attrs['id'],
            'name': name,
            'choices': self.choices,
            'value': value
        }))


class CheckPhoneWidget(forms.TextInput):
    def render(self, name, value, attrs=None):
        tmpl = loader.get_template('main/block/checkphone-widget.html')
        return tmpl.render(Context({
            'id': name,
            'value': value
        }))


class TariffListWidget(forms.SelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/tariff-list-widget.html')
        return tmpl.render(Context({
            'id': name,
            'choices': self.choices,
            'value': value
        }))


class CheckListWidget(forms.Select):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/check-list-widget.html')
        return tmpl.render(Context({
            'id': name,
            'choices': self.choices,
            'value': value
        }))


class OptionWidget(forms.CheckboxInput):
    label = None

    def __init__(self, attrs=None, check_test=None, label=None):
        super(OptionWidget, self).__init__(attrs, check_test)
        self.label = label

    def render(self, name, value, attrs=None):
        tmpl = loader.get_template('main/block/option-widget.html')
        return tmpl.render(Context({
            'name': name,
            'checked': self.check_test(value),
            'label': self.label,
            'attrs': attrs
        }))


class DatepickerWidget(forms.DateInput):
    def render(self, name, value, attrs=None):
        tmpl = loader.get_template('main/block/datepicker-widget.html')
        return tmpl.render(Context({
            'name': name,
            'value': value,
            'attrs': attrs
        }))


class MetroWidget(forms.Select):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/metro-widget.html')
        return tmpl.render(Context({
            'attrs': attrs,
            'name': name,
            'value': value,
            'choices': self.choices,
        }))


class MetroMultipleWidget(forms.SelectMultiple):
    town = None

    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/metro-multiple-widget.html')
        if isinstance(value, list):
            value = [str(v) for v in value]
        else:
            if value:
                value = [str(value)]
            else:
                value = None
        return tmpl.render(Context({
            'attrs': attrs,
            'name': name,
            'value': value,
            'choices': self.choices,
            'tmpl': super(MetroMultipleWidget, self).render(name, value, attrs=attrs),
            'town': self.town,
            'metro_list': self.town.metro_set.all().order_by('color', 'title') if self.town else []
            }))


class DistrictWidget(forms.Select):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/district-widget.html')
        return tmpl.render(Context({
            'attrs': attrs,
            'name': name,
            'value': value,
            'choices': self.choices,
            }))


class BFHSelectWidget(forms.Select):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/bfhselect-widget.html')
        return tmpl.render(Context({
            'attrs': attrs,
            'name': name,
            'value': value,
            'choices': self.choices,
            }))


class BFHNumberWidget(forms.TextInput):
    min = None
    max = None

    def __init__(self, attrs=None, min=None, max=None):
        super(BFHNumberWidget, self).__init__(attrs)
        self.max = max
        self.min = min

    def render(self, name, value, attrs=None):
        tmpl = loader.get_template('main/block/bfhnumber-widget.html')
        attrs.update(self.attrs)
        return tmpl.render(Context({
            'attrs': attrs,
            'name': name,
            'value': value,
            'min': self.min,
            'max': self.max
            }))


class CompanyWidget(forms.Select):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/company-widget.html')
        return tmpl.render(Context({
            'attrs': attrs,
            'name': name,
            'value': value,
            'choices': self.choices,
            }))


class UserWidget(forms.Select):
    site_id = None

    def __init__(self, site_id=None, *args, **kwargs):
        super(UserWidget, self).__init__(*args, **kwargs)
        self.site_id = site_id

    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/user-widget.html')
        if value:
            user_list = User.admin_objects.filter(id=value)
        else:
            user_list = []
        return tmpl.render(Context({
            'attrs': attrs,
            'name': name,
            'value': value,
            'choices': self.choices,
            'site_id': self.site_id,
            'user_list': user_list
            }))


class SelectMultipleWidget(forms.SelectMultiple):
    town = None

    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('main/block/select-multiple-widget.html')
        if not isinstance(value, list):
            if value:
                value = [str(value)]
            else:
                value = None
        return tmpl.render(Context({
            'attrs': attrs,
            'name': name,
            'value': value,
            'choices': self.choices,
            'tmpl': super(SelectMultipleWidget, self).render(name, value, attrs=attrs),
            }))


class RegisterForm(BootstrapFormMixin, RegistrationForm):
    """
    Форма регистрации
    """
    REGISTER_STATUS_AGENT = 'a'
    REGISTER_STATUS_COMPANY = 'c'
    REGISTER_STATUSES = {
        REGISTER_STATUS_AGENT: 'Я хочу зарегистрироваться как агент',
        REGISTER_STATUS_COMPANY: 'Я хочу зарегистрироваться как руководитель агентства'
    }

    username = forms.EmailField(label="Имя пользователя", error_messages={'required': 'Введите имя пользователя'})
    # captcha = ReCaptchaField(label='Введите текст с картинки')
    company_name = forms.CharField(label='Название агентства *', required=False,
                                   help_text='Например: "ООО Агентство недвижимости" или "ИП Иванов И.И."',
                                   error_messages={'required': 'Введите название агентства недвижимости'})
    company_tel = forms.CharField(label='Телефон *', required=True,
                                  error_messages={'required': 'Введите телефон'})
    company_address = forms.CharField(label='Юридический адрес', required=False)
    company_fact_address = forms.CharField(label='Фактический адрес', required=False)
    company_town = forms.ChoiceField(label='Город *', required=False,
                                     error_messages={'required': 'Ввыберите город'})
    company_ogrn = forms.CharField(label='ОГРН', required=False)
    company_inn = forms.CharField(label='ИНН', required=False)
    company_person = forms.CharField(label='ФИО контактного лица *', required=False,
                                     error_messages={'required': 'Введите ФИО контактного лица'})
    agree = forms.BooleanField(label='Я согласен с условиями', error_messages={
        'required': 'Вы не приняли условия работы сервиса заявок'
    })
    agent_status = forms.ChoiceField(label='Статус агента', required=True,
                                     choices=REGISTER_STATUSES.items(), widget=CheckListWidget(),
                                     initial=REGISTER_STATUS_AGENT)
    agent_company_msk = forms.ChoiceField(label='Ваше агентство', widget=CompanyWidget(), required=False,
                                      error_messages={'required': 'Выберите агентство из списка'})
    agent_company_spb = forms.ChoiceField(label='Ваше агентство', widget=CompanyWidget(), required=False,
                                      error_messages={'required': 'Выберите агентство из списка'})
    agent_company_nsk = forms.ChoiceField(label='Ваше агентство', widget=CompanyWidget(), required=False,
                                      error_messages={'required': 'Выберите агентство из списка'})
    agent_company_ekb = forms.ChoiceField(label='Ваше агентство', widget=CompanyWidget(), required=False,
                                      error_messages={'required': 'Выберите агентство из списка'})
    agent_name = forms.CharField(label='Ваше ФИО *', required=False)

    def __init__(self, *args, **kwargs):
        from django.template.defaultfilters import escape_filter

        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['company_town'].choices = [(town.id, town.title) for town in Town.objects.all()]
        self.fields['company_town'].initial = 1
        self.fields['username'].help_text = 'Указывайте существующий адрес, на него будет выслано подтверждение регистрации'
        self.fields['password1'].help_text = 'Пароль может состоять из букв латинского алфавита и цифр, длина пароля не менее 6-ти символов'
        self.fields['password1'].label = 'Пароль *'
        self.fields['password2'].label = 'Пароль (еще раз) *'
        self.fields['company_tel'].widget.attrs['class'] = 'masked-phone ' + self.fields['company_tel'].widget.attrs.get('class', '')
        self.fields['agent_company_msk'].choices = [(0, '')] + \
                                               [(company.id, u'<span class="item">%s <span class="cnt"><span class="town">%s</span><span class="inn">ИНН: %s</span></span></span>' %
                                                 (escape_filter(company.title), company.town.title, escape_filter(company.inn) if company.inn else '')) for company in Company.objects.filter(hidden=False, town_id=1).exclude(status=Company.STATUS_BLOCK).order_by('title').select_related('town')]
        self.fields['agent_company_spb'].choices = [(0, '')] + \
                                               [(company.id, u'<span class="item">%s <span class="cnt"><span class="town">%s</span><span class="inn">ИНН: %s</span></span></span>' %
                                                 (escape_filter(company.title), company.town.title, escape_filter(company.inn) if company.inn else '')) for company in Company.objects.filter(hidden=False, town_id=2).exclude(status=Company.STATUS_BLOCK).order_by('title').select_related('town')]
        self.fields['agent_company_msk'].help_text = 'Введите название вашего агентства или ИНН'
        self.fields['agent_company_spb'].help_text = 'Введите название вашего агентства или ИНН'

        self.fields['password1'].error_messages['required'] = 'Введите пароль'
        self.fields['password2'].error_messages['required'] = 'Введите подтверждение пароля'

        self.fields['agent_company_nsk'].choices = [(0, '')] + \
                                               [(company.id, u'<span class="item">%s <span class="cnt"><span class="town">%s</span><span class="inn">ИНН: %s</span></span></span>' %
                                                 (escape_filter(company.title), company.town.title, escape_filter(company.inn) if company.inn else '')) for company in Company.objects.filter(hidden=False, town__slug='novosibirsk').exclude(status=Company.STATUS_BLOCK).order_by('title').select_related('town')]
        self.fields['agent_company_nsk'].help_text = 'Введите название вашего агентства или ИНН'
        self.fields['agent_company_ekb'].choices = [(0, '')] + \
                                               [(company.id, u'<span class="item">%s <span class="cnt"><span class="town">%s</span><span class="inn">ИНН: %s</span></span></span>' %
                                                 (escape_filter(company.title), company.town.title, escape_filter(company.inn) if company.inn else '')) for company in Company.objects.filter(hidden=False, town__slug='ekaterinburg').exclude(status=Company.STATUS_BLOCK).order_by('title').select_related('town')]
        self.fields['agent_company_ekb'].help_text = 'Введите название вашего агентства или ИНН'

    def clean_email(self):
        return self.data['username']

    def clean_company_tel(self):
        data = self.cleaned_data['company_tel']
        data = clear_tel(data)
        return data

    def clean_company_name(self):
        data = self.cleaned_data['company_name']
        if self.REGISTER_STATUS_COMPANY in self.data['agent_status'] and not data:
            raise ValidationError(u'Введите название агентства', code='required')
        return data

    def clean_company_person(self):
        data = self.cleaned_data['company_person']
        if self.REGISTER_STATUS_COMPANY in self.data['agent_status'] and not data:
            raise ValidationError(u'Введите ФИО контактного лица', code='required')
        return data

    def clean_agent_company_msk(self):
        try:
            company_list = Company.objects.filter(id=self.cleaned_data['agent_company_msk'])
        except:
            company_list = []
        if self.REGISTER_STATUS_AGENT in self.data['agent_status'] and (self.data['company_town'] == '1') and not company_list:
            raise ValidationError(u'Выберите агентство из списка', code='required')
        return company_list[0].id if company_list else None

    def clean_agent_company_spb(self):
        try:
            company_list = Company.objects.filter(id=self.cleaned_data['agent_company_spb'])
        except:
            company_list = []
        if self.REGISTER_STATUS_AGENT in self.data['agent_status'] and (self.data['company_town'] == '2') and not company_list:
            raise ValidationError(u'Выберите агентство из списка', code='required')
        return company_list[0].id if company_list else None

    def clean_agent_company_nsk(self):
        try:
            company_list = Company.objects.filter(id=self.cleaned_data['agent_company_nsk'])
        except:
            company_list = []
        town = Town.objects.get(slug='novosibirsk')
        if self.REGISTER_STATUS_AGENT in self.data['agent_status'] and (self.data['company_town'] == str(town.id)) and not company_list:
            raise ValidationError(u'Выберите агентство из списка', code='required')
        return company_list[0].id if company_list else None

    def clean_agent_company_ekb(self):
        try:
            company_list = Company.objects.filter(id=self.cleaned_data['agent_company_ekb'])
        except:
            company_list = []
        town = Town.objects.get(slug='ekaterinburg')
        if self.REGISTER_STATUS_AGENT in self.data['agent_status'] and (self.data['company_town'] == str(town.id)) and not company_list:
            raise ValidationError(u'Выберите агентство из списка', code='required')
        return company_list[0].id if company_list else None

    def clean_agent_name(self):
        data = self.cleaned_data['agent_name']
        if self.REGISTER_STATUS_AGENT in self.data['agent_status'] and not data:
            raise ValidationError(u'Введите ваше имя', code='required')
        return data


class FilterAdvertForm(BootstrapFormMixin, forms.Form):

    ESTATE_FLAT = 'F'
    ESTATE_HOUSE = 'H'
    ESTATE_TERRITORY = 'T'
    ESTATE_COMMERCIAL = 'C'
    ESTATES = [
        (ESTATE_FLAT, u'Жилая'),
        (ESTATE_HOUSE, u'Загородная'),
        (ESTATE_COMMERCIAL, u'Коммерческая'),
        (ESTATE_TERRITORY, u'Земля'),
    ]

    ROOMS = [
        ('R', 'Комната'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4+')
    ]

    DATES = [
        (0, 'Показать все'),
        (1, 'За сегодня'),
        (3, 'За 3 дня'),
        (7, 'За 7 дней'),
        (30, 'За месяц'),
    ]

    # поле публичного фильтра
    type = forms.ChoiceField(choices=Advert.TYPES.items(), widget=AdvertTypeButtonWidget(), required=False)
    need = forms.MultipleChoiceField(choices=Advert.NEEDS.items(), widget=RadioButtonWidget(), required=False)
    metro = forms.MultipleChoiceField(label='Метро', widget=MetroMultipleWidget())
    district = forms.ChoiceField(label='Район', widget=forms.Select())
    estate = forms.ChoiceField(label='Категория', widget=AdvertEstateRadioButtonWidget())
    min_price = forms.IntegerField(label='Цены от', widget=forms.TextInput(attrs={'placeholder': 'от'}))
    max_price = forms.IntegerField(label='Цены до', widget=forms.TextInput(attrs={'placeholder': 'до'}))
    rooms = forms.MultipleChoiceField(label='Кол-во комнат', widget=RoomMultipleWidget(), choices=ROOMS)
    country = forms.MultipleChoiceField(label='Тип загородной недвижимости', required=False, choices=Advert.COUNTRIES.items(), widget=Btn8CheckButtonWidget())
    commercial = forms.MultipleChoiceField(label='Тип коммерческой недвижимости', required=False, choices=Advert.COMMERCIALS.items(), widget=Btn8CheckButtonWidget())
    territory = forms.MultipleChoiceField(label='Тип земли', required=False, choices=Advert.TERRITORIES.items(), widget=Btn8CheckButtonWidget())

    refrigerator = forms.BooleanField(label='Холодильник', widget=OptionWidget(label='холодильник'))
    tv = forms.BooleanField(label='Телевизор', widget=OptionWidget(label='телевизор'))
    washer = forms.BooleanField(label='Стиральная машина', widget=OptionWidget(label='стир.машина'))
    phone = forms.BooleanField(label='Телефон', widget=OptionWidget(label='телефон'))
    internet = forms.BooleanField(label='Интернет', widget=OptionWidget(label='интернет'))
    conditioner = forms.BooleanField(label='Кондиционер', widget=OptionWidget(label='кондиционер'))
    furniture = forms.BooleanField(label='Мебель', widget=OptionWidget(label='мебель'))
    euroremont = forms.BooleanField(label='Евроремонт', widget=OptionWidget(label='евроремонт'))
    separate_wc = forms.BooleanField(label='Раздельный санузел', widget=OptionWidget(label='разд.санузел'))
    balcony = forms.BooleanField(label='Балкон', widget=OptionWidget(label='балкон'))
    lift = forms.BooleanField(label='Лифт', widget=OptionWidget(label='лифт'))
    parking = forms.BooleanField(label='Парковка', widget=OptionWidget(label='парковка'))
    redecoration = forms.BooleanField(label='Косметический ремонт', widget=OptionWidget(label='косметический ремонт'))
    no_remont = forms.BooleanField(label='Без ремонта', widget=OptionWidget(label='без ремонта'))
    need_remont = forms.BooleanField(label='Нужен ремонт', widget=OptionWidget(label='нужен ремонт'))
    electric = forms.BooleanField(label='Электричество', widget=OptionWidget(label='электричество'))
    gas = forms.BooleanField(label='Газ', widget=OptionWidget(label='газ'))
    water = forms.BooleanField(label='Вода', widget=OptionWidget(label='вода'))
    sewage = forms.BooleanField(label='Канализация', widget=OptionWidget(label='канализация'))
    brick_building = forms.BooleanField(label='Кирпичная постройка', widget=OptionWidget(label='кирпичная постройка'))
    wood_building = forms.BooleanField(label='Деревянная постройка', widget=OptionWidget(label='деревянная постройка'))
    live_one = forms.BooleanField(label='Для одного', widget=OptionWidget(label='для одного'))
    live_two = forms.BooleanField(label='Для двух', widget=OptionWidget(label='для двух'))
    live_pare = forms.BooleanField(label='Для сем. пары', widget=OptionWidget(label='для сем.пары'))
    live_more = forms.BooleanField(label='Более двух чел.', widget=OptionWidget(label='более двух чел.'))
    live_child = forms.BooleanField(label='С детьми', widget=OptionWidget(label='с детьми'))
    live_animal = forms.BooleanField(label='С животными', widget=OptionWidget(label='с животными'))
    live_girl = forms.BooleanField(label='Для девушек', widget=OptionWidget(label='для девушек'))
    live_man = forms.BooleanField(label='Для мужчин', widget=OptionWidget(label='для мужчин'))
    concierge = forms.BooleanField(label='Консьерж', widget=OptionWidget(label='консьерж'))
    guard = forms.BooleanField(label='Охрана', widget=OptionWidget(label='охрана'))
    garage = forms.BooleanField(label='Гараж', widget=OptionWidget(label='гараж'))

    # дата
    date = forms.ChoiceField(label='Дата', choices=DATES, required=False, widget=forms.Select())
    archive = forms.BooleanField(label='Архив', widget=forms.CheckboxInput())

    # площадь
    min_square = forms.IntegerField(label='Площадь от', widget=forms.TextInput(attrs={'placeholder': 'от'}), required=False)
    max_square = forms.IntegerField(label='Площадь до', widget=forms.TextInput(attrs={'placeholder': 'до'}), required=False)

    map = forms.BooleanField(required=False, widget=forms.HiddenInput())

    def __init__(self, town, *args, **kwargs):
        super(FilterAdvertForm, self).__init__(*args, **kwargs)
        self.fields['metro'].choices = [(str(metro.id), metro.title) for metro in Metro.objects.filter(town=town)]
        self.fields['district'].choices = [(0, '--Район--')] + [(district.id, district.title) for district in District.objects.filter(town=town)]
        self.fields['metro'].widget.town = town


class FilterAdvertClientForm(FilterAdvertForm):

    TYPES2 = [
        ('LS', 'Сдам', 'L'),
        # ('LD', 'Сниму', 'L'),
        # ('SS', 'Продам', 'S'),
        # ('SD', 'Куплю', 'S')
    ]

    DATES = [
        (30, 'За месяц'),
        (1, 'За сегодня'),
        (3, 'За 3 дня'),
        (7, 'За 7 дней'),
        (0, 'Показать все'),
    ]

    id = forms.IntegerField(label='Номер', required=False, widget=forms.TextInput(attrs={'placeholder': 'Номер...'}))
    owner_tel = forms.CharField(label='Телефон', required=False, widget=forms.TextInput(attrs={'placeholder': 'Телефон...'}))
    type = forms.ChoiceField(choices=Advert.TYPES.items(), widget=forms.HiddenInput(), required=False)
    # поле для фильтра клиенской части по аренде
    type2 = forms.ChoiceField(choices=TYPES2, widget=RadioButtonWidget(), required=False)
    # поле для фильтра клиенской части по продаже
    # type3 = forms.ChoiceField(choices=TYPES3.items(), widget=RadioButtonWidget(), required=False)
    estate = forms.ChoiceField(label='Категория', widget=forms.HiddenInput(), choices=Advert.ESTATES.items(), required=False)
    limit_day = forms.BooleanField(label='Посуточно', widget=forms.CheckboxInput())
    rooms = forms.MultipleChoiceField(label='Кол-во комнат', widget=SelectMultipleWidget(),
                              choices=FilterAdvertForm.ROOMS)
    country = forms.ChoiceField(label='Тип загородной недвижимости', required=False,
                                choices=[('0', 'Выбрать тип')] + Advert.COUNTRIES.items())
    commercial = forms.ChoiceField(label='Тип коммерческой недвижимости', required=False,
                                   choices=[('0', 'Выбрать тип')] + Advert.COMMERCIALS.items())
    territory = forms.ChoiceField(label='Тип земли', required=False,
                                  choices=[('0', 'Выбрать тип')] + Advert.TERRITORIES.items())
    date = forms.ChoiceField(label='Дата', choices=DATES, required=False, widget=forms.Select())

    #арендодатель
    owner_agent = forms.BooleanField(label='Агентство', widget=forms.CheckboxInput())
    owner_owner = forms.BooleanField(label='Частное лицо', widget=forms.CheckboxInput())

    # этаж
    min_floor = forms.IntegerField(label='Этаж от', widget=forms.TextInput(attrs={'placeholder': 'от'}), required=False)
    max_floor = forms.IntegerField(label='Этаж до', widget=forms.TextInput(attrs={'placeholder': 'до'}), required=False)
    not_first_floor = forms.BooleanField(label='Не первый', widget=forms.CheckboxInput())
    not_last_floor = forms.BooleanField(label='Не последний', widget=forms.CheckboxInput())

    def __init__(self, town, adtype=None, *args, **kwargs):
        data = dict(kwargs['data'])
        if adtype:
            type2_choices = [(x, y) for x, y, z in self.TYPES2 if z == adtype]
        else:
            type2_choices = self.TYPES2
        if not 'type2' in data:
            data['type2'] = type2_choices[0][0]
        kwargs['data'] = data
        super(FilterAdvertClientForm, self).__init__(town, *args, **kwargs)

        self.fields['type2'].choices = type2_choices


class FilterVKAdvertClientForm(FilterAdvertClientForm):
    owner_vkid = forms.CharField(label='VK ID', required=False, widget=forms.TextInput(attrs={'placeholder': 'VK ID...'}))
    town = forms.ChoiceField(label='Город', required=False)

    def __init__(self, *args, **kwargs):
        super(FilterVKAdvertClientForm, self).__init__(*args, **kwargs)
        self.fields['town'].choices = [(0, 'Любой')] + [(town.id, town.title) for town in Town.admin_objects.all().order_by('order')]


class NewsForm(BootstrapFormMixin, forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'body', 'images', 'video']

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['images'].widget = MultiUploadImageWidget()
        self.fields['images'].required = False
        self.fields['video'].widget = UploadVideoWidget()
        self.fields['video'].required = False


class TownForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Town
        fields = ['title', 'latitude', 'longitude', 'zoom']


class DistrictForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = District
        fields = ['title', 'town']
        widgets = {
            'town': forms.HiddenInput()
        }


class MetroForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Metro
        fields = ['title', 'town']
        widgets = {
            'town': forms.HiddenInput()
        }


class AdvertForm(BootstrapFormMixin, forms.ModelForm):

    type = forms.ChoiceField(label='Я хочу', widget=Btn8RadioButtonWidget(), choices=(
        ('LS', u'Сдать'),
        ('SS', u'Продать'),
        ('LD', u'Снять'),
        ('SD', u'Купить')
    ), error_messages={'required': 'Выберите операцию СДАТЬ | ПРОДАТЬ | СНЯТЬ | КУПИТЬ'})
    agree = forms.BooleanField(label='Я согласен с условиями', error_messages={
        'required': 'Вы не приняли условия работы сервиса заявок'
    })

    class Meta:
        model = Advert
        fields = [
            'body',
            'images',
            'estate',
            'live',
            'country',
            'commercial',
            'territory',
            'town',
            'address',
            'district',
            'metro',
            'square',
            'living_square',
            'kitchen_square',
            'rooms',
            'price',
            'refrigerator',
            'washer',
            'tv',
            'phone',
            'internet',
            'conditioner',
            'furniture',
            'euroremont',
            'separate_wc',
            'balcony',
            'lift',
            'parking',
            'redecoration',
            'no_remont',
            'need_remont',
            'electric',
            'gas',
            'water',
            'sewage',
            'brick_building',
            'wood_building',
            'live_one',
            'live_two',
            'live_pare',
            'live_more',
            'live_child',
            'live_animal',
            'live_girl',
            'live_man',
            'concierge',
            'guard',
            'garage',
            'latitude',
            'longitude',
            'owner_name',
            'owner_tel',
            'owner_email',
            'limit'
        ]
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5}),
            'estate': AdvertEstateRadioButtonWidget(),
            'live': Btn8RadioButtonWidget(),
            'country': Btn8RadioButtonWidget(),
            'commercial': Btn8RadioButtonWidget(),
            'territory': Btn8RadioButtonWidget(),
            'address': forms.TextInput(),
            'metro': MetroWidget(),
            'district': DistrictWidget(),
            'images': MultiUploadImageWidget(),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'refrigerator': OptionWidget(label='Холодильник'),
            'washer': OptionWidget(label='Стиральная машина'),
            'tv': OptionWidget(label='Телевизор'),
            'phone': OptionWidget(label='Телефон'),
            'internet': OptionWidget(label='Интернет'),
            'conditioner': OptionWidget(label='Кондиционер'),
            'furniture': OptionWidget(label='Мебель'),
            'euroremont': OptionWidget(label='Евроремонт'),
            'separate_wc': OptionWidget(label='Раздельный санузел'),
            'balcony': OptionWidget(label='Балкон'),
            'lift': OptionWidget(label='Лифт'),
            'parking': OptionWidget(label='Парковка'),
            'rooms': forms.Select(choices=[(n, str(n)) for n in xrange(1, 7)]),
            'redecoration': OptionWidget(label='Косм.ремонт'),
            'no_remont': OptionWidget(label='Нет ремонта'),
            'need_remont': OptionWidget(label='Нужен ремонт'),
            'electric': OptionWidget(label='Электричество'),
            'gas': OptionWidget(label='Газ'),
            'water': OptionWidget(label='Вода'),
            'sewage': OptionWidget(label='Канализация'),
            'brick_building': OptionWidget(label='Кирпичная постройка'),
            'wood_building': OptionWidget(label='Деревянная постройка'),
            'live_one': OptionWidget(label='Одному чел.'),
            'live_two': OptionWidget(label='Двум людям'),
            'live_pare': OptionWidget(label='Семейной паре'),
            'live_more': OptionWidget(label='Более 2-х чел.'),
            'live_child': OptionWidget(label='Можно с детьми'),
            'live_animal': OptionWidget(label='Можно с животными'),
            'live_girl': OptionWidget(label='Для девушек'),
            'live_man': OptionWidget(label='Для мужчин'),
            'concierge': OptionWidget(label='Консьерж'),
            'guard': OptionWidget(label='Охрана'),
            'garage': OptionWidget(label='Гараж'),
            'price': forms.TextInput(),
            'square': forms.TextInput(attrs={'placeholder': 'Общая'}),
            'living_square': forms.TextInput(attrs={'placeholder': 'Жилая'}),
            'kitchen_square': forms.TextInput(attrs={'placeholder': 'Кухни'}),
            'limit': Btn8RadioButtonWidget(),
        }

        error_messages = {
            'estate': {'required': 'Выберите тип недвижимости'},
            'owner_name': {'required': 'Введите ФИО'},
            'owner_tel': {'required': 'Введите телефон'},
            'square': {'invalid': 'Неправильно указана площадь'},
            'living_square': {'invalid': 'Неправильно указана жилая площадь'},
            'kitchen_square': {'invalid': 'Неправильно указана площадь кухни'},
            'price': {'invalid': 'Неправильно указана цена'},
        }

    def __init__(self, filter_town=None, check_tel=False, initial=None, *args, **kwargs):
        if not initial:
            initial = {}
        initial['town'] = filter_town.id
        super(AdvertForm, self).__init__(initial=initial, *args, **kwargs)
        self.fields['metro'].queryset = self.fields['metro'].queryset.filter(town=filter_town)
        self.fields['district'].queryset = self.fields['district'].queryset.filter(town=filter_town)
        self.fields['estate'].initial = None
        self.fields['owner_name'].required = True
        self.fields['owner_tel'].required = True
        self.fields['owner_tel'].widget.attrs['class'] = 'masked-phone ' + self.fields['owner_tel'].widget.attrs.get('class', '')
        self.fields['limit'].choices = [(Advert.LIMIT_DAY, 'посуточно'), (Advert.LIMIT_LONG, 'длительно')]

    def clean_owner_tel(self):
        return clear_tel(self.cleaned_data['owner_tel'])



class AdvertForm_Client(BootstrapFormMixin, forms.ModelForm):
    TYPES2 = [
        ('LS', 'Сдам'),
        ('SS', 'Продам'),
        ('LD', 'Сниму'),
        ('SD', 'Куплю')
    ]

    ESTATE2 = [
        ('F', 'Жилая'),
        ('H', 'Загородная'),
        ('C', 'Коммерч.'),
        ('T', 'Земля'),
    ]

    ROOMS = [
        ('1', '1к'),
        ('2', '2к'),
        ('3', '3к'),
        ('4', '4к+'),
        ]

    type2 = forms.ChoiceField(widget=RadioButtonWidget(), choices=TYPES2, initial='LS')
    estate = forms.ChoiceField(widget=RadioButtonWidget(), choices=ESTATE2, initial='F')

    class Meta:
        model = Advert
        fields = [
            'estate',
            'body',
            'images',
            'address',
            'district',
            'metro',
            'need_metro',
            'square',
            'square_max',
            'living_square',
            'living_square_max',
            'kitchen_square',
            'kitchen_square_max',
            'rooms',
            'price',
            'min_price',
            'refrigerator',
            'washer',
            'tv',
            'phone',
            'internet',
            'conditioner',
            'furniture',
            'euroremont',
            'separate_wc',
            'balcony',
            'lift',
            'parking',
            'redecoration',
            'no_remont',
            'need_remont',
            'electric',
            'gas',
            'water',
            'sewage',
            'brick_building',
            'wood_building',
            'live_one',
            'live_two',
            'live_pare',
            'live_more',
            'live_child',
            'live_animal',
            'live_girl',
            'live_man',
            'concierge',
            'guard',
            'garage',
            'latitude',
            'longitude',
            'floor',
            'count_floor',
            'floor_max',
            'owner_name',
            'owner_tel',
            'country',
            'commercial',
            'territory',
            'live',
            'live_flat1',
            'live_flat2',
            'live_flat3',
            'live_flat4',
            'limit'
        ]
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5}),
            'address': forms.TextInput(),
            'metro': MetroWidget(),
            'need_metro': MetroMultipleWidget(),
            'district': DistrictWidget(),
            'images': MultiUploadImageWidget(),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'refrigerator': OptionWidget(label='Холодильник'),
            'washer': OptionWidget(label='Стиральная машина'),
            'tv': OptionWidget(label='Телевизор'),
            'phone': OptionWidget(label='Телефон'),
            'internet': OptionWidget(label='Интернет'),
            'conditioner': OptionWidget(label='Кондиционер'),
            'furniture': OptionWidget(label='Мебель'),
            'euroremont': OptionWidget(label='Евроремонт'),
            'separate_wc': OptionWidget(label='Раздельный санузел'),
            'balcony': OptionWidget(label='Балкон'),
            'lift': OptionWidget(label='Лифт'),
            'parking': OptionWidget(label='Парковка'),
            'floor': forms.TextInput(attrs={'placeholder': 'этаж'}),
            'count_floor': forms.TextInput(attrs={'placeholder': 'всего'}),
            'floor_max': forms.TextInput(attrs={'placeholder': 'этаж'}),
            'square': forms.TextInput(attrs={'placeholder': 'общая'}),
            'square_max': forms.TextInput(attrs={'placeholder': 'до'}),
            'living_square': forms.TextInput(attrs={'placeholder': 'жилая', 'class': 'for_flat for_room for_house for_commercial'}),
            'living_square_max': forms.TextInput(attrs={'placeholder': 'до', 'class': 'for_flat for_room for_house for_commercial'}),
            'kitchen_square': forms.TextInput(attrs={'placeholder': 'кухня', 'class': 'for_flat for_room for_house for_commercial'}),
            'kitchen_square_max': forms.TextInput(attrs={'placeholder': 'до', 'class': 'for_flat for_room for_house for_commercial'}),
            'price': forms.TextInput(),
            'min_price': forms.TextInput(),
            'country': RadioButtonWidget(),
            'commercial': RadioButtonWidget(),
            'territory': RadioButtonWidget(),
            'live': RadioButtonWidget(),
            'redecoration': OptionWidget(label='Косм.ремонт'),
            'no_remont': OptionWidget(label='Нет ремонта'),
            'need_remont': OptionWidget(label='Нужен ремонт'),
            'electric': OptionWidget(label='Электричество'),
            'gas': OptionWidget(label='Газ'),
            'water': OptionWidget(label='Вода'),
            'sewage': OptionWidget(label='Канализация'),
            'brick_building': OptionWidget(label='Кирпичная постройка'),
            'wood_building': OptionWidget(label='Деревянная постройка'),
            'live_one': OptionWidget(label='Одному чел.'),
            'live_two': OptionWidget(label='Двум людям'),
            'live_pare': OptionWidget(label='Семейной паре'),
            'live_more': OptionWidget(label='Более 2-х чел.'),
            'live_child': OptionWidget(label='Можно с детьми'),
            'live_animal': OptionWidget(label='Можно с животными'),
            'live_girl': OptionWidget(label='Для девушек'),
            'live_man': OptionWidget(label='Для мужчин'),
            'concierge': OptionWidget(label='Консьерж'),
            'guard': OptionWidget(label='Охрана'),
            'garage': OptionWidget(label='Гараж'),
            'limit': RadioButtonWidget(),
        }

        initial = {
            'rooms': 1
        }

        error_messages = {
            'square': {'invalid': 'Неправильно указана площадь'},
            'living_square': {'invalid': 'Неправильно указана жилая площадь'},
            'kitchen_square': {'invalid': 'Неправильно указана площадь кухни'},
            'price': {'invalid': 'Неправильно указана цена'},
        }

    def __init__(self, filter_town=None, check_tel=False, *args, **kwargs):
        super(AdvertForm_Client, self).__init__(*args, **kwargs)
        self.fields['metro'].queryset = self.fields['metro'].queryset.filter(town=filter_town)
        self.fields['district'].queryset = self.fields['district'].queryset.filter(town=filter_town)
        self.fields['rooms'].widget = RadioSelectWidget(choices=self.ROOMS)
        self.fields['rooms'].initial = 1
        self.fields['country'].required = False
        self.fields['commercial'].required = False
        self.fields['territory'].required = False
        if check_tel:
            self.fields['owner_tel'].widget = CheckPhoneWidget()
        self.fields['owner_tel'].widget.attrs['class'] = 'masked-phone ' + self.fields['owner_tel'].widget.attrs.get('class', '')
        self.fields['limit'].choices = [(Advert.LIMIT_DAY, 'посуточно'), (Advert.LIMIT_LONG, 'длительно')]
        self.fields['need_metro'].choices = [(str(metro.id), metro.title) for metro in Metro.objects.filter(town=filter_town)]
        self.fields['need_metro'].widget.town = filter_town

    def clean_owner_tel(self):
        return clear_tel(self.cleaned_data['owner_tel'])


class SmartAdvertForm(BootstrapFormMixin, forms.ModelForm):

    msk_metro = forms.ChoiceField(label='Метро')
    spb_metro = forms.ChoiceField(label='Метро')

    image1 = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)
    image3 = forms.ImageField(required=False)
    image4 = forms.ImageField(required=False)
    image5 = forms.ImageField(required=False)

    class Meta:
        model = Advert
        fields = [
            'body',
            'live',
            'town',
            'address',
            'square',
            'living_square',
            'kitchen_square',
            'rooms',
            'price',
            'refrigerator',
            'washer',
            'tv',
            'phone',
            'internet',
            'conditioner',
            'furniture',
            'euroremont',
            'separate_wc',
            'balcony',
            'lift',
            'parking',
            'redecoration',
            'no_remont',
            'need_remont',
            'electric',
            'gas',
            'water',
            'sewage',
            'brick_building',
            'wood_building',
            'live_one',
            'live_two',
            'live_pare',
            'live_more',
            'live_child',
            'live_animal',
            'live_girl',
            'live_man',
            'concierge',
            'guard',
            'garage',
            'owner_name',
            'owner_tel',
            'floor',
            'count_floor'
        ]
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5}),
            'rooms': forms.Select(choices=[(n, str(n)) for n in xrange(1, 7)]),
            'price': forms.TextInput(),
            'address': forms.TextInput(attrs={'placeholder': 'Введите адрес'}),
            'square': forms.TextInput(attrs={'placeholder': 'Общая'}),
            'living_square': forms.TextInput(attrs={'placeholder': 'Жилая'}),
            'kitchen_square': forms.TextInput(attrs={'placeholder': 'Кухни'}),
            'floor': forms.TextInput(attrs={'placeholder': 'Этаж'}),
            'count_floor': forms.TextInput(attrs={'placeholder': 'Этажность'}),
        }

        error_messages = {
            'owner_name': {'required': 'Введите ФИО'},
            'owner_tel': {'required': 'Введите телефон'},
        }

    def __init__(self, *args, **kwargs):
        super(SmartAdvertForm, self).__init__(*args, **kwargs)
        self.fields['msk_metro'].choices = [(metro.id, metro.title) for metro in Metro.objects.filter(town_id=1)]
        self.fields['spb_metro'].choices = [(metro.id, metro.title) for metro in Metro.objects.filter(town_id=2)]
        self.fields['owner_name'].required = True
        self.fields['owner_tel'].required = True
        self.fields['owner_tel'].widget.attrs['class'] = 'masked-phone ' + self.fields['owner_tel'].widget.attrs.get('class', '')
        self.fields['town'].initial = 1

    def clean_owner_tel(self):
        return clear_tel(self.cleaned_data['owner_tel'])


class VacancyForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'body']


class QuestionForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Question
        fields = ['body', 'answer']


class FaqForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Question
        fields = ['body']


class BlacklistForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Blacklist
        fields = ['tel', 'body']

    def clean_tel(self):
        data = self.cleaned_data['tel']
        if not 'X' in data:
            data = clear_tel(data)
        return data


class BlacklistMultiForm(BootstrapFormMixin, forms.Form):
    tel = forms.CharField(label='Список телефонов', widget=forms.Textarea())


class UserForm(BootstrapFormMixin, forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(), required=False)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'tel', 'is_active', 'groups', 'town', 'company',
                  'independent']
        widgets = {
            'company': CompanyWidget()
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['tel'].widget.attrs['class'] = 'masked-phone ' + self.fields['tel'].widget.attrs.get('class', '')

    def clean_tel(self):
        data = self.cleaned_data['tel']
        data = clear_tel_list(data)
        return data


class UserForm_User(BootstrapFormMixin, forms.ModelForm):
    username = forms.EmailField(label='E-mail пользователя')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(), required=False)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'tel', 'is_active']

    def __init__(self, user, *args, **kwargs):
        super(UserForm_User, self).__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['tel'].widget.attrs['class'] = 'masked-phone ' + self.fields['tel'].widget.attrs.get('class', '')

    def clean_tel(self):
        data = self.cleaned_data['tel']
        data = clear_tel(data)
        return data


class CompanyForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Company
        fields = ['title', 'tel', 'email', 'address', 'inn', 'ogrn', 'desc', 'town', 'owner', 'is_real', 'hidden']
        widgets = {
            'owner': UserWidget()
        }

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['tel'].widget.attrs['class'] = 'masked-phone ' + self.fields['tel'].widget.attrs.get('class', '')
        # self.fields['owner'].choices = [0] + [(user.id, u'<strong>%s</strong><br>%s' % (user.username, user.get_full_name())) for user in User.objects.all().order_by('username')]
        # self.fields['owner'].choices = [(user.id, user.username) for user in User.admin_objects.all()]

    def clean_tel(self):
        data = self.cleaned_data['tel']
        data = clear_tel(data)
        return data


class TariffForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Tariff
        fields = ['title', 'desc', 'price', 'perms']
        widgets = {
            'perms': forms.CheckboxSelectMultiple()
        }


class PaymentOrderForm(BootstrapFormMixin, forms.Form):
    MONTH_CHOICES = [
        (1, '1 месяц'),
        (1, '2 месяца'),
        (3, '3 месяца'),
        (6, '6 месяцев'),
        (9, '9 месяцев'),
        (12, '12 месяцев'),
    ]
    tariff = forms.ChoiceField(label='Тарифы', widget=forms.HiddenInput(), error_messages={'required': "Выберите тариф"})
    months = forms.IntegerField(label='Количество месяцев', widget=forms.Select(choices=MONTH_CHOICES), error_messages={'required': "Выберите количество месяцев"})

    def __init__(self, town, *args, **kwargs):
        from main.templatetags.main_tags import fmt_price
        super(PaymentOrderForm, self).__init__(*args, **kwargs)
        choices = []
        # for tariff in Tariff.objects.filter(town=town).order_by('order'):
        #     disabled = u' '
        #     if not town in tariff.town.all():
        #         disabled = u'disabled'
        #     choices.append((tariff.id, {'label': u'<span>%s</span><strong data-sum="%s">%s р.</strong>' % (tariff.title, tariff.price, fmt_price(tariff.price)), 'class':disabled }))
        self.fields['tariff'].choices = [(tariff.id, tariff.title) for tariff in Tariff.objects.filter(town__id=town.id, code__isnull=False)]
        self.tariffs = dict((tariff.code, tariff) for tariff in Tariff.objects.filter(town__id=town.id, code__isnull=False))


class BuyOrderForm(BootstrapFormMixin, forms.Form):
    COUNT_CHOICES = [
        (u'5', u'5 выкупов'),
        (u'10', u'10 выкупов'),
        (u'20', u'20 выкупов'),
        (u'50', u'50 выкупов'),
        ]
    count = forms.ChoiceField(label='Количество выкупов', choices=COUNT_CHOICES, widget=CheckListWidget())


class BuyPayForm(BootstrapFormMixin, forms.Form):
    advert_id = forms.IntegerField(widget=forms.HiddenInput())
    days = forms.IntegerField(label='Количество дней выкупа объявления', initial=1,
                              validators=[MinValueValidator(1), MaxValueValidator(1000)],
                              widget=BFHNumberWidget(min=1, max=1000))


class FeedbackForm(BootstrapFormMixin, forms.Form):
    title = forms.CharField(label='Заголовок вопроса', error_messages={'required': 'Введите заголовок сообщения'})
    body = forms.CharField(label='Текст вопроса', widget=forms.Textarea(attrs={'rows': 5}), error_messages={'required': 'Введите имя отправителя'})
    name = forms.CharField(label='Имя отправителя', error_messages={'required': 'Введите заголовок сообщения'})
    tel = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'masked-phone'}), error_messages={'required': 'Введите телефон'})
    email = forms.EmailField(label='Email', error_messages={'required': 'Введите E-mail'})


class FeedbackAdvertForm(BootstrapFormMixin, forms.Form):
    email = forms.EmailField(label='Ваш Email')
    friend_email = forms.EmailField(label='Email друга')


class RequestForm(BootstrapFormMixin, forms.ModelForm):
    min_price = forms.FloatField(label='Цены от', widget=forms.TextInput(attrs={'placeholder': 'от'}), required=False)
    price = forms.FloatField(label='Цены до', widget=forms.TextInput(attrs={'placeholder': 'до'}), required=False)
    adtype2 = forms.ChoiceField(widget=Btn8RadioButtonWidget(), initial=Advert.TYPE_LEASE)
    agree2 = forms.BooleanField(label='Я согласен с условиями', error_messages={
        'required': 'Вы не приняли условия работы сервиса заявок'
    })

    class Meta:
        model = Advert
        fields = [
            'body',
            'estate',
            'district',
            'need_metro',
            'owner_name',
            'owner_tel',
            'owner_email',
            'price',
            'min_price',
            'live',
            'country',
            'commercial',
            'territory'
        ]
        widgets = {
            'estate': AdvertEstateRadioButtonWidget(),
            'body': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Описание заявки'}),
            'live': Btn8RadioButtonWidget(),
            'country': Btn8RadioButtonWidget(),
            'commercial': Btn8RadioButtonWidget(),
            'territory': Btn8RadioButtonWidget(),
            'need_metro': MetroMultipleWidget(),
        }
        initial = {
            'estate': Advert.ESTATE_LIVE,
        }
        error_messages = {
            'owner_name': {
                'required': 'Заполните ФИО'
            },
            'owner_tel': {
                'required': 'Заполните телефон'
            },
            'owner_email': {
                'required': 'Заполните e-mail'
            },
        }

    def __init__(self, filter_town=None, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.fields['need_metro'].choices = [(metro.id, metro.title) for metro in Metro.objects.filter(town=filter_town)]
        self.fields['need_metro'].widget.town = filter_town
        self.fields['need_metro'].required = False
        self.fields['district'].choices = [('', '--Район--')] + \
                                          [(district.id, district.title) for district in District.objects.filter(town=filter_town)]
        self.fields['district'].required = False
        self.fields['adtype2'].choices = (
            (Advert.TYPE_LEASE, u'Я хочу снять'),
            (u'LP', u'Я хочу снять посуточно'),
            (Advert.TYPE_SALE, u'Я хочу купить')
        )
        self.fields['owner_name'].required = True
        self.fields['owner_tel'].required = True
        self.fields['owner_tel'].widget.attrs['class'] = 'masked-phone ' + self.fields['owner_tel'].widget.attrs.get('class', '')
        self.fields['owner_email'].required = True

    def clean_owner_tel(self):
        data = self.cleaned_data['owner_tel']
        data = clear_tel(data)
        return data


class RequestRemoveForm(BootstrapFormMixin, forms.Form):
    nomer = forms.CharField(label='Номер объявления', error_messages={'required': 'Введите номер объявления'})
    tel = forms.CharField(label='Телефон', error_messages={'required': 'Введите телефон'}, widget=forms.TextInput(attrs={'class': 'masked-phone'}))


class ReclameForm(BootstrapFormMixin, forms.Form):
    body = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'rows': 5}),
                           error_messages={'required': 'Введите сообщение'})
    name = forms.CharField(label='Имя', error_messages={'required': 'Введите имя'})
    tel = forms.CharField(label='Телефон', error_messages={'required': 'Введите телефон для связи'}, widget=forms.TextInput(attrs={'class': 'masked-phone'}))
    email = forms.EmailField(label='Email', error_messages={'required': 'Введите почту', 'invalid': 'Введите корректную почту'})


class UserFilterForm(BootstrapFormMixin, forms.Form):
    username = forms.CharField(label='Имя пользователя', required=False)
    company = forms.ChoiceField(label='Агентство', required=False, widget=CompanyWidget())
    moderator = forms.BooleanField(label='Модератор', required=False)
    email = forms.CharField(label='E-mail', required=False)
    tel = forms.CharField(label='Телефон', required=False)
    status = forms.ChoiceField(label='Статус', required=False, choices=[(0, 'НЕТ')] + User.STATUSES.items())
    site = forms.ChoiceField(label='Сайт', required=False)

    def __init__(self, *args, **kwargs):
        kwargs['auto_id'] = 'id_flt_%s'
        super(UserFilterForm, self).__init__(*args, **kwargs)
        self.fields['company'].choices = [(0, '--')] + [(company.id, company.title) for company in Company.objects.all().order_by('title')]
        self.fields['site'].choices = [(0, 'Любой')] + [(site.id, site.name) for site in Site.objects.all()]


class CompanyFilterForm_Client(BootstrapFormMixin, forms.Form):
    title = forms.CharField(label='Название', required=False)
    email = forms.CharField(label='E-mail', required=False)
    tel = forms.CharField(label='Телефон', required=False)
    is_real = forms.BooleanField(label='Подключенные агентства', required=False)
    status = forms.ChoiceField(label='Статус', required=False, choices=[(0, 'НЕТ')] + Company.STATUSES.items())
    town = forms.ChoiceField(label='Город', required=False)

    def __init__(self, *args, **kwargs):
        kwargs['auto_id'] = 'id_flt_%s'
        super(CompanyFilterForm_Client, self).__init__(*args, **kwargs)
        self.fields['town'].choices = [(0, 'НЕТ')] + [(town.id, town.title) for town in Town.objects.all()]


class CompanyFilterForm(BootstrapFormMixin, forms.Form):
    town = forms.ChoiceField(label=u'Город', required=False)
    title = forms.CharField(label='Название', required=False)
    inn = forms.CharField(label='ИНН', required=False)
    tel = forms.CharField(label='Телефон', required=False, widget=forms.TextInput(attrs={'placeholder': 'Укажите телефон'}))

    def __init__(self, *args, **kwargs):
        kwargs['auto_id'] = 'id_flt_%s'
        super(CompanyFilterForm, self).__init__(*args, **kwargs)
        self.fields['town'].choices = [(0, 'НЕТ')] + [(town.id, town.title) for town in Town.objects.all().order_by('id')]


class FeedbackForm_Client(BootstrapFormMixin, forms.Form):
    title = forms.CharField(label='Тема', error_messages={'required': 'Введите тему сообщения'})
    desc = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'rows': 5}), error_messages={'required': 'Введите текст сообщения'})


class BlacklistFilterForm(BootstrapFormMixin, forms.Form):
    tel = forms.CharField(label='Телефон', required=False, widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))


class VKBlacklistFilterForm(BootstrapFormMixin, forms.Form):
    vkid = forms.CharField(label='VK ID', required=False, widget=forms.TextInput(attrs={'placeholder': 'VK ID'}))


class AbbrForm(BootstrapFormMixin, forms.ModelForm):

    class Meta:
        model = Abbr
        fields = ['title', 'desc']


class ConnectedServiceForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = ConnectedService
        fields = [
            'company',
            'user',
            'perm',
            'start_date',
            'end_date',
            'active'
        ]
        widgets = {
            'company': forms.HiddenInput(),
            'user': forms.HiddenInput(),
            'start_date': DatepickerWidget(),
            'end_date': DatepickerWidget()
        }


class ModeratorStatFilterForm(BootstrapFormMixin, forms.Form):
    start_date = forms.DateTimeField(label='Начало периода', required=False, widget=DatepickerWidget())
    end_date = forms.DateTimeField(label='Конец периода', required=False, widget=DatepickerWidget())


class ParserStatFilterForm(BootstrapFormMixin, forms.Form):
    start_date = forms.DateTimeField(label='Начало периода', required=False, widget=DatepickerWidget())
    end_date = forms.DateTimeField(label='Конец периода', required=False, widget=DatepickerWidget())


class CompanyAvatarForm(forms.Form):
    image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        kwargs['auto_id'] = 'id_company_%s'
        super(CompanyAvatarForm, self).__init__(*args, **kwargs)


class SearchRequestForm_Client(BootstrapFormMixin, forms.ModelForm):
    TYPES2 = [
        # ('LS', 'Сдам'),
        # ('SS', 'Продам'),
        ('LD', 'Сниму'),
        ('SD', 'Куплю')
    ]

    ESTATE2 = [
        ('F', 'Жилая'),
        ('H', 'Загородная'),
        # ('C', 'Коммерч.'),
        # ('T', 'Земля'),
    ]

    ROOMS = [
        ('1', '1к'),
        ('2', '2к'),
        ('3', '3к'),
        ('4', '4к+'),
        ]

    type2 = forms.ChoiceField(widget=RadioButtonWidget(), choices=TYPES2, initial='LD')
    estate = forms.ChoiceField(widget=RadioButtonWidget(), choices=ESTATE2, initial='F')

    class Meta:
        model = SearchRequest
        fields = [
            'estate',
            'body',
            'district',
            'metro',
            'square',
            'square_max',
            'living_square',
            'living_square_max',
            'kitchen_square',
            'kitchen_square_max',
            # 'rooms',
            'price',
            'min_price',
            'refrigerator',
            'washer',
            'tv',
            'phone',
            'internet',
            'conditioner',
            'furniture',
            'euroremont',
            'separate_wc',
            'balcony',
            'lift',
            'parking',
            'redecoration',
            'no_remont',
            'need_remont',
            'electric',
            'gas',
            'water',
            'sewage',
            'brick_building',
            'wood_building',
            'live_one',
            'live_two',
            'live_pare',
            'live_more',
            'live_child',
            'live_animal',
            'live_girl',
            'live_man',
            'concierge',
            'guard',
            'garage',
            'floor',
            'floor_max',
            'owner_name',
            'owner_tel',
            'owner_email',
            'country',
            'commercial',
            'territory',
            'live',
            # 'live_room',
            'live_flat1',
            'live_flat2',
            'live_flat3',
            'live_flat4',
            'limit',
            'period',
            'from_agent',
            'from_owner'
        ]
        widgets = {
            'metro': MetroMultipleWidget(),
            'district': SelectMultipleWidget(),
            'refrigerator': OptionWidget(label='Холодильник'),
            'washer': OptionWidget(label='Стиральная машина'),
            'tv': OptionWidget(label='Телевизор'),
            'phone': OptionWidget(label='Телефон'),
            'internet': OptionWidget(label='Интернет'),
            'conditioner': OptionWidget(label='Кондиционер'),
            'furniture': OptionWidget(label='Мебель'),
            'euroremont': OptionWidget(label='Евроремонт'),
            'separate_wc': OptionWidget(label='Раздельный санузел'),
            'balcony': OptionWidget(label='Балкон'),
            'lift': OptionWidget(label='Лифт'),
            'parking': OptionWidget(label='Парковка'),
            'floor': forms.TextInput(attrs={'placeholder': 'от'}),
            'floor_max': forms.TextInput(attrs={'placeholder': 'до'}),
            'square': forms.TextInput(attrs={'placeholder': 'от'}),
            'square_max': forms.TextInput(attrs={'placeholder': 'до'}),
            'living_square': forms.TextInput(attrs={'placeholder': 'от', 'class': 'for_flat for_room for_house for_commercial'}),
            'living_square_max': forms.TextInput(attrs={'placeholder': 'до', 'class': 'for_flat for_room for_house for_commercial'}),
            'kitchen_square': forms.TextInput(attrs={'placeholder': 'от', 'class': 'for_flat for_room for_house for_commercial'}),
            'kitchen_square_max': forms.TextInput(attrs={'placeholder': 'до', 'class': 'for_flat for_room for_house for_commercial'}),
            'price': forms.TextInput(attrs={'placeholder': 'до'}),
            'min_price': forms.TextInput(attrs={'placeholder': 'от'}),
            'country': RadioButtonWidget(),
            'commercial': RadioButtonWidget(),
            'territory': RadioButtonWidget(),
            'live': RadioButtonWidget(),
            'redecoration': OptionWidget(label='Косм.ремонт'),
            'no_remont': OptionWidget(label='Нет ремонта'),
            'need_remont': OptionWidget(label='Нужен ремонт'),
            'electric': OptionWidget(label='Электричество'),
            'gas': OptionWidget(label='Газ'),
            'water': OptionWidget(label='Вода'),
            'sewage': OptionWidget(label='Канализация'),
            'brick_building': OptionWidget(label='Кирпичная постройка'),
            'wood_building': OptionWidget(label='Деревянная постройка'),
            'live_one': OptionWidget(label='Одному чел.'),
            'live_two': OptionWidget(label='Двум людям'),
            'live_pare': OptionWidget(label='Семейной паре'),
            'live_more': OptionWidget(label='Более 2-х чел.'),
            'live_child': OptionWidget(label='Можно с детьми'),
            'live_animal': OptionWidget(label='Можно с животными'),
            'live_girl': OptionWidget(label='Для девушек'),
            'live_man': OptionWidget(label='Для мужчин'),
            'concierge': OptionWidget(label='Консьерж'),
            'guard': OptionWidget(label='Охрана'),
            'garage': OptionWidget(label='Гараж'),
            'limit': RadioButtonWidget(),
            'body': forms.Textarea(attrs={'rows': 5})
        }

    def __init__(self, filter_town=None, check_tel=False, *args, **kwargs):
        super(SearchRequestForm_Client, self).__init__(*args, **kwargs)
        self.fields['metro'].choices = [(str(metro.id), metro.title) for metro in Metro.objects.filter(town=filter_town)]
        self.fields['metro'].widget.town = filter_town
        self.fields['metro'].required = False
        self.fields['district'].choices = [(str(district.id), district.title) for district in District.objects.filter(town=filter_town)]
        self.fields['country'].required = False
        self.fields['commercial'].required = False
        self.fields['territory'].required = False
        self.fields['owner_tel'].widget.attrs['class'] = 'masked-phone ' + self.fields['owner_tel'].widget.attrs.get('class', '')
        self.fields['limit'].choices = [(Advert.LIMIT_DAY, 'посуточно'), (Advert.LIMIT_LONG, 'длительно')]
        self.fields['owner_email'].required = True
        self.fields['owner_email'].error_messages = {'required': 'Введите Email клиента'}

    def clean_owner_tel(self):
        return clear_tel(self.cleaned_data['owner_tel'])


class UserWeekPermForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ['is_active']

    def __init__(self, user, *args, **kwargs):
        super(UserWeekPermForm, self).__init__(*args, **kwargs)
        for day in xrange(1, 8):
            self.fields['day%s_min_hour' % day] = forms.IntegerField(initial=0, required=False)
            self.fields['day%s_max_hour' % day] = forms.IntegerField(initial=24, required=False)
            self.fields['day%s_active' % day] = forms.BooleanField(initial=True, label='Активен', required=False)

        self.fields['enable_perms'] = forms.MultipleChoiceField(choices=[(perm.id, perm.title) for perm in user.get_perms()],
                                                                 widget=RadioMultipleSelectWidget(),
                                                                 required=False)


class Agent24PermsForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ['agent24_view_owner', 'agent24_view_company']

    def __init__(self, user, *args, **kwargs):
        super(Agent24PermsForm, self).__init__(*args, **kwargs)
        self.fields['enable_perms'] = forms.MultipleChoiceField(choices=[(perm[0], perm[1]) for perm in user.get_agent24_perms().items()],
                                                                 widget=RadioMultipleSelectWidget(),
                                                                 required=False)


class PromoForm(BootstrapFormMixin, forms.Form):
    code = forms.CharField(label='Промокод', required=True)
    payment = forms.IntegerField(widget=forms.HiddenInput(), required=True)


class PromotionForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Promotion
        fields = [
            'site',
            'title',
            'start_date',
            'end_date',
            'discount',
            'prefix'
        ]
        widgets = {
            'start_date': DatepickerWidget(),
            'end_date': DatepickerWidget()
        }


class PromocodeForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Promocode
        fields = [
            'promotion',
            'code',
            'user'
        ]
        widgets = {
            'user': UserWidget()
        }


class ReferralForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Referral
        fields = [
            'user',
            'code',
            'site'
        ]
        widgets = {
            'user': UserWidget()
        }


class ReferralFilterForm(BootstrapFormMixin, forms.Form):
    start_date = forms.DateTimeField(label='Начальная дата', widget=DatepickerWidget(), required=False)
    end_date = forms.DateTimeField(label='Конечная дата', widget=DatepickerWidget(), required=False)


class DeliveryFilterForm(BootstrapFormMixin, forms.Form):
    username = forms.CharField(label='Имя пользователя', required=False)
    email = forms.CharField(label='E-mail', required=False)
    site = forms.ChoiceField(label='Сайт', required=False)

    def __init__(self, *args, **kwargs):
        super(DeliveryFilterForm, self).__init__(*args, **kwargs)
        self.fields['site'].choices = [(0, 'Любой')] + [(site.id, site.name) for site in Site.objects.all()]