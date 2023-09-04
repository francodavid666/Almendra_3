from django.contrib import admin
from django.urls import path,include
from .views import * 
from django.conf.urls.static import static
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
     path('appPedidos/<id>/', appPedidos, name = 'appPedidos'),
     path('accounts/',include('django.contrib.auth.urls')),
     path('register/',register,name='register'), 
     path('login/',Login_request,name='login'), 
     path('profile/',profile,name='profile'), 
     path('settingProfile/',settingProfile,name='settingProfile'), 
     path('edit_email/',edit_email,name='edit_email'), 
     path('edit_username/',edit_username,name='edit_username'), 
     path('edit_name/',edit_name,name='edit_name'), 
     path('update_item/',update_item,name='update_item'),
     path('cart/',cart,name='cart'),
     path('checkout/',checkout,name='checkout'),
     path('processOrden/',processOrden,name='processOrden'),

 
 
]