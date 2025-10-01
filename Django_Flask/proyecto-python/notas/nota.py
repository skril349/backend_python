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

    def mostrarTodas(self):
        sql = "SELECT * FROM notas WHERE usuario_id = %s ORDER BY id DESC"
        cursor.execute(sql, (self.usuario_id,))
        result = cursor.fetchall()
        return result
    
    def mostrar(self):
        sql = "SELECT * FROM notas WHERE usuario_id = %s AND titulo LIKE %s ORDER BY id DESC"
        nota = (self.usuario_id, f"%{self.titulo}%")
        cursor.execute(sql, nota)
        result = cursor.fetchall()
        return result
    def borrar(self):
        sql = "DELETE FROM notas WHERE usuario_id = %s AND titulo = %s"
        nota = (self.usuario_id, self.titulo)
        cursor.execute(sql, nota)
        database.commit()
        return cursor.rowcount
    def editar(self):
        sql = "UPDATE notas SET descripcion = %s WHERE usuario_id = %s AND titulo = %s"
        nota = (self.descripcion, self.usuario_id, self.titulo)
        cursor.execute(sql, nota)
        database.commit()
        return cursor.rowcount