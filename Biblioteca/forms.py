from socket import fromshare
from django import forms


class FormularioLibros(forms.Form):
    
    titulo = forms.CharField()
    autor = forms.CharField()


class FormularioEmpleados(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()


class FormularioClientes(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()

