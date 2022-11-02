"""
Generated by 'django-admin startproject' using Django 4.1.2.
"""
import os
from pathlib import Path
import mimetypes

from dotenv import load_dotenv

mimetypes.add_type("application/javascript", ".js", True)

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(Path(BASE_DIR, '.env'))

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',

    'core.apps.CoreConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Path(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    Path(BASE_DIR, 'static'),
]

DEFAULT_ACCOUNTS = {
    'Card': 1000,
    'Cash': 1000,
}
DEFAULT_INCOME_CATEGORIES = ('Salary', 'Presents', 'Prize', 'Debt')
DEFAULT_EXPENSE_CATEGORIES = (
    'Products',
    'Hygiene',
    'Canteen',
    'Restaurant',
    'Transport',
    'Clothes',
    'Shoes',
    'Rent',
    'Public services',
    'Internet services',
    'Devices',
    'Presents',
    'Debt',
)

CORS_ORIGIN_ALLOW_ALL = True

# Settings for command 'python manage.py generatenotes'
INCOME_NOTES_COUNT = 200
EXPENSE_NOTES_COUNT = 200
DAYS_RANGE = (-365, 1)
COUNT_RANGE = (500, 1000)