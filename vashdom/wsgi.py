"""
WSGI config for gsnru project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vashdom.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", 'Prod')

# if os.environ.get('PTVSD', 'False') == 'True':
#     import ptvsd
#     ptvsd.enable_attach('dev', address = ('0.0.0.0', 3000))

# from django.core.wsgi import get_wsgi_application
from configurations.wsgi import get_wsgi_application
application = get_wsgi_application()
