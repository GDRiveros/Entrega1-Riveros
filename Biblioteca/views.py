from django.shortcuts import render
from Biblioteca.forms import (
    FormularioLibros,
    FormularioEmpleados,
    FormularioClientes
)
from Biblioteca.models import Libro, Empleado, Cliente
from django.http import HttpResponse

# Create your views here.

def mostrar_inicio(request):
    return render(request, "Biblioteca/inicio.html")

def mostrar_libros(request):
    return render(request, "Biblioteca/libros.html")

def mostrar_empleados(request):
    return render(request, "Biblioteca/empleados.html")

def mostrar_clientes(request):
    return render(request, "Biblioteca/clientes.html")


def formulario_de_libros(request):
    if request.method != "POST":
        mi_form = FormularioLibros()
    else:
        mi_form = FormularioLibros(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            libro = Libro(autor=info["autor"], titulo=info["titulo"])
            libro.save()
            return render(request, "Biblioteca/inicio.html")

    contexto = {
        "formulario": mi_form
        }

    return render(request, "Biblioteca/formulariolibros.html", contexto)

def buscar_libros(request):
    return render(request, "Biblioteca/buscarlibros.html")

def buscando(request):
   if not request.GET["titulo"]:
      return HttpResponse("No enviaste datos")
   else:
        titulo_a_buscar = request.GET["titulo"]
        libro = Libro.objects.filter(titulo=titulo_a_buscar)

        contexto = {
            "titulo": titulo_a_buscar,
            "libro": libro
        }

        return render(request, "Biblioteca/resultadobusquedalibro.html", contexto)


def formulario_de_empleados(request):

    if request.method != "POST":
        mi_form = FormularioEmpleados()
    else:
        mi_form = FormularioEmpleados(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            empleado = Empleado(nombre=info["nombre"], apellido=info["apellido"])
            empleado.save()
            return render(request, "Biblioteca/inicio.html")

    contexto = {
        "formulario": mi_form
        }

    return render(request, "Biblioteca/formularioempleados.html", contexto)

def buscar_empleados(request):
    return render(request, "Biblioteca/buscarempleados.html")

def buscando_empleados(request):
   if not request.GET["apellido"]:
      return HttpResponse("No enviaste datos")
   else:
        apellido_a_buscar = request.GET["apellido"]
        empleado = Empleado.objects.filter(apellido=apellido_a_buscar)

        contexto = {
            "apellido": apellido_a_buscar,
            "empleado": empleado
        }

        return render(request, "Biblioteca/resultadobusquedaempleado.html", contexto)


def formulario_de_clientes(request):

    if request.method != "POST":
        mi_form = FormularioClientes()
    else:
        mi_form = FormularioClientes(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            cliente = Cliente(nombre=info["nombre"], apellido=info["apellido"])
            cliente.save()
            return render(request, "Biblioteca/inicio.html")

    contexto = {
        "formulario": mi_form
        }

    return render(request, "Biblioteca/formularioclientes.html", contexto)

def buscar_clientes(request):
    return render(request, "Biblioteca/buscarclientes.html")

def buscando_clientes(request):
   if not request.GET["apellido"]:
      return HttpResponse("No enviaste datos")
   else:
        apellido_a_buscar = request.GET["apellido"]
        cliente = Cliente.objects.filter(apellido=apellido_a_buscar)

        contexto = {
            "apellido": apellido_a_buscar,
            "cliente": cliente
        }

        return render(request, "Biblioteca/resultadobusquedacliente.html", contexto)
    



