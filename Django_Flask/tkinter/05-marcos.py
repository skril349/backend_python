from tkinter import *

ventana  = Tk()
ventana.title("Mi segunda ventana")
ventana.geometry("500x500")

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="grey",
    bd=5,
    relief=SOLID
)
marco_padre.pack(side=TOP, fill=X, expand=YES)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="red",
    bd=5,
    relief=SOLID
)
marco.pack(anchor=CENTER)
# Label 1

marco2 = Frame(ventana, width=250, height=250)
marco2.config(
    bg="green",
    bd=5,
    relief=SOLID
)
marco2.pack(side=RIGHT, anchor=SE)
# Label 1

texto1 = Label(ventana, text="Hola soy un texto verde")
texto1.config(
    fg="black",
    background="green",
    font=("Arial", 20),
    cursor="spider"
)
texto1.pack(side=TOP, expand=YES, fill=X)


ventana.mainloop()