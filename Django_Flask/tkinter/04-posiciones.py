from tkinter import *

ventana = Tk()
ventana.title("Mi segunda ventana")
ventana.geometry("500x500")

# Label 1
texto1 = Label(ventana, text="Hola soy un texto verde")
texto1.config(
    fg="black",
    background="green",
    font=("Arial", 20),
    cursor="spider"
)
texto1.pack(side=TOP, expand=YES, fill=X)

# Label 2
texto2 = Label(ventana, text="Hola soy un texto azul")
texto2.config(
    fg="white",
    background="blue",
    font=("Arial", 18),
    cursor="heart"
)
texto2.pack(side=BOTTOM, expand=YES, fill=X)

# Label 3
texto3 = Label(ventana, text="Texto rojo")
texto3.config(
    fg="white",
    background="red",
    font=("Arial", 16),
    cursor="pirate"
)
texto3.pack(side=LEFT, expand=YES, fill=X)

# Label 4
texto4 = Label(ventana, text="Texto amarillo")
texto4.config(
    fg="black",
    background="yellow",
    font=("Arial", 14),
    cursor="cross"
)
texto4.pack(side=RIGHT, expand=YES, fill=X)

# Label 5
texto5 = Label(ventana, text="Texto morado")
texto5.config(
    fg="white",
    background="purple",
    font=("Arial", 12),
    cursor="dot"
)
texto5.pack(anchor=N)

# Label 6
texto6 = Label(ventana, text="Texto naranja")
texto6.config(
    fg="black",
    background="orange",
    font=("Arial", 10),
    cursor="plus"
)
texto6.pack()

ventana.mainloop()