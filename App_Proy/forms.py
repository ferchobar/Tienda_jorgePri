#from django.forms   import ModelForm
from django import forms
from App_Proy.models import cliente, producto, venta, carrito_ventas, ingreso_producto
#from .validators import MaxSizeFileValidator, StockValidator,validar_stock

class clienteForm(forms.ModelForm):
    class Meta:
        model=cliente
        fields = '__all__'
        
#from django.forms import Widget

class productoForm(forms.ModelForm):
    class Meta:
        model=producto
        #fields = '__all__'
        fields =['id_producto','nombre_producto','tipo_producto','precio_producto','descripcion_producto','stock']

class ventaForm(forms.ModelForm):
    class Meta:
        model=venta
        fields = '__all__'
        #fields = ['id_venta','cliente','fecha_venta','nombre_vendedor','Producto','precio_Venta_Total']
      

     #ingreso_productoForm
class ingreso_productoForm(forms.ModelForm):
    class Meta:
        model=ingreso_producto
        fields = '__all__'    
        

class carrito_ventasForm(forms.ModelForm):
    class Meta:
        model=carrito_ventas
        #    fields = '__all__' 
        fields=['id_carrito_ventas','venta','producto','unidades_vendidas','precio']




   
            