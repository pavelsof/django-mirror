SECRET_KEY = 'must-not-be-empty'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = [
    'django_mirror',
    'tests',
]
