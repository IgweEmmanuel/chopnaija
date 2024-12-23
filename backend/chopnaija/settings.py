"""
Django settings for chopnaija project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

from datetime import timedelta

import os
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^h&u&$flrojnm8*v5a@nn2n!%j+n!ogd2&0)(c&mxtkbi_o+zq'



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["myshop-api-k2yc.onrender.com", "localhost", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop_app',
    'rest_framework',
    "drf_spectacular",
    'core',
    'corsheaders',
    'rest_framework_simplejwt',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chopnaija.urls'

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

WSGI_APPLICATION = 'chopnaija.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = 'img/'
MEDIA_ROOT = BASE_DIR/"media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "core.CustomUser"

CORS_ALLOWED_ORIGINS = [
"http://localhost:5173",
"http://localhost:5174",
"http://localhost:5175"
]

CORS_ALLOW_CREDENTIALS = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60)
}


SPECTACULAR_SETTINGS = {
    'TITLE': 'Product API',
    'DESCRIPTION': 'API for managing products, categories, and related data',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
    }
}

JAZZMIN_SETTINGS = {
    "site_brand": "ChopNaija",
    "welcome_sign": "Welcome to ChopNaija",
    "copyright": "ChopNaija",
    "site_brand_short": "CN",
    "welcome_sign": "Welcome to ChopNaija",
    "copyright": "ChopNaija",
    "site_brand": "ChopNaija",
    "site_icon": "img/logo.png",
    "welcome_sign": "Welcome to ChopNaija",
    "copyright": "ChopNaija",
    "side_header": "ChopNaija",
    "site_brand": "ChopNaija",
    "site_icon": "img/logo.png",
    "welcome_sign": "Welcome to ChopNaija",
    "copyright": "ChopNaija",
    "show_sidebar": True,
    "sidebar_fixed": True,
    "sidebar_title": True,
    "sidebar_nav_small_text": True,
    "sidebar_footer": True,
    "sidebar_nav_small_text": True,
    "sidebar_nav_small_text": True,
    "sidebar_nav_small_text": True,
    "sidebar_nav_small_text": True,
}

FLUTTERWAVE_SECRET_KEY = "FLWSECK_TEST-825d260605a1fb0170d7af0cc15520f5-X"



# settings.py

PAYPAL_CLIENT_ID = 'AUFAAAZmMXFnD3XQJs9JsS2H2kNKUypugbRuUpuQGGe_HUJtHTM9xg2k30pjNYG0YeSdpuvYO_0sUOPy'
PAYPAL_CLIENT_SECRET = 'EK9s6BVZ3An7zhw_19fW_5c_gMreGrqc2b-r__9huHwl8yeDsl2_ej4t-mPAJvEWPvFCThmZiBD5oVDX'
PAYPAL_MODE = 'sandbox'  # or 'live' when you are ready for production

REACT_BASE_URL = os.getenv("REACT_BASE_URL", "http://localhost:5173")