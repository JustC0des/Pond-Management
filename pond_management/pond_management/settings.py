"""
Django settings for pond_management project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.templatetags.static import static

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j#01@f8cz*r9=azp2d!0^j$f2q8pvf71zyop%vrciki62n8=$u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["dceu0142"]


# Application definition

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'leaflet',
    'pond_management',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'pond_management.urls'

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

WSGI_APPLICATION = 'pond_management.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
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

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "pond_management/static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (51.1657, 10.4515),
    'DEFAULT_ZOOM': 6,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 20,
    'SCALE': 'both',
}

# Translations

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en', _('English')),
    ('de', _('German')),
    # Add other languages here
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]


UNFOLD = {
    "SITE_TITLE": _("Pond Management"),
    "SITE_HEADER": _("Pond Management"),
    "SITE_SUBHEADER": _("Manage your ponds and fishes"),
    "STYLES": [
        lambda request: static("css/style.css"),
    ],
    "SCRIPTS": [
        lambda request: static("js/script.js"),
    ],
    "SITE_ICON": lambda request: static("images/pond.png"),
    # "SITE_SYMBOL": "water",
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "16x16",
            "type": "image/x-icon",
            "href": lambda request: static("images/pond.png"),
        },
    ],
    "SHOW_LANGUAGES": True,
    "TABS": [
        {
            "page": "ponds",
            "models": [
                "pond_management.pond",
                "pond_management.fish",
                "pond_management.fishspecies",
                "pond_management.pondfish"
            ],
            "items": [
                {
                    "title": _("Fish Stock"),
                    "icon": "fish",
                    "link": reverse_lazy("admin:pond_management_pondfish_changelist"),
                },
                {
                    "title": _("Ponds"),
                    "icon": "water",
                    "link": reverse_lazy("admin:pond_management_pond_changelist"),
                },
                {
                    "title": _("Fish Species"),
                    "icon": "species",
                    "link": reverse_lazy("admin:pond_management_fishspecies_changelist"),
                },
                {
                    "title": _("Fishes"),
                    "icon": "shark",
                    "link": reverse_lazy("admin:pond_management_fish_changelist"),
                },
            ],
        },
    ],
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": _("Navigation"),
                "items": [
                    {
                        "title": _("Ponds"),
                        "icon": "water",
                        "link": reverse_lazy("admin:pond_management_pond_changelist"),
                    },
                    {
                        "title": _("Map"),
                        "icon": "map",
                        "link": reverse_lazy("admin:custom_view"),
                    },
                ],
            },
        ],
    },
}