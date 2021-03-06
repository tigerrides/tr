"""
Django settings for tr project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import psycopg2

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0$0r3abyzpwp0s6fm7uc@8%!4d4+b%spr%lyfvglpqsm3bne^i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'login.apps.LoginConfig',
    'create_ride.apps.CreateRideConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'uniauth',
    'star_ratings',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #'django.template.context_processors.media',
                #'django.core.context_processors.request',
            ],
        },
    },
]

TEMPLATE_CONTEXT_PROCESSORS = [
   'django.core.context_processors.request',
]

WSGI_APPLICATION = 'tr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#DATABASE_URL = os.environ['DATABASE_URL']
#conn = psycopg2.connect(DATABASE_URL, sslmode='require')
#DATABASES = { 
 #       'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
 #       }

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.postgresql',
    #    'NAME': os.path.join(BASE_DIR, 'postgres_db'),
    #}

 #   'default': {
  #      'ENGINE': 'django.db.backends.postgresql_psycopg2',
   #     'NAME': 'DATABASE',
    #    'USER': '',
     #   'PASSWORD': os.environ.get('DB_PASS', ''),
      #  'HOST': 'localhost',
       # 'PORT': '5432',
   # }
}

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'LogInInformation',
        # 'USER': 'admin',
        # 'PASSWORD': 'GoTigers123',
        # 'HOST': 'localhost',
        # 'PORT': '5432',

        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# This will be overwritten when we import dj_database_url
# DATABASES['default'] = {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME' : os.path.join(BASE_DIR, 'db.sqlite3')
# }

# for dj_database_url
#db_from_env = dj_database_url.config()
#DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

#PARSE database configuration from $DATABASE_URL
#COMMENT THIS BACK 
import dj_database_url
DATABASE_URL = os.getenv('DATABASE_URL')
DATABASES['default'] = dj_database_url.parse(DATABASE_URL)

# enable HTTPS
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# allow all host headers
ALLOWED_HOSTS = ['*']


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#django_heroku.settings(locals())

# for now it redirects to homepage after login, will change
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/home/'
UNIAUTH_LOGIN_DISPLAY_STANDARD = False
UNIAUTH_LOGOUT_CAS_COMPLETELY = True

# specify path to media directory for user uploaded static data
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/'

# # added for CAS authentication
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'uniauth.backends.CASBackend',
]

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'princetontigerrides@gmail.com'
EMAIL_HOST_PASSWORD = 'bcjbzdidbihjnzks'
