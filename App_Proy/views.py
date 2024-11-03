from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from App_Proy.models import cliente, producto, venta, carrito_ventas, ingreso_producto
from App_Proy import forms
from .forms import carrito_ventasForm # Se importa este formulario para impedir que se venda mas del inventario

from App_Proy.views import *
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt    
from django.utils.decorators import method_decorator


class ClienteCreateView(CreateView):
    model= cliente
    form_class = forms.clienteForm #Debe haberse creado ClienteForm en el archivo form.py
    template_name = 'Crear/Crear_Cliente.html'
    success_url = reverse_lazy('mostrarCli')
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['titulo']= 'Creación de un Cliente'
        context['entity'] = 'Cliente'
        return context
    

class ProductoCreateView(CreateView):
    model= producto
    form_class = forms.productoForm #Debe haberse creado ClienteForm en el archivo form.py
    template_name = 'Crear/Crear_Cliente.html' # FUNCIONA para abrir la pagina html
    success_url = reverse_lazy('mostrarPro') #  FUNCIONA para enrutar una pagina de respuesta despues de haber guardado el nuevo registro en la base de datos
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['titulo']= 'Creación de un Producto'
        return context
    

class VentaCreateView(CreateView):
    model= venta
    form_class = forms.ventaForm #Debe haberse creado ClienteForm en el archivo form.py
    template_name = 'Crear/Crear_Cliente.html'
    success_url = reverse_lazy('Nuevo_Carrito_ventas') 

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['titulo']= 'Creación de una Venta'
        return context
    

class Carrito_ventasCreateView(CreateView):
    model= carrito_ventas
    form_class = forms.carrito_ventasForm  #Debe haberse creado ClienteForm en el archivo form.py
    template_name = 'Crear/Crear_Cliente.html'
    ssuccess_url = reverse_lazy('muestra_Carrito_Ven') 
   
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['titulo']= 'Productos Seleccionados en la Venta'
        return context
    

class Ingreso_productoCreateView(CreateView):
    model= ingreso_producto
    form_class = forms.ingreso_productoForm #Debe haberse creado ClienteForm en el archivo form.py
    template_name = 'Crear/Crear_Cliente.html'
    success_url = reverse_lazy('muestra_inventario') 

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['titulo']= 'Alimentación de Inventario de Productos'
        return context


class ClienteListView(ListView):
    model = cliente
    template_name = 'muestra_clientes.html'

    #@csrf_exempt
    #@method_decorator(csrf_exempt) #Esta linea de codigo sirve para deshabilitar la seguridad y permitir realizar el proceso
    #def dispatch(self, request, *args, **kwargs ):
    #    return super().dispatch(request,*args, **kwargs )

    def post(self, request, *args, **kwargs ):
        data={'name' : 'Wlliam'}
        return JsonResponse(data)
    
    def get_queryset(self):
        return cliente.objects.all() #Muestra toda la informacion de la tabla
        #return cliente.objects.filter(nombres__startswith='f') 

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        
        context['col0']= 'Identificador del Cliente'
        context['col1']='Nombres '
        context['col2']='Apellidos'
        context['col3']='Teléfono'
        context['col4']='Genero'
        context['titulo']='Clientes'
        #context['object_list'] = cliente.objects.all() #Muestra toda la informacion de la tabla
        return context
    

class ProductoListView(ListView):
    model = producto
    template_name = 'muestra_productos.html'

    def get_queryset(self):
        return producto.objects.all() #Muestra toda la informacion de la tabla
        #return cliente.objects.filter(nombres__startswith='f') 

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['col0']= 'Identificador del Producto'
        context['col1']='Producto'
        context['col2']='Tipo de Producto'
        context['col3']='Precio'
        context['col4']='Existencias'
        context['titulo']='Productos'
        #context['object_list'] = cliente.objects.all() #Muestra toda la informacion de la tabla
        return context
    

class VentaListView(ListView):
    model = venta
    template_name = 'muestra_venta.html'

    def get_queryset(self):
        return venta.objects.all() #Muestra toda la informacion de la tabla
        #return cliente.objects.filter(nombres__startswith='f') 

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['col0']= 'Identificador de la Venta'
        context['col1']='Cliente'
        context['col2']='Fecha de Venta'
        context['col3']='Vendedor'
        context['col4']=''
        context['titulo']='Ventas'
        #context['object_list'] = cliente.objects.all() #Muestra toda la informacion de la tabla
        return context
    

class CarritoVentaListView(ListView):
    model = carrito_ventas
    template_name = 'muestra_CarritoVenta.html'

    def get_queryset(self):
        return carrito_ventas.objects.all() #Muestra toda la informacion de la tabla
        #return cliente.objects.filter(nombres__startswith='f') 

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['col0']= 'Identificador del Producto Vendido'
        context['col1']='Venta'
        context['col2']='Producto'
        context['col3']='Unidades Vendidas'
        context['col4']='Precio'
        context['titulo']='Carrito de ventas'
        #context['object_list'] = cliente.objects.all() #Muestra toda la informacion de la tabla
        return context
    

class Ingreso_productoListView(ListView):
    model = ingreso_producto
    template_name = 'muestra_Inventario_Pro.html'

    def get_queryset(self):
        return ingreso_producto.objects.all() #Muestra toda la informacion de la tabla
        #return cliente.objects.filter(nombres__startswith='f') 
        
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['col0']= 'Identificador del Inventario'
        context['col1']='Producto'
        context['col2']='Cantidad'
        context['col3']='Fecha'
        context['col4']='Alimentador'
        context['titulo']='Alimentación del Inventario'
        
        return context
    

def indexx(request):
    return render(request,'index.html')