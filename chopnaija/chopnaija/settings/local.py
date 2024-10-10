from .base import *
import os
from getpass import getpass
SECRET_KEY = getpass('Enter key')#'b#7$%2_v(&narw_0-08d&okq^$_+yry0#+#_g3e4n1+tvu2!%y'
os.environ['SECRET_KEY'] = SECRET_KEY
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
