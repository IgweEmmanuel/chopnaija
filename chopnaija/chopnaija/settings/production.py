from .base import *

SECRET_KEY = "%89_*2bsbbt69tm8vwh^gm6gvddod$bx@!7!t@ao_=ai63p4(p"

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "chopnaija",
        "USER": "root",
        "PASSWORD": "admin",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
