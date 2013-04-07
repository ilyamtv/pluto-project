
from project.conf.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        'NAME': 'fry-project',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'init_command': 'SET names "utf8"',
            },
        }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
    }
}
