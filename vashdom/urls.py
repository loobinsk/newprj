from django.conf.urls import patterns, include, url
from gsnru import service_urls
from vashdom.views.public import *
from vashdom.views.private import *
from vashdom.views.advert import *
from vashdom.views.a_test import Test_AdvertListView  # for testing
from vashdom.views.payment import *
from vashdom.views.tel import *
from vashdom.views.referral import *
from vashdom.views.search_request import *
from vashdom.views.news import *
import api
from vashdom.sitemap import sitemaps
from django.contrib.sitemaps import views as sitemaps_views
from django.views.decorators.cache import cache_page
from django.views.generic import RedirectView

advert_patterns = patterns('',
                           url(r'^arenda/$', RedirectView.as_view(url='/sankt-peterburg/')),
                           url(r'^sankt-peterburg/arenda/$', RedirectView.as_view(url='/sankt-peterburg/')),
                           url(r'^moskva/arenda/$', RedirectView.as_view(url='/moskva/')),

                           url(r'^/na_karte/$', AdvertMapView.as_view(), name='map'),
                           url(r'^(?P<town>[\w|-]+)/na_karte/$', AdvertMapView.as_view()),
                           url(r'^id(?P<pk>\d+)$', RewriteAdvertDetailView.as_view()),
                           url(r'^(.+)/id(?P<pk>\d+)$', AdvertDetailView.as_view(), name='detail'),
                           url(r'^id(?P<pk>\d+)/complain$', AdvertComplainView.as_view(), name='complain'),
                           url(r'^vkid(?P<pk>\d+)$', VKAdvertDetailView.as_view()),
                           url(r'^(.+)/vkid(?P<pk>\d+)$', VKAdvertDetailView.as_view(), name='vkdetail'),
                           url(r'^vkid(?P<pk>\d+)/complain$', VKAdvertComplainView.as_view(), name='vkcomplain'),
                           url(r'^id(?P<pk>\d+)/bal$', AdvertBalloonView.as_view(), name='ballon'),
                           url(r'^phone$', AdvertPhoneView.as_view(), name='phone'),
                           url(r'^vkphone$', VKAdvertPhoneView.as_view(), name='vkphone'),
                           url(r'^vkid$', VKAdvertLinkView.as_view(), name='vkid'),
                           url(r'^add$', AdvertCreateView.as_view(), name='create'),
                           url(r'^get-access$', AdvertGetAccessView.as_view(), name='access'),

                           url(r'^vk$', RedirectView.as_view(url='/vk/sankt-peterburg/')),
                           url(r'^vk/(?P<town>[\w|-]+)/$', VKAdvertListView.as_view()),
                           # url(r'^vk/(?P<town>[\w|-]+)/(?P<estate>[\w|-]+)/$', VKAdvertListView.as_view()),
                           # url(r'^vk/(?P<town>[\w|-]+)/(?P<estate>[\w|-]+)/(?P<type>[\w|-]+)/$', VKAdvertListView.as_view()),
                           url(r'^vk/(?P<town>[\w|-]+)/metro-(?P<metro>[\w|-]+)/$', VKAdvertListView.as_view()),
                           url(r'^vk/(?P<town>[\w|-]+)/rayon-(?P<district>[\w|-]+)/$', VKAdvertListView.as_view()),
                           url(r'^vk/(?P<town>[\w|-]+)/(?P<type>[\w|-]+)/$', VKAdvertListView.as_view()),
                           url(r'^vk/(?P<town>[\w|-]+)/(?P<type>[\w|-]+)/__(?P<shortcut>[\w|-]+)/$', VKShortcutAdvertListView.as_view()),
                           url(r'^vk/(?P<town>[\w|-]+)/(?P<type>[\w|-]+)/(?P<type2>[\w|-]+)/$', VKAdvertListView.as_view()),
                           url(r'^vk/(?P<town>[\w|-]+)/(?P<type>[\w|-]+)/(?P<type2>[\w|-]+)/metro-(?P<metro>[\w|-]+)/$', VKAdvertListView.as_view()),
                           url(r'^vk/(?P<town>[\w|-]+)/(?P<type>[\w|-]+)/(?P<type2>[\w|-]+)/rayon-(?P<district>[\w|-]+)/$', VKAdvertListView.as_view()),

                           url(r'^(?P<town>[\w|-]+)/$', AdvertListView.as_view()),
                           url(r'^(?P<town>[\w|-]+)/metro-(?P<metro>[\w|-]+)/$', AdvertListView.as_view()),
                           url(r'^(?P<town>[\w|-]+)/rayon-(?P<district>[\w|-]+)/$', AdvertListView.as_view()),
                           url(r'^(?P<town>[\w|-]+)/(?P<type>[\w|-]+)/$', AdvertListView.as_view()),
                           url(r'^(?P<town>[\w|-]+)/(?P<type>[\w|-]+)/__(?P<shortcut>[\w|-]+)/$', ShortcutAdvertListView.as_view()),
                           url(r'^(?P<town>[\w|-]+)/(?P<type>[\w|-]+)/(?P<type2>[\w|-]+)/$', AdvertListView.as_view()),
                           url(r'^(?P<town>[\w|-]+)/(?P<type>[\w|-]+)/(?P<type2>[\w|-]+)/metro-(?P<metro>[\w|-]+)/$', AdvertListView.as_view()),
                           url(r'^(?P<town>[\w|-]+)/(?P<type>[\w|-]+)/(?P<type2>[\w|-]+)/rayon-(?P<district>[\w|-]+)/$', AdvertListView.as_view()),
                           # url(r'^(?P<pk>\d+)/preview$', AdvertPreviewView_Client.as_view(), name='preview'),
                           # url(r'^(?P<pk>\d+)/balloon$', AdvertBalloonView_Client.as_view(), name='balloon'),
                           # url(r'^(?P<pk>\d+)/img$', AdvertImageGalleryView_Client.as_view(), name='img'),
                           # url(r'^(?P<pk>\d+)/map$', AdvertAddressMapView_Client.as_view(), name='map'),
                           )

payment_patterns = patterns('payment',
                                     url(r'^(?P<pk>\d+)/detail$', PaymentDetailView.as_view(), name='detail'),
                                     url(r'^order/$', PaymentOrderView.as_view(), name='order'),
                                     url(r'^promocode/$', PromocodeActivateView.as_view(), name='promocode'),\
                                     url(r'^success/$', PaymentSuccessView.as_view(), name='success'),
                                     url(r'^fail/$', PaymentFailView.as_view(), name='fail'),
                                  )

referral_patterns = patterns('referral',
                                     url(r'^$', ReferralView.as_view(), name='page'),
                                     url(r'^create$', ReferralCreateView.as_view(), name='create'),
                                     url(r'^(?P<pk>\d+)/users$', ReferralUserListView.as_view(), name='user'),
                                     url(r'^(?P<pk>\d+)/payments$', ReferralPaymentListView.as_view(), name='payment'),
                                     url(r'^(?P<pk>\d+)/referers$', ReferralRefererListView.as_view(), name='referer'),
                                  )

api_patterns = patterns('api',
                            url(r'^bezkomis3f0afkrmq8gntn4bwpf62maql0a6htsf5g/$', api.AdvertList.as_view()),
                            url(r'^bezkomis3f0afkrmq8gntn4bwpf62maql0a6htsf5g/(?P<pk>\d+)/$', api.AdvertDetail.as_view()),

                            url(r'^advert/$', api.Advert2List.as_view()),
                            url(r'^advert/vk/$', api.AdvertVkList.as_view()),
                            url(r'^load/$', api.LoadAdvert.as_view()),
                        )

sr_patterns = patterns('search-request',
                                     url(r'^create/$', SearchRequestCreateView.as_view(), name='create'),
                                     url(r'^simple/$', SearchRequestSimpleCreateView.as_view(), name='simple'),
                                     url(r'^(?P<pk>\d+)/unsubscribe$', SearchRequestUnsubsribeView.as_view(), name='unsubscribe'),
                                  )


news_patterns = patterns('news',
                         url(r'^$', NewsListView.as_view(), name='list'),
                         url(r'^(?P<pk>\d+)$', NewsDetailView.as_view(), name='detail'),
                         url(r'^(?P<pk>\d+)/preview$', NewsPreviewView.as_view(), name='preview'),
                         url(r'^create$', NewsCreateView.as_view(), name='create'),
                         url(r'^(?P<pk>\d+)/edit$', NewsUpdateView.as_view(), name='edit'),
                         url(r'^(?P<pk>\d+)/del$', NewsDeleteView.as_view(), name='del'),
                         )

urlpatterns = patterns('',
    url(r'^login/$', LoginView.as_view()),
    url(r'^login/ajax$', AjaxLoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^register/$', RegisterView.as_view()),
    url(r'^register/complete/$', RegisterCompleteView.as_view()),
    url(r'^profile/$', ActiveUserProfileView.as_view()),
    url(r'^profile/change_avatar/$', ChangeAvatarView.as_view(), name='change_avatar'),
    url(r'^payments$', TariffView.as_view(), name='tariff'),
    # url(r'^free$', FreeAccessView.as_view(), name='free'),
    url(r'^contact$', ContactsView.as_view(), name='contacts'),
    url(r'^otzhiv$', MentionsView.as_view(), name='mentions'),
    url(r'^buy_alert$', PaymentAlertView.as_view(), name='payment-alert'),
    url(r'^api/',  include(api_patterns, namespace='api', app_name='vashdom')),
    url(r'^partner$', PartnerView.as_view(), name='partner'),

     url(r'^buy$', RedirectView.as_view(url='/payments')),
     url(r'^robokassa/payment/$', RedirectView.as_view(url='/payments')),

    url(r'', include('registration.backends.default.urls')),
    url(r'', include('django.contrib.auth.urls')),
    url(r'', include('social_auth.urls')),
    url(r'', include(service_urls.urlpatterns)),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^payment/', include(payment_patterns, namespace='payment', app_name='vashdom')),
    url(r'^referral/', include(referral_patterns, namespace='referral', app_name='vashdom')),
    url(r'^search-request/', include(sr_patterns, namespace='search-request', app_name='vashdom')),
    url(r'^news/', include(news_patterns, namespace='news', app_name='vashdom')),

    url(r'^sitemap.xml$', cache_page(300000, cache='file')(sitemaps_views.index), {'sitemaps': sitemaps, 'sitemap_url_name': 'sitemaps'}),
    url(r'^sitemap-(?P<section>.+)\.xml$',
        cache_page(300000, cache='file')(sitemaps_views.sitemap),
        {'sitemaps': sitemaps}, name='sitemaps'),

    url(r'', include(advert_patterns, namespace='advert', app_name='vashdom')),
)

handler404 = 'vashdom.views.public.page_not_found'