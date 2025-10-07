from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

#MVC = Modelo vista controlador -> Acciones (metodos)

#MVT = Modelo vista template -> Acciones (metodos)

layout = """

<h1>Sitio web con Django - TV</h1>

<hr/>
<ul>
    <li><a href="/">Index</a></li>
    <li><a href="/hola-mundo/">Hola mundo</a></li>
    <li><a href="/pagina-principal/">Pagina principal</a></li>  
    <li><a href="/contacto/">Contacto</a></li>
</ul>
<hr/>
"""

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

    return HttpResponse(layout + html)

def hola_mundo(request):
    return HttpResponse(layout + "<h1>Hola mundo con Django - TV </h1>")

def pagina(request,redirigir=0):
    if redirigir == 1:
        return redirect("/contacto/Toni/Alvarez")
    
    return HttpResponse(layout + "<h1>Mi primera pagina - TV </h1>")

def contacto(request,nombre="", apellidos=""):
    return HttpResponse(layout + f"<h1>Contacto - TV </h1><p>Nombre: {nombre}</p><p>Apellidos: {apellidos}</p>")