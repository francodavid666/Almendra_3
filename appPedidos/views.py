from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from appPedidos.models import *
from almendra_app.models import *
from almendra_app.views import inicio
from appPedidos.forms import *
from django.template import loader
from django.contrib.auth.decorators import login_required
import json
import datetime





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
    

def register(request):
    if request.method == 'POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
           
           # username= form.cleaned_data['username']
            #email= form.cleaned_data['email']
            #password1= form.cleaned_data['password1']
            #password2= form.cleaned_data['password2']
        
            form.save()
            messages.success (request,'¡Nuevo producto creado!')
            return redirect ('login')
        else:
            return redirect ('register')
    else:
        form  = UserRegisterForm()
        return render(request,'register/register.html',{
            'form':form
        })
    


def Login_request(request):
    if request.method =='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password =request.POST["password"]

            usuario = authenticate(username = username, password = password)
            if usuario is not None:
                login(request,usuario)
            
                
                return inicio(request)

                
            else:
                form = AuthenticationForm()
                mensaje = 'Usuario o contraseña incorresta'
                return render (request,'registration/login.html',{'mensaje':mensaje,
                                                                  'form':form})

        else:
            form = AuthenticationForm()
            mensaje = 'Formulario incorrecto'
            return render (request,'registration/login.html',{'mensaje':mensaje,
                                                              'form':form})
            # Redirect to a success page.
        
            # Return an 'invalid login' error message.
    else:
        form = AuthenticationForm()
        return render(request,'registration/login.html',{'form':form})
    



@login_required
def profile (request):
    return render (request,'profile/profile.html')    

@login_required
def settingProfile (request):
    return render (request,'profile/settingProfile.html')

@login_required
def edit_email(request):
    usuario = request.user
    if request.method == 'POST':
        form =UserEditForm (request.POST , instance = usuario)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info["email"]
            usuario.password1 = info["password1"]
            usuario.password1 = info["password2"]
          
            usuario.save()
            return render(request,'profile/profile.html')

        else:
            messages = 'algo salio mal'
            return render(request,'profile/edit_email.html',{'form': form,'messages':messages})
    else:
        form = UserEditForm()     
    return render(request,'profile/edit_email.html',{'form': form})

@login_required
def edit_username(request):
    usuario = request.user
    if request.method == 'POST':
        form =UserEditFormUsername (request.POST , instance = usuario)
        if form.is_valid():
            info = form.cleaned_data
            usuario.username = info["username"]
            usuario.password1 = info["password1"]
            usuario.password1 = info["password2"]
          
            usuario.save()
            return render(request,'profile/profile.html')

        else:
            messages = 'algo salio mal'
            return render(request,'profile/edit_username.html',{'form': form,'messages':messages})
    else:
        form = UserEditFormUsername()     
    return render(request,'profile/edit_username.html',{'form': form})


@login_required
def edit_name(request):
    usuario = request.user
    if request.method == 'POST':
        form =UserEditFormName (request.POST , instance = usuario)
        if form.is_valid():
            info = form.cleaned_data
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            #usuario.password1 = info["password2"]
          
            usuario.save()
            return render(request,'profile/profile.html')

        else:
            messages = 'algo salio mal'
            return render(request,'profile/edit_name.html',{'form': form,'messages':messages})
    else:
        form = UserEditFormName()     
    return render(request,'profile/edit_name.html',{'form': form})




def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:',action)
    print('productId:',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer,complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)
   
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    print('se guardo')
    orderItem.save()
    
    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)




def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer =customer,complete=False )
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items =[]
        cartItems  = order['get_cart_items']
        order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}
    return render(request,'almendra_app/cart.html',{'items':items,'order':order,'cartItems':cartItems})


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer =customer,complete=False )
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items =[]
        order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems  = order['get_cart_items']
    context = {'items':items,'order':order,'cartItems':cartItems}
    return render(request,'almendra_app/checkout.html', context)


def processOrden(request):
   # print('Data:',request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer =customer,complete=False )
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()


        if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address= data['shipping']['address'],
                city= data['shipping']['city'],
                state= data['shipping']['state'],
                zip= data['shipping']['zip'],
                zip2= data['shipping']['zip2'],
    
            )

    else:
        print('User is not logged in...')
    return JsonResponse('Paymen complete', safe=False)