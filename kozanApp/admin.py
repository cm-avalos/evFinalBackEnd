from django.contrib import admin

# Register your models here.


from kozanApp.models import Equipos,Empleado,Area,Trabajador


class EquiposAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'procesador', 'grafica', 'memoria', 'nequipo']

admin.site.register(Equipos, EquiposAdmin)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'rut', 'correo', 'cargo', 'telefono']

admin.site.register(Empleado, EmpleadoAdmin)    

class AreaAdmin(admin.ModelAdmin):
    list_display = ['nombreArea', 'encargado', 'piso', 'sector', 'descripcion', 'capacitacion']

admin.site.register(Area, AreaAdmin) 

class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'rut', 'correo', 'cargo', 'numero']

admin.site.register(Trabajador, TrabajadorAdmin)
   