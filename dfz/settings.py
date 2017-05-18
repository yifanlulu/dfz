#coding: utf-8

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(os.path.join(BASE_DIR,'vendor_apps'))
sys.path.append(os.path.join(BASE_DIR,'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2--mf$)ic$-2^8pzo@pec#6(ve=oi!q0+)o4t5(wztms06nyw5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 第三方app
    'xadmin',
    'crispy_forms',
    'reversion',
    'DjangoUeditor',
    'DjangoQiniu',
    'CustomFilters',

    # 项目app
    'course',
    'news',
    'payinfo',
    'frontuser',
    'dfz_auth',
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

ROOT_URLCONF = 'dfz.urls'

AUTH_USER_MODEL = 'dfz_auth.DFZUser'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'dfz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dfz',
        'USER': 'root',
        'PASSWORD': 'neusoft',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh_Hans'#'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)


# xadmin config
XADMIN_CONF= 'dfz.xsite'

# 七牛配置
QINIU_DOMAIN = 'http://7xqenu.com1.z0.glb.clouddn.com/'
QINIU_ACCESS_KEY = 'M4zCEW4f9XPanbMN-Lb9O0S8j893f0e1ezAohFVL'
QINIU_SECRET_KEY = '7BKV7HeEKM3NDJk8_l_C89JI3SMmeUlAIatzl9d4'
QINIU_BUCKET_NAME = 'hyvideo'


# DjangoUeditor配置
DJANGO_UEDITOR_QINIU = {
    'QINIU_DOMAIN':QINIU_DOMAIN,
    'QINIU_ACCESS_KEY':QINIU_ACCESS_KEY,
    'QINIU_SECRET_KEY':QINIU_SECRET_KEY,
    'QINIU_BUCKET_NAME': QINIU_BUCKET_NAME
}

# 一页展示多少条数据
COUNT_PER_PAGE = 5

# FRONT_SESSION_KEY
FRONT_SESSION_KEY = 'sdkfjasldfjsdkf'


# 阿里大于的配置
ALIDAYU_APP_KEY = '23709557'
ALIDAYU_APP_SECRET = 'd9e430e0a96e21c92adacb522a905c4b'
ALIDAYU_SIGN_NAME = 'python论坛'
ALIDAYU_TEMPLATE_CODE = 'SMS_37105066'