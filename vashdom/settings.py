# coding=utf8

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.contrib import messages
from kombu import Exchange, Queue
from configurations import Configuration

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Prod(Configuration):
    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'da5@exqb2g5ymmiiq9@jj7z1$z301qf#p7)ik#f1^h$l48#r8o'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = os.environ.get('DEBUG') == '1'
    TEMPLATE_DEBUG = False
    THUMBNAIL_DEBUG = False

    ALLOWED_HOSTS = ['212.109.220.150', 'bazavashdom.ru', 'XN--80AAABHNR8BR2H.XN--P1AI']

    ADMINS = [
        ('Администратор', '5319777@gmail.com'),
    ]


    # Application definition

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'user_sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        #'admin_tools',
        #'admin_tools.theming',
        #'admin_tools.menu',
        #'admin_tools.dashboard',
        'django.contrib.admin',
        'django.contrib.admindocs',

        'debug_toolbar',
        'breadcrumbs',
        'maintenancemode',
        'django.contrib.sitemaps',
        'django.contrib.flatpages',
        'annoying',
        'registration',
        'bootstrap_pagination',
        'captcha',
        'sorl.thumbnail',
        'sorl_watermarker',
        'mptt',
        'ckeditor',
        'paysto',
        'robokassa',
        'uprofile',
        'uimg',
        'uvideo',
        'ufile',
        'gutils',
        'mail_templated',
        'ucomment',
        'djcelery',
        'djcelery_email',
        'django_assets',
        'slugify',
        #'static_precompiler',
        'main',
        'online',
        'vashdom',
        'social_auth',
        'socialauthpatch',
        'django_extensions',
        'rest_framework',
        'walletone',
        'vkposting',
        'smsgate',
        # 'social.apps.django_app.default',
    )

    MIDDLEWARE_CLASSES = (
        #'main.middleware.DbTestMiddleware',
        'user_sessions.middleware.SessionMiddleware',
        'main.middleware.ModerMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'maintenancemode.middleware.MaintenanceModeMiddleware',
        'breadcrumbs.middleware.BreadcrumbsMiddleware',
        'breadcrumbs.middleware.FlatpageFallbackMiddleware',
        'main.middleware.TownMiddleware',
        'main.middleware.ReferralMiddleware',
        'online.middleware.OnlineMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    ROOT_URLCONF = 'vashdom.urls'
    APPEND_SLASH = True

    WSGI_APPLICATION = 'vashdom.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/1.6/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'vd',
            'USER': 'vd',
            'PASSWORD': 'JwuCin7cXvq3pr',
            'HOST': '172.18.0.1',
            'CONN_MAX_AGE': 500,
        }
    }

    #DATABASE_ROUTERS = ['vashdom.dbrouter.MasterSlaveRouter']
    #ENABLE_RESERVE_DB = False

    SITE_ID = 5     #vashdom
    SERVER_ID = 1

    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/

    LANGUAGE_CODE = 'ru-RU'

    TIME_ZONE = 'Europe/Moscow'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = False


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.6/howto/static-files/

    STATIC_ROOT = os.path.join(BASE_DIR, 'vashdom/static')
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

    STATICFILES_DIRS = (
        # os.path.join(BASE_DIR, 'vashdom/static'),
    )

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
        #'static_precompiler.finders.StaticPrecompilerFinder'
    )


    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.csrf',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.request',
        'django.core.context_processors.static',
        'django.contrib.messages.context_processors.messages',
        'main.context_processors.current_town',
        # 'main.context_processors.moder_panel',
        # 'agent24.context_processors.agent24_panel',
        #'social_auth.context_processors.social_auth_by_name_backends',
        'social_auth.context_processors.social_auth_backends',
        #'social_auth.context_processors.social_auth_by_type_backends',
        'social_auth.context_processors.social_auth_login_redirect',
    )

    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'vashdom/templates'),
    )

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        #'admin_tools.template_loaders.Loader',
    )


    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': '/var/www/logs/debug.log',
                'formatter': 'verbose',
            },
            'import': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': '/var/www/logs/import.log',
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins', 'file'],
                'level': 'ERROR',
                'propagate': True,
            },
            'file': {
                'handlers': ['file'],
                'level': 'INFO',
                'propagate': True,
            },
            'walletone.views': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'import': {
                'handlers': ['import'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s: %(message)s'
            }
        }
    }

    # DEBUG TOOLBAR ===============================================
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'JQUERY_URL': None
        }

    INTERNAL_IPS = ('127.0.0.1', '*')

    # EMAIL =========================================================
    ACCOUNT_ACTIVATION_DAYS = 2 # кол-во дней для хранения кода активации
    # для отправки кода активации
    AUTH_USER_EMAIL_UNIQUE = True
    SERVER_EMAIL = 'noreply2@bazavashdom.ru'
    EMAIL_HOST = 'smtp.yandex.ru'
    EMAIL_PORT = 25
    EMAIL_HOST_USER = 'noreply2@bazavashdom.ru'
    EMAIL_HOST_PASSWORD = 'v1001122V'
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = 'БазаВашДом <noreply2@bazavashdom.ru>'

    EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

    NOTICE_COMPLAIN_EMAIL = ['Info@bazavashdom.ru']
    NOTICE_FEEDBACK_EMAIL = ['Info@bazavashdom.ru']

    # MESSAGES=========================================================
    MESSAGE_TAGS = {
        messages.DEBUG: 'alert-info',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-error',
        messages.ERROR: 'alert-error',
    }

    # AUTH USER =======================================================
    AUTH_USER_MODEL = 'vashdom.VashdomUser'
    SOCIAL_AUTH_USER_MODEL = 'vashdom.VashdomUser'
    SILENCED_SYSTEM_CHECKS = ['auth.E003', 'auth.W004']

    AUTHENTICATION_BACKENDS = (
        # 'social_auth.backends.twitter.TwitterBackend',
        # 'social_auth.backends.facebook.FacebookBackend',
        'social_auth.backends.google.GoogleOAuth2Backend',
        # 'social_auth.backends.yahoo.YahooBackend',
        # 'social_auth.backends.browserid.BrowserIDBackend',
        # 'social_auth.backends.contrib.linkedin.LinkedinBackend',
        # 'social_auth.backends.contrib.disqus.DisqusBackend',
        # 'social_auth.backends.contrib.livejournal.LiveJournalBackend',
        # 'social_auth.backends.contrib.orkut.OrkutBackend',
        # 'social_auth.backends.contrib.foursquare.FoursquareBackend',
        # 'social_auth.backends.contrib.github.GithubBackend',
        'social_auth.backends.contrib.vk.VKOAuth2Backend',
        # 'social_auth.backends.contrib.live.LiveBackend',
        # 'social_auth.backends.contrib.skyrock.SkyrockBackend',
        # 'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
        # 'social_auth.backends.contrib.readability.ReadabilityBackend',
        # 'social_auth.backends.contrib.fedora.FedoraBackend',
        # 'social_auth.backends.OpenIDBackend',
        'django.contrib.auth.backends.ModelBackend',
    )

    SOCIAL_AUTH_PIPELINE = (
        'social_auth.backends.pipeline.social.social_auth_user',
        #'social_auth.backends.pipeline.associate.associate_by_email',
        'social_auth.backends.pipeline.user.get_username',
        'social_auth.backends.pipeline.user.create_user',
        'social_auth.backends.pipeline.social.associate_user',
        'social_auth.backends.pipeline.social.load_extra_data',
        'social_auth.backends.pipeline.user.update_user_details',
        'uprofile.models.load_user_image',
        'uprofile.models.social_user_referral'
    )

    LOGIN_URL          = '/login/'
    LOGIN_REDIRECT_URL = '/profile/'
    LOGIN_ERROR_URL    = '/login/'

    VK_APP_ID = '4933745'
    VK_API_SECRET = 'LPNPorgvGCwk6NFbt24d'
    VK_ACCESS_TOKEN = '24afb8e624afb8e624afb8e6b724f3ca48224af24afb8e67d9e574d4fe876c32785b540'

    GOOGLE_OAUTH2_CLIENT_ID = '988740791815-kv4e2k3vfemmpfq5263vr6lk45v65vu4.apps.googleusercontent.com'
    GOOGLE_OAUTH2_CLIENT_SECRET = 'RwhmAnGwV53XLHxGkGG7VBzm'

    SOCIAL_AUTH_SESSION_EXPIRATION = False

    #THUMBNAIL
    THUMBNAIL_QUALITY = 85
    THUMBNAIL_ENGINE = 'sorl_watermarker.engines.pil_engine.Engine'
    #THUMBNAIL_WATERMARK = 'img/watermark.png'
    THUMBNAIL_WATERMARK_ALWAYS = False
    THUMBNAIL_WATERMARK_OPACITY = 0.5
    THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
    THUMBNAIL_REDIS_HOST = '172.18.0.1'


    # CACHE
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '172.18.0.1:11211',
            },
        'file': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': os.path.join(BASE_DIR, 'media/vashdom-cache'),
        },
        'cache_machine': {
            'BACKEND': 'caching.backends.memcached.MemcachedCache',
            'LOCATION': '172.18.0.1:11211',
            'KEY_PREFIX': 'cm:',
        },
        'redis': {
            'BACKEND': 'redis_cache.backends.single.RedisCache',
            'LOCATION': '172.18.0.1:6379',
            'OPTIONS': {
                'DB': 1,
                'PARSER_CLASS': 'redis.connection.HiredisParser',
                'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
                'PICKLE_VERSION': -1,
            },
            'KEY_PREFIX': 'vd:',
        },
    }

    CACHE_COUNT_TIMEOUT = 600
    CACHE_EMPTY_QUERYSETS = True


    # BREADCRUMB
    BREADCRUMBS_AUTO_HOME = True
    BREADCRUMBS_HOME_TITLE = 'Главная'


    # CKEDITOR
    CKEDITOR_UPLOAD_PATH = os.path.join(BASE_DIR, 'media')
    CKEDITOR_RESTRICT_BY_USER = True

    CKEDITOR_CONFIGS = {
        'default': {
            'toolbar': [
                ['Undo', 'Redo',
                '-', 'Bold', 'Italic', 'Underline',
                '-', 'Format',
                ],
                ['Link', 'Unlink', 'Anchor'],
                ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
                ['-', 'BulletedList', 'NumberedList',
                '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord',
                '-', 'SpecialChar',
                '-', 'Source',
                ],
                ],
            'width': 840,
            'height': 300,
            'toolbarCanCollapse': False,
            }
    }



    # COOKIES
    # SESSION_COOKIE_DOMAIN = 'localhost'
    SESSION_ENGINE = 'user_sessions.backends.db'


    PAYSTO_SHOP_ID = 0
    PAYSTO_PAYMENT_MODEL = 'main.Payment'

    ROBOKASSA_LOGIN = 'bazavashdom.ru'
    ROBOKASSA_PASSWORD1 = 'lq3MF18fc3htKQPa1Woi'
    ROBOKASSA_PASSWORD2 = 'Fs2O9m6EtpZ6SThMwGZ9'
    ROBOKASSA_TEST_MODE = False
    ROBOKASSA_USE_POST = False
    ROBOKASSA_STRICT_CHECK = False

    DJANGO_W1_MERCHANT_ID = '159731934390'
    DJANGO_W1_SIGN_METHOD = 'md5'
    DJANGO_W1_SECRET_KEY = '426b4450505b6c5130426977755c435c736e455b694d48735f4c7a'
    DJANGO_W1_SUCCESS_URL = 'https://bazavashdom.ru/payment/success/'
    DJANGO_W1_FAIL_URL = 'https://bazavashdom.ru/payment/fail/'
    DJANGO_W1_CURRENCY_DEFAULT = '643'

    from paysto import settings

    # CELERY
    import djcelery
    djcelery.setup_loader()

    CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
    #BROKER_HOST = "192.168.10.1"
    #BROKER_PORT = 5672
    #BROKER_USER = "celery"
    #BROKER_PASSWORD = "celery"
    #BROKER_VHOST = "gsnru"
    BROKER_URL = 'redis://172.18.0.1:6379/1'
    CELERY_RESULT_BACKEND = 'redis://172.18.0.1:6379/1'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    BROKER_HOST = "172.18.0.1"
    BROKER_PORT = 6379
    CELERY_BACKEND = "amqp"
    CELERY_IMPORTS = ('vashdom.tasks',)
    CELERY_TIME_ZONE = 'Europe/Moscow'
    CELERY_DEFAULT_QUEUE = 'vashdom'
    CELERY_IGNORE_RESULT = True
    # CELERY_DEFAULT_ROUTING_KEY = 'vashdom'

    from celery.schedules import crontab
    from datetime import timedelta
    CELERY_QUEUES = {
        'vashdom': {
            # 'exchange': 'vashdom',
            'routing_key': 'vashdom',
        },
    }
    CELERY_ROUTES = {
            'vashdom.tasks.forgotten_payments': {
                'queue': 'vashdom',
            },
            'vashdom.tasks.request_to_client': {
                'queue': 'vashdom',
            },
            'vashdom.tasks.import_from_vashdom': {
                'queue': 'vashdom',
            },
    }
    CELERYBEAT_SCHEDULE = {
        'vashdom.tasks.forgotten_payments': {
            'task': 'vashdom.tasks.forgotten_payments',
            'schedule': crontab(hour=12, minute=0),
        },
        # 'vashdom.tasks.import_from_vashdom': {
        #     'task': 'vashdom.tasks.import_from_vashdom',
        #     'schedule': timedelta(hours=1),
        # },
    }


    # MODERATE PANEL
    MODER_PANEL_DOMAIN = 'admin.bazavashdom.ru'


    # ASSETS
    ASSETS_ROOT = os.path.join(BASE_DIR, 'vashdom/static')
    ASSETS_URL = '/static/'
    ASSETS_DEBUG = False


    # Настройки автопоиска
    SEARCH_REQUEST_COUNT_LIMIT = 20
    SEARCH_REQUEST_NOTICE_LIMIT = 5


    CAPTCHA_OUTPUT_FORMAT = u'<label>Введите символы с картинки</label> %(image)s ' \
                            u'<button class="btn btn-refresh-captcha"><span class="glyphicon glyphicon-refresh" aria-hidden="true"></span></button>' \
                            u'%(hidden_field)s %(text_field)s'

    COMMENT_AUTHORIZATION = True

    ONLINE_COUNT_TIMEOUT = 60*15


    # Архив
    ARCHIVE_LEASE_DAYS = 30
    ARCHIVE_SALE_DAYS = 180


    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        ],
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 30
    }

    SMSGATE = {
        'DEBUG': False,
        'DEFAULT_GATE': 'ALOHASMS',
        'ALOHASMS': {
            'LOGIN': '5319777@gmail.com',
            'PASSWORD': 'Cklsnfdk7l2tlg4',
            'SENDER': 'VIRTA'
        },
        'EMAIL': {
            'MAILTO': 'forkhammer@gmail.com'
        }
    }


class Dev(Prod):
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    THUMBNAIL_DEBUG = DEBUG

    ALLOWED_HOSTS = []

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'HOST': 'postgresql',
            'NAME': 'vd',
            'USER': 'postgres',
            'PASSWORD': '1'
        }
    }

    INTERNAL_IPS = ('127.0.0.1', '172.23.0.1')

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': 'memcached:11211',
            },
        'file': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': os.path.join(BASE_DIR, 'media/vashdom-cache'),
        },
        'cache_machine': {
            'BACKEND': 'caching.backends.memcached.MemcachedCache',
            'LOCATION': 'memcached:11211',
            'KEY_PREFIX': 'cm:',
        },
        'redis': {
            'BACKEND': 'redis_cache.backends.single.RedisCache',
            'LOCATION': 'redis:6379',
            'OPTIONS': {
                'DB': 2,
                'PARSER_CLASS': 'redis.connection.HiredisParser',
                'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
                'PICKLE_VERSION': -1,
            },
            'KEY_PREFIX': 'vd:',
        },
    }

    BROKER_URL = 'redis://redis:6379/1'
    CELERY_RESULT_BACKEND = 'redis://redis:6379/1'
    BROKER_HOST = "redis"

    THUMBNAIL_REDIS_HOST = 'redis'


class Test(Prod):
    ALLOWED_HOSTS = ['212.109.220.150', 'test.bazavashdom.ru']

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '172.18.0.1:11211',
            'KEY_PREFIX': 'test:',
            },
        'file': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': os.path.join(BASE_DIR, 'media/vashdom-cache'),
        },
        'cache_machine': {
            'BACKEND': 'caching.backends.memcached.MemcachedCache',
            'LOCATION': '172.18.0.1:11211',
            'KEY_PREFIX': 'testcm:',
        },
        'redis': {
            'BACKEND': 'redis_cache.backends.single.RedisCache',
            'LOCATION': '172.18.0.1:6379',
            'OPTIONS': {
                'DB': 3,
                'PARSER_CLASS': 'redis.connection.HiredisParser',
                'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
                'PICKLE_VERSION': -1,
            },
            'KEY_PREFIX': 'testvd:',
        },
    }