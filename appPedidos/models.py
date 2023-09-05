from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from almendra_app.models import *
from django.contrib.auth.models import User

 

# Create your models here.

class usuario_model (models.Model):
    # foto_perfil = models.ImageField(blank=True, null = True)
     nombre =models.CharField(max_length=100,blank = True, null = True)
     email = models.EmailField(max_length=100,blank = True, null = True)
     contrasenia = models.CharField(max_length=100,blank = True, null = True)
     #tags = models.CharField(max_length=100,blank = True, null = True)
     
class Customer(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
     name = models.CharField(max_length=200,null=True)
     email = models.CharField(max_length=200,null=True)

     def __str__(self):
          return self.name

class pedidos_model (models.Model):
     cantidad = models.IntegerField(blank=True,null=True)
     tamanio = models.CharField(max_length=30,blank = True, null = True)
     tamanio_precio =  models.IntegerField(blank=True,null=True)
     azucar = models.CharField(max_length=30,blank = True, null = True)
     adicional = models.CharField(max_length=30,blank = True, null = True)
     total = models.FloatField(blank=True,null=True)

     #mrt



class Order(models.Model):
     customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, blank=True, null=True)
     date_orderd= models.DateTimeField(auto_now_add=True)
     complete = models.BooleanField(default=False,null= True, blank=False)
     transaction_id= models.CharField(max_length=200, null=True)

     def __str__(self):
          return str(self.id)
     
     @property
     def shipping(self):
          shipping = False
          orderitems = self.orderitem_set.all()
          for i in orderitems:
               if i.product.digital ==False:
                    shipping = True
          return shipping

     @property
     def get_cart_total(self):
          orderitems=self.orderitem_set.all()
          total = sum([item.get_total for item in orderitems])
          return total
     
     @property
     def get_cart_items(self):
          orderitems = self.orderitem_set.all()
          total = sum([item.quantity for item in orderitems])
          return total
     
class OrderItem(models.Model):
     product = models.ForeignKey(Product,on_delete=models.SET_NULL, blank=True, null=True)  
     order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True, null=True ) 
     quantity = models.IntegerField(default=0 ,blank=True, null=True)
     date_added = models.DateTimeField(auto_now=True)

     @property
     def get_total(self):
          total = self.product.price * self.quantity
          return total

#direcion de envio
class ShippingAddress(models.Model):
     customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, blank=True, null=True)
     order = models.ForeignKey(Order,on_delete=models.SET_NULL, blank=True, null=True)
     address = models.CharField(max_length=200, null=True)
     city = models.CharField(max_length=200, null=True)
     state = models.CharField(max_length=200, null=True)
     zipcode = models.CharField(max_length=200, null=True)
     date_added = models.CharField(max_length=200, null=True)


     def __str__(self):
          return self.address

