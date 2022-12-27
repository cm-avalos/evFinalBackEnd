from django.db import models


# Create your models here.


class Equipos(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    procesador = models.CharField(max_length=50)
    grafica = models.CharField(max_length=50)
    memoria= models.CharField(max_length=50)
    nequipo=models.CharField(max_length=50)






class Area(models.Model):
    nombreArea = models.CharField(max_length=50)
    encargado = models.CharField(max_length=50)
    piso = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    capacitacion = models.CharField(max_length=2)

    def nombre_area(self):
        return "{}".format(self.nombreArea)

    def __str__(self): 
        return self.nombre_area()

    class Meta:
        verbose_name='Area'
        verbose_name_plural='Areas'
        db_table='area'
        ordering=['nombreArea']


class Empleado(models.Model):
    area=models.ForeignKey(Area,null=True,blank=True,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

# API REST ---------------------------------------------------------------------------------------------------------------------------


class Trabajador(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    numero = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self) :
        return str(self.id)+ " " + self.nombre + " (RUT: " + str(self.numero) + ")"

