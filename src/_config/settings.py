"""
Django settings for _config project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import sys
from pathlib import Path

from django.utils.translation import gettext_lazy as _
from environs import Env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env(override=True)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ## Sitemaps.
    'django.contrib.sitemaps',
    # External.
    'django_bootstrap5',
    'rosetta',
    # Apps.
    'accounts',
    'base',
    'home',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # GZip.
    'django.middleware.gzip.GZipMiddleware',
    # Whitenoise.
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Locales.
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = '_config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '_config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {'default': env.dj_db_url('DATABASE_URL')}
match DATABASES['default']['ENGINE']:
    case 'django.db.backends.postgresql':
        DATABASES['OPTIONS'] = {
            'conn_max_age': 600,
            'conn_health_checks': True,
        }
    case 'django.db.backends.mysql':
        DATABASES['OPTIONS'] = {
            'charset': 'utf8mb4',
            'init_command': 'SET default_storage_engine=INNODB',
        }
    case 'django.db.backends.sqlite3':
        DATABASES['OPTIONS'] = {
            'transaction_mode': 'IMMEDIATE',
            'init_command': 'PRAGMA journal_mode=WAL;PRAGMA synchronous=NORMAL;',
        }
    case _:
        pass

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = 'pt-BR'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Rosetta.
LANGUAGES = [
    ('en-US', _('English')),
    ('pt-BR', _('Brazilian Portuguese')),
]
LOCALE_PATHS = (BASE_DIR / 'locale',)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = '/public/staticfiles/'
STATIC_ROOT = BASE_DIR.parent / 'public' / 'staticfiles'

MEDIA_URL = '/public/media/'
MEDIA_ROOT = BASE_DIR.parent / 'public' / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

if DEBUG:
    # Django debug toolbar.
    INTERNAL_IPS = ['127.0.0.1', 'localhost']
    TESTING = 'test' in sys.argv
    if not TESTING:
        INSTALLED_APPS.append('debug_toolbar')
        MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
