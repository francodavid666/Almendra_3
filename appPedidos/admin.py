from django.contrib import admin
from .models import*

admin.site.register (Customer)
admin.site.register (pedidos_model)
admin.site.register (usuario_model)
admin.site.register (Order)
admin.site.register (OrderItem)
admin.site.register (ShippingAddress)

