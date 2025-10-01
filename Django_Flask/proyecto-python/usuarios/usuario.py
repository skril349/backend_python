import datetime
import hashlib
import usuarios.conexion as conexion

connect = conexion.connectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
    
    def registrar(self):
        fecha = datetime.datetime.now()
        #cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode("utf-8"))
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha )
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

