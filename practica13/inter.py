from tkinter import Tk, Button
from tkinter import *
from passwords import *

passw = passwords() #Este va de a fuerzas para usar la clase passwords.py

def setPassword():
    passw.createPass(length.get(),mayus.get(),special.get())
    #Los .get() son para obtener el valor de las variables que se usan en la función createPass() de la clase passwords.py
    #este def es el que se conecta a la class passwords.py, es decir, es el QROBús de la clase. Porque falla, pero luego sí da :D


#Ventana de TKinter
window = Tk() #Aquí se crea la ventana
window.configure(background='#b3e6ff') #Background de la ventana
window.title("Práctica 13 - Generador de Contraseñas") #Título de la ventana
window.geometry("600x400") #Tamaño

length = IntVar() #Aquí se guardará la longitud de la contraseña (por defecto es 8)
lenLabel = Label(window, background='#b3e6ff', text="¿Cuántos caracteres necesitas?").pack()
#aquí se crea una etiqueta con una indicación para el usuario
lenEntry = Entry(window, textvariable=length).pack()
#Entry para introducir una longitud de contraseña, se guarda en la variable length

mayus = BooleanVar() #Estas variables son para los checkbuttons
special = BooleanVar() #Como BoolVar() devuelve un valor booleano, se puede usar en la función createPass() de la clase passwords.py
mayusBox = Checkbutton(window, background='#b3e6ff', text='Usar Mayúsculas',variable=mayus, onvalue=True, offvalue=False)
#onvalue y offvalue son para que el checkbutton devuelva un valor booleano según si está activado o no el checkbutton
mayusBox.pack() #pack() es el organizador de los destos en la ventana
specialBox = Checkbutton(window, background='#b3e6ff', text='Caracteres Especial',variable=special, onvalue=True, offvalue=False)
specialBox.pack()

#genButton = ttk.Button(window, text='Generar Contraseña', command=setPassword).pack()
genButton = Button(window, text='Generar Contraseña', command=setPassword).pack()
#Este botón mandará a llamar a la función setPassword() que a su vez llama a la función createPass() de la clase passwords.py

pLabel = Label(window, background='#b3e6ff', text="Contraseña para copypastear:").pack()
""" pEntry = Entry(window)
pEntry.insert(0, passw.createPass)
pEntry.pack() """

window.mainloop()
#Este se encarga de renderizar la ventana