# Programación orientada a objetos (POO)

# Definir una clase (molde para crear mas objetos)

class Coche:

    # Atributos o propiedades
    color = "rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # metodos

    def acelerar(self):
        self.velocidad += 1
    def frenar(self):
        self.velocidad -= 1
    def getVelocidad(self):
        return self.velocidad
    
coche = Coche()

print(coche.marca)