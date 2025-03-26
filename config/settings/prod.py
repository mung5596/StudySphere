'''
Django settings used in the production environment.
'''
from .base import *

ALLOWED_HOSTS = ['13.213.128.146', 'studysphere2025.com']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = True
