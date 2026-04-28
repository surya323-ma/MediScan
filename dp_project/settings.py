from pathlib import Path
<<<<<<< HEAD
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-m!6#-fa61_up-bh-t33r(0w7@pwh_dhw-tb^13hrt+p&q0tvnh')

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

=======

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-m!6#-fa61_up-bh-t33r(0w7@pwh_dhw-tb^13hrt+p&q0tvnh'
DEBUG = True
>>>>>>> 9582de5a67a4aacc8cf569d14565f2d2b725f814
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dpapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
<<<<<<< HEAD
    'whitenoise.middleware.WhiteNoiseMiddleware',
=======
>>>>>>> 9582de5a67a4aacc8cf569d14565f2d2b725f814
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dp_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dp_project.wsgi.application'

<<<<<<< HEAD
# Database — uses DATABASE_URL env var on Render, else SQLite locally
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
=======
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
>>>>>>> 9582de5a67a4aacc8cf569d14565f2d2b725f814

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
<<<<<<< HEAD

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

=======
STATIC_URL = '/static/'
>>>>>>> 9582de5a67a4aacc8cf569d14565f2d2b725f814
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
