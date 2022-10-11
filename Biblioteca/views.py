from django.shortcuts import render

# Create your views here.

def mostrar_inicio(request):
    return render(request, "Biblioteca/inicio.html")

def mostrar_libros(request):
    return render(request, "Biblioteca/libros.html")

def mostrar_empleados(request):
    return render(request, "Biblioteca/empleados.html")

def mostrar_clientes(request):
    return render(request, "Biblioteca/clientes.html")

def ver_nav(request):
    return render(request, "Biblioteca/nav.html")


