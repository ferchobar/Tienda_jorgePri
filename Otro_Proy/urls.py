
from django.contrib import admin
from django.urls import path, include
from App_Proy.views import *
from App_Proy import views


app_name = 'vst'

urlpatterns = [
    path('', admin.site.urls),
    #path('mostrarCli/',views.Muestra_clientes), 
    path('mostrarCli/',ClienteListView.as_view(),name='mostrarCli'),
    path('mostrarPro/',ProductoListView.as_view(),name='mostrarPro'),
    path('mostrarVen/',VentaListView.as_view(),name='mostrarVen'),
    path('muestra_Carrito_Ven/',CarritoVentaListView.as_view(),name='muestra_Carrito_Ven'),
    path('muestra_inventario',Ingreso_productoListView.as_view(),name='muestra_inventario'),


    path('Nuevo_Cliente/',ClienteCreateView.as_view(),name='Nuevo_Cliente'),
    path('Nuevo_Producto/',ProductoCreateView.as_view(),name='Nuevo_Producto'),
    path('Nuevo_Venta/',VentaCreateView.as_view(),name='Nuevo_Venta'),
    path('Nuevo_Carrito_ventas/',Carrito_ventasCreateView.as_view(),name='Nuevo_Carrito_ventas'),
    path('Nuevo_inventario/',Ingreso_productoCreateView.as_view(),name='Nuevo_inventario'),
    #path('Combinada/',VENTA_CLIENTECreateView.as_view(),name='Combinada'),
    #path('agregar_producto_a_venta/<int:venta>/', views.agregar_producto_a_venta, name='agregar_producto'),


    #path('guardar_carrito/', guardar_carrito, name='guardar_carrito'),
    
    #path('',include('App_Proy.urls')),  
    
    #path('',indexx),  

    
    
 
]
