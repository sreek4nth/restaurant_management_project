from django.urls import path
from .views import *

urlpatterns = [
    path('',views.home, name='home')
    path('restaurant',views.home_view, name='restuarant_home'),
]