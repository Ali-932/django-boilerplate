import os
import sys
from datetime import timedelta
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
default_secret_key = "django-insecure-xu^a#n@-zn(8**8*x#v%^2juezuai=irdo(%(p!-2*)hbhd7tj"
default_DEBUG = False
default_ALLOWED_HOSTS = 'localhost,127.0.0.1'
default_TESTING = False

TESTING = config('TESTING', default=default_TESTING, cast=bool)
SECRET_KEY = config('SECRET_KEY', default_secret_key)
DEBUG = config('DEBUG', default=default_DEBUG, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=default_ALLOWED_HOSTS, cast=lambda v: [s.strip() for s in v.split(',')])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'silk',
    'drf_spectacular',
    "drf_standardized_errors",
    'account'
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_currentuser.middleware.ThreadLocalUserMiddleware',
]

ROOT_URLCONF = 'urls'

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

WSGI_APPLICATION = 'wsgi.application'

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

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler",

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

DRF_STANDARDIZED_ERRORS = {
    "ENABLE_IN_DEBUG_FOR_UNHANDLED_EXCEPTIONS": True,
}

AUTH_USER_MODEL = 'account.User'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=60),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

PERSISTENT_DATA_PATH = 'persistent_data/'
Path(PERSISTENT_DATA_PATH).mkdir(parents=True, exist_ok=True)
LOG_FILE_PATH = os.path.join(PERSISTENT_DATA_PATH + 'logs')  # Path for log files

LOGGING_CONFIG = None

# Formatters Configuration
import os
import sys
from logging.handlers import RotatingFileHandler

# Log file path setup
LOG_FILE_PATH = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_FILE_PATH, exist_ok=True)

# Formatters Configuration
LOGGING_FORMATTERS = {
    "date_time": {
        "format": "%(asctime)s [%(levelname)s] %(name)s %(pathname)s:%(lineno)d - %(message)s"
    },
    "console": {
        "format": "%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        "datefmt": "%H:%M:%S"
    },
    "simple": {
        "format": "%(levelname)s %(message)s"
    },
}

# Handlers Configuration
LOGGING_HANDLERS = {
    # Application log handlers with rotation
    "app_info_file": {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": os.path.join(LOG_FILE_PATH, "app.info.log"),
        "maxBytes": 10485760,  # 10MB
        "backupCount": 5,
        "level": "INFO",
        "formatter": "date_time",
    },
    "app_error_file": {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": os.path.join(LOG_FILE_PATH, "app.error.log"),
        "maxBytes": 10485760,  # 10MB
        "backupCount": 5,
        "level": "ERROR",
        "formatter": "date_time",
    },
    "app_debug_file": {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": os.path.join(LOG_FILE_PATH, "app.debug.log"),
        "maxBytes": 10485760,  # 10MB
        "backupCount": 5,
        "level": "DEBUG",
        "formatter": "date_time",
    },
    # Django-specific log handlers
    "django_file": {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": os.path.join(LOG_FILE_PATH, "django.log"),
        "maxBytes": 10485760,  # 10MB
        "backupCount": 5,
        "level": "INFO",
        "formatter": "date_time",
    },
    "django_request_file": {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": os.path.join(LOG_FILE_PATH, "django.request.log"),
        "maxBytes": 10485760,  # 10MB
        "backupCount": 5,
        "level": "INFO",
        "formatter": "date_time",
    },
    "console": {
        "level": "INFO",
        "class": "logging.StreamHandler",
        "formatter": "console",
        "stream": sys.stdout,
    },
}

# Loggers Configuration
LOGGING_LOGGERS = {
    # Root logger configuration
    "": {
        "handlers": ["app_info_file", "app_error_file", "app_debug_file", "console"],
        "level": "INFO",
        "propagate": True,
    },
    # Django framework loggers
    "django": {
        "handlers": ["django_file", "console"],
        "level": "INFO",
        "propagate": False,
    },
    "django.request": {
        "handlers": ["django_request_file", "console"],
        "level": "INFO",
        "propagate": False,
    },
    "django.server": {
        "handlers": ["django_file", "console"],
        "level": "INFO",
        "propagate": False,
    },
    "django.template": {
        "handlers": ["django_file", "console"],
        "level": "INFO",
        "propagate": False,
    },
    "django.db.backends": {
        "handlers": ["django_file", "console"],
        "level": "INFO",  # Set to DEBUG to log all SQL queries
        "propagate": False,
    }
}

# Full Logging Configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': LOGGING_FORMATTERS,
    'handlers': LOGGING_HANDLERS,
    'loggers': LOGGING_LOGGERS,
}