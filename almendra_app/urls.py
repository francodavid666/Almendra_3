from django.contrib import admin
from django.urls import path,include
from .views import * 
from django.conf.urls.static import static
from django.urls import re_path
from django.conf import settings
from django.views.static import serve



urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('inicio/', inicio_2, name = 'inicio_2'),


    path('ckeditor/',include('ckeditor_uploader.urls')),
    
 

  

    path('login_formulario/',login_formulario,name = 'login_formulario'),


]


#+static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


