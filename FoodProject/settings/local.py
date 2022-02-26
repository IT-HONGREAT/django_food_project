from .base import *

local_env = open(os.path.join(BASE_DIR, '.env'))

env_list = dict()

while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\n', '')
    start = line.find('=')
    key = line[:start]
    value = line[start + 1:]
    env_list[key] = value

SECRET_KEY = env_list['SECRET_KEY']

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'food_db',
#         'USER': 'food-role',
#         'PASSWORD': '1234567890',
#         'HOST': '127.0.0.1',
#         'PORT': '5432'
#     }
# }
