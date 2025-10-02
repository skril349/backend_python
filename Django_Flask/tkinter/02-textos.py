from tkinter import *

ventana = Tk()
ventana.title("Mi segunda ventana")
ventana.geometry("500x500")

texto = Label(ventana, text="Hola soy un texto")
texto.config(
    fg="black",
    background="green",
    font=("Arial", 20),
    height=3
    
)
texto.pack(anchor=CENTER)

ventana.mainloop()