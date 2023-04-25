from django import forms
from .models import *
from django.forms import ModelForm
from django.conf import settings


class pasteleria_form (forms.ModelForm):

    

    class Meta:
        model = pasteleria_model 
        fields = '__all__'
        widgets = {'descripcion':forms.Textarea(
            attrs = {'class':'form__descripcion','placeholder':'Descripcion'}
        ),
        'informacion': forms.Textarea(
            attrs ={'class':'form__informacion','placeholder':'Informacion'}
        )}


class salados_form(forms.ModelForm):

    class Meta:
        model = pasteleria_model
        fields = '__all__'
        widgets = {'descripcion':forms.Textarea(
            attrs = {'class':'form__descripcion','placeholder':'Descripcion'}
        ),
        'informacion': forms.Textarea(
            attrs ={'class':'form__informacion','placeholder':'Informacion'}
        )}


class bebidas_form(forms.ModelForm):

    class Meta:
        model = bebidas_model
        fields = '__all__'
        widgets = {'descripcion':forms.Textarea(
            attrs = {'class':'form__descripcion','placeholder':'Descripcion'}
        ),
        'informacion': forms.Textarea(
            attrs ={'class':'form__informacion','placeholder':'Informacion'}
        )}


class cafes_form(forms.ModelForm):

    class Meta:
        model = cafes_model
        fields = '__all__'
        widgets = {'descripcion':forms.Textarea(
            attrs = {'class':'form__descripcion','placeholder':'Descripcion'}
        ),
        'informacion': forms.Textarea(
            attrs ={'class':'form__informacion','placeholder':'Informacion'}
        )}
    


class brunch_form(forms.ModelForm):

    class Meta:
        model = brunch_model
        fields = '__all__'
        widgets = {'descripcion':forms.Textarea(
            attrs = {'class':'form__descripcion','placeholder':'Descripcion'}
        ),
        'informacion': forms.Textarea(
            attrs ={'class':'form__informacion','placeholder':'Informacion'}
        )
        }
        

       

class populares_form(forms.ModelForm):

    class Meta:
        model = populares_model
        fields = '__all__'
        widgets = {'descripcion':forms.Textarea(
            attrs = {'class':'form__descripcion','placeholder':'Descripcion'}
        ),
        'informacion': forms.Textarea(
            attrs ={'class':'form__informacion','placeholder':'Informacion'}
        )}
    



class login_form(forms.ModelForm):

    class Meta: 
        model= login_model
        fields = '__all__'
        

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class crear_usuario (UserCreationForm):
    username=forms.CharField(label= 'Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)