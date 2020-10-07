"""
Django settings for upscbasicfunda project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1c37q-d$w#nt9hw5d#detc!kf=n@4bv*+1@&-&3)o2hnxg2jvw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['upscbasicfunda.herokuapp.com', 'localhost', 'upscbasicfunda.com','upscbasicfunda.in', 'www.upscbasicfunda.com', 'www.upscbasicfunda.in', "15.207.106.26", "api.upscbasicfunda.com", "127.0.0.1","http://53a9679257f8.ngrok.io"]
ALLOWED_HOSTS =['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    'corsheaders',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'django.contrib.sites',
    'django_celery_results',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'nested_admin',
    # "kombu.transport.django",


    'core',
    'blog',
    'quiz',
    'cart',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'upscbasicfunda.urls'

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

WSGI_APPLICATION = 'upscbasicfunda.wsgi.application'

# from __future__ import absolute_import

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
 'django.contrib.auth.backends.ModelBackend',
 'allauth.account.auth_backends.AuthenticationBackend',
 )

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

CORS_ORIGIN_ALLOW_ALL = True


SITE_ID = 1

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_venv')]
STATICFILES_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DATETIME_FORMAT': "%b %d %Y %H:%M:%S",
}

CSRF_COOKIE_NAME = "csrftoken"


# ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_USERNAME_REQUIRED = False
AUTH_USER_MODEL = 'core.User'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'core.serializers.UserSerializer',
    'TOKEN_SERIALIZER': 'core.serializers.TokenSerializer',
    'PASSWORD_RESET_SERIALIZER':'PasswordResetSerializer',
}

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'core.serializers.CustomRegisterSerializer',
}


RAZORPAY_KEY_ID = "rzp_test_d60JA5dzjyDyZ0"
RAZORPAY_KEY_SECRET = "Kj6MjRcvzX30fZXfpTqhpgU0"

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "1059696678278-alrfk4hk0jvpu3hqcok9vjr7fnnbtf6r.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET ="9eaJWRlPNhOOTFaSJfnaCyV0"


# EMAIL
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'upscbasicfunda@gmail.com'
EMAIL_HOST_PASSWORD = 'upscupscupsc_1234'
DEFAULT_FROM_EMAIL = 'UpscBasicFunda Team <noreply@upscbasicfunda.com>'

# CELERY STUFF
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND='django-cache'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

#google login 
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}


