#-*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, DeleteView
from uprofile.models import User
from django.contrib.auth.models import Group
from gutils.views import BreadcrumbMixin, AjaxableResponseMixin, AjaxPageMixin
from django.core.urlresolvers import reverse
from gutils.views import class_view_decorator
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from annoying.decorators import ajax_request
from main.form import UserForm, UserForm_User, UserFilterForm, UserWeekPermForm
from main.models import Advert, Company, clear_tel_list, WeekPerm, Perm, RegViewed
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from main.views.private import ClientPermMixin
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from mail_templated import send_mail
from django.contrib.sites.models import Site
from vashdom.models import VashdomUser


class UserDetailView(BreadcrumbMixin, DetailView):
    model = User
    template_name = 'main/user/detail.html'
    context_object_name = 'object'

    def get_breadcrumbs(self):
        breadcrumbs = [
            ('Агентства недвижимости', reverse('company:list'))
        ]
        if self.object.company:
            breadcrumbs.append((self.object.company.title, self.object.company.get_absolute_url))
        breadcrumbs.append((self.object.get_full_name(), reverse('user:detail', kwargs={'pk': self.object.id})))
        return super(UserDetailView, self).get_breadcrumbs() + breadcrumbs

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['count_adverts'] = Advert.objects.filter(user=self.object, status=Advert.STATUS_VIEW).count()
        context['advert_list'] = self.object.advert_set.filter(status=Advert.STATUS_VIEW).order_by('-date')[:8]
        return context


class UserReviewsView(BreadcrumbMixin, DetailView):
    model = User
    template_name = 'main/user/reviews.html'
    context_object_name = 'object'

    def get_breadcrumbs(self):
        breadcrumbs = [
            ('Агентства недвижимости', reverse('company:list'))
        ]
        if self.object.company:
            breadcrumbs.append((self.object.company.title, self.object.company.get_absolute_url))
        breadcrumbs.append((self.object.get_full_name(), reverse('user:detail', kwargs={'pk': self.object.id})))
        breadcrumbs.append(('Отзывы об агенте', reverse('user:reviews', kwargs={'pk': self.object.id})))
        return super(UserReviewsView, self).get_breadcrumbs() + breadcrumbs

    def get_context_data(self, **kwargs):
        context = super(UserReviewsView, self).get_context_data(**kwargs)
        context['count_adverts'] = Advert.objects.filter(user=self.object, status=Advert.STATUS_VIEW).count()
        return context


# CLIENT PART
@class_view_decorator(permission_required('uprofile.view_user'))
class UserListView_Client(ClientPermMixin, BreadcrumbMixin, ListView):
    """
    Список агентов
    """
    model = User
    context_object_name = 'user_list'
    paginate_by = 50
    template_name = 'main/client/user/page.html'

    def get_breadcrumbs(self):
        return super(UserListView_Client, self).get_breadcrumbs() + [('Пользователи', reverse('client:user:list'))]

    def get_queryset(self):
        query = Q()
        if self.request.GET.get('status') in User.STATUSES:
            query &= Q(status=self.request.GET.get('status'))
        if self.request.REQUEST.get('username'):
            query &= Q(username__icontains=self.request.REQUEST.get('username'))
        if self.request.REQUEST.get('email'):
            query &= (Q(email__icontains=self.request.REQUEST.get('email')) | Q(agent_email__icontains=self.request.REQUEST.get('email')))
        if self.request.REQUEST.get('tel'):
            query &= Q(tel__icontains=clear_tel_list(self.request.REQUEST.get('tel')))
        if self.request.REQUEST.get('company'):
            company_list = Company.objects.filter(id=self.request.REQUEST.get('company'))
            if company_list:
                query &= Q(company=company_list[0])
        if self.request.REQUEST.get('site'):
            site_list = Site.objects.filter(id=self.request.REQUEST.get('site'))
            if site_list:
                query &= Q(site=site_list[0])
        if self.request.REQUEST.get('moderator'):
            query &= (Q(groups__name='Модератор') | Q(groups__name='Старший модератор'))
        return User.admin_objects.filter(query).order_by('first_name').select_related('company')

    def get_context_data(self, **kwargs):
        context = super(UserListView_Client, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('uprofile.change_user')
        context['filter_form'] = UserFilterForm(data=self.request.REQUEST)
        return context


class UserDetailView_Client(ClientPermMixin, BreadcrumbMixin, AjaxPageMixin, DetailView):
    model = User
    template_name = 'main/client/user/detail.html'
    template_name_ajax = 'main/client/user/detail-ajax.html'
    queryset = User.admin_objects.all()
    context_object_name = 'object'

    def get_breadcrumbs(self):
        return super(UserDetailView_Client, self).get_breadcrumbs() + [
            ('Пользователи', reverse('client:user:list')),
            (self.object.get_full_name(), reverse('client:user:detail', kwargs={'pk': self.object.id}))
        ]

    def get_context_data(self, **kwargs):
        context = super(UserDetailView_Client, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('uprofile.change_user')
        context['count_adverts'] = Advert.objects.filter(user=self.object).count()
        context['count_adverts_images'] = Advert.objects.filter(user=self.object).exclude(images=None).count()
        return context


class UserPreviewView_Client(ClientPermMixin, DetailView):
    model = User
    template_name = 'main/client/user/preview.html'

    def get_context_data(self, **kwargs):
        context = super(UserPreviewView_Client, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('uprofile.change_user')
        return context


@class_view_decorator(permission_required('main.add_user'))
class UserCreateView_Client(ClientPermMixin, AjaxableResponseMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'main/client/user/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(UserCreateView_Client, self).get_context_data(**kwargs)
        context['action'] = reverse('client:user:create')
        return context

    def form_valid(self, form):
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        if password1 != password2:
            raise Exception(u'Пароль и подтверждение не совпадают')
        form.instance.set_password(password1)
        form.instance.gen_access_code()

        result = super(UserCreateView_Client, self).form_valid(form)

        #активация тарифов для новых юзеров
        # if form.instance.company:
        #     for service in form.instance.company.connectedservice_set.filter(active=True):
        #         service.tariff.activate(form.instance)

        return result

    def get_model_dict(self):
        return {
            'url': reverse('client:user:detail', kwargs={'pk': self.object.id})
        }


@class_view_decorator(permission_required('uprofile.change_user'))
class UserUpdateView_Client(ClientPermMixin, AjaxableResponseMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'main/client/user/form.html'
    success_url = '/'
    queryset = User.admin_objects.all()

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView_Client, self).get_context_data(**kwargs)
        context['action'] = reverse('client:user:edit', kwargs={'pk': self.object.id})
        return context

    def get_form_kwargs(self):
        kwargs = super(UserUpdateView_Client, self).get_form_kwargs()
        if self.object.company:
            kwargs['initial'] = {
                'company': self.object.company.id
            }
        return kwargs

    def form_valid(self, form):
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        if password1 or password2:
            if password1 != password2:
                raise Exception(u'Пароль и подтверждение не совпадают')
            form.instance.set_password(password1)
        if not form.instance.agent24_code:
            form.instance.gen_access_code()
        return super(UserUpdateView_Client, self).form_valid(form)

    def get_model_dict(self):
        return {
            'url': reverse('client:user:detail', kwargs={'pk': self.object.id})
        }


@class_view_decorator(permission_required('uprofile.delete_user'))
class UserDeleteView_Client(ClientPermMixin, AjaxableResponseMixin, DeleteView):
    model = User
    success_url = '/'
    queryset = User.admin_objects.all()

    def delete(self, request, *args, **kwargs):
        if self.get_object().id == request.user.id:
            raise Exception(u'Нельзя удалить свой аккаунт')
        return super(UserDeleteView_Client, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        return {
            'url': reverse('client:user:list')
        }


class UserCreatePermMixin(object):
    def dispatch(self, request, *args, **kwargs):
        company = request.user.company
        if company and (company.owner == request.user):
            return super(UserCreatePermMixin, self).dispatch(request, *args, **kwargs)
        return HttpResponseForbidden()


class UserUpdatePermMixin(object):
    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        company = user.company
        if company and (company.owner == request.user):
            return super(UserUpdatePermMixin, self).dispatch(request, *args, **kwargs)
        return HttpResponseForbidden()


class UserDeletePermMixin(object):
    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        company = user.company
        if company and (company.owner == request.user):
            return super(UserDeletePermMixin, self).dispatch(request, *args, **kwargs)
        return HttpResponseForbidden()


class UserCreateView_User(UserCreatePermMixin, AjaxableResponseMixin, CreateView):
    model = User
    success_url = '/'
    template_name = 'main/client/user/less/form.html'
    form_class = UserForm_User

    def get_form_kwargs(self):
        kwargs = super(UserCreateView_User, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(UserCreateView_User, self).get_context_data(**kwargs)
        context['action'] = reverse('client:company:user-create')
        return context

    def form_valid(self, form):
        form.instance.email = form.instance.username
        form.instance.company = self.request.user.company
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        if password1 or password2:
            if password1 != password2:
                raise Exception(u'Пароль и подтверждение не совпадают')
            form.instance.set_password(password1)
        form.instance.gen_access_code()
        return super(UserCreateView_User, self).form_valid(form)

    def get_model_dict(self):
        return {
            'url': reverse('client:user:detail', kwargs={'pk': self.object.id})
        }


class UserUpdateView_User(UserUpdatePermMixin, AjaxableResponseMixin, UpdateView):
    model = User
    success_url = '/'
    template_name = 'main/client/user/less/form.html'
    form_class = UserForm_User

    def get_form_kwargs(self):
        kwargs = super(UserUpdateView_User, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView_User, self).get_context_data(**kwargs)
        context['action'] = reverse('client:company:user-edit', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        form.instance.email = form.instance.username
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        if password1 or password2:
            if password1 != password2:
                raise Exception(u'Пароль и подтверждение не совпадают')
            form.instance.set_password(password1)
        return super(UserUpdateView_User, self).form_valid(form)

    def get_model_dict(self):
        return {
            'url': reverse('client:user:detail', kwargs={'pk': self.object.id})
        }


class UserDeleteView_User(UserDeletePermMixin, AjaxableResponseMixin, DeleteView):
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        if self.get_object().id == request.user.id:
            raise Exception(u'Нельзя удалить свой аккаунт')
        return super(UserDeleteView_User, self).delete(request, *args, **kwargs)

    def get_model_dict(self):
        company = self.request.user.owner.all()[0]
        return {
            'url': reverse('client:company:agents', kwargs={'pk': company.id})
        }


class UserPermsView_User(UserUpdatePermMixin, BreadcrumbMixin, AjaxableResponseMixin, UpdateView):
    model = User
    success_url = '/'
    template_name = 'main/client/user/perms.html'
    form_class = UserWeekPermForm
    queryset = User.admin_objects.all()
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super(UserPermsView_User, self).get_context_data(**kwargs)
        context['action'] = reverse('client:company:user-perms', kwargs={'pk': self.object.id})
        context['week_range'] = range(1, 8)
        return context

    def get_form_kwargs(self):
        kwargs = super(UserPermsView_User, self).get_form_kwargs()
        perm_list = self.object.weekperm_set.all()
        initial = {}
        for perm in perm_list:
            initial['day%s_min_hour' % perm.day] = perm.min_hour
            initial['day%s_max_hour' % perm.day] = perm.max_hour
            initial['day%s_active' % perm.day] = perm.active
        initial['enable_perms'] = [perm.id for perm in self.object.get_active_perms()]
        kwargs['initial'] = initial
        kwargs['user'] = self.object
        return kwargs

    def form_valid(self, form):
        user = form.instance
        if user.independent:
            raise Exception(u'Агент работает как независимый. Нельзя изменить настройки доступа.')

        for day in xrange(1, 8):
            perm_list = user.weekperm_set.filter(day=day)
            if perm_list:
                perm = perm_list[0]
            else:
                perm = WeekPerm(user=user, day=day)
            perm.min_hour = form.cleaned_data.get('day%s_min_hour' % day, 0)
            perm.max_hour = form.cleaned_data.get('day%s_max_hour' % day, 0)
            perm.active = form.cleaned_data.get('day%s_active' % day, True)
            perm.save()

        user.enable_perms.clear()
        perm_list = user.get_perms().filter(id__in=form.cleaned_data['enable_perms'])
        user.enable_perms.add(*perm_list)

        return super(UserPermsView_User, self).form_valid(form)

    def get_model_dict(self):
        return {
            'message': 'Ограничения доступа сохранены'
        }

    def get_breadcrumbs(self):
        return super(UserPermsView_User, self).get_breadcrumbs() + [
            ('Настройки', reverse('client:company:my')),
            (u'Ограничения доступа %s' % self.object.get_full_name(), reverse('client:company:user-perms', kwargs={'pk': self.object.id}))
        ]


@class_view_decorator(permission_required('main.change_user'))
class UserStatusView_Client(ClientPermMixin, View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserStatusView_Client, self).dispatch(request, *args, **kwargs)

    @method_decorator(ajax_request)
    def post(self, request, *args, **kwargs):
        user = User.admin_objects.get(id=kwargs['pk'])
        if User.STATUSES.has_key(request.GET.get('status')):
            user.status = request.GET.get('status')
            user.save()

        return {
            'id': user.id
        }


@class_view_decorator(permission_required('uprofile.view_user'))
class UserServicesListView_Client(ClientPermMixin, BreadcrumbMixin, ListView):
    model = User
    template_name = 'main/client/user/services.html'
    context_object_name = 'service_list'
    user = None

    def get(self, request, *args, **kwargs):
        self.user = get_object_or_404(User.admin_objects.all(), id=kwargs['pk'])
        return super(UserServicesListView_Client, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.user.connectedservice_set.all().order_by('-end_date')

    def get_context_data(self, **kwargs):
        context = super(UserServicesListView_Client, self).get_context_data(**kwargs)
        context['agent'] = self.user
        return context

    def get_breadcrumbs(self):
        return super(UserServicesListView_Client, self).get_breadcrumbs() + [
            ('Пользователи', reverse('client:user:list')),
            (self.user.get_full_name(), reverse('client:user:detail', kwargs={'pk': self.user.id})),
            ('Подключенные услуги', reverse('client:user:services', kwargs={'pk': self.user.id})),
            ]


@class_view_decorator(permission_required('uprofile.view_user'))
class UserAdvertsListView_Client(ClientPermMixin, BreadcrumbMixin, ListView):
    model = User
    template_name = 'main/client/user/adverts.html'
    context_object_name = 'advert_list'
    user = None
    paginate_by = 50

    def get(self, request, *args, **kwargs):
        self.user = get_object_or_404(User.admin_objects.all(), id=kwargs['pk'])
        return super(UserAdvertsListView_Client, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.user.advert_set.all().order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(UserAdvertsListView_Client, self).get_context_data(**kwargs)
        context['agent'] = self.user
        return context

    def get_breadcrumbs(self):
        return super(UserAdvertsListView_Client, self).get_breadcrumbs() + [
            ('Пользователи', reverse('client:user:list')),
            (self.user.get_full_name(), reverse('client:user:detail', kwargs={'pk': self.user.id})),
            ('Объявления', reverse('client:user:adverts', kwargs={'pk': self.user.id})),
            ]


@class_view_decorator(permission_required('uprofile.view_user'))
class UserViewedListView_Client(ClientPermMixin, BreadcrumbMixin, ListView):
    model = User
    template_name = 'main/client/user/viewed.html'
    context_object_name = 'advert_list'
    user = None
    paginate_by = 50

    def get(self, request, *args, **kwargs):
        self.user = get_object_or_404(User.admin_objects.all(), id=kwargs['pk'])
        return super(UserViewedListView_Client, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.user.viewed.all().order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(UserViewedListView_Client, self).get_context_data(**kwargs)
        context['agent'] = self.user

        # кол-во открытых объявлений в день
        query_limit = Q(advert__company=None)
        context['open_count_owner'] = RegViewed.day_count_user(self.user, query=query_limit & Q(advert__need=Advert.NEED_SALE))
        context['open_count_client'] = RegViewed.day_count_user(self.user, query=query_limit & Q(advert__need=Advert.NEED_DEMAND))
        return context

    def get_breadcrumbs(self):
        return super(UserViewedListView_Client, self).get_breadcrumbs() + [
            ('Пользователи', reverse('client:user:list')),
            (self.user.get_full_name(), reverse('client:user:detail', kwargs={'pk': self.user.id})),
            ('Открытые объявления', reverse('client:user:viewed', kwargs={'pk': self.user.id})),
            ]


@class_view_decorator(permission_required('uprofile.view_user'))
class UserPaymentListView_Client(ClientPermMixin, BreadcrumbMixin, ListView):
    model = User
    template_name = 'main/client/user/payments.html'
    context_object_name = 'payment_list'
    user = None

    def get(self, request, *args, **kwargs):
        self.user = get_object_or_404(User.admin_objects.all(), id=kwargs['pk'])
        return super(UserPaymentListView_Client, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.user.payment_set.all().order_by('-created')

    def get_context_data(self, **kwargs):
        context = super(UserPaymentListView_Client, self).get_context_data(**kwargs)
        context['agent'] = self.user
        return context

    def get_breadcrumbs(self):
        return super(UserPaymentListView_Client, self).get_breadcrumbs() + [
            ('Пользователи', reverse('client:user:list')),
            (self.user.get_full_name(), reverse('client:user:detail', kwargs={'pk': self.user.id})),
            ('Платежи', reverse('client:user:payments', kwargs={'pk': self.user.id})),
            ]


@class_view_decorator(permission_required('uprofile.view_user'))
class UserVashdomPaymentListView_Client(ClientPermMixin, BreadcrumbMixin, ListView):
    model = VashdomUser
    template_name = 'main/client/user/vashdom-payments.html'
    context_object_name = 'payment_list'
    user = None

    def get(self, request, *args, **kwargs):
        self.user = get_object_or_404(VashdomUser.objects.all(), id=kwargs['pk'])
        return super(UserVashdomPaymentListView_Client, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.user.vashdom_payments.all().order_by('-created')

    def get_context_data(self, **kwargs):
        context = super(UserVashdomPaymentListView_Client, self).get_context_data(**kwargs)
        context['agent'] = self.user
        return context

    def get_breadcrumbs(self):
        return super(UserVashdomPaymentListView_Client, self).get_breadcrumbs() + [
            ('Пользователи', reverse('client:user:list')),
            (self.user.get_full_name(), reverse('client:user:detail', kwargs={'pk': self.user.id})),
            ('Платежи', reverse('client:user:vashdom-payments', kwargs={'pk': self.user.id})),
            ]


class UserTypeheadView(View):
    """
    Автодополнение пользователя
    """
    @method_decorator(ajax_request)
    def get(self, request, *args, **kwargs):
        text = self.request.GET.get('query').lower()
        query = Q(username__icontains=text) | Q(email__icontains=text) | Q(first_name__icontains=text) | Q(last_name__icontains=text)
        site_id = self.request.GET.get('site_id')
        if site_id:
            try:
                site = Site.objects.get(id=site_id)
                query &= Q(site=site)
            except:
                pass

        user_list = User.admin_objects.filter(query).select_related('site').order_by('username')[:20]

        options = [{
            'id': '',
            'username': 'НЕТ'
        }]
        for user in user_list:
            options.append({
                'id': user.id,
                'username': user.username,
                'fullname': user.get_full_name(),
                'site': user.site.domain,
                'email': user.email
            })
        return options