import usuarios.usuario as modelo

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
        email = input("cual es tu email?")
        password = input("introduce tu conrtraseña: ")