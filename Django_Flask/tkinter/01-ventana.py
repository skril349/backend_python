#tkinter
#modulo para crear interfaces gráficas de usuario (GUI)
from tkinter import *


class Programa:
    def __init__(self):
        self.title="Mi primera ventana"
        self.size = "400x300"
        self.resizable = False
        self.bg_color = "green"

    def cargar(self):
        self.root = Tk()
        self.root.title(self.title)
        self.root.geometry(self.size) 
        if self.resizable:
            self.root.resizable(1,1)
        else:
            self.root.resizable(0,0)
        self.root.config(bg=self.bg_color)
        

    def addTexto(self):
        texto = Label(self.root, text="Hola soy un texto")
        texto.config(
            fg="white",
            bg="green",
            font=("Arial", 20)
        )
        texto.pack()
    
    def mostrar(self):
        self.root.mainloop()

# Instanciemos y cargamosmos el programa
programa = Programa()
programa.cargar()
programa.addTexto()
programa.addTexto()
programa.addTexto()
programa.addTexto()
programa.addTexto()
programa.addTexto()
programa.mostrar()