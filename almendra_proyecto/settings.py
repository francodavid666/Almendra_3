"""
Django settings for almendra_proyecto project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#BASE_DIR = 'postgres://base_datos_almendra_user:H3vGVXki83w7q0nNN1iZoRgOhKOPbks3@dpg-cg8libg2qv21l3b6ufrg-a.oregon-postgres.render.com/base_datos_almendra'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ['SECRET_KEY']

SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []

# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME: 
       ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'almendra_app',
    'ckeditor',
    'ckeditor_uploader',
]

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom':[
            ['Image']

        ],
         
         'width': '100%',
         'height': '1%',
        'toolbarCanCollapse': False,
        'defaultLanguage' : 'es',

    } 
}



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

ROOT_URLCONF = 'almendra_proyecto.urls'

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

WSGI_APPLICATION = 'almendra_proyecto.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

import dj_database_url


DATABASES = {
    'default': dj_database_url.config( 
        default='postgresql://francodavid666:v2_43TAT_w4cYqbM8rnc5PEwS7FvXRZf@db.bit.io:5432/francodavid666/Almendra_BD',
       #default='postgres://bd_almendra_user:whdkjTcv26l2sR1wLvCCOiTojnsY3Y3o@dpg-ch0kgtj3cv2c5b5dsje0-a.oregon-postgres.render.com/bd_almendra',
        
         conn_max_age=600 )
}

#
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''
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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


#STATIC_ROOT = BASE_DIR / 'static'


#Carpeta en donde se encuentran los estaticos (imagenes,javascript o css)
STATIC_URL = '/static/'
#MEDIA_URL='postgres://base_datos_almendra_user:H3vGVXki83w7q0nNN1iZoRgOhKOPbks3@dpg-cg8libg2qv21l3b6ufrg-a.oregon-postgres.render.com/base_datos_almendra/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#MEDIA_ROOT = os.path.join(BASE_DIR,'postgres://base_datos_almendra_user:H3vGVXki83w7q0nNN1iZoRgOhKOPbks3@dpg-cg8libg2qv21l3b6ufrg-a.oregon-postgres.render.com/')



MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR,'almendra_app/static/almendra_app/media')



STATICFILES_DIRS=(
    os.path.join(BASE_DIR, 'static'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



