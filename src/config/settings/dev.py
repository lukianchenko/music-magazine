import os

from config.settings.base import *  # NOQA: F403

DEBUG = True

CURRENT_ENV = "DEV"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_URL = "/static/"

# Media files
# https://docs.djangoproject.com/en/4.0/topics/files/

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
