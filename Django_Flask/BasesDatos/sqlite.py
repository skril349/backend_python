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

#guardar cambios

conexion.commit()

#Insertar datos
# cursor.execute("INSERT INTO productos VALUES(null,'primer producto','Descripcion de mi producto',550)")
# conexion.commit()

# #Borrar registros
# cursor.execute("DELETE FROM productos")
# conexion.commit()


# Insertar muchos reistros de golpe

# productos = [
#     ("ordenador portatil","Buen PC", 700),
#     ("telefono portatil","Buen orde", 1000),
#     ("PC portatil","BC", 670),
#     ("placa base","electronica", 800),
#     ("tablet","IT", 1200),

# ]

# cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)",productos)
# conexion.commit()

#Listar datos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

for producto in productos:
    print(producto)

#UPDATE
cursor.execute("UPDATE productos SET precio=678 WHERE precio=700;")
conexion.commit()
#Cerrar conexion

conexion.close()