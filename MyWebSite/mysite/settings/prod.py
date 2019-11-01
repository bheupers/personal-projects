from __future__ import absolute_import, unicode_literals

from socket import gethostname, gethostbyname
from .base import *

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ALLOWED_HOSTS = ['192.168.178.*', 'localhost', '127.0.0.1', 'bartheupers.nl', 'www.bartheupers.nl', ]

try:
    from .local import *
except ImportError:
    pass
