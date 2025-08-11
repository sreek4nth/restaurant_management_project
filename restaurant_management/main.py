import os
import django
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core .management import execute_from_command_line

BASE_DIR = os.path.dirname(__file__)
settings.configure(
    DEBUG=True,
    SECRET_KEY=__name__,
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[
        'django.middleware.commom.CommonMiddleware',
    ],
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS':[os.path.join(BASE_DIR,'templates')],
            'APP_DIRS':True,
        },
    ],
)

django.setup()

def home(request):
    return Httpresponse('<h1>welcome to my homepage </h1>')

urlpatterns=[
    path('',home),
]    

if__name__ = "__main__":
    execute_from_command_line([__file__,'runserver','0.0.0.0:8000'])