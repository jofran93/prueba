from django.db import models
from django.contrib.auth.models import User

# Modelo para representar a una Comunidad
class Comunidad(models.Model):
    nombre = models.CharField(max_length=100)
    num_inmueble = models.CharField(max_length=100)
    estacionamientos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='comunidad_fotos/', blank=True)

    def __str__(self):
        return self.nombre

# Modelo para representar un Propietario
class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=15)
    comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
    residente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='residentes', blank=True, null=True)
    estacionamiento = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo para representar un Administrador
class Administrador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='administrador_fotos/', blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo para representar un Usuario (Trabajador)
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='usuario_fotos/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuarios')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo para representar una Visita
class Visita(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='visita_fotos/', blank=True)
    num_departamento = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

