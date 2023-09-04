from django import forms
from .models import *
from django.forms import ModelForm
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class UserEditFormName(UserCreationForm):
    first_name = forms.CharField(label = 'Primer Nombre')
    last_name = forms.CharField(label = 'Apellido')

    class Meta:
       model = User
       fields = ['last_name','first_name']
       help_texts = {k:'ashe' for k in fields}


class UserEditFormUsername(UserCreationForm):
    username = forms.CharField(label = 'Nuevo nombre de usuario')


    class Meta:
       model = User
       fields = ['username']
       help_texts = {k:'ashe' for k in fields}



class UserEditForm(UserCreationForm):
   
   email = forms.EmailField(label='Ingrese el nuevo Email')
   password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput)
   password2 = forms.CharField(label='Confirmar contraseña', widget= forms.PasswordInput)

   class Meta:
       model = User
       fields = ['email','password1','password2']
       help_texts = {k:'ashe' for k in fields}


class UserRegisterForm(UserCreationForm):
   
   first_name = forms.CharField(label = 'Nombre')
   last_name = forms.CharField(label = 'Apellido')
   username = forms.CharField(label = 'Nombre de usuario')
   email = forms.EmailField()
   password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput)
   password2 = forms.CharField(label='Confirmar contraseña', widget= forms.PasswordInput)

   class Meta:
       model = User
       fields = [ 'first_name','last_name','username','email', 'password1','password2']
       #help_texts = {k:'ashe' for k in fields}



#LOGIN
class UserCreationForm(AuthenticationForm):
   email = forms.EmailField()
   password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput)

   class Meta:
       model = User
       fields = [ 'email', 'password1']
       



class usuario_form(forms.ModelForm):
    class Meta:
        model = usuario_model
        fields='__all__'
        

class pedidos_form (forms.ModelForm):

    class Meta:
        model = pedidos_model
        fields ='__all__'
        widgets={'tamanio':forms.TextInput(
            attrs={
              'class':'input_tamanio',
          
              'id':'inputCafe'
            },    
        ),
        'azucar':forms.TextInput(
            attrs={
                'class':'input_azucar',

                'id':'inputAzucar'
            }
        ),
        'adicional':forms.TextInput(
            attrs={
                'class':'input_adicional',
                'id':'inputAdicional'
            }
        ),
           'total':forms.NumberInput(
            attrs={
                'class':'input_total',
                'id':'inputTotal'
            }
        )
        ,
           'tamanio_precio':forms.NumberInput(
            attrs={
                'class':'input_tamanio-precio',
                'id':'inputTamanioPrecio'
            }
        )
        }
