These are all the applications and the css and html that I use for my website at www.namalliv.com. My website is developed in 
Django using Python.
I love Django for evething you can do with little code and it works perfectly.

Here is part of my Settings.py, only the applications I have installed as of today the last day of February 2017. 

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # 'django.contrib.sites',
    'home',
    'People',
    'about',
    'gallery',
    'contact',
    'account',
    'shop',
    'cart',
    'orders',
    'paypal.standard.ipn',
    'payment',
    'rosetta',
    'courses',
    'students',
    'embed_video',
    'django_nvd3',
    'rest_framework',
    'chartit',
    'yearly',
    'polls',
    'pelota',
    'blog',
    'taggit',
    'posts',
    #'social.apps.django_app.default',
]

