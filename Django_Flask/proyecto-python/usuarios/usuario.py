import mysql.connector
import datetime
database = mysql.connector.connect(
    host= "localhost",
    user = "root",
    passwd="",
    database = "master_python",
    port = 3306
)

cursor = database.cursor(buffered=True)

class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
    
    def registrar(self):
        fecha = datetime.datetime.now()
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, self.password, fecha )
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
            return result
        except Exception as e:
            print("Error al registrar usuario:", e)
            result = [0, self]
            return result

    def identificar(self):
        return self.nombre

