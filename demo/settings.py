SECRET_KEY = 'spam'
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ROOT_URLCONF = 'demo.urls'
INSTALLED_APPS = ['demo']
TEMPLATE_CONTEXT_PROCESSORS = ['django_settings_export.settings_export']
DATABASES = {'default': {'NAME': 'db.sqlite',
                         'ENGINE': 'django.db.backends.sqlite3'}}


FOO = 'foo'
BAR = 'bar'
SETTINGS_EXPORT = [
    'FOO',
    'BAR',
]
