from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.title("Mi ventana con imagen")
ventana.geometry("700x500")

imagen = Image.open("imagenes/lobo.png")
foto = ImageTk.PhotoImage(imagen)

label_imagen = Label(ventana, image=foto)
label_imagen.pack(anchor=CENTER)

ventana.mainloop()