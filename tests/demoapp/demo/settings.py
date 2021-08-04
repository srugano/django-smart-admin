import os
from pathlib import Path
import environ
env = environ.Env(
    DEBUG=(bool, False)
)

DEBUG = True
BASE_DIR = Path(__file__).resolve(strict=True).parents[3]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / '~build' / 'static'
SITE_ID = 1
ROOT_URLCONF = 'demo.urls'
SECRET_KEY = 'abc'
ALLOWED_HOSTS = ['*']
AUTHENTICATION_BACKENDS = ('demo.backends.AnyUserAuthBackend',
                           )

INSTALLED_APPS = ['django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.sites',
                  'django.contrib.messages',
                  'django.contrib.staticfiles',
                  'django_sysinfo',
                  'adminfilters',
                  'smart_admin.logs',
                  'smart_admin.templates',
                  'smart_admin',
                  'demo']

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DATABASES = {
    'default': env.db()
}

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': ['django.contrib.messages.context_processors.messages',
                                   'django.contrib.auth.context_processors.auth',
                                   "django.template.context_processors.request",
                                   ]
        },
    },
]

SMART_ADMIN_SECTIONS = {
    'Demo': ['demo', ],
    'Security': ['auth',
                 'auth.User',
                 ],

    'Logs': ['admin.LogEntry',
             ],
    'Other': [],
    '_hidden_': ["sites"]
}

SMART_ADMIN_BOOKMARKS = ['--']
