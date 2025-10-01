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

    soy_publico = "Hola, soy un atributo publico"
    __soy_privado = "Hola, soy un atributo privado"


    # constructor
    def __init__(self,color,marca,modelo,velocidad,caballaje,plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    # metodos

    #setters
    def setColor(self, color):
        self.color = color
    def setModelo(self, modelo):
        self.modelo = modelo
    #getters
    def acelerar(self):
        self.velocidad += 1
    def frenar(self):
        self.velocidad -= 1
    def getVelocidad(self):
        return self.velocidad
    

    def getSoyPrivado(self):
        return self.__soy_privado