"""
Proyecto python mysql:
- abrir asistente 
- Login o Registro
- Si elegimos registro: crear usuario en bbdd
- Login, identifica al isuario y preguntara si:
- crear nota, mostrar nota o borrar notas.

"""

from usuarios import acciones

print("""

Acciones disponibles:
      - Login
      - Registro
""")

hazEl = acciones.Acciones()

accion = input("Que quieres hacer?")

if accion == "Registro":
    hazEl.registro()

elif accion == "Login":
    hazEl.login()
    
