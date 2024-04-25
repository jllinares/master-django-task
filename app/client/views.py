from django.shortcuts import render
from django.http import HttpResponse

# Creacion de vistas
def saludar(request):
    return HttpResponse("Hola mundo")