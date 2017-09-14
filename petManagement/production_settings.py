from .settings import *

SITE_ID = 1
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'petmanagement',
        'USER': 'petmanagement',
        'PASSWORD': 'petmanagement',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}