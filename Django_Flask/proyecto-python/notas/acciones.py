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

    def mostrarNotas(self,usuario):
        print(f"Ok {usuario[1]}, aqui tienes tus notas:")
        nota = modelo.Nota(usuario[0], "", "")
        notas = nota.mostrarTodas()
        for n in notas:
            print("\n----------------")
            print(n[2])
            print(n[3])
            print("----------------\n")
    
    def mostrarNota(self,usuario,titulo):
        print(f"Ok {usuario[1]}, aqui tienes tus notas:")
        nota = modelo.Nota(usuario[0], titulo, "")
        notas = nota.mostrar()
        for n in notas:
            print("\n----------------")
            print(n[2])
            print(n[3])
            print("----------------\n")
    def borrarNota(self,usuario,titulo):
        print(f"Ok {usuario[1]}, vamos a borrar la nota: {titulo}")
        nota = modelo.Nota(usuario[0], titulo, "")
        borradas = nota.borrar()
        if borradas >= 1:
            print(f"Se han borrado {borradas} notas con el titulo {titulo}")
        else:
            print("No se ha borrado ninguna nota, intenta de nuevo")
    def editarNota(self,usuario,titulo):
        print(f"Ok {usuario[1]}, vamos a editar la nota: {titulo}")
        descripcion = input("Introduce la nueva descripcion de la nota: ")
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        editadas = nota.editar()
        if editadas >= 1:
            print(f"Se han editado {editadas} notas con el titulo {titulo}")
        else:
            print("No se ha editado ninguna nota, intenta de nuevo")