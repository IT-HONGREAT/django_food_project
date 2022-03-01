def read_secret(secret_name):
    file = open("/run/secrets/" + secret_name)
    secret = file.read()
    secret = secret.lstrip().rstrip()
    file.close()
    return secret


SECRET_KEY = read_secret("DJANGO_SECRET_KEY")


DEBUG = False

ALLOWED_HOSTS = ["*"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django",
        "USER": read_secret("MARIADB_USER"),
        "PASSWORD": read_secret("MARIADB_PASSWORD"),
        "HOST": "mariadb",
        "PORT": "3306",
    }
}
