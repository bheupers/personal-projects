from __future__ import absolute_import, unicode_literals

from socket import gethostname, gethostbyname
from .base import *

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ALLOWED_HOSTS = ['127.0.0.1', gethostname(), gethostbyname(gethostname()), ]

try:
    from .local import *
except ImportError:
    pass