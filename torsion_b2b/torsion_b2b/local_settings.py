import os
import datetime
from defaults import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

SECRET_KEY = '*12y*#gfd#3#%0-t**fzd*=ur_nu97x)-1*#b%t&pa#2i6j)mq^jsy^zrd'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'decort.com.ua', 'www.decort.com.ua', 'torsion.kiev.ua',
                 'www.torsion.kiev.ua']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'torsion_shop_b2b',
        'USER': 'torsion_prog',
        'PASSWORD': 'sdr%7ujK',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'tecdoc': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'td3q2017',
        'USER': 'torsion_prog',
        'PASSWORD': 'sdr%7ujK',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
