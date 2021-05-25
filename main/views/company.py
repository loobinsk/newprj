#-*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, DeleteView, FormView, TemplateView
from gutils.views import BreadcrumbMixin, AjaxableResponseMixin, AjaxPageMixin, AdminRequiredMixin
from django.core.urlresolvers import reverse
from gutils.views import class_view_decorator
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from annoying.decorators import ajax_request
from main.models import Company, Advert, Tariff, ConnectedService, clear_tel, Town, RegViewed
from main.form import CompanyForm, PaymentOrderForm, BuyOrderForm, CompanyFilterForm_Client, CompanyAvatarForm, \
    CompanyFilterForm
from uprofile.models import User
from django.shortcuts import get_object_or_404, Http404
from main.templatetags.main_tags import fmt_date
from datetime import datetime
from main.views.private import ClientPermMixin
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from mail_templated import send_mail
from uprofile.forms import ProfileForm, AvatarForm
from sorl.thumbnail import get_thumbnail
import string
from django.http import HttpResponsePermanentRedirect, Http404



class CompanyUpdatePermMixin(object):
    def dispatch(self, request, *args, **kwargs):
        company = self.get_object()
        if request.user.has_perm('main.change_company'):
            return super(CompanyUpdatePermMixin, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404()


class CompanyListView(BreadcrumbMixin, ListView):
    """
    Список агентов
    """
    model = Company
    context_object_name = 'company_list'
    paginate_by = 50
    template_name = 'main/company/page.html'
    town = None
    page_kwargs = {}

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CompanyListView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        reqdict = dict(request.REQUEST.dicts[0].lists())
        params = {}
        for key, value in reqdict.iteritems():
            if isinstance(value, list) and len(value) == 1:
                params[key] = value[0]
            else:
                params[key] = value
        return HttpResponsePermanentRedirect(Company.get_catalog_url(params))

    def get_breadcrumbs(self):
        return super(CompanyListView, self).get_breadcrumbs() + [('Агентства недвижимости', reverse('company:list'))]

    def get_queryset(self):
        query = Q(status=Company.STATUS_ACTIVE, hidden=False)
        if self.request.REQUEST.get('town'):
            self.town = get_object_or_404(Town, id=self.request.REQUEST.get('town'))
            query &= Q(town=self.town)
        elif self.kwargs.get('town'):
            self.town = get_object_or_404(Town, slug=self.kwargs.get('town'))
            query &= Q(town=self.town)
            self.page_kwargs['town'] = self.town.id
        if self.request.REQUEST.get('title'):
            query &= Q(title__icontains=self.request.REQUEST.get('title'))
        if self.request.REQUEST.get('inn'):
            query &= Q(inn__icontains=self.request.REQUEST.get('inn'))
        if self.request.REQUEST.get('tel'):
            tel = clear_tel(self.request.REQUEST.get('tel'))
            query &= (Q(tel__icontains=tel) | Q(user__tel__icontains=tel))
        if self.request.REQUEST.get('letter'):
            if len(self.request.REQUEST.get('letter')) == 1:
                query &= Q(title__istartswith=self.request.REQUEST.get('letter'))

        return Company.objects.filter(query).order_by('-rating', 'title')

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        form_data = {}
        for key, value in self.request.GET.lists():
            if isinstance(value, list) and len(value) > 1:
                form_data[key] = value
            else:
                form_data[key] = value[0]
        form_data.update(self.page_kwargs)
        context['form'] = CompanyFilterForm(form_data)
        context['eng_letters'] = u'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        context['rus_letters'] = u'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ'
        context['num_letters'] = u'0123456789'
        context['letter'] = self.request.REQUEST.get('letter')
        context['town'] = self.town
        context['page_kwargs'] = self.page_kwargs
        return context


class CompanyDetailView(BreadcrumbMixin, DetailView):
    model = Company
    template_name = 'main/company/detail.html'

    def get_breadcrumbs(self):
        return super(CompanyDetailView, self).get_breadcrumbs() + [
            ('Агентства недвижимости', reverse('company:list')),
            (self.object.title, self.object.get_absolute_url())
        ]

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['advert_list'] = self.object.advert_set.filter(status=Advert.STATUS_VIEW).order_by('-date')[:8]
        context['agent_list'] = self.object.user_set.filter(is_active=True, status=User.STATUS_ACTIVE).order_by('first_name', 'username')
        return context


class CompanyReviewsView(BreadcrumbMixin, DetailView):
    model = Company
    template_name = 'main/company/reviews.html'

    def get_breadcrumbs(self):
        return super(CompanyReviewsView, self).get_breadcrumbs() + [
            ('Агентства недвижимости', reverse('company:list')),
            (self.object.title, self.object.get_absolute_url()),
            ('Отзывы об агентстве', reverse('company:reviews', kwargs={'slug': self.object.slug, 'pk': self.object.id}))
        ]

    def get_context_data(self, **kwargs):
        context = super(CompanyReviewsView, self).get_context_data(**kwargs)
        return context


# CLIENT PART

@class_view_decorator(permission_required('main.view_company'))
class CompanyListView_Client(ClientPermMixin, BreadcrumbMixin, ListView):
    """
    Список агентов
    """
    model = Company
    context_object_name = 'company_list'
    paginate_by = 50
    template_name = 'main/client/company/page.html'
    status = Company.STATUS_ACTIVE
    blocked = False

    def get_breadcrumbs(self):
        return super(CompanyListView_Client, self).get_breadcrumbs() + [('Агентства', reverse('client:company:list'))]

    def get_queryset(self):
        query = Q()

        if self.request.GET.get('status') in Company.STATUSES:
            query &= Q(status=self.request.GET.get('status'))

        if self.request.GET.get('title'):
            query &= Q(title__icontains=self.request.GET.get('title'))

        if self.request.GET.get('email'):
            query &= Q(email__icontains=self.request.GET.get('email'))

        if self.request.GET.get('tel'):
            query &= Q(tel__icontains=clear_tel(self.request.GET.get('tel')))

        if self.request.GET.get('is_real'):
            query &= Q(is_real=True)

        if self.request.GET.get('town') and self.request.GET.get('town') != '0':
            query &= Q(town_id=self.request.GET.get('town'))

        return Company.objects.filter(query).order_by('title')

    def get_context_data(self, **kwargs):
        context = super(CompanyListView_Client, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_company')
        context['form'] = CompanyFilterForm_Client(data=self.request.GET)
        return context


@class_view_decorator(permission_required('main.view_company'))
class CompanyDetailView_Client(ClientPermMixin, BreadcrumbMixin, AjaxPageMixin, DetailView):
    model = Company
    template_name = 'main/client/company/detail.html'
    template_name_ajax = 'main/client/company/detail-ajax.html'

    def get_breadcrumbs(self):
        return super(CompanyDetailView_Client, self).get_breadcrumbs() + [
            ('Агентства', reverse('client:company:list')),
            (self.object.title, reverse('client:company:detail', kwargs={'pk': self.object.id}))
        ]

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView_Client, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_company')
        return context


@class_view_decorator(permission_required('main.view_company'))
class CompanyPreviewView_Client(ClientPermMixin, DetailView):
    model = Company
    template_name = 'main/client/company/preview.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyPreviewView_Client, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_company')
        return context


@class_view_decorator(permission_required('main.change_company'))
class CompanyStatusView(ClientPermMixin, View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CompanyStatusView, self).dispatch(request, *args, **kwargs)

    @method_decorator(ajax_request)
    def post(self, request, *args, **kwargs):
        company = Company.objects.get(id=kwargs['pk'])
        if Company.STATUSES.has_key(request.GET.get('status')):
            company.status = request.GET.get('status')
        company.save()

        return {
            'id': company.id
        }


@class_view_decorator(permission_required('main.change_company'))
class CompanyUpdateView_Client(ClientPermMixin, AjaxableResponseMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'main/client/company/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(CompanyUpdateView_Client, self).get_context_data(**kwargs)
        context['action'] = reverse('client:company:edit', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        form.instance.clear_cache()
        return super(CompanyUpdateView_Client, self).form_valid(form)

    def get_model_dict(self):
        return {
            'url': reverse('client:company:detail', kwargs={'pk': self.object.id})
        }


@class_view_decorator(permission_required('main.view_company'))
class CompanyAgentsListView_Client(ClientPermMixin, BreadcrumbMixin, ListView):
    model = User
    template_name = 'main/client/company/agents.html'
    context_object_name = 'user_list'
    company = None

    def get(self, request, *args, **kwargs):
        self.company = get_object_or_404(Company, id=kwargs['pk'])
        return super(CompanyAgentsListView_Client, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.company.user_set.all()

    def get_context_data(self, **kwargs):
        context = super(CompanyAgentsListView_Client, self).get_context_data(**kwargs)
        context['company'] = self.company
        context['can_edit'] = self.request.user.has_perm('change_user') or (self.request.user == self.company.owner)
        context['less_rights'] = True
        return context

    def get_breadcrumbs(self):
        return super(CompanyAgentsListView_Client, self).get_breadcrumbs() + [
            ('Агентства', reverse('client:company:list')),
            (self.company.title, reverse('client:company:detail', kwargs={'pk': self.company.id})),
            ('Агенты', reverse('client:company:agents', kwargs={'pk': self.company.id})),
            ]


@class_view_decorator(permission_required('main.view_company'))
class CompanyAdvertsListView_Client(ClientPermMixin, BreadcrumbMixin, ListView):
    model = User
    template_name = 'main/client/company/adverts.html'
    context_object_name = 'advert_list'
    paginate_by = 20
    company = None

    def get(self, request, *args, **kwargs):
        self.company = get_object_or_404(Company, id=kwargs['pk'])
        return super(CompanyAdvertsListView_Client, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.company.advert_set.all().order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(CompanyAdvertsListView_Client, self).get_context_data(**kwargs)
        context['company'] = self.company
        return context

    def get_breadcrumbs(self):
        return super(CompanyAdvertsListView_Client, self).get_breadcrumbs() + [
            ('Агентства', reverse('client:company:list')),
            (self.company.title, reverse('client:company:detail', kwargs={'pk': self.company.id})),
            ('Объявления', reverse('client:company:adverts', kwargs={'pk': self.company.id})),
        ]


class CompanyOpenAdvertsListView_Client(AdminRequiredMixin, ClientPermMixin, BreadcrumbMixin, ListView):
    model = User
    template_name = 'main/client/company/open-adverts.html'
    context_object_name = 'advert_list'
    paginate_by = 20
    company = None

    def get(self, request, *args, **kwargs):
        self.company = get_object_or_404(Company, id=kwargs['pk'])
        return super(CompanyOpenAdvertsListView_Client, self).get(request, *args, **kwargs)

    def get_queryset(self):
        open_ids = []
        for user in self.company.user_set.all():
            open_ids += [advert.id for advert in user.viewed.all()]
        return Advert.objects.filter(id__in=open_ids).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(CompanyOpenAdvertsListView_Client, self).get_context_data(**kwargs)
        context['company'] = self.company

        # кол-во открытых объявлений в день
        query_limit = Q(advert__company=None)
        context['open_count_owner'] = RegViewed.day_count_company(self.company, query=query_limit & Q(advert__need=Advert.NEED_SALE))
        context['open_count_client'] = RegViewed.day_count_company(self.company, query=query_limit & Q(advert__need=Advert.NEED_DEMAND))
        return context

    def get_breadcrumbs(self):
        return super(CompanyOpenAdvertsListView_Client, self).get_breadcrumbs() + [
            ('Агентства', reverse('client:company:list')),
            (self.company.title, reverse('client:company:detail', kwargs={'pk': self.company.id})),
            ('Открытые объявления', reverse('client:company:open-adverts', kwargs={'pk': self.company.id})),
            ]


@class_view_decorator(permission_required('main.view_company'))
class CompanyServicesListView_Client(ClientPermMixin, BreadcrumbMixin, ListView):
    model = User
    template_name = 'main/client/company/services.html'
    context_object_name = 'service_list'
    company = None

    def get(self, request, *args, **kwargs):
        self.company = get_object_or_404(Company, id=kwargs['pk'])
        return super(CompanyServicesListView_Client, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.company.connectedservice_set.all().order_by('-end_date')

    def get_context_data(self, **kwargs):
        context = super(CompanyServicesListView_Client, self).get_context_data(**kwargs)
        context['company'] = self.company
        return context

    def get_breadcrumbs(self):
        return super(CompanyServicesListView_Client, self).get_breadcrumbs() + [
            ('Агентства', reverse('client:company:list')),
            (self.company.title, reverse('client:company:detail', kwargs={'pk': self.company.id})),
            ('Подключенные услуги', reverse('client:company:services', kwargs={'pk': self.company.id})),
            ]


class MyCompanyDetailView(ClientPermMixin, BreadcrumbMixin, AjaxPageMixin, DetailView):
    model = Company
    template_name = 'main/client/company/my.html'
    template_name_ajax = 'main/client/company/my-ajax.html'

    def get_object(self, queryset=None):
        if self.request.user.company:
            return self.request.user.company
        raise Http404()

    def get_breadcrumbs(self):
        return super(MyCompanyDetailView, self).get_breadcrumbs() + [
            ('Мое агентство', reverse('client:company:my'))
        ]

    def get_context_data(self, **kwargs):
        context = super(MyCompanyDetailView, self).get_context_data(**kwargs)
        context['can_edit'] = self.request.user.has_perm('main.change_company') or (self.object.owner == self.request.user)
        context['my'] = True

        if self.request.user.independent:
            # если агент независимый
            service_query = Q(user=self.request.user, active=True, end_date__gte=datetime.now())
        else:
            # если агент под агентством
            service_query = Q(company=self.object, active=True, end_date__gte=datetime.now())
        context['service_list'] = ConnectedService.objects.filter(service_query).order_by('-end_date')
        context['payment_form'] = PaymentOrderForm(self.request.current_town)
        context['buy_form'] = BuyOrderForm()
        context['user_list'] = self.object.user_set.exclude(status=User.STATUS_BLOCK)
        context['photo_form'] = CompanyAvatarForm()
        context['profile_form'] = ProfileForm(instance=self.request.user)
        context['avatar_form'] = AvatarForm()

        # кол-во открытых объявлений в день
        query_limit = Q(advert__company=None)
        if self.request.user.independent or not self.request.user.company:
            context['open_count_owner'] = RegViewed.day_count_user(self.request.user, query=query_limit & Q(advert__need=Advert.NEED_SALE))
            context['open_count_client'] = RegViewed.day_count_user(self.request.user, query=query_limit & Q(advert__need=Advert.NEED_DEMAND))
        else:
            context['open_count_owner'] = RegViewed.day_count_company(self.request.user.company, query=query_limit & Q(advert__need=Advert.NEED_SALE))
            context['open_count_client'] = RegViewed.day_count_company(self.request.user.company, query=query_limit & Q(advert__need=Advert.NEED_DEMAND))
        return context


class CompanyAvatarView(ClientPermMixin, AjaxableResponseMixin, FormView):
    form_class = CompanyAvatarForm
    success_url = '/'

    def form_valid(self, form):
        if not self.request.user.company:
            raise Exception(u'У вас не агентства')
        if self.request.user.company.owner != self.request.user:
            raise Exception(u'Нет прав')
        self.request.user.company.image = form.cleaned_data['image']
        self.request.user.company.save()
        self.request.user.company.clear_cache()
        return super(CompanyAvatarView, self).form_valid(form)

    def get_model_dict(self):
        thumb = get_thumbnail(self.request.user.company.image, '200x200', crop='center')
        return thumb.url


class MyCompanyCommentsView(ClientPermMixin, BreadcrumbMixin, DetailView):
    model = Company
    template_name = 'main/client/company/comments.html'
    context_object_name = 'company'

    def get_object(self, queryset=None):
        if self.request.user.company:
            return self.request.user.company
        raise Http404()

    def get_breadcrumbs(self):
        return super(MyCompanyCommentsView, self).get_breadcrumbs() + [
            ('Мое агентство', reverse('client:company:my')),
            ('Отзывы', reverse('client:company:my')),
        ]