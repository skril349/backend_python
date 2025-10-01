import usuarios.usuario as modelo
import notas.acciones as notas
class Acciones:
    def registro(self):
        print("\nOk! Vamos a registrarnos en el sistema ...")
        nombre = input("qual es tu nombre?")
        apellidos = input("cuales son tus apellidos?")
        email = input("cual es tu email?")
        password = input("introduce tu conrtraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre}, te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente")
    
    def login(self):
        print("Vale! Identificate en el sistema ...")
        try:
            email = input("cual es tu email?")
            password = input("introduce tu conrtraseña: ")
            usuario = modelo.Usuario("", "", email, password)
            login = usuario.identificar()
            if email == login[3]:
                print(f"Bienvenido {login[1]} {login[2]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print("Error al iniciar sesión: Usuario o contraseña incorrecta")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
              - Crear nota (crear)
              - Mostrar notas (mostrar)
              - Borrar notas (borrar)
              - Salir (salir)
        """)

        accion = input( "Que quieres hacer?")
        if accion == "crear":
            crear = notas.Acciones()
            crear.crearNota(usuario)
            self.proximasAcciones(usuario)
            #crear.crear()
            pass
        elif accion == "mostrar":
            print("Ok, vamos a mostrar tus notas")
            self.proximasAcciones(usuario)

            #mostrar = notas.MostrarNotas(usuario)
            #mostrar.mostrar()
            pass
        elif accion == "borrar":
            print("Ok, vamos a borrar tus notas")
            self.proximasAcciones(usuario)

            #borrar = notas.BorrarNotas(usuario)
            #borrar.borrar()
            pass
        elif accion == "salir":
            print(f"Ok {usuario[1]}, hasta pronto!") 
            exit()
        else:
            print("Acción no reconocida")
            self.proximasAcciones(usuario)

        return None
      