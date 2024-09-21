"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from decouple import config
from django.contrib import messages
from pathlib import Path


#Kaniko Build number 
BUILD_NUMBER =  os.environ.get('BUILD_NUMBER', config('BUILD_NUMBER', default='localhost'))
DEMO_VERSION_WATERMARK =  True if os.environ.get('DEMO_VERSION_WATERMARK', config('DEMO_VERSION_WATERMARK', default="False")).lower() == 'true' else False  
DEBUG_INFORMATION_SHOW =  True if os.environ.get('DEBUG_INFORMATION_SHOW', config('DEBUG_INFORMATION_SHOW', default="False")).lower() == 'true' else False  
# Colorful messages to inform user
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',    
)
SITE_ID=1

#Proxy Settings
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'daphne',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    #'django_clamd',
    'website',    
    'ConceptMan.apps.ConceptManConfig',
    'BoltMan.apps.BoltManConfig',
    'EcoMan.apps.EcoManConfig',
    'NormMan.apps.NormManConfig',
    'MatMan.apps.MatManConfig',
    'CatiaFramework.apps.CatiaFrameworkConfig',
    'widget_tweaks',
    'bootstrapsidebar',
    'django_extensions',
    'django.contrib.humanize',
    'channels',
    'django_keycloak',
]

'''
Availability of the aplications on installed system can be decided on Systen Environment variables

'''
GROUPS= dict()

for key, value in dict(os.environ).items():
    if key.startswith('APP_'):
        GROUPS['/be_paramount/' + key.lower().replace('_','-')] =  value 



AUTHENTICATION_BACKENDS = [
   "django.contrib.auth.backends.ModelBackend",
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

KEYCLOAK_CONFIG = {
    "KEYCLOAK_SERVER_URL" : os.environ.get('KEYCLOAK_SERVER_URL', config('KEYCLOAK_SERVER_URL', default='')),
    "KEYCLOAK_REDIRECT_URI" : os.environ.get('KEYCLOAK_REDIRECT_URI', config('KEYCLOAK_REDIRECT_URI', default='')),
    "KEYCLOAK_REALM" : os.environ.get('KEYCLOAK_REALM', config('KEYCLOAK_REALM', default='')),
    "KEYCLOAK_CLIENT_ID" : os.environ.get('KEYCLOAK_CLIENT_ID', config('KEYCLOAK_CLIENT_ID', default='')),
    "KEYCLOAK_CLIENT_SECRET_KEY" : os.environ.get('KEYCLOAK_CLIENT_SECRET_KEY', config('KEYCLOAK_CLIENT_SECRET_KEY', default='')),
    "KEYCLOAK_CLIENT_PUBLIC_KEY" : os.environ.get('KEYCLOAK_CLIENT_PUBLIC_KEY', config('KEYCLOAK_CLIENT_PUBLIC_KEY', default='')),
    "KEYCLOAK_DEFAULT_ACCESS" : os.environ.get('KEYCLOAK_DEFAULT_ACCESS', config('KEYCLOAK_DEFAULT_ACCESS', default='')),
    "KEYCLOAK_AUTHORIZATION_CONFIG" : os.path.join(os.path.dirname(__file__), 'your-client-authz-config.json'),
    "KEYCLOAK_METHOD_VALIDATE_TOKEN" : os.environ.get('KEYCLOAK_METHOD_VALIDATE_TOKEN', config('KEYCLOAK_METHOD_VALIDATE_TOKEN', default=''))
   }

ROOT_URLCONF = 'website.urls'
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240 # higher than the count of fields
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
                'django.template.context_processors.media',
                'website.context_processors.environment_details',
            ],
        },
    },
]
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

WSGI_APPLICATION = 'website.wsgi.application'
ASGI_APPLICATION = 'website.asgi.application'  

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', config('DJANGO_SECRET_KEY', default=False, cast=str)) #'django-insecure-j!a-mt6t@5try$)ue&nz%c&u8n-sc_1l!per-$e_+u#85jbolo'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = os.environ.get('DJANGO_DEBUG_MODE', config('DJANGO_DEBUG_MODE', default=False, cast=bool))
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', config('DB_NAME', default='qlca_dev')),
        'USER': os.environ.get('DB_USER', config('DB_USER', default='r')),
        'PASSWORD': os.environ.get('DB_PASSWORD', config('DB_PASSWORD', default='')),
        'HOST': os.environ.get('DB_HOST', config('DB_HOST', default='')),
        'PORT': os.environ.get('DB_PORT', config('DB_PORT', default='5432')),
    }
}

try:
    from website.settings_dev import CHANNEL_LAYERS as channel_conf
    CHANNEL_LAYERS = channel_conf
except ImportError:
    CHANNEL_LAYERS = {
        "default": {
            "CONFIG": {
                "hosts": [(os.environ.get('REDIS_HOSTNAME', config('REDIS_HOSTNAME', default='')),'6379')],
            },
            "BACKEND": "channels_redis.core.RedisChannelLayer"
        },
    }

LOGIN_REDIRECT_URL = '/home/'
LOGIN_URL = '/user/login'
LOGOUT_REDIRECT_URL = '/home/'

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS =  [ os.path.join(BASE_DIR,'staticfiles')]
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime}  {process:d}  {message}',
            'style': '{',
        },
    },
    'handlers': {
        'newfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': f'{MEDIA_ROOT}/debug.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'filelogger': {
            'level': 'DEBUG',
            'handlers': ['newfile'],
            'propagate': False,
        },
    },
}

FREE_USER_TRIAL_TIME_DAYS = 30