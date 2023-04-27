"""
Django settings for rental_application project.
Generated by 'django-admin startproject' using Django 4.1.5.
For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from decouple import config

from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY ='django-insecure-t9^pxze^4n$zjo0p1!84m0gh8h6fau11@16n*464(_w+)zdjgp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =True

ALLOWED_HOSTS = ['127.0.0.1','rentapp-jl2v.onrender.com','localhost']


# Application definition

AUTH_USER_MODEL = 'accounts.User'
AUTH_PROFILE_MODULE = 'user_profile.OwnerProfile'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False


INSTALLED_APPS = [
    "django_celery_results",
    "django_celery_beat",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    "corsheaders",
    'accounts',
    'notification',
    'user_profile',
    'propertyManager',
    # Third party app
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'social_django'
   

]
REST_FRAMEWORK = {
    "NON_FIELD_ERRORS_KEY": "erros",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated', )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',)
}


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'social_django.middleware.SocialAuthExceptionMiddleware',
]
CORS_ALLOWED_ORIGINS = [
    'https://rentapp-jl2v.onrender.com',
    "http://localhost:3000",
    "http://127.0.0.1:9000",
    "http://127.0.0.1:8000' "
]

ROOT_URLCONF = 'rental_application.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, os.path.join(BASE_DIR, 'build')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ],
        },
    },
]

WSGI_APPLICATION = 'rental_application.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '281277703969-9o6traa7isfslkkodnv3fs590hcpn5c7.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        },
        # 'SCOPE': ['email', 'profile'],
        # 'AUTH_PARAMS': {'access_type': 'online'},
    }
}

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'path.to.your.CustomRegisterSerializer',
}

REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'path.to.your.CustomLoginSerializer',
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS=[
     os.path.join(BASE_DIR, 'build/static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Directory where uploaded media is saved.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'  # Public URL at the browser

CORS_ORIGIN_ALLOW_ALL = True

# for celery
CELERY_BROKER_URL = "redis://127.0.0.1:6379"
CELERY_ACEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"
CELERY_TIMEZONE = "Asia/Kolkata"
CELERY_RESULT_BACKEND = "django-db"
# clery beat setting
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"


TWILIO_ACCOUNT_SID ='AC74043bacf892c093c3c0a87b54a4393e'
TWILIO_AUTH_TOKEN = '66090e8aef8e7022b3d89f3a633b3bd1'
# ALLOWED_HOSTS=['76ff-117-99-244-24.in.ngrok.io']

# email configuration
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = 'roopapratyush29@gmail.com'
EMAIL_HOST_PASSWORD = 'xvspzcusahjrdcbx'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

SITE_ID = 2

LOGIN_REDIRECT_URL = "/"

ACCOUNT_FORMS = {'signup': 'users.forms.UserCreationForm'}



AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

#Djoser
DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "SET_USERNAME_RETYPE": True,
    "SET_PASSWORD_RETYPE": False,  
    "USERNAME_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "PASSWORD_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,

   "SERIALIZERS": {
        "user_create": "accounts.serializers.UserCreateSerializer",  # custom serializer
        "user": "accounts.serializers.UserCreateSerializer",
        "current_user": "accounts.serializers.UserCreateSerializer",
        "user_delete": "djoser.serializers.UserSerializer",
    },
    'SOCIAL_AUTH_TOKEN_STRATEGY': 'djoser.social.token.jwt.TokenStrategy',
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': ['http://127.0.0.1:8000','http://127.0.0.1:3000/home/', 'http://127.0.0.1:8000/auth/accounts/profile/'],
}

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend'
)
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '281277703969-9o6traa7isfslkkodnv3fs590hcpn5c7.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
#     'https://www.googleapis.com/auth/userinfo.email',
#     'https://www.googleapis.com/auth/userinfo.profile',
#     'openid'
# ]
# SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['first_name', 'last_name']

GOOGLE_OAUTH_CLIENT_ID = '281277703969-9o6traa7isfslkkodnv3fs590hcpn5c7.apps.googleusercontent.com'
# GOOGLE_OAUTH2_CLIENT_SECRET = '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'
# SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SESSION_COOKIE_SAMESITE = None
