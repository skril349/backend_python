from django.shortcuts import render, HttpResponse


# Create your views here.

#MVC = Modelo vista controlador -> Acciones (metodos)

#MVT = Modelo vista template -> Acciones (metodos)

def index(request):
    html = """<h1>Index - TV </h1>
        <p>Años hasta 2050:</p>
        <ul>
    
    """
    year = 2025
    while year <=2050:
        html += "<li>" + str(year) + "</li>"
        year += 1
    html += "</ul>"
    
    return HttpResponse(html)

def hola_mundo(request):
    return HttpResponse("<h1>Hola mundo con Django - TV </h1>")

def pagina(request):
    return HttpResponse("<h1>Mi primera pagina - TV </h1>")