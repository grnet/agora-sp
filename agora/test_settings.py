from agora.settings import *

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/db.agora.sqlite3'
    }
}

DATABASES = SQLITE
EMAIL_FILE_PATH = '/tmp/agora/agora_emails'
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'

LOGGING = {
    'version': 1            
}
