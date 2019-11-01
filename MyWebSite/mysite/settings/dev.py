from __future__ import absolute_import, unicode_literals

from socket import gethostname, gethostbyname
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]

INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE
INTERNAL_IPS = ['127.0.0.1']

try:
    from .local import *
except ImportError:
    pass
