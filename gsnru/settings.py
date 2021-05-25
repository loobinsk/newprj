# coding=utf8

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.contrib import messages
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

    ALLOWED_HOSTS = ['admin.bazavashdom.ru',
                    '212.109.220.150']

    ADMINS = (
        ('Admin', '5319777@gmail.com'),
        )

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
        'main',
        'online',
        'vashdom',
        'social_auth',
        'socialauthpatch',
        'debug_toolbar',
        'django_extensions',
        'walletone',
        'vkposting'
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
        'breadcrumbs.middleware.BreadcrumbsMiddleware',
        'breadcrumbs.middleware.FlatpageFallbackMiddleware',
        'main.middleware.TownMiddleware',
        'maintenancemode.middleware.MaintenanceModeMiddleware',
        'online.middleware.OnlineMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    ROOT_URLCONF = 'gsnru.urls'

    WSGI_APPLICATION = 'gsnru.wsgi.application'


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

    #DATABASE_ROUTERS = ['gsnru.dbrouter.MasterSlaveRouter']
    #ENABLE_RESERVE_DB = False

    SITE_ID = 5
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

    STATIC_ROOT = os.path.join(BASE_DIR, 'gsnru/static')
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

    STATICFILES_DIRS = (
        # os.path.join(BASE_DIR, 'gsnru/static'),
    )

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
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
        'main.context_processors.moder_panel',
    )

    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'gsnru/templates'),
    )

    #TEMPLATE_LOADERS = (
        #'django.template.loaders.filesystem.Loader',
        #'django.template.loaders.app_directories.Loader',
    #)

    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            #'admin_tools.template_loaders.Loader',
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
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
            'paystolog': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '/var/www/logs/paysto.log',
                'formatter': 'verbose',
                },
            'vkpost_piter': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '/var/www/logs/vkpost_piter.log',
                'formatter': 'verbose',
                },
            'avitolog': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '/var/www/logs/avitolog.log',
                'formatter': 'verbose',
                },
            'irrlog': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '/var/www/logs/irrlog.log',
                'formatter': 'verbose',
                },
            'multlog': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '/var/www/logs/multlog.log',
                'formatter': 'verbose',
                },
            'chancelog': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '/var/www/logs/chancelog.log',
                'formatter': 'verbose',
                },
            'autopostlog': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '/var/www/logs/autopost.log',
                'formatter': 'verbose',
                },
            'vashdomlog': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '/var/www/logs/vashdom.log',
                'formatter': 'verbose',
                },
            'vklog': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '/var/www/logs/vklog.log',
                'formatter': 'verbose',
                },
            'autoexam': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '/var/www/logs/autoexam.log',
                'formatter': 'verbose',
                },
            'stopagent': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '/var/www/logs/stopagent.log',
                'formatter': 'verbose',
                },
            'kvarnado': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '/var/www/logs/kvarnado.log',
                'formatter': 'verbose',
                },
            'domofond': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '/var/www/logs/domofond.log',
                'formatter': 'verbose',
                },
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
            'file': {
                'handlers': ['file'],
                'level': 'INFO',
                'propagate': True,
                },
            #'sorl.thumbnail.base': {
                #'handlers': ['file'],
                #'level': 'INFO',
                #'propagate': True,
            #},
            'paysto': {
                'handlers': ['paystolog'],
                'level': 'INFO',
                'propagate': True,
                },
            'vkpost_piter': {
                'handlers': ['vkpost_piter'],
                'level': 'INFO',
                'propagate': True,
                },
            'avito': {
                'handlers': ['avitolog'],
                'level': 'INFO',
                'propagate': True,
                },
            'irr': {
                'handlers': ['irrlog'],
                'level': 'INFO',
                'propagate': True,
                },
            'mult': {
                'handlers': ['multlog'],
                'level': 'INFO',
                'propagate': True,
                },
            'chance': {
                'handlers': ['chancelog'],
                'level': 'INFO',
                'propagate': True,
                },
            'autopost': {
                'handlers': ['autopostlog'],
                'level': 'INFO',
                'propagate': True,
                },
            'vashdom': {
                'handlers': ['vashdomlog'],
                'level': 'INFO',
                'propagate': True,
                },
            'vk': {
                'handlers': ['vklog'],
                'level': 'INFO',
                'propagate': True,
                },
            'autoexam': {
                'handlers': ['autoexam'],
                'level': 'INFO',
                'propagate': True,
                },
            'stopagent': {
                'handlers': ['stopagent'],
                'level': 'INFO',
                'propagate': True,
                },
            'kvarnado': {
                'handlers': ['kvarnado'],
                'level': 'INFO',
                'propagate': True,
                },
            'domofond': {
                'handlers': ['domofond'],
                'level': 'INFO',
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

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

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
    EMAIL_USE_TLS = True

    #NOTICE_REGISTER_EMAIL = ['Reg@gsnru.ru']
    #NOTICE_FEEDBACK_EMAIL = ['info@gsnru.ru']
    #NOTICE_RECLAME_EMAIL = ['Reklama@gsnru.ru']
    #NOTICE_REMOVE_EMAIL = ['del@gsnru.ru']
    #NOTICE_COMPLAIN_EMAIL = ['del@gsnru.ru']
    #NOTICE_SUPPORT_EMAIL = ['Support@gsnru.ru']
    #NOTICE_SUPPORT_MSK_EMAIL = ['msk@gsnru.ru']
    #NOTICE_SUPPORT_SPB_EMAIL = ['spb@gsnru.ru']

    EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

    # MESSAGES=========================================================
    MESSAGE_TAGS = {
        messages.DEBUG: 'alert-info',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-error',
        messages.ERROR: 'alert-error',
    }

    # AUTH USER =======================================================
    AUTH_USER_MODEL = 'uprofile.User'
    SILENCED_SYSTEM_CHECKS = ['auth.E003', 'auth.W004']

    LOGIN_URL          = '/login/'
    LOGIN_REDIRECT_URL = '/'
    LOGIN_ERROR_URL    = '/login/'

    #THUMBNAIL
    THUMBNAIL_QUALITY = 85
    THUMBNAIL_ENGINE = 'sorl_watermarker.engines.pil_engine.Engine'
    THUMBNAIL_WATERMARK = 'img/watermark.png'
    THUMBNAIL_WATERMARK_ALWAYS = False
    THUMBNAIL_WATERMARK_OPACITY = 0.5
    THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'

    # CACHE
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '172.18.0.1:11211',
            },
        'file': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': os.path.join(BASE_DIR, 'media/gsn-cache'),
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
                'DB': 2,
                'PARSER_CLASS': 'redis.connection.HiredisParser',
                'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
                'PICKLE_VERSION': -1,
            },
            'KEY_PREFIX': 'gsn:',
        },
    }

    CACHE_COUNT_TIMEOUT = 600
    CACHE_EMPTY_QUERYSETS = True


    # BREADCRUMB
    BREADCRUMBS_AUTO_HOME = True
    BREADCRUMBS_HOME_TITLE = 'Главная'

    # RECAPTCHA
    RECAPTCHA_PUBLIC_KEY = '6Le1EvMSAAAAAEeGY3RXbEyLvfGBr1wHealAEtEF'
    RECAPTCHA_PRIVATE_KEY = '6Le1EvMSAAAAAMKVPq8nm8PstRK0P3XQdJwT9C8J'


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

    from paysto import settings

    ROBOKASSA_LOGIN = 'bazavashdom.ru'
    ROBOKASSA_PASSWORD1 = 'lq3MF18fc3htKQPa1Woi'
    ROBOKASSA_PASSWORD2 = 'Fs2O9m6EtpZ6SThMwGZ9'
    ROBOKASSA_TEST_MODE = False
    ROBOKASSA_USE_POST = False
    ROBOKASSA_STRICT_CHECK = False

    MAINTENANCE_MODE = False
    MAINTENANCE_IGNORE_URLS = (
        r'^/adminpanel/.*',
    )


    # CELERY
    import djcelery
    djcelery.setup_loader()

    CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
    #BROKER_HOST = "localhost"
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
    CELERY_IMPORTS = ("main.task")
    CELERY_TIME_ZONE = 'Europe/Moskow'
    CELERY_IGNORE_RESULT = True
    CELERY_DEFAULT_QUEUE = 'default'
    # CELERY_DEFAULT_ROUTING_KEY = 'default'

    CELERY_QUEUES = {
        'default': {
            'exchange': 'default',
        },
        'parser': {
            'exchange': 'parser',
        },
        'vk': {
            'exchange': 'vk',
        },
        'exams': {
            'exchange': 'exams',
        },
        'post': {
            'exchange': 'post',
        },
        'vashdom': {
            'exchange': 'vashdom',
        }
    }

    # MODERATE PANEL
    MODER_PANEL_DOMAIN = 'admin.bazavashdom.ru'

    # ASSETS
    ASSETS_ROOT = os.path.join(BASE_DIR, 'gsnru/static')
    ASSETS_URL = '/static/'
    ASSETS_DEBUG = False


    # Настройки автопоиска
    SEARCH_REQUEST_COUNT_LIMIT = 20
    SEARCH_REQUEST_NOTICE_LIMIT = 5


    CAPTCHA_OUTPUT_FORMAT = u'<label>Введите символы с картинки</label> %(image)s ' \
                            u'<button class="btn btn-refresh-captcha"><span class="glyphicon glyphicon-refresh" aria-hidden="true"></span></button>' \
                            u'%(hidden_field)s %(text_field)s'


    ONLINE_COUNT_TIMEOUT = 60*15


    # Архив
    ARCHIVE_LEASE_DAYS = 7
    ARCHIVE_SALE_DAYS = 180

    # Авторизация парсера ВК
    VK_ACCESS_TOKEN = '24afb8e624afb8e624afb8e6b724f3ca48224af24afb8e67d9e574d4fe876c32785b540'

    # Настройки парсера Вконтакте
    VK_PARSER_LOGIN = '79684715519'
    VK_PARSER_PASS = 'ljdfnbz9d8NDSck'

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

    TEMPLATE_LOADERS = (
        #'admin_tools.template_loaders.Loader',
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    INTERNAL_IPS = ('127.0.0.1', '192.168.32.1')

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': 'memcached:11211',
            },
        'file': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': os.path.join(BASE_DIR, 'media/gsn-cache'),
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
            'KEY_PREFIX': 'gsn:',
        },
    }

    BROKER_URL = 'redis://redis:6379/1'
    CELERY_RESULT_BACKEND = 'redis://redis:6379/1'
    BROKER_HOST = "redis"

    MODER_PANEL_DOMAIN = 'localhost:8000'

    TEMPLATE_LOADERS = (
        #'admin_tools.template_loaders.Loader',
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    THUMBNAIL_REDIS_HOST = 'redis'