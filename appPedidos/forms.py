from django import forms
from .models import *
from django.forms import ModelForm
from django.conf import settings


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
