# Django settings for project project.

from os import path
import project as project_module

PROJECT_ROOT = path.dirname(path.realpath(project_module.__file__))

ADMINS = (
    ('Fry', 'fry@domain.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = []

SITE_ID = 1

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-RU'

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = path.join(PROJECT_ROOT, 'web/media')
MEDIA_URL = '/media/'

STATIC_ROOT = path.join(PROJECT_ROOT, 'web/static')
STATIC_URL = '/static/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '(l5g7tk1*3-ngtri_zhqp3_%1=ph5t&amp;03&amp;et*&amp;9ps269olo@3-'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'project.urls'

TEMPLATE_DIRS = (
    path.join(PROJECT_ROOT, 'templates/default'),
    path.join(PROJECT_ROOT, 'templates/default/layout')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'mptt',
    'south',

    'example',
)

