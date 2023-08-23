from django.shortcuts import render, redirect
from appPedidos.forms import *
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from appPedidos.models import *
from almendra_app.models import *


def appPedidos(request,id):
    if request.method =='POST':
        form = pedidos_form(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            cantidad = info.get('cantidad')
            tamanio= info.get('tamanio')
            tamanio_precio= info.get('tamanio_precio')
            azucar= info.get('azucar')
            adicional= info.get('adicional')
            total= info.get('total')

            pedido_1 = pedidos_model(
                cantidad = cantidad,
                tamanio = tamanio,
                tamanio_precio = tamanio_precio,
                azucar = azucar,
                adicional = adicional,
                total = total
            )

            pedido_1.save()
            return redirect ('appPedidos')
            messages.success (request,'¡Nuevo producto creado!')
    else:
        
        model_producto = cafes_model.objects.get(id=id)
        model = pedidos_model.objects.all()
        hola = id
        form = pedidos_form()
        return render(request,'especificaciones.html',{'model':model,
                                                       'model_product':model_producto,
                                                    'form':form,
                                                    'hola':hola},
                                                    )