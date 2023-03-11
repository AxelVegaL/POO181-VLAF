from Caja import *
from tkinter import *
from tkinter import Tk, Button
import random
user = Caja()

def setAccount():
    user.accountData(cuenta.get(),titular.get(),edad.get(),saldo.get()) #Aquí se mandan los datos a la clase Caja.py

window = Tk()
window.configure(background='#b3e6ff')
window.title("Práctica 14 - Caja Popular")
window.geometry("600x400")

introLabel = Label(window, background='#b3e6ff', text="CREAR NUEVA CUENTA").grid(row=0, column=0)
#se introduce el nombre del titular de la cuenta
titular = StringVar()
nameLabel = Label(window, background='#b3e6ff', text="Nombre del titular:").grid(row=1, column=1)
nameEntry = Entry(window, textvariable=titular).grid(row=1, column=2)

#se introduce la edad del titular de la cuenta
edad = IntVar()
ageLabel = Label(window, background='#b3e6ff', text="Edad del titular:").grid(row=2, column=1)
ageEntry = Entry(window, textvariable=edad).grid(row=2, column=2)

#se introduce el saldo inicial de la cuenta
saldo = DoubleVar()
balLabel = Label(window, background='#b3e6ff', text="Saldo de apertura:").grid(row=3, column=1)
balEntry = Entry(window, textvariable=saldo).grid(row=3, column=2)

cuenta = IntVar()
cuenta.set(random.randint(0,9999999999)) #Aquí se genera un número para el número de cuenta

#boton para crear la cuenta
genButton = Button(window, text='Crear cuenta', command=setAccount).grid(row=4, column=2)

window.mainloop()
