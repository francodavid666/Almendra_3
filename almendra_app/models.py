from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.



     


class login_model(models.Model):
     username= models.CharField(blank=True,null=True, max_length=50)
     password = models.CharField(blank=True,null=True, max_length=15)

'''

    def __str__(self):
     return f'usuario: {self.id}'
'''




class Product(models.Model):
     imagen = models.ImageField(blank=True, null = True,upload_to='products/')
     name = models.CharField(max_length=50, blank = True, null = True)
     description =  models.CharField(max_length=70, blank = True, null = True)
     price = models.DecimalField(max_digits=7,decimal_places=2)
     digital = models.BooleanField(default=False,null=True, blank=False)

     def __str__(self)-> str:
          return self.name

