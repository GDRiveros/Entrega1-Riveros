from django.db import models

# Create your models here.

class Libros(models.Model):
    autor = models.CharField(max_length=40)
    titulo = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.titulo} de {self.autor}"

class Empleados(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


