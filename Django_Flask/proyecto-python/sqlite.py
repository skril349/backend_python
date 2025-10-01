import sqlite3

# Conexion

conexion = sqlite3.connect("pruebas.db")

#crear cursor
cursor = conexion.cursor()
#Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
    "id INTEGER PRIMARY KEY AUTOINCREMENT, "+
    "titulo VARCHAR(255), "+
    "descripcion TEXT, "+
    "precio INT(255)"
")")