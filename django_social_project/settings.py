"""
Django settings for django_social_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "mystatic")

# STATICFILES_DIRS =(
#                   os.path.join(STATIC_ROOT, 'css/'),
#                    os.path.join(STATIC_ROOT, 'javascript/'),
#                    os.path.join(STATIC_ROOT, 'images/'),
#                  )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&ls071mhp^x518x6#p@to5gr7k$w10f9_*bx4nkkgziqh*ss#c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

#please set this to False, if you don't need auto update and restart the server or reload the page to make this effect
ALLOW_AUTO_UPDATE = True

# please set this time in milliseconds, for example if 10mins, give 600000 and restart the server or reload the page to make this effect
USER_TIMELINE_AUTO_UPDATE_PERIOD = 600000

from config import *

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_social_app',
    'social.apps.django_app.default',
    #    'twitter_feed',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
)


# SOCIAL_AUTH_PIPELINE = (
#    'social.pipeline.social_auth.social_details',
#    'social.pipeline.social_auth.social_uid',
#    'social.pipeline.social_auth.auth_allowed',
#    'social.pipeline.social_auth.social_user',
#    'social.pipeline.user.get_username',
#    'social.pipeline.mail.mail_validation',
#    'social.pipeline.user.create_user',
#    'social.pipeline.social_auth.associate_user',
#    'social.pipeline.social_auth.load_extra_data',
#    'social.pipeline.user.user_details',
#   'login_demo_app.pipeline.get_profile_picture',
#)

AUTHENTICATION_BACKENDS = (
    #    'social.backends.facebook.FacebookOAuth2',
    #    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'django_social_project.urls'

WSGI_APPLICATION = 'django_social_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or
        # 'oracle'.
        'ENGINE': 'django.db.backends.',
        # Or path to database file if using sqlite3.
        'NAME': '',
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        # Set to empty string for localhost. Not used with sqlite3.
        'HOST': '',
        # Set to empty string for default. Not used with sqlite3.         # set
        # the connection timeout for
        'PORT': '',
    }
}


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
