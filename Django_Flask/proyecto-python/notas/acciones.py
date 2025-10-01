import notas.nota as modelo

class Acciones:
    def crearNota(self,usuario):
        print(f"Ok {usuario[1]}, vamos a crear una nota...")
        titulo = input("Introduce el titulo de la nota: ")
        descripcion = input("Introduce el contenido de la nota: ")  
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        resultado = nota.guardar()
        if resultado[0] >= 1:
            print(f"Nota creada con éxito: {resultado[1].titulo}")
        else:
            print("Error al crear la nota.")