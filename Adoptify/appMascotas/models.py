from django.db import models

# Create your models here.
# clase para guardar las diferentes localidades
class Localidad(models.Model):
    nombre = models.CharField(max_length=25)
    def __str__(self):
        return self.nombre

#clase para clasificar la edad del animal
class Edad(models.Model):
    edad = models.DecimalField(decimal_places=0, max_digits=3)
    def __str__(self):
        return "{}".format(self.edad)

#clase para clasificar el sexo de los animales
class Sexo(models.Model):
    nombre = models.CharField(max_length=15)
    def __str__(self):
        return self.nombre

#clase para clasificar las razas de los animales
class Raza(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

#clase para clasificar las especies de los animales
class Especie(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Publicacion(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    descripcion= models.CharField(max_length=300,default='')
    # foto
    telefono = models.DecimalField(max_digits=15,decimal_places=0)
    localidad = models.ForeignKey(Localidad, default=1, on_delete=models.PROTECT)
    edad = models.ForeignKey(Edad, default=1, on_delete=models.PROTECT)
    especie = models.ForeignKey(Especie, default=1, on_delete=models.PROTECT)
    raza = models.ForeignKey(Raza, default=1, on_delete=models.PROTECT)
    sexo = models.ForeignKey(Sexo, default=1, on_delete=models.PROTECT)
    def __str__(self):
        return "Fecha:{} Descripcion:{} Telefono:{} Localidad: {} Edad:{} Especie: {} Raza:{} Sexo: {}".format(self.fecha,self.descripcion, self.telefono, self.localidad, self.edad, self.especie, self.raza, self.sexo)

        