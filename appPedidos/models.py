from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

     

class pedidos_model (models.Model):
     cantidad = models.IntegerField(blank=True,null=True)
     tamanio = models.CharField(max_length=30,blank = True, null = True)
     tamanio_precio =  models.IntegerField(blank=True,null=True)
     azucar = models.CharField(max_length=30,blank = True, null = True)
     adicional = models.CharField(max_length=30,blank = True, null = True)
     total = models.FloatField(blank=True,null=True)

     #mrt

class usuario_model (models.Model):
     foto_perfil = models.ImageField(blank=True, null = True)
     nombre =models.CharField(max_length=100,blank = True, null = True)
     email = models.EmailField(max_length=100,blank = True, null = True)
     contraseña = models.EmailField(max_length=10,blank = True, null = True)
     tags = models.CharField(max_length=100,blank = True, null = True)
