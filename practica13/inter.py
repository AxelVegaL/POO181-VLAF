from tkinter import Tk, ttk, Button, messagebox
from tkinter import *
from passwords import *

#Ventana de TKinter
window = Tk()
window.configure(background='#b3e6ff')
window.title("Práctica 13 - Generador de Contraseñas")
window.geometry("600x400")

length = IntVar()
ttk.lenLabel = Label(window, background='#b3e6ff', text="¿Cuántos caracteres necesitas?").pack()
ttk.lenEntry = Entry(window, textvariable=length, show=8).pack()

""" mayus = window.boolVar()
ttk.mayusLabel = Label(window, background='#b3e6ff', text="¿Necesitas mayúsculas?").pack()
ttk.mayusEntry = Entry(window, textvariable=mayus).pack()

special = window.boolVar()
ttk.speLabel = Label(window, background='#b3e6ff', text="¿Necesitas caracteres especiales?").pack()
ttk.speEntry = Entry (window, text) """

def maySel():
    if (mayus.get() == TRUE):
        print('a')
    else:
        print('b')

def speSel():
    if (special.get() == TRUE):
        print('a')
    else:
        print('b')

mayus = BooleanVar()
special = BooleanVar()
mayusBox = Checkbutton(window, background='#b3e6ff', text='Usar Mayúsculas',variable=mayus, onvalue=TRUE, offvalue=FALSE, command=maySel)
mayusBox.pack()
specialBox = Checkbutton(window, background='#b3e6ff', text='Caracteres Especial',variable=special, onvalue=TRUE, offvalue=FALSE, command=speSel)
specialBox.pack()

genButton = ttk.Button(window, text='Generar Contraseña', command=passwords.juan).pack()

#ttk.passGen = Entry(window, textvariable=passw).pack()

window.mainloop()