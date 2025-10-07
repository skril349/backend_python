from django.shortcuts import render, HttpResponse


# Create your views here.

#MVC = Modelo vista controlador -> Acciones (metodos)

#MVT = Modelo vista template -> Acciones (metodos)

def index(request):
    return HttpResponse("<h1>Index - TV </h1>")

def hola_mundo(request):
    return HttpResponse("<h1>Hola mundo con Django - TV </h1>")

def pagina(request):
    return HttpResponse("<h1>Mi primera pagina - TV </h1>")