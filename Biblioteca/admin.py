from django.contrib import admin

# Register your models here.

from Biblioteca.models import Libro, Empleado, Cliente

admin.site.register(Libro)
admin.site.register(Empleado)
admin.site.register(Cliente)
