from django.contrib import admin 
from App_Proy.models import cliente 
from App_Proy.models import venta 
from App_Proy.models import producto
from App_Proy.models import ingreso_producto 
from App_Proy.models import carrito_ventas
from App_Proy.forms import carrito_ventasForm, productoForm

#Las siguientes 3 importacines son para la exportacion de datos en excel
import openpyxl, numpy # Se importa esta libreria para que muestre el formato excel en la exportacion de reportes
from openpyxl.utils.dataframe import dataframe_to_rows  # Se importa esta libreria para que muestre el formato excel en la exportacion de reportes
from import_export.admin import ImportExportModelAdmin # Se importa esta libreria para activar la funcion importar y exportar datos

#Octubre 30 de 2024
# LAs siguientes lineas desde aqui hasta el siguiente comentario de cierre
#Tiene la funcion de hacer que cuando se exporte la informacion a excel
# tambien exporte el nombre del cliente aunque a la fecha aun no exporta el nombre del producto
from import_export import resources, fields

class VentaResource(resources.ModelResource):
    cliente_nombre = fields.Field(column_name='Nombre del Cliente', attribute='cliente__nombre_completo')    
    # Para mostrar los nombres de todos los productos asociados a la venta
    producto = fields.Field(column_name='Producto', attribute='producto_set__nombre_producto')
    
    def get_producto(self, obj):
        return ', '.join(producto.nombre_producto for producto in obj.producto_set.all())

    class Meta:
        model = venta
        exclude = ('id_venta',)  # Excluye el ID de la venta si no lo necesitas
        prefetch_related = ('producto_set',)  # Precarga los productos relacionados
# Cierre del comentario


# Creamos una clase administrador para el carrito de ventas
# esta clase carrito_ventasInLine sirve para que los productos salgan en el mismo formulario debajo 
# del formulario venta
class carrito_ventasInLine(admin.TabularInline):
    model= carrito_ventas
    extra =1
    autocomplete_fields = ['producto_id']

#class clientesAdmin(admin.ModelAdmin): 
class clientesAdmin(ImportExportModelAdmin):
    #list_display=("nombres","apellidos","telefono") 
    search_fields=("nombres","apellidos","telefono") 
    list_filter=("nombres","apellidos")
    ordering=('apellidos',)
    list_per_page=5

    #El siguiente codigo hace que los datos se conviertan en mayuscula
    #Tambien tener en cuenta que tambien debe cambiar el titulo en list_display (nnombre y aapellido)
    list_display=("nnombres","aapellidos","telefono") 
    def nnombres(self, obj):
        return obj.nombres.upper()
    
    def aapellidos(self, obj):
        return obj.apellidos.upper()
    #   https://www.youtube.com/watch?v=QtYJ70yFWjQ


from django.utils.html import format_html # Se importa esta libreria para dar formato al valor que se muestra

class VentasAdmin(ImportExportModelAdmin):
    resource_class = VentaResource # Codigo que exporta el nombre del cliente a a excel en el informe
    inlines =[carrito_ventasInLine] # esta linea sirve para que en el mismo formulario de venta se anexen los productos en un solo guardado
    list_display=["id_venta","total_venta","fecha_venta","cliente", "nombre_vendedor"] # esta linea list_dysplay sirve para mostrar los datos en el formulario y tambien para exportar los datos a un archivo externo
    search_fields = ('nombre_vendedor','cliente__nombres__icontains',) #cliente__nombres__icontains Este codig permitio que se hiciera una busqueda en el atributo nombre de la tabla cliente, que al se llave foranea no permitia hacer busquedas por si sola
    list_filter = ('fecha_venta','nombre_vendedor','Producto') # Filtro dentro de la pagina
    list_per_page=5

#Las siguientes 3 lineas de codigo dan un formato a la variable total_venta que viene del modelo 
#de una funcion en la tabla venta. Colocando el signo pesos adelante del precio

    def total_venta(self, obj):
        return format_html('$ {}', obj.total_venta)
    total_venta.short_description = 'Total Venta'

    
"""
    @property
    def export(self, queryset, *args, **kwargs):
        # Obtener los datos en forma de DataFrame (por ejemplo, usando pandas)
        dataframe = pd.DataFrame(queryset.values())

        # Crear un nuevo libro de trabajo de Excel
        workbook = openpyxl.Workbook()
        worksheet = workbook.active

        # Escribir los datos del DataFrame en la hoja de cálculo
        for r in dataframe_to_rows(dataframe, index=False, header=True):
            worksheet.append(r)

        # Guardar el archivo Excel
        filename = 'productos.xlsx'
        workbook.save(filename)
"""

""" # El siguiente codigo fue desactivado porque fue reemplacado porque se 
    # cambio admin.ModelAdmin por ImportExportModelAdmin
class VentasAdmin(admin.ModelAdmin): 
    inlines =[carrito_ventasInLine]
    #list_display=("id_venta","total_venta","fecha_venta","cliente", "nombre_vendedor")
    #search_fields = ('fecha_venta','nombre_vendedor','producto','cliente') 
    search_fields = ('nombre_vendedor','cliente__nombres__icontains',) #cliente__nombres__icontains Este codig permitio que se hiciera una busqueda en el atributo nombre de la tabla cliente, que al se llave foranea no permitia hacer busquedas por si sola
    list_filter = ('fecha_venta','nombre_vendedor','Producto')
    list_per_page=5
    #exclude=('precio_Venta_Total',)

#Las siguientes 3 lineas de codigo dan un formato a la variable total_venta que viene del modelo 
#de una funcion en la tabla venta. Colocando el signo pesos adelante del precio

    def total_venta(self, obj):
        return format_html('$ {}', obj.total_venta)
    total_venta.short_description = 'Total Venta'
"""

   
class ProductoAdmin(ImportExportModelAdmin): 
    inlines =[carrito_ventasInLine] 
    #list_display=("nombre_producto","tipo_producto","precio_producto","stock","descripcion_producto") # Muestra los campos en el formulario
    list_display=("nombre_completo_producto","precio_producto","stock","descripcion_producto") # Muestra los campos en el formulario
    list_display_links=("nombre_completo_producto",) # Permite que el campo sea vinculo para editar registro
    
    search_fields=("nombre_producto","tipo_producto") # Muestra cuadro de texto para escribir y buscar información
    list_filter=("nombre_producto","tipo_producto",) # Permite mostrar campos a filtrar
    list_editable = ('descripcion_producto',) # Permite editar campos directamente y guardarlos masivamente
    list_per_page=5 # Organiza mucha informacion en páginas
    exclude=('stock',)

   
class IngresoPAdmin(ImportExportModelAdmin): 
    list_display=("producto","add_Cantidad_producto","fecha_add","nombre_alimentador") 
    search_fields=("add_Cantidad_producto","nombre_alimentador") 
    list_filter=("nombre_alimentador","fecha_add")
    list_per_page=5

"""class Carrito_VentasAdmin(admin.ModelAdmin): 
    list_display=("venta","producto","unidades_vendidas") 
    search_fields=("venta","producto") 
    list_filter=("producto",)
    list_per_page=10
"""

admin.site.register(cliente,clientesAdmin) 
admin.site.register(venta,VentasAdmin)
admin.site.register(producto,ProductoAdmin) 
admin.site.register(ingreso_producto,IngresoPAdmin) 
#admin.site.register(carrito_ventas,Carrito_VentasAdmin)