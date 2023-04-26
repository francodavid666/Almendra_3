from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class pasteleria_model (models.Model):

     imagen = models.ImageField(blank=True, null = True,upload_to='media/')
     titulo = models.CharField(max_length=50, blank = True, null = True)
     descripcion =  models.CharField(max_length=50, blank = True, null = True)
     informacion = models.CharField(max_length=184, blank = True, null = True)
     precio = models.CharField(max_length=50, blank = True, null = True)



class salados_model (models.Model):
     imagen = models.ImageField(blank=True, null = True)#upload_to='salados/')
     titulo = models.CharField(max_length=42, blank = True, null = True)
     descripcion =  models.CharField(max_length=50, blank = True, null = True)
     informacion = models.CharField(max_length=184, blank = True, null = True)
     precio = models.CharField(max_length=50, blank = True, null = True)


class bebidas_model (models.Model):
     imagen = models.ImageField(blank=True, null = True)#upload_to='bebidas/')
     titulo = models.CharField(max_length=42, blank = True, null = True)
     descripcion =  models.CharField(max_length=50, blank = True, null = True)
     informacion = models.CharField(max_length=184, blank = True, null = True)
     precio = models.CharField(max_length=50, blank = True, null = True)

   

class cafes_model(models.Model):
     imagen = models.ImageField(blank=True, null = True)#upload_to='cafes/')
     titulo = models.CharField(max_length=42, blank = True, null = True)
     descripcion =  models.CharField(max_length=184, blank = True, null = True)
     informacion = models.CharField(max_length=184, blank = True, null = True)
     precio = models.CharField(max_length=50, blank = True, null = True)


class brunch_model(models.Model):
     imagen = models.ImageField(blank=True, null = True)#upload_to='brunchs/')
     titulo = models.CharField(max_length=42, blank = True, null = True)
     informacion = models.CharField(max_length=184, blank = True, null = True)
     p1=models.CharField(max_length=40, blank = True, null = True)
     p2=models.CharField(max_length=40, blank = True, null = True)
     p3=models.CharField(max_length=40, blank = True, null = True)
     p4=models.CharField(max_length=40, blank = True, null = True)
     p5=models.CharField(max_length=40, blank = True, null = True)
    
     precio = models.CharField(max_length=50, blank = True, null = True)
     
 

class populares_model(models.Model):
     imagen = models.ImageField(blank=True, null = True)#upload_to='populares/')
     titulo = models.CharField(max_length=42, blank = True, null = True)
     
     informacion = models.CharField(max_length=184, blank = True, null = True)
     precio = models.CharField(max_length=50, blank = True, null = True)
     
     
     

class login_model(models.Model):
     username= models.CharField(blank=True,null=True, max_length=50)
     password = models.CharField(blank=True,null=True, max_length=15)

'''

    def __str__(self):
     return f'usuario: {self.id}'
'''