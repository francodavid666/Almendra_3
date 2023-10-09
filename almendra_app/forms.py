from django import forms
from .models import *
from django.forms import ModelForm
from django.conf import settings

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class login_form(forms.ModelForm):

    class Meta: 
        model= login_model
        fields = '__all__'
        



class crear_usuario (UserCreationForm):
    username=forms.CharField(label= 'Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)