"""
Proyecto python mysql:
- abrir asistente 
- Login o Registro
- Si elegimos registro: crear usuario en bbdd
- Login, identifica al isuario y preguntara si:
- crear nota, mostrar nota o borrar notas.

"""

print("""

Acciones disponibles:
      - Login
      - Registro
""")

accion = input("Que quieres hacer?")

if accion == "Registro":
    print("Vamos a registrarnos")

if accion == "Login":
    print("vamos a logearnos")
