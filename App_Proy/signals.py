from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import  carrito_ventas,ingreso_producto,producto,venta
from django.db import transaction
from .forms import carrito_ventasForm
from django.core.exceptions import ValidationError
from django.db.models import Sum

@receiver(post_save, sender=carrito_ventas)
def actualizar_stock2(sender, instance, created, **kwargs):
     total_precio = producto.objects.aggregate(total=Sum('stock'))['total']
     print('Precio ',total_precio)
     

@receiver(post_save, sender=carrito_ventas)
def actualizar_stock(sender, instance, created, **kwargs):
             
    if created:
        producto = instance.producto
        producto.stock -= instance.unidades_vendidas
        producto.save()


@receiver(pre_save, sender=carrito_ventas)
def validar_stock(sender, instance, **kwargs):
    producto = instance.producto
    if producto.stock - instance.unidades_vendidas < 0:
         raise ValueError("No hay suficiente stock111")
         

@receiver(pre_save, sender=ingreso_producto)
def actualizar_stock_add(sender, instance, **kwargs):
        producto = instance.producto
        producto.stock += instance.add_Cantidad_producto
        producto.save()
