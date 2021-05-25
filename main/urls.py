#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from main.views.public import *
from main.views.advert import *
from main.views.town import *
from main.views.vacancy import *
from main.views.metro import *
from main.views.user import *
from main.views.news import *
from main.views.district import *
from main.views.question import *
from main.views.metro import *
from main.views.blacklist import *
from main.views.vkblacklist import *
from main.views.company import *
from main.views.tariff import *
from main.views.payment import *
from main.views.tel import *
from main.views.private import *
from main.views.abbr import *
from main.views.service import *
from main.views.stats import *
from main.views.subscribe import *
from main.views.search_request import *
from main.views.comment import *
from main.views.vkadvert import *
from main.views.password import *
from main.views.promotion import *
from main.views.referral import *

# PUBLIC

advert_patterns = patterns('',

                           url(r'^catalog/(?P<pk>\d+)/detail$', AdvertDetailView.as_view(), name='detail'),
                           url(r'^(.+)/id(?P<pk>\d+)$', AdvertDetailView.as_view()),
                           url(r'^catalog/(?P<pk>\d+)/balloon$', AdvertBalloonView.as_view(), name='balloon'),
                           url(r'^catalog/(?P<pk>\d+)/map$', AdvertAddressMapView.as_view(), name='map'),
                           url(r'^catalog/create$', AdvertCreateView.as_view(), name='create'),
                           url(r'^catalog/request$', RequestView.as_view(), name='request'),
                           url(r'^catalog/(?P<pk>\d+)/send$', AdvertSendFriendView.as_view(), name='send'),
                           url(r'^catalog/request/remove$', AdvertRequestRemoveView.as_view(), name='request-remove'),
                           url(r'^catalog/(?P<pk>\d+)/complain$', AdvertComplainView.as_view(), name='complain'),

                           url(r'^nedvizhimost/$', AdvertListView.as_view(), name='list'),
                           url(r'^catalog/$', AdvertListView.as_view()),
                           url(r'^(?P<town>[\w|-]+)/nedvizhimost/$', AdvertListView.as_view()),
                           url(r'^(?P<town>[\w|-]+)/(?P<estate>[\w|-]+)/$', AdvertListView.as_view()),
                           url(r'^(?P<town>[\w|-]+)/(?P<estate>[\w|-]+)/(?P<type>[\w|-]+)/$', AdvertListView.as_view()),
                           url(r'^(?P<town>[\w|-]+)/(?P<estate>[\w|-]+)/(?P<type>[\w|-]+)/metro-(?P<metro>[\w|-]+)/$', AdvertListView.as_view()),
                           url(r'^(?P<town>[\w|-]+)/(?P<estate>[\w|-]+)/(?P<type>[\w|-]+)/rayon-(?P<district>[\w|-]+)/$', AdvertListView.as_view()),
                           url(r'^(?P<town>[\w|-]+)/(?P<estate>[\w|-]+)/(?P<type>[\w|-]+)/(?P<type2>[\w|-]+)/$', AdvertListView.as_view()),
                           url(r'^(?P<town>[\w|-]+)/(?P<estate>[\w|-]+)/(?P<type>[\w|-]+)/(?P<type2>[\w|-]+)/metro-(?P<metro>[\w|-]+)/$', AdvertListView.as_view()),
                           url(r'^(?P<town>[\w|-]+)/(?P<estate>[\w|-]+)/(?P<type>[\w|-]+)/(?P<type2>[\w|-]+)/rayon-(?P<district>[\w|-]+)/$', AdvertListView.as_view()),
                           )


company_patterns = patterns('company',
                           url(r'^$', CompanyListView.as_view(), name='list'),
                           url(r'^(?P<town>[\w|-]+)/$', CompanyListView.as_view()),
                           url(r'^(?P<slug>[\w|-]+)/id(?P<pk>\d+)$', CompanyDetailView.as_view(), name='detail'),
                           url(r'^(?P<slug>[\w|-]+)/id(?P<pk>\d+)/reviews$', CompanyReviewsView.as_view(), name='reviews'),
                           )

vacancy_patterns = patterns('vacancy',
                                   url(r'^$', VacancyListView.as_view(), name='list'),
                                   url(r'^(?P<pk>\d+)/detail$', VacancyDetailView.as_view(), name='detail'),
                                   )

question_patterns = patterns('question',
                            url(r'^$', QuestionListView.as_view(), name='list'),
                            url(r'^(?P<pk>\d+)/detail$', QuestionDetailView.as_view(), name='detail'),
                            url(r'^create$', FaqCreateView.as_view(), name='create'),
                            )

user_patterns = patterns('user',
                                url(r'^id(?P<pk>\d+)$', UserDetailView.as_view(), name='detail'),
                                url(r'^id(?P<pk>\d+)/reviews$', UserReviewsView.as_view(), name='reviews'),
)

phone_patterns = patterns('phone',
                         url(r'^company$', CompanyPhoneView.as_view(), name='company'),
                         url(r'^user$', UserPhoneView.as_view(), name='user'),
                         url(r'^owner$', AdvertPhoneView.as_view(), name='owner'),
                         url(r'^ownervk$', VKAdvertPhoneView.as_view(), name='ownervk'),
                         url(r'^ownervkid$', VKAdvertLinkView.as_view(), name='ownervkid'),
                         )

metro_patterns = patterns('metro',
                           url(r'^typehead$', MetroTypeheadView.as_view(), name='typehead'),
                           )

district_patterns = patterns('district',
                          url(r'^typehead$', DistrictTypeheadView.as_view(), name='typehead'),
                          )

subscribe_patterns = patterns('subscribe',
                             url(r'^subscribe$', SubscribeView.as_view(), name='subscribe'),
                             url(r'^unsubscribe$', UnsubscribeView.as_view(), name='unsubscribe'),
                             )


news_patterns = patterns('news',
                         url(r'^$', NewsListView.as_view(), name='list'),
                         url(r'^(?P<pk>\d+)/detail$', NewsDetailView.as_view(), name='detail'),
                         url(r'^(?P<pk>\d+)/preview$', NewsPreviewView.as_view(), name='preview'),
                         url(r'^create$', NewsCreateView.as_view(), name='create'),
                         url(r'^(?P<pk>\d+)/edit$', NewsUpdateView.as_view(), name='edit'),
                         url(r'^(?P<pk>\d+)/del$', NewsDeleteView.as_view(), name='del'),
                         )


# CLIENT
client_news_patterns = patterns('news',
                         url(r'^$', NewsListView_Client.as_view(), name='list'),
                         url(r'^(?P<pk>\d+)/detail$', NewsDetailView_Client.as_view(), name='detail'),
                         url(r'^(?P<pk>\d+)/preview$', NewsPreviewView_Client.as_view(), name='preview'),
                         url(r'^create$', NewsCreateView.as_view(), name='create'),
                         url(r'^(?P<pk>\d+)/edit$', NewsUpdateView.as_view(), name='edit'),
                         url(r'^(?P<pk>\d+)/del$', NewsDeleteView.as_view(), name='del'),
                         )

client_company_patterns = patterns('company',
                         url(r'^$', CompanyListView_Client.as_view(), name='list'),
                         url(r'^(?P<pk>\d+)/detail$', CompanyDetailView_Client.as_view(), name='detail'),
                         url(r'^(?P<pk>\d+)/preview$', CompanyPreviewView_Client.as_view(), name='preview'),
                         url(r'^(?P<pk>\d+)/status$', CompanyStatusView.as_view(), name='status'),
                         url(r'^(?P<pk>\d+)/edit$', CompanyUpdateView_Client.as_view(), name='edit'),
                         url(r'^(?P<pk>\d+)/agents$', CompanyAgentsListView_Client.as_view(), name='agents'),
                         url(r'^(?P<pk>\d+)/adverts$', CompanyAdvertsListView_Client.as_view(), name='adverts'),
                         url(r'^(?P<pk>\d+)/open-adverts$', CompanyOpenAdvertsListView_Client.as_view(), name='open-adverts'),
                         url(r'^(?P<pk>\d+)/services$', CompanyServicesListView_Client.as_view(), name='services'),
                         url(r'^my$', MyCompanyDetailView.as_view(), name='my'),
                         url(r'^comments$', MyCompanyCommentsView.as_view(), name='comments'),
                         url(r'^avatar$', CompanyAvatarView.as_view(), name='change_avatar'),

                         url(r'^user/create$', UserCreateView_User.as_view(), name='user-create'),
                         url(r'^user/(?P<pk>\d+)/edit$', UserUpdateView_User.as_view(), name='user-edit'),
                         url(r'^user/(?P<pk>\d+)/del$', UserDeleteView_User.as_view(), name='user-del'),
                         # url(r'^user/(?P<pk>\d+)/preview', UserPreviewView_User.as_view(), name='user-preview'),
                         # url(r'^user/(?P<pk>\d+)/detail', UserPreviewView_User.as_view(), name='user-detail'),
                         url(r'^user/(?P<pk>\d+)/perms$', UserPermsView_User.as_view(), name='user-perms'),
                         )

client_user_patterns = patterns('user',
                                url(r'^$', UserListView_Client.as_view(), name='list'),
                                url(r'^(?P<pk>\d+)/detail$', UserDetailView_Client.as_view(), name='detail'),
                                url(r'^(?P<pk>\d+)/preview$', UserPreviewView_Client.as_view(), name='preview'),
                                url(r'^create$', UserCreateView_Client.as_view(), name='create'),
                                url(r'^(?P<pk>\d+)/edit$', UserUpdateView_Client.as_view(), name='edit'),
                                url(r'^(?P<pk>\d+)/del$', UserDeleteView_Client.as_view(), name='del'),
                                url(r'^(?P<pk>\d+)/status$', UserStatusView_Client.as_view(), name='status'),
                                url(r'^(?P<pk>\d+)/services$', UserServicesListView_Client.as_view(), name='services'),
                                url(r'^(?P<pk>\d+)/catalog$', UserAdvertsListView_Client.as_view(), name='adverts'),
                                url(r'^(?P<pk>\d+)/viewed$', UserViewedListView_Client.as_view(), name='viewed'),
                                url(r'^(?P<pk>\d+)/payments/gsn$', UserPaymentListView_Client.as_view(), name='payments'),
                                url(r'^(?P<pk>\d+)/payments/vashdom$', UserVashdomPaymentListView_Client.as_view(), name='vashdom-payments'),
                                url(r'^(?P<pk>\d+)/passwords$', PasswordUserView.as_view(), name='passwords'),
                                # url(r'^(?P<pk>\d+)/catalog', ModeratorAdvertListView.as_view(), name='adverts'),
                                url(r'^typehead$', UserTypeheadView.as_view(), name='typehead'),
                                )

client_town_patterns = patterns('town',
                                url(r'^$', TownListView.as_view(), name='list'),
                                url(r'^(?P<pk>\d+)/detail$', TownDetailView.as_view(), name='detail'),
                                url(r'^(?P<pk>\d+)/preview$', TownPreviewView.as_view(), name='preview'),
                                url(r'^create$', TownCreateView.as_view(), name='create'),
                                url(r'^(?P<pk>\d+)/edit$', TownUpdateView.as_view(), name='edit'),
                                url(r'^(?P<pk>\d+)/del$', TownDeleteView.as_view(), name='del'),
                                )

client_district_patterns = patterns('district',
                                url(r'^(?P<pk>\d+)/preview$', DistrictPreviewView.as_view(), name='preview'),
                                url(r'^create$', DistrictCreateView.as_view(), name='create'),
                                url(r'^(?P<pk>\d+)/edit$', DistrictUpdateView.as_view(), name='edit'),
                                url(r'^(?P<pk>\d+)/del$', DistrictDeleteView.as_view(), name='del'),
                                )

client_metro_patterns = patterns('metro',
                                    url(r'^(?P<pk>\d+)/preview$', MetroPreviewView.as_view(), name='preview'),
                                    url(r'^create$', MetroCreateView.as_view(), name='create'),
                                    url(r'^(?P<pk>\d+)/edit$', MetroUpdateView.as_view(), name='edit'),
                                    url(r'^(?P<pk>\d+)/del$', MetroDeleteView.as_view(), name='del'),
                                    )

client_password_patterns = patterns('password',
                                    url(r'^$', PasswordListView.as_view(), name='list'),
                                    url(r'^(?P<pk>\d+)/preview$', PasswordPreviewView.as_view(), name='preview'),
                                    url(r'^create$', PasswordCreateView.as_view(), name='create'),
                                    url(r'^(?P<pk>\d+)/edit$', PasswordUpdateView.as_view(), name='edit'),
                                    url(r'^(?P<pk>\d+)/del$', PasswordDeleteView.as_view(), name='del'),
                                    url(r'^(?P<pk>\d+)/adverts$', PasswordAdvertsListView.as_view(), name='adverts'),
                                    )


client_promotion_patterns = patterns('promotion',
                                    url(r'^$', PromotionListView.as_view(), name='list'),
                                    url(r'^(?P<pk>\d+)/preview$', PromotionPreviewView.as_view(), name='preview'),
                                    url(r'^create$', PromotionCreateView.as_view(), name='create'),
                                    url(r'^(?P<pk>\d+)/edit$', PromotionUpdateView.as_view(), name='edit'),
                                    url(r'^(?P<pk>\d+)/del$', PromotionDeleteView.as_view(), name='del'),
                                    )

client_promocode_patterns = patterns('promocode',
                                    url(r'^$', PromocodeListView.as_view(), name='list'),
                                    url(r'^(?P<pk>\d+)/preview$', PromocodePreviewView.as_view(), name='preview'),
                                    url(r'^create$', PromocodeCreateView.as_view(), name='create'),
                                    url(r'^(?P<pk>\d+)/edit$', PromocodeUpdateView.as_view(), name='edit'),
                                    url(r'^(?P<pk>\d+)/del$', PromocodeDeleteView.as_view(), name='del'),
                                    )

client_vkadvert_patterns = patterns('vk',
                                        url(r'^$', VKAdvertListView_Client.as_view(), name='list'),
                                        url(r'^(?P<pk>\d+)/is_agent$', VKAdvertIsAgentView_Client.as_view(), name='is_agent'),
                                        url(r'^(?P<pk>\d+)/irrelevant$', VKAdvertIrrelevantView_Client.as_view(), name='irrelevant'),
                                        url(r'^(?P<pk>\d+)/preview$', VKAdvertPreview_Client.as_view(), name='preview'),
                                        url(r'^(?P<pk>\d+)/img$', VKAdvertImageGalleryView_Client.as_view(), name='img'),
                                        url(r'^(?P<pk>\d+)/complain$', VKAdvertComplainView_Client.as_view(), name='complain'),
                                    )

client_advert_stat_patterns = patterns('stat',
                                       url(r'^(?P<pk>\d+)/users$', AdvertViewByUsersView.as_view(), name='users'),
                                       url(r'^(?P<pk>\d+)/password/vashdom/$', AdvertViewByVashdomPasswordView.as_view(), name='password-vashdom'),
                                       )

client_advert_patterns = patterns('catalog',
                           url(r'^(?P<pk>\d+)/preview$', AdvertPreviewView_Client.as_view(), name='preview'),
                           url(r'^(?P<pk>\d+)/balloon$', AdvertBalloonView_Client.as_view(), name='balloon'),
                           url(r'^(?P<pk>\d+)/img$', AdvertImageGalleryView_Client.as_view(), name='img'),
                           url(r'^(?P<pk>\d+)/map$', AdvertAddressMapView_Client.as_view(), name='map'),
                           url(r'^(?P<pk>\d+)/clients$', AdvertClientsView_Client.as_view(), name='clients'),
                           url(r'^(?P<pk>\d+)/complains$', AdvertComplainsView_Client.as_view(), name='complains'),
                           url(r'^create$', AdvertCreateView_Client.as_view(), name='create'),
                           url(r'^(?P<pk>\d+)/edit$', AdvertUpdateView_Client.as_view(), name='edit'),
                           url(r'^(?P<pk>\d+)/del$', AdvertDeleteView_Client.as_view(), name='del'),
                           url(r'^buy$', AdvertBuyView_Client.as_view(), name='buy'),
                           url(r'^(?P<pk>\d+)/fold$', AdvertFoldView_Client.as_view(), name='fold'),
                           url(r'^(?P<pk>\d+)/approve$', AdvertApproveView_Client.as_view(), name='approve'),
                           url(r'^(?P<pk>\d+)/is_agent$', AdvertIsAgentView_Client.as_view(), name='is_agent'),
                           url(r'^(?P<pk>\d+)/irrelevant$', AdvertIrrelevantView_Client.as_view(), name='irrelevant'),
                           url(r'^(?P<pk>\d+)/block$', AdvertSetBlockView_Client.as_view(), name='block'),
                           url(r'^duplicate$', AdvertSearchDuplicateView_Client.as_view(), name='duplicate'),
                           url(r'^my$', MyAdvertView_Client.as_view(), name='my'),
                           url(r'^moderated$', MyModerateAdvertView_Client.as_view(), name='moderated'),
                           url(r'^fav$', AddFavoriteView_Client.as_view(), name='addfav'),
                           url(r'^favorites$', FavoritesView_Client.as_view(), name='favorites'),
                           url(r'^buyed$', AdvertBuyedView_Client.as_view(), name='buyed'),
                           url(r'^not-answer$', AdvertNotAnswerListView_Client.as_view(), name='not_answer'),
                           url(r'^archive$', AdvertSetArchiveView_Client.as_view(), name='archive'),
                           url(r'^vk/', include(client_vkadvert_patterns, namespace='vk', app_name='main')),
                           url(r'^stat/', include(client_advert_stat_patterns, namespace='stat', app_name='main')),
                           )

client_vacancy_patterns = patterns('vacancy',
                                url(r'^$', VacancyListView_Client.as_view(), name='list'),
                                url(r'^(?P<pk>\d+)/detail$', VacancyDetailView_Client.as_view(), name='detail'),
                                url(r'^(?P<pk>\d+)/preview$', VacancyPreviewView.as_view(), name='preview'),
                                url(r'^create$', VacancyCreateView.as_view(), name='create'),
                                url(r'^(?P<pk>\d+)/edit$', VacancyUpdateView.as_view(), name='edit'),
                                url(r'^(?P<pk>\d+)/del$', VacancyDeleteView.as_view(), name='del'),
                                )

client_question_patterns = patterns('question',
                                   url(r'^$', QuestionListView_Client.as_view(), name='list'),
                                   url(r'^(?P<pk>\d+)/detail$', QuestionDetailView_Client.as_view(), name='detail'),
                                   url(r'^(?P<pk>\d+)/preview$', QuestionPreviewView.as_view(), name='preview'),
                                   url(r'^create$', QuestionCreateView.as_view(), name='create'),
                                   url(r'^(?P<pk>\d+)/edit$', QuestionUpdateView.as_view(), name='edit'),
                                   url(r'^(?P<pk>\d+)/del$', QuestionDeleteView.as_view(), name='del'),
                                   )

client_blacklist_patterns = patterns('blacklist',
                                url(r'^$', BlacklistListView.as_view(), name='list'),
                                url(r'^(?P<pk>\d+)/preview$', BlacklistPreviewView.as_view(), name='preview'),
                                url(r'^create$', BlacklistCreateView.as_view(), name='create'),
                                url(r'^multi-create$', BlacklistCreateMultiView.as_view(), name='multi-create'),
                                url(r'^(?P<pk>\d+)/edit', BlacklistUpdateView.as_view(), name='edit'),
                                url(r'^(?P<pk>\d+)/del', BlacklistDeleteView.as_view(), name='del'),
                                url(r'^check$', BlacklistCheckView.as_view(), name='check'),
                                url(r'^addtel$', BlacklistAddTelView.as_view(), name='addtel'),
                                )

client_vkblacklist_patterns = patterns('vkblacklist',
                                url(r'^$', VKBlacklistListView.as_view(), name='list'),
                                url(r'^(?P<pk>\d+)/del', VKBlacklistDeleteView.as_view(), name='del'),
                                )

client_tariff_patterns = patterns('tariff',
                                  url(r'^$', TariffListView_Client.as_view(), name='list'),
                                  url(r'^(?P<pk>\d+)/preview$', TariffPreviewView.as_view(), name='preview'),
                                  url(r'^create$', TariffCreateView.as_view(), name='create'),
                                  url(r'^(?P<pk>\d+)/edit', TariffUpdateView.as_view(), name='edit'),
                                  url(r'^(?P<pk>\d+)/del', TariffDeleteView.as_view(), name='del'),
                                  )

client_payment_patterns = patterns('payment',
                                     url(r'^(?P<pk>\d+)/detail$', PaymentDetailView.as_view(), name='detail'),
                                     url(r'^order/$', PaymentOrderView.as_view(), name='order'),
                                     url(r'^buy/$', BuyOrderView.as_view(), name='buy'),
                                     url(r'^history/$', PaymentHistoryView.as_view(), name='history'),
                                     url(r'^all/$', AllPaymentListView.as_view(), name='all'),
                                     url(r'^all-vashdom/$', AllVashdomPaymentListView.as_view(), name='all-vashdom'),
                                     url(r'^promocode$', PromocodeActivateView.as_view(), name='promocode'),
                                  )

client_abbr_patterns = patterns('abbr',
                                url(r'^$', AbbrListView.as_view(), name='list'),
                                url(r'^(?P<pk>\d+)/preview$', AbbrPreviewView.as_view(), name='preview'),
                                url(r'^create$', AbbrCreateView.as_view(), name='create'),
                                url(r'^(?P<pk>\d+)/del$', AbbrDeleteView.as_view(), name='del'),
                                )

client_service_patterns = patterns('service',
                                 url(r'^(?P<pk>\d+)/preview$', ConnectedServicePreviewView.as_view(), name='preview'),
                                 url(r'^create$', ConnectedServiceCreateView.as_view(), name='create'),
                                 url(r'^(?P<pk>\d+)/edit$', ConnectedServiceUpdateView.as_view(), name='edit'),
                                 url(r'^(?P<pk>\d+)/del$', ConnectedServiceDeleteView.as_view(), name='del'),
                                 )

client_stat_patterns = patterns('stat',
                                   url(r'^moderator$', ModeratorStatView.as_view(), name='moderator'),
                                   url(r'^parser$', ParserStatView.as_view(), name='parser'),
                                   )

client_request_patterns = patterns('search-request',
                           url(r'^(?P<pk>\d+)/clients$', SearchRequestClientsView_Client.as_view(), name='clients'),
                           url(r'^create$', SearchRequestCreateView_Client.as_view(), name='create'),
                           url(r'^(?P<pk>\d+)/edit$', SearchRequestUpdateView_Client.as_view(), name='edit'),
                           url(r'^(?P<pk>\d+)/del$', SearchRequestDeleteView_Client.as_view(), name='del'),
                           url(r'^(?P<pk>\d+)/start$', SearchRequestStartView_Client.as_view(), name='start'),
                           url(r'^(?P<pk>\d+)/stop$', SearchRequestStopView_Client.as_view(), name='stop'),
                           url(r'^(?P<pk>\d+)/preview$', SearchRequestPreviewView_Client.as_view(), name='preview'),
                           url(r'^my$', MySearchRequestView_Client.as_view(), name='my'),
                           url(r'^(?P<pk>\d+)/not-send$', SearchRequestNotSendView_Client.as_view(), name='not-send'),
                           url(r'^(?P<pk>\d+)/do-send$', SearchRequestDoSendView_Client.as_view(), name='do-send'),
                           )

moder_sr_patterns = patterns('search-request',
                           url(r'^delivery$', DeliveryListView_Client.as_view(), name='delivery'),
                           url(r'^(?P<pk>\d+)/edit$', SearchRequestUpdateView_Client.as_view(), name='edit'),
                           )

client_comment_patterns = patterns('comment',
                           url(r'^list$', CommentListView.as_view(), name='list'),
                           )

client_referral_patterns = patterns('referral',
                                    url(r'^$', ReferralListView.as_view(), name='list'),
                                    url(r'^(?P<pk>\d+)/preview$', ReferralPreviewView.as_view(), name='preview'),
                                    url(r'^create$', ReferralCreateView.as_view(), name='create'),
                                    url(r'^(?P<pk>\d+)/edit$', ReferralUpdateView.as_view(), name='edit'),
                                    url(r'^(?P<pk>\d+)/del$', ReferralDeleteView.as_view(), name='del'),
                                    url(r'^(?P<pk>\d+)/users$', ReferralUserListView_Client.as_view(), name='user'),
                                    url(r'^(?P<pk>\d+)/payments$', ReferralPaymentListView_Client.as_view(), name='payment'),
                                    url(r'^(?P<pk>\d+)/referers$', ReferralRefererListView_Client.as_view(), name='referer'),
                                    )

client_patterns = patterns('client',
                           url(r'^$', HomeView_Client.as_view(), name='home'),
                           url(r'^news/', include(client_news_patterns, namespace='news', app_name='main')),
                           url(r'^company/', include(client_company_patterns, namespace='company', app_name='main')),
                           url(r'^district/', include(client_district_patterns, namespace='district', app_name='main')),
                           url(r'^metro/', include(client_metro_patterns, namespace='metro', app_name='main')),
                           url(r'^catalog/', include(client_advert_patterns, namespace='advert', app_name='main')),
                           url(r'^vacancy/', include(client_vacancy_patterns, namespace='vacancy', app_name='main')),
                           url(r'^question/', include(client_question_patterns, namespace='question', app_name='main')),
                           url(r'^payment/', include(client_payment_patterns, namespace='payment', app_name='main')),
                           url(r'^feedback$', FeedbackView_Client.as_view(), name='feedback'),
                           url(r'^user/', include(client_user_patterns, namespace='user', app_name='main')),
                           url(r'^service/', include(client_service_patterns, namespace='service', app_name='main')),
                           url(r'^search-request/', include(client_request_patterns, namespace='search-request', app_name='main')),
                           )

# MODERATOR URLS
moder_panel_patterns = patterns('client',
                           url(r'^$', HomeView_Client.as_view(), name='home'),
                           url(r'^news/', include(client_news_patterns, namespace='news', app_name='main')),
                           url(r'^company/', include(client_company_patterns, namespace='company', app_name='main')),
                           url(r'^user/', include(client_user_patterns, namespace='user', app_name='main')),
                           url(r'^town/', include(client_town_patterns, namespace='town', app_name='main')),
                           url(r'^district/', include(client_district_patterns, namespace='district', app_name='main')),
                           url(r'^metro/', include(client_metro_patterns, namespace='metro', app_name='main')),
                           url(r'^catalog/', include(client_advert_patterns, namespace='advert', app_name='main')),
                           url(r'^vacancy/', include(client_vacancy_patterns, namespace='vacancy', app_name='main')),
                           url(r'^question/', include(client_question_patterns, namespace='question', app_name='main')),
                           url(r'^blacklist/', include(client_blacklist_patterns, namespace='blacklist', app_name='main')),
                           url(r'^vkblacklist/', include(client_vkblacklist_patterns, namespace='vkblacklist', app_name='main')),
                           url(r'^tariff/', include(client_tariff_patterns, namespace='tariff', app_name='main')),
                           url(r'^payment/', include(client_payment_patterns, namespace='payment', app_name='main')),
                           url(r'^feedback$', FeedbackView_Client.as_view(), name='feedback'),
                           url(r'^abbr/', include(client_abbr_patterns, namespace='abbr', app_name='main')),
                           url(r'^service/', include(client_service_patterns, namespace='service', app_name='main')),
                           url(r'^stat/', include(client_stat_patterns, namespace='stat', app_name='main')),
                           url(r'^comment/', include(client_comment_patterns, namespace='comment', app_name='main')),
                           url(r'^password/', include(client_password_patterns, namespace='password', app_name='main')),
                           url(r'^promotion/', include(client_promotion_patterns, namespace='promotion', app_name='main')),
                           url(r'^promocode/', include(client_promocode_patterns, namespace='promocode', app_name='main')),
                           url(r'^referral/', include(client_referral_patterns, namespace='referral', app_name='main')),
                           url(r'^search-request/', include(moder_sr_patterns, namespace='search-request', app_name='main')),
                           )


urlpatterns = patterns('',
                       url(r'', include('registration.backends.default.urls')),
                       url(r'', include('django.contrib.auth.urls')),
                       )

moder_patterns = patterns('',
                       url(r'^$', LoginView_Moder.as_view()),
                       url(r'^login/$', LoginView_Moder.as_view()),
                       url(r'^login/ajax$', AjaxLoginView.as_view()),
                       url(r'^register/$', LoginView_Moder.as_view()),
                       url(r'^register/complete/$',RegisterCompleteView.as_view()),
                       url(r'^logout/$', LogoutView_Moder.as_view()),
                       url(r'^password_change/$', 'django.contrib.auth.views.password_change',
                           {'template_name': 'registration/moder/password_change_form.html'}),
                       url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done',
                           {'template_name': 'registration/moder/password_change_done.html'}),

                       url(r'', include('registration.backends.default.urls')),
                       url(r'', include('django.contrib.auth.urls')),

                       url(r'^client/', include(moder_panel_patterns, namespace='client', app_name='main')),
                       url(r'^phone/', include(phone_patterns, namespace='phone', app_name='main')),
                       url(r'^metro/', include(metro_patterns, namespace='metro', app_name='main')),
                       url(r'^district/', include(district_patterns, namespace='district', app_name='main')),
                       )
