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

# needed since django 3.2
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
