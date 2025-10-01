import usuarios.conexion as conexion


connect = conexion.connectar()
database = connect[0]
cursor = connect[1]



class Nota:
    def __init__(self, usuario_id, titulo, descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        sql = "INSERT INTO notas VALUES (null, %s, %s, %s, NOW())"
        cursor.execute(sql, (self.usuario_id, self.titulo, self.descripcion))
        database.commit()

        return [cursor.rowcount, self]