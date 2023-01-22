

import datetime
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-e3loxx_7qa(4gqif4f)d3620x_!8bni6&2pta53gr1kc1)hd)*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ 'localhost', '127.0.0.1']
MAX_OTP_TRY=3

# Application definition

INSTALLED_APPS = [
    'drf_yasg',

    'ask.apps.AskConfig',
    'notice.apps.NoticeConfig',
    'authentication.apps.AuthenticationConfig',
    'social_auth.apps.SocialAuthConfig',
    'faq.apps.FaqConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "corsheaders",
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',
    'django.contrib.sites',
    'taggit',
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',
    


]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_htmx.middleware.HtmxMiddleware",
]
CORS_ALLOWED_ORIGINS = [
    
    "http://localhost:8080",
    "http://127.0.0.1:9000",
    
]

CORS_ORIGIN_REGEX_WHITELIST = [
    r"^https://\w+\.netlify\.app$",
]

ROOT_URLCONF = 'forum.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'forum.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field


CRISPY_TEMPLATE_PACK='bootstrap4'

STATIFILES_DIS=os.path.join(BASE_DIR, 'static/')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# LOGIN_REDIRECT_URL = 'blog-home'
# LOGIN_URL = 'login'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_ALLOW_NONIMAGE_FILES = False

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 250,
        'width': 'auto',
    },
    'special':{
        'toolbar':'custom',
        'toolbar_custom':[['Bold','Italic','Underline','Link','Unlink','Superscript','Subscript','Maximize','Blockquote','TextColor','BGColor','NumberedList','BulletedList','Find','Table','Replace','SelectAll','JustifyLeft','JustifyCenter','JustifyBlock','JustifyRight','HorizontalRule','Button','FontSize','Font','Format']],
        'height': 250,
        'width': 'auto',
    },
    'reply':{
        'toolbar':'custom',
        'toolbar_custom':[['Bold','Italic','Underline','Link','Unlink','Superscript','Subscript','Maximize','Blockquote','TextColor','BGColor','NumberedList','BulletedList','Find','Table','Replace','SelectAll','JustifyLeft','JustifyCenter','JustifyBlock','JustifyRight','HorizontalRule','Button','FontSize','Font','Format']],
        'height': 250,
        'width': 'auto',
    },

}
AUTH_USER_MODEL = 'authentication.User'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    
    'NON_FIELD_ERRORS_KEY': 'error',

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
     'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=1),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },'info': {
        'contact': 'apiteam@wordnik.com',
        'description': 'This is a sample server Petstore server. '
                       'You can find out more about Swagger at '
                       '<a href="http://swagger.wordnik.com">'
                       'http://swagger.wordnik.com</a> '
                       'or on irc.freenode.net, #swagger. '
                       'For this sample, you can use the api key '
                       '"special-key" to test '
                       'the authorization filters',
        'license': 'Apache 2.0',
        'licenseUrl': 'http://www.apache.org/licenses/LICENSE-2.0.html',
        'termsOfServiceUrl': 'http://helloreverb.com/terms/',
        'title': 'Swagger Sample App',
    },
}

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey' # Name for all the SenGrid accounts
EMAIL_HOST_PASSWORD = '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'
DEFAULT_FROM_EMAIL = 'noreply@gmail.com'
LOGIN_REDIRECT_URL = 'success'