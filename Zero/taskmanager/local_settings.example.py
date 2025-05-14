"""
Local settings example for the Django project.
Copy this file to local_settings.py and modify the settings as needed.
"""

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sua_chave_secreta_aqui'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'
