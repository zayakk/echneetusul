from datetime import datetime
from pathlib import Path
import psycopg2

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5os_@r)olasdlposr85_i%yp!=kcr2icp$v3h=k3+w2-)aiqwk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'benglish'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


########## user defined functions ##########
def sendResponse(action, resultCode, data):
    response = {}
    response["action"] = action
    response["data"] = data
    response["resultCode"] = resultCode
    response["resultMessage"] = resultMessages[resultCode]
    response["size"] = len(data)
    response["curdate"] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    return response

def connectDB():
    conn  = psycopg2.connect(
        host = "192.168.0.15", 
        # host = "59.153.86.254", 
        dbname = "dbechnee",
        user = "userechnee", 
        password = "passechnee",
        port = 5938
    )
    return conn

def disconnectDB(conn):
    conn.close()
    
########## user defined contants ##########
resultMessages = { 
    200 : "Success",
    400 : "action key baihgui",
    404 : "Not found",
    406 : "Iim action baihgui",
    1001 : "getuser api usermail key baihgui",
    1002 : "reguser api usermail, pwd ali neg key baihgui",
    1003 : "Hereglegch Amjilttai burtguullee",
    1004 : "Already registered user mail",
    1005 : "loginuser api key baihgui",
    1006 : "Amjilttai nevterlee",
    1007 : "Hereglegchiin ner esvel nuuts ug buruu",
    1008 : "reguser action dotood aldaa",
    2001 : "Shine ug burtgegdlee",
    2002 : "Umnu burtgegdsen ug baina. burtgeh bolomjgui",
    
 
    4001 : "dt_getWord api-d uid key bhgu",
    4002 : "Hereglegchin buh ugiig olloo",
    4003 : "dt_DeleteUserWord api-d uid, wid key bhgu",
    4004 : "Amjilttai ustgalaa",
    
    5003: "Tseejilsen ug ustgalaa",
    
    6001 : "getCategory api-d cid key baihgui",
    6002 : "getCategory api-d cid key amjilttai avlaa",
    6003 : "getAllCategory api-d amjilttai avlaa",
    
    7001 : "getsubcategory scid key байхгүй",
    7002 : "getsubcategory scid key амжилттай ",
    7003 : "getAllsubcategory scid key байхгүй ",
    7004 : "getAllsubcategory scid key амжилттай ",
    
    8001: "ug uurchlugdluu",
    
    9001: "ug ustgagdlaa",
    
    10001 : "select_word api-d uwid key baihgui",
    
    
}
