"""Staging settings and globals."""


from os import environ

from base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

DEBUG = True

# ensure that celeryd is not run with DEBUG = True as it casues memory leak
if "celeryd" in sys.argv:
    DEBUG = False

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION

########## DATABASE CONFIGURATION
#DATABASES = {}
# Load external database module if it exists
try:
    from database import *
except ImportError:
    pass
########## END DATABASE CONFIGURATION

########## RAVEN CONFIGURATION
try:
    from raven_settings import *
    INSTALLED_APPS += RAVEN_APPS
    LOGGING = dict(LOGGING.items() + RAVEN_LOGGING.items())
except ImportError:
    pass
########## END RAVEN CONFIGURATION

########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
try:
    from cache_settings import *
except ImportError:
    pass
########## END CACHE CONFIGURATION

########## STATSD CONFIGURATION
# See: https://django-statsd.readthedocs.org/en/latest/#installation
try:
    from statsd_settings import *

    STATSD_CLIENT = 'django_statsd.clients.normal'

    INSTALLED_APPS += (
        'django_statsd'
    )

    MIDDLEWARE_CLASSES += (
        'django_statsd.middleware.GraphiteRequestTimingMiddleware',
        'django_statsd.middleware.GraphiteMiddleware',
    )

    STATSD_PATCHES = [
        'django_statsd.patches.db',
        'django_statsd.patches.cache',
    ]
except ImportError:
    pass
########## END STATSD CONFIGURATION

########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION
