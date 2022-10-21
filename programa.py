#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cmath
from sre_parse import State
import sys
import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


raiz = Tk()

raiz.title("Armaduras")
raiz.state('zoomed')

miFrame = Frame(raiz, #adaptar imagen a la ventana raiz
                width=raiz.winfo_screenwidth(),
                height=raiz.winfo_screenheight())

miFrame.pack()

fondo = PhotoImage(file="C:/Users/aaron/OneDrive/Escritorio/1x/fondoapp.png")
Label(miFrame, image=fondo).place(x=0, y=0)
miFrame.config(height=raiz.winfo_screenheight(), width=raiz.winfo_screenwidth())

barra = Frame(miFrame, width=227, height= 714, bg="white")
barra.place(x=0, y=57)

boton1 = Button(barra, text="Inicio", bg="white", fg="black", font=("Arial", 12), width=6, height=1)
boton1.grid(row=0, column=0)

boton2 = Button(barra, text="Inicio", bg="white", fg="black", font=("Arial", 12), width=6, height=1)
boton2.grid(row=1, column=1)




#boton en barra
# boton = Button(barra, text="Inicio", bg="red", fg="#FFFFFF", font=("Arial", 10), width=10, height=3)
# boton.place(x=0, y=0)

# boton = Button(barra, text="Inicio", bg="red", fg="#FFFFFF", font=("Arial", 10), width=10, height=3)
# boton.place(x=0, y=0)

# boton = Button(barra, text="Inicio", bg="red", fg="#FFFFFF", font=("Arial", 10), width=10, height=3)
# boton.place(x=0, y=0)

# boton = Button(barra, text="Inicio", bg="red", fg="#FFFFFF", font=("Arial", 10), width=10, height=3)
# boton.place(x=0, y=0)

# boton = Button(barra, text="Inicio", bg="red", fg="#FFFFFF", font=("Arial", 10), width=10, height=3)
# boton.place(x=0, y=0)

# boton = Button(barra, text="Inicio", bg="red", fg="#FFFFFF", font=("Arial", 10), width=10, height=3)
# boton.place(x=0, y=0)

# boton = Button(barra, text="Inicio", bg="red", fg="#FFFFFF", font=("Arial", 10), width=10, height=3)
# boton.place(x=0, y=0)
#si el boton es presionado imprime hola mundo
def presionar():
    messagebox.showinfo(message="Que pasa makiabelico", title="Malaya")

# boton.config(command=presionar)

raiz.mainloop()
