from .base import *

DEBUG = False
ALLOWED_HOSTS = ['zfun.woooo.tech']
MEDIA_ROOT = '/var/opt/hackergame/media'
STATIC_ROOT = '/var/opt/hackergame/static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hackergame',
        'USER': 'hackergame',
        'CONN_MAX_AGE': 0,
        'ATOMIC_REQUESTS': True,
        'HOST': 'postgres',
        'PORT': 6432,
    },
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': 'memcached:11211',
        'TIMEOUT': 3600,
        'KEY_PREFIX': 'hackergame',
    },
}
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_COOKIE_AGE = 365 * 86400
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
        'request': {
            'format': '%(asctime)s %(ip)s %(userid)s %(levelname)s %(message)s',
        },
    },
    'filters': {
        'add_user_info': {
            '()': 'frontend.utils.UserInfoFilter'
        },
    },
    'handlers': {
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'frontend.utils.ThrottledAdminEmailHandler',
        },
        'request': {
            'class': 'logging.StreamHandler',
            'formatter': 'request',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['mail_admins', 'django.server'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'filters': ['add_user_info'],
            'handlers': ['request'],
            'propagate': False,
        },
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = SMTP_HOSTNAME
EMAIL_PORT = 587
EMAIL_HOST_USER = SMTP_USERNAME
EMAIL_HOST_PASSWORD = SMTP_PASSWORD
EMAIL_USE_TLS = False
