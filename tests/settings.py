import os
from typing import List

import django

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = "NOTASECRET"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "ATOMIC_REQUESTS": True,
    },
    "other": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "ATOMIC_REQUESTS": True,
    },
}

ALLOWED_HOSTS: List[str] = []

INSTALLED_APPS = [
    "django.contrib.sites",
    "debug_toolbar",
    "mrbenn_panel",
]

MIDDLEWARE: List[str] = ["debug_toolbar.middleware.DebugToolbarMiddleware", ]

ROOT_URLCONF = "tests.urls"
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True

if django.VERSION < (4, 0):
    USE_L10N = True

SITE_ID = 1

USE_TZ = True

DEBUG_TOOLBAR_PANELS = [
    "mrbenn_panel.panel.MrBennPanel",
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/tests/templates'],
        'APP_DIRS': True,
    },
]