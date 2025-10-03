from tkinter import *

ventana = Tk()
ventana.title("Mi segunda ventana")
ventana.geometry("500x500")

texto1 = Label(ventana, text="Hola soy un texto")
texto1.config(
    fg="black",
    background="green",
    font=("Arial", 20),
    cursor="spider"
)
texto1.pack(anchor=SE)

def pruebas(nombre, apellidos, pais):
    texto = f"Hola {nombre} {apellidos} tu país es {pais}"
    return texto

texto2 = Label(ventana, text=pruebas("Toni", "Vives", "España"))
texto2.config(
    fg="white",
    background="blue",
    font=("Arial", 18),
    cursor="heart"
    )
texto2.pack(anchor=NW)

ventana.mainloop()