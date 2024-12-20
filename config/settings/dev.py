from config.settings.base import *
from dotenv import load_dotenv

load_dotenv()
# DEBUG = os.getenv("DJANGO_DEBUG", "") != "False"

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
