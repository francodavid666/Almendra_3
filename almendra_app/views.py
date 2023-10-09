from django.shortcuts import render, redirect
from almendra_app.forms import *
from django.contrib import messages
from .models import *
from django.template import loader
from django.http import HttpResponse
from appPedidos.models import *
from django.contrib.auth.decorators import login_required
from appPedidos.utils import cookieCart,cartData


#@login_required
def inicio (request):
    data = cartData(request)
    cartItems = data['cartItems']

    form  = Product.objects.all()    
    context = {'form':form,'cartItems':cartItems}
    
    return render (request,'almendra_app/inicio.html',context)

def inicio_2 (request):

    products = Product.objects.all()
   
    
    return render (request,'almendra_app/inicio.html',{'products':products,                                          
                   })
# LOGIN

#importamos para auntenticar usuarios
from django.contrib.auth.forms import AuthenticationForm
#importamos para logearse y auntenticar usuarios
from django.contrib.auth import login,authenticate




def login_formulario (request):
    if request.user.is_authenticated:
     return redirect("opciones")

    if request.method=='POST':
                #rechaza a los usuarios cuyo indicador de false
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            usu= request.POST['username']
            contra = request.POST['password']

            usuario = authenticate(username=usu,password=contra)
            
            if usuario is not None:
                login(request,usuario)
                return redirect ('opciones')
        else:
            messages.info(request,'usuario o contraseña incorrectos')
            return redirect ('login_formulario')

    else:
        form = AuthenticationForm()
        return render (request,'almendra_app/login_formulario.html',{'form':form})