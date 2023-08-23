from django.contrib import admin
from django.urls import path,include
from .views import * 
from django.conf.urls.static import static
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
     path('appPedidos/<id>/', appPedidos, name = 'appPedidos'),
]