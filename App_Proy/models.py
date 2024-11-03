from django.db import models, transaction
from datetime import datetime
from .choices import sexos


class cliente(models.Model):
    id_cliente=models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=150,verbose_name="Nombre del Cliente",null=True,blank=True)
    apellidos = models.CharField(max_length=150,verbose_name="Apellidos del Cliente",null=True,blank=True)
    telefono = models.CharField(default="3",max_length=15,blank=True,null=True)
    sexo =models.CharField(max_length=1, choices=sexos,default='F')

    def nombre_completo(self):
        return "{} {}".format(self.nombres, self.apellidos)

    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name='cliente'
        db_table='cliente'

class producto(models.Model):
    id_producto=models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=50,default="")
    tipo_producto = models.CharField(max_length=35,default="Tipo")
    precio_producto = models.DecimalField(max_digits=10, decimal_places =2, default=0)
    descripcion_producto = models.CharField(default="Desc",max_length=150,blank=True,null=True)
    #stock = models.PositiveIntegerField(default=0)#, validators=[validar_cantidad_positiva]) 
    stock = models.IntegerField(default=0)

    def nombre_completo_producto(self):
        return "{},{}".format(self.nombre_producto, self.tipo_producto)

    def __str__(self):
        return self.nombre_completo_producto()    
    
    class Meta:
        verbose_name='producto'
        db_table='producto'



from django.db.models import Sum
#from import_export import resources

class venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(cliente,null=True,blank=True,on_delete=models.CASCADE)
    fecha_venta = models.DateField("Fecha de la Venta",auto_now=True)
    nombre_vendedor = models.CharField(max_length=20)
    #Creamos un nuevo campo de tipo muchos a muchos
    Producto = models.ManyToManyField(producto,through = 'carrito_ventas', blank = True,)
    #precio_Venta_Total = models.BigIntegerField("Precio Venta Total",default=0)
    #precio_Venta_Total = models.DecimalField(max_digits=10, decimal_places =0, default=0)
 
    def nombre_venta(self):
        return "{},{}".format(self.id_venta, self.cliente,  self.fecha_venta, self.nombre_vendedor)

    def __str__(self):
        return self.nombre_venta()
    
    class Meta:
        verbose_name='venta'
        db_table='venta'




#Oct 27 2024 Prueba, primero se instalo "pip install django-import-export"
#Luego se configuro en INSTALLED_APPS importando 'import_export',
#La siguiente clase ProductoResource ayudará a exportar un archivo con informacion del modelo
#class ventaResource(resources.ModelResource):
#    class Meta:
#        model = venta
    
#LAs siguientes 3 lineas de codigo funcionan muy bien, crean un nuevo campo llamado total_venta
# y lo incluye dentro del list_display del archivo admin en la tabla venta
#Esta informacion en la funcion total_venta luego adquiere un formato en el admin
    @property
    def total_venta(self):
        return self.carrito_ventas_set.aggregate(total=Sum('precio'))['total']

 
class carrito_ventas(models.Model): 
    id_carrito_ventas = models.AutoField(primary_key=True)
    venta = models.ForeignKey(venta,on_delete=models.CASCADE)
    producto = models.ForeignKey(producto,null=True,blank=True,on_delete=models.CASCADE)
    unidades_vendidas =models.PositiveIntegerField(default=0) 
    precio=models.BigIntegerField("Precio_carrito",default=0)
        
    def save(self, *args, **kwargs):
        self.precio = self.unidades_vendidas * self.producto.precio_producto
        super().save(*args, **kwargs)

    class Meta:
        verbose_name='Carrito_ventas'
        db_table='carrito_ventas'


class ingreso_producto(models.Model):
    id_ingreso = models.AutoField(primary_key=True)
    producto = models.ForeignKey(producto,null=True,blank=True,on_delete=models.CASCADE)
    add_Cantidad_producto = models.IntegerField(default=0)
    fecha_add = models.DateField(auto_now=True)
    nombre_alimentador = models.CharField(max_length=200)
   
    class Meta:
        verbose_name='Inventario de Producto'
        db_table='ingreso_producto'  