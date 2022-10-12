"""EntregaFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Biblioteca.views import (
    mostrar_inicio,
    mostrar_libros,
    mostrar_empleados,
    mostrar_clientes,
    formulario_de_libros,
    buscar_libros,
    buscando,
    formulario_de_empleados,
    buscar_empleados,
    buscando_empleados,
    formulario_de_clientes,
    buscar_clientes,
    buscando_clientes
)


urlpatterns = [
    path("inicio/", mostrar_inicio, name="inicio"),
    path("libros/", mostrar_libros, name="libros"),
    path("empleados/", mostrar_empleados, name="empleados"),
    path("clientes/", mostrar_clientes, name="clientes"),
    path("registro-de-libros/", formulario_de_libros, name="registro-de-libros"),
    path("busqueda-libros/", buscar_libros, name="busqueda-libros"),
    path("buscando/", buscando),
    path("registro-de-empleados/", formulario_de_empleados, name="registro-de-empleados"),
    path("busqueda-empleados/", buscar_empleados, name="busqueda-empleados"),
    path("buscando-empleados/", buscando_empleados),
    path("registro-de-clientes/", formulario_de_clientes, name="registro-de-clientes"),
    path("busqueda-clientes/", buscar_clientes, name="busqueda-clientes"),
    path("buscando-clientes/", buscando_clientes),
]