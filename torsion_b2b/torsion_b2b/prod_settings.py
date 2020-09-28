import os
import datetime
from defaults import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

SECRET_KEY = '@#1145g*p#3#%0-t**fzd*56463#$#%fdg32b%t&pa#2i6j)mq1jsy^zrd'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'decort.com.ua', 'www.decort.com.ua', 'torsion.kiev.ua',
                 'www.torsion.kiev.ua']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'torsion_shop_b2b',
        'USER': 'torsion_prog',
        'PASSWORD': 'sdr%7ujK',
        'HOST': 'localhost',
        'PORT': '6432',
    },
    'tecdoc': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'td3q2017',
        'USER': 'torsion_prog',
        'PASSWORD': 'sdr%7ujK',
        'HOST': 'localhost',
        'PORT': '6432',
    }
}

STATIC_URL = '/static/'
