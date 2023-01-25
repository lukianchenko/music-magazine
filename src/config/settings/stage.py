from config.settings.base import *  # NOQA

DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
]

CURRENT_ENV = "STAGE"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB"),
            "USER": os.environ.get("POSTGRES_USER"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
            "HOST": os.environ.get("POSTGRES_HOST"),
            "PORT": os.environ.get("POSTGRES_PORT"),
        },
    }
