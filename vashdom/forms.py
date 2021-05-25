# -*- coding: utf-8 -*-
from django import forms
from gutils.forms import BootstrapFormMixin
from main.models import Advert, Metro, District, Town, clear_tel, SearchRequest
from main.form import MetroMultipleWidget, RoomMultipleWidget, Btn8RadioButtonWidget, \
    MetroWidget, DistrictWidget, OptionWidget, RadioSelectWidget, SelectMultipleWidget, \
    DatepickerWidget, UserWidget
from uimg.forms import MultiUploadImageWidget
from registration.forms import RegistrationForm
from uprofile.models import User
from vashdom.models import Tariff, Password, VashdomUser
from django.core.exceptions import ValidationError
from django.template import loader, Context


class TownWidget(forms.Select):
    def render(self, name, value, attrs=None, choices=()):
        tmpl = loader.get_template('vashdom/block/town-widget.html')
        town_bases = {}
        for town in Town.objects.filter(id__in=[choice[0] for choice in self.choices]).order_by('title'):
            town_bases[town.id] = {'main_base': town.main_base, 'vk_base': town.vk_base}

        return tmpl.render(Context({
            'attrs': attrs,
            'name': name,
            'value': value,
            'choices': self.choices,
            'town_bases': town_bases,
            'select': super(TownWidget, self).render(name, value, attrs=attrs, choices=choices)
            }))


class RegisterForm(BootstrapFormMixin, RegistrationForm):
    """
    Форма регистрации
    """

    username = forms.EmailField(label="Имя пользователя", error_messages={'required': 'Введите имя пользователя'})
    tel = forms.CharField(label='Телефон', required=False, widget=forms.TextInput(attrs={'class': 'masked-phone'}))
    # captcha = ReCaptchaField(label='Введите текст с картинки')
    tariff = forms.ChoiceField(label='Тариф', required=True, error_messages={'required': 'Выберите тариф'})
    town = forms.ChoiceField(label='Город', required=True, error_messages={'required': 'Выберите город'},
                             widget=TownWidget())

    agree = forms.BooleanField(label='Я согласен с условиями', error_messages={
        'required': 'Вы не приняли условия работы сервиса'
    })

    def __init__(self, town=None, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['username'].help_text = 'Указывайте существующий адрес, на него будет выслано подтверждение регистрации'
        self.fields['password1'].help_text = 'Пароль может состоять из букв латинского алфавита и цифр, длина пароля не менее 6-ти символов'
        self.fields['password1'].label = 'Пароль *'
        self.fields['password2'].label = 'Пароль (еще раз) *'
        self.fields['password1'].error_messages['required'] = 'Введите пароль'
        self.fields['password2'].error_messages['required'] = 'Введите подтверждение пароля'
        self.fields['tariff'].choices = [(tariff.id, tariff.title) for tariff in Tariff.objects.filter(hidden=False)]
        self.fields['town'].choices = [(t.id, t.title) for t in Town.objects.all().order_by('order')]
        if town:
            self.fields['town'].initial = town.id

    def clean_email(self):
        if VashdomUser.objects.filter(username=self.data['username']):
            raise ValidationError(u'Это имя пользователя уже зарегистрировано')
        return self.data['username']

    def clean_tel(self):
        from main.models import clear_tel
        return clear_tel(self.cleaned_data['tel'])


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'tel']

    def clean_tel(self):
        from main.models import clear_tel
        return clear_tel(self.cleaned_data['tel'])


class AvatarForm(forms.Form):
    image = forms.ImageField()


class FilterAdvertForm(BootstrapFormMixin, forms.Form):

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
    metro = forms.MultipleChoiceField(label='Метро', widget=SelectMultipleWidget())
    # district = forms.ChoiceField(label='Район', widget=DistrictWidget())
    min_price = forms.IntegerField(label='Цены от', widget=forms.TextInput(attrs={'placeholder': 'от'}))
    max_price = forms.IntegerField(label='Цены до', widget=forms.TextInput(attrs={'placeholder': 'до'}))
    rooms = forms.MultipleChoiceField(label='Кол-во комнат', widget=RoomMultipleWidget(), choices=ROOMS)

    # дата
    date = forms.ChoiceField(label='Дата', choices=DATES, required=False, widget=forms.Select())
    # archive = forms.BooleanField(label='Архив', widget=forms.CheckboxInput())

    # площадь
    # min_square = forms.IntegerField(label='Площадь от', widget=forms.TextInput(attrs={'placeholder': 'от'}), required=False)
    # max_square = forms.IntegerField(label='Площадь до', widget=forms.TextInput(attrs={'placeholder': 'до'}), required=False)

    with_photo = forms.BooleanField(label='Только с фото', initial=False)

    refrigerator = forms.BooleanField(label='Холодильник', required=False)
    tv = forms.BooleanField(label='Телевизор', required=False)
    washer = forms.BooleanField(label='Стиральная машина', required=False)
    furniture = forms.BooleanField(label='Мебель', required=False)

    # map = forms.BooleanField(required=False, widget=forms.HiddenInput())

    def __init__(self, town, *args, **kwargs):
        super(FilterAdvertForm, self).__init__(*args, **kwargs)
        self.fields['metro'].choices = [(str(metro.id), metro.title) for metro in Metro.objects.filter(town=town)]
        # self.fields['district'].choices = [(0, 'Любой')] + [(district.id, district.title) for district in District.objects.filter(town=town)]
        self.fields['metro'].widget.town = town


class FilterVKAdvertForm(BootstrapFormMixin, forms.Form):

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
    metro = forms.MultipleChoiceField(label='Метро', widget=SelectMultipleWidget())
    district = forms.MultipleChoiceField(label='Район', widget=SelectMultipleWidget())
    min_price = forms.IntegerField(label='Цены от', widget=forms.TextInput(attrs={'placeholder': 'от'}))
    max_price = forms.IntegerField(label='Цены до', widget=forms.TextInput(attrs={'placeholder': 'до'}))
    rooms = forms.MultipleChoiceField(label='Кол-во комнат', widget=RoomMultipleWidget(), choices=ROOMS)

    # дата
    # date = forms.ChoiceField(label='Дата', choices=DATES, required=False, widget=forms.Select())
    # archive = forms.BooleanField(label='Архив', widget=forms.CheckboxInput())

    # площадь
    # min_square = forms.IntegerField(label='Площадь от', widget=forms.TextInput(attrs={'placeholder': 'от'}), required=False)
    # max_square = forms.IntegerField(label='Площадь до', widget=forms.TextInput(attrs={'placeholder': 'до'}), required=False)

    # with_photo = forms.BooleanField(label='Только с фото', initial=False)

    def __init__(self, town, *args, **kwargs):
        super(FilterVKAdvertForm, self).__init__(*args, **kwargs)
        self.fields['metro'].choices = [(str(metro.id), metro.title) for metro in Metro.objects.filter(town=town)]
        self.fields['district'].choices = [(str(district.id), district.title) for district in District.objects.filter(town=town)]


class PaymentOrderForm(BootstrapFormMixin, forms.Form):
    tariff = forms.ChoiceField(label='Тариф', required=True, error_messages={'required': 'Выберите тариф'})
    # count = forms.ChoiceField(label='Кол-во объявлений', required=False,
    #                           initial=10, choices=[(x, u'%s объявл. x 10 руб.'%x) for x in xrange(10, 110, 10)])
    town = forms.ChoiceField(label='Город', required=True, error_messages={'required': 'Выберите город'},
                             widget=TownWidget())
    tel = forms.CharField(label='Телефон', max_length=20, required=False, error_messages={'required': 'Введите телефон'},
                          widget=forms.TextInput(attrs={'class': 'masked-phone', 'placeholder': 'Номер телефона'}))
    email = forms.EmailField(label='Электронная почта', max_length=20, required=False,
                          widget=forms.TextInput(attrs={'placeholder': 'Электронная почта'}))

    def __init__(self, town=None, user=None, *args, **kwargs):
        super(PaymentOrderForm, self).__init__(*args, **kwargs)
        self.fields['tariff'].choices = [(tariff.id, tariff.title) for tariff in Tariff.objects.filter(hidden=False)]
        self.fields['town'].choices = [(t.id, t.title) for t in Town.objects.filter(
            slug__in=['moskva', 'sankt-peterburg', 'ekaterinburg', 'novosibirsk']
        ).order_by('order')]
        if town:
            self.fields['town'].initial = town.id
        if user:
            self.fields['tel'].initial = user.tel

    def clean_tel(self):
        data = self.cleaned_data['tel']
        return clear_tel(data)

    # def clean_count(self):
    #     data = self.cleaned_data['count']
    #     try:
    #         tariff = Tariff.objects.get(id=self.cleaned_data['tariff'])
    #     except:
    #         tariff = None
    #     if tariff:
    #         if tariff.tariff_type == Tariff.TYPE_COUNT and not data:
    #             raise ValidationError(u'Выберите количество объявлений', code='required')
    #     return data


class AdvertForm(BootstrapFormMixin, forms.ModelForm):

    ROOMS = [
        ('R', 'Комнату'),
        ('1', '1 комн.квартиру'),
        ('2', '2 комн.квартиру.'),
        ('3', '3 комн.квартиру'),
        ('4', '4+ комн.квартиру'),
        ]

    # type = forms.ChoiceField(label='Я хочу', widget=Btn8RadioButtonWidget(), choices=(
    #     ('LS', u'Я хочу Сдать'),
    #     ('LD', u'Я хочу Снять'),
    # ), error_messages={'required': 'Выберите операцию СДАТЬ  | СНЯТЬ '}, initial='LS')
    agree = forms.BooleanField(label='Я согласен с условиями', error_messages={
        'required': 'Вы не приняли условия работы сервиса заявок'
    })
    rooms_ext = forms.ChoiceField(label='Я хочу сдать', choices=ROOMS, initial='1')

    class Meta:
        model = Advert
        fields = [
            'body',
            'images',
            'town',
            'address',
            'district',
            'metro',
            'square',
            'living_square',
            'kitchen_square',
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
            # 'limit'
        ]
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5}),
            'address': forms.TextInput(),
            'metro': MetroWidget(),
            'district': DistrictWidget(),
            'images': MultiUploadImageWidget(),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            # 'refrigerator': OptionWidget(label='Холодильник'),
            # 'washer': OptionWidget(label='Стиральная машина'),
            # 'tv': OptionWidget(label='Телевизор'),
            # 'phone': OptionWidget(label='Телефон'),
            # 'internet': OptionWidget(label='Интернет'),
            # 'conditioner': OptionWidget(label='Кондиционер'),
            # 'furniture': OptionWidget(label='Мебель'),
            # 'euroremont': OptionWidget(label='Евроремонт'),
            # 'separate_wc': OptionWidget(label='Раздельный санузел'),
            # 'balcony': OptionWidget(label='Балкон'),
            # 'lift': OptionWidget(label='Лифт'),
            # 'parking': OptionWidget(label='Парковка'),
            # 'redecoration': OptionWidget(label='Косм.ремонт'),
            # 'no_remont': OptionWidget(label='Нет ремонта'),
            # 'need_remont': OptionWidget(label='Нужен ремонт'),
            # 'electric': OptionWidget(label='Электричество'),
            # 'gas': OptionWidget(label='Газ'),
            # 'water': OptionWidget(label='Вода'),
            # 'sewage': OptionWidget(label='Канализация'),
            # 'brick_building': OptionWidget(label='Кирпичная постройка'),
            # 'wood_building': OptionWidget(label='Деревянная постройка'),
            # 'live_one': OptionWidget(label='Одному чел.'),
            # 'live_two': OptionWidget(label='Двум людям'),
            # 'live_pare': OptionWidget(label='Семейной паре'),
            # 'live_more': OptionWidget(label='Более 2-х чел.'),
            # 'live_child': OptionWidget(label='Можно с детьми'),
            # 'live_animal': OptionWidget(label='Можно с животными'),
            # 'live_girl': OptionWidget(label='Для девушек'),
            # 'live_man': OptionWidget(label='Для мужчин'),
            # 'concierge': OptionWidget(label='Консьерж'),
            # 'guard': OptionWidget(label='Охрана'),
            # 'garage': OptionWidget(label='Гараж'),
            'price': forms.TextInput(),
            'square': forms.TextInput(attrs={'placeholder': 'Общая'}),
            'living_square': forms.TextInput(attrs={'placeholder': 'Жилая'}),
            'kitchen_square': forms.TextInput(attrs={'placeholder': 'Кухни'}),
            # 'limit': Btn8RadioButtonWidget(),
        }

        error_messages = {
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
        self.fields['town'].choices = [(town.id, town.title) for town in Town.objects.filter(main_base=True)]
        self.fields['metro'].queryset = self.fields['metro'].queryset.filter(town=filter_town)
        self.fields['district'].queryset = self.fields['district'].queryset.filter(town=filter_town)
        self.fields['owner_name'].required = True
        self.fields['owner_tel'].required = True
        self.fields['owner_tel'].widget.attrs['class'] = 'masked-phone ' + self.fields['owner_tel'].widget.attrs.get('class', '')
        # self.fields['limit'].choices = [(Advert.LIMIT_DAY, 'посуточно'), (Advert.LIMIT_LONG, 'длительно')]

    def clean_owner_tel(self):
        return clear_tel(self.cleaned_data['owner_tel'])


class FeedbackForm(BootstrapFormMixin, forms.Form):
    body = forms.CharField(label='Текст вопроса', widget=forms.Textarea(attrs={'rows': 5}), error_messages={'required': 'Введите текст сообщения'})
    name = forms.CharField(label='Имя отправителя', error_messages={'required': 'Введите имя отправителя'})
    tel = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'masked-phone'}), error_messages={'required': 'Введите телефон'}, required=False)
    email = forms.EmailField(label='Email', error_messages={'required': 'Введите E-mail'})
    town = forms.ChoiceField(label='Город', widget=TownWidget(), error_messages={'required': 'Выберите город'})

    def __init__(self, town=None, initial=None, *args, **kwargs):
        if not initial:
            initial = {}
        initial['town'] = town.id
        super(FeedbackForm, self).__init__(initial=initial, *args, **kwargs)
        self.fields['town'].choices = [(town.id, town.title) for town in Town.objects.all().order_by('order')]
        self.fields['town'].initial = town.id if town else None


class PasswordForm(BootstrapFormMixin, forms.ModelForm):
    generate = forms.BooleanField(label='Сгенерировать новый пароль', required=False)
    sms = forms.BooleanField(label='Отправить СМС', required=False)

    class Meta:
        model = Password
        fields = [
            'password',
            'start_date',
            'end_date',
            'count',
            'town',
            'tel',
            'user',
            'main_base',
            'vk_base'
        ]
        widgets = {
            'start_date': DatepickerWidget(),
            'end_date': DatepickerWidget(),
            'user': UserWidget(site_id=VashdomUser.SITE_ID)
        }

    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        self.fields['password'].required = False

    def clean_tel(self):
        return clear_tel(self.cleaned_data['tel'])


class PaymentAlertForm(BootstrapFormMixin, forms.Form):
    town = forms.ChoiceField(label='Город', widget=TownWidget(), error_messages={'required': 'Выберите город'})
    date = forms.DateField(label='Дата оплаты', widget=DatepickerWidget(), error_messages={'required': 'Укажите дату оплаты'})
    hour = forms.ChoiceField(label='Час оплаты', choices=[(h, h) for h in xrange(0, 25)], error_messages={'required': 'Укажите час оплаты'})
    minute = forms.ChoiceField(label='Минута оплаты', choices=[(h, h) for h in xrange(0, 60)], error_messages={'required': 'Укажите минуту оплаты'})
    sum = forms.IntegerField(label='Сумма к зачислению без комиссии', widget=forms.TextInput(), error_messages={'required': 'Укажите сумму к зачислению'})
    receiver = forms.CharField(label='Куда совершен платеж', error_messages={'required': 'Укажите сумму к зачислению'})
    tel = forms.CharField(label='Ваш телефон', widget=forms.TextInput(attrs={'class': 'masked-phone'}), error_messages={'required': 'Укажите телефон для смс'})
    name = forms.CharField(label='Имя отправителя', error_messages={'required': 'Введите ваше имя'})
    email = forms.EmailField(label='Email', error_messages={'required': 'Введите ваш E-mail'})


    def __init__(self, town=None, initial=None, *args, **kwargs):
        if not initial:
            initial = {}
        initial['town'] = town.id
        super(PaymentAlertForm, self).__init__(initial=initial, *args, **kwargs)
        self.fields['town'].choices = [(town.id, town.title) for town in Town.objects.all().order_by('order')]
        self.fields['town'].initial = town.id if town else None


class SearchRequestForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = SearchRequest
        fields = [
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
            'live',
            # 'live_room',
            'live_flat1',
            'live_flat2',
            'live_flat3',
            'live_flat4',
        ]
        widgets = {
            'metro': SelectMultipleWidget(),
            'district': SelectMultipleWidget(),
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
        }

    def __init__(self, filter_town=None, check_tel=False, *args, **kwargs):
        super(SearchRequestForm, self).__init__(*args, **kwargs)
        self.fields['metro'].choices = [(str(metro.id), metro.title) for metro in Metro.objects.filter(town=filter_town)]
        self.fields['metro'].widget.town = filter_town
        self.fields['metro'].required = False
        self.fields['district'].choices = [(str(district.id), district.title) for district in District.objects.filter(town=filter_town)]
        self.fields['owner_tel'].required = False
        self.fields['owner_tel'].widget.attrs['class'] = 'masked-phone ' + self.fields['owner_tel'].widget.attrs.get('class', '')
        self.fields['owner_email'].required = True
        self.fields['owner_email'].error_messages = {'required': 'Введите Email'}

    def clean_owner_tel(self):
        return clear_tel(self.cleaned_data['owner_tel'])


class SearchRequestSimpleForm(BootstrapFormMixin, forms.Form):
    email = forms.EmailField(label='Ваш Email', error_messages={'required': u'Введите Email', 'invalid': 'Неверный Email'})
    catalog_id = forms.IntegerField(widget=forms.HiddenInput())