# -*- coding: utf-8 -*-
from django.core.management.utils import get_random_secret_key

import environ
from decouple import Csv, config
from dj_database_url import parse as db_url

# --------------------------------------------------- Basics
env = environ.Env()
root = environ.Path(__file__) - 3

BASE_DIR = root()

SECRET_KEY = config("DJANGO_SECRET_KEY", default=get_random_secret_key())
DEBUG = config("DJANGO_DEBUG", cast=bool, default=False)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv(), default="localhost")


LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

ROOT_URLCONF = "project.urls"
WSGI_APPLICATION = "project.wsgi.application"

# --------------------------------------------------- Apps

LOCAL_APPS = ["api", "project"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_yasg",
] + LOCAL_APPS


# --------------------------------------------------- Databases

DATABASES = {
    "default": config(
        "DATABASE_URLs", default="sqlite:///" + (root)("db.sqlite3"), cast=db_url
    )
}


# --------------------------------------------------- Statics

STATIC_URL = env("STATIC_URL", default="/static/")
STATIC_ROOT = env("STATIC_ROOT", default=(root)("static"))
MEDIA_URL = env("MEDIA_URL", default="/media/")
MEDIA_ROOT = env("MEDIA_ROOT", default=(root)("media"))


# --------------------------------------------------- Rest settings

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}


# --------------------------------------------------- Middleware

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# --------------------------------------------------- Other

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
