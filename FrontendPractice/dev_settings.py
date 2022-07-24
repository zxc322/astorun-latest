from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-+bfj%fojvekw#wwi4vpngr3m@1n8wf@7w-_lv)@6+$&@x(1@+p'
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('POSTGRES_DB'),
#         'USER': os.environ.get('POSTGRES_USER'),
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD'), 
#         'HOST': os.environ.get('DB_HOST'),
#         'PORT': 5432, 
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': "postgres",
#         'USER': "postgres",
#         'PASSWORD': "postgres", 
#         'HOST': "db",
#         'PORT': 5432, 
#     }
# }

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')