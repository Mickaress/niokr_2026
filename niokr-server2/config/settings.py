import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent


def _env_bool(name: str, default: bool) -> bool:
    val = os.environ.get(name)
    if val is None:
        return default
    return val.strip().lower() in ('1', 'true', 'yes', 'on')


def _env_list(name: str, default: list[str] | None = None) -> list[str]:
    raw = os.environ.get(name, '')
    if not raw.strip():
        return list(default) if default is not None else []
    return [x.strip() for x in raw.split(',') if x.strip()]


DEBUG = _env_bool('DJANGO_DEBUG', True)

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
if not SECRET_KEY:
    if DEBUG:
        SECRET_KEY = 'django-insecure-dev-only-not-for-production'
    else:
        raise ImproperlyConfigured(
            'Задайте переменную окружения DJANGO_SECRET_KEY для продакшена.'
        )

ALLOWED_HOSTS = _env_list('DJANGO_ALLOWED_HOSTS')
if not ALLOWED_HOSTS:
    if DEBUG:
        ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']
    else:
        raise ImproperlyConfigured(
            'Задайте DJANGO_ALLOWED_HOSTS (через запятую), например: api.example.com'
        )

APPEND_SLASH = False


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'api',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
]

AUTH_USER_MODEL = 'api.User'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

_cors_origins = _env_list('CORS_ALLOWED_ORIGINS')
if _cors_origins:
    CORS_ALLOWED_ORIGINS = _cors_origins
else:
    CORS_ALLOWED_ORIGINS = [
        'http://localhost:5173',
        'http://127.0.0.1:5173',
    ]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'token',
]

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# База: SQLite по умолчанию (локально). Для PostgreSQL задайте POSTGRES_DB (остальное — опционально).
if os.environ.get('POSTGRES_DB'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['POSTGRES_DB'],
            'USER': os.environ.get('POSTGRES_USER', 'postgres'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
            'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
            'PORT': os.environ.get('POSTGRES_PORT', '5432'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'api.authentication.CookieTokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

MEDIA_URL = os.environ.get('DJANGO_MEDIA_URL', '/media/')
_media_root = os.environ.get('MEDIA_ROOT')
MEDIA_ROOT = Path(_media_root) if _media_root else (BASE_DIR / 'media')

# HTTPS / cookies в проде (включите при работе за reverse proxy с TLS)
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = _env_bool('DJANGO_SESSION_COOKIE_SECURE', True)
    CSRF_COOKIE_SECURE = _env_bool('DJANGO_CSRF_COOKIE_SECURE', True)
    SECURE_SSL_REDIRECT = _env_bool('DJANGO_SECURE_SSL_REDIRECT', False)
