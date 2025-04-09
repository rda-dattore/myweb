from .base import *
from . import local_settings  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']


try:
    from .local import *
except ImportError:
    pass
