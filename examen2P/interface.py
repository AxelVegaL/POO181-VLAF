from Matriculador import *
from tkinter import *
import random

matr = Matriculador()


def setMatricula():
    numrand1 = StringVar()
    numrand1.set(random.randint(0,9))
    numrand2 = StringVar()
    numrand2.set(random.randint(0,9))

    numrand = StringVar()
    numrand.set(numrand1.get() + numrand2.get())
    matr.matriculaData(nombre.get(),apellido_p.get(),apellido_m.get(),nacimiento.get(),carrera.get(),year.get(),numrand.get())
    

root = Tk()
root.title("EXAMEN - Generador de Matrículas")
root.configure(background='#b3e6ff')
root.geometry("600x400")

introLabel = Label(root, background='#b3e6ff', text="GENERADOR DE MATRÍCULAS").grid(row=0, column=0)
nombre = StringVar()
nombreLabel = Label(root, background='#b3e6ff', text="Nombre:").grid(row=1, column=1)
nombreEntry = Entry(root, textvariable=nombre)
nombreEntry.grid(row=1, column=2)

apellido_p = StringVar()
apellido_pLabel = Label(root, background='#b3e6ff', text="Apellido Paterno:").grid(row=2, column=1)
apellido_pEntry = Entry(root, textvariable=apellido_p)
apellido_pEntry.grid(row=2, column=2)

apellido_m = StringVar()
apellido_mLabel = Label(root, background='#b3e6ff', text="Apellido Materno:").grid(row=3, column=1)
apellido_mEntry = Entry(root, textvariable=apellido_m)
apellido_mEntry.grid(row=3, column=2)

nacimiento = IntVar()
nacimientoLabel = Label(root, background='#b3e6ff', text="Año de Nacimiento:").grid(row=4, column=1)
nacimientoEntry = Entry(root, textvariable=nacimiento)
nacimientoEntry.grid(row=4, column=2)

carrera = StringVar()
carreraLabel = Label(root, background='#b3e6ff', text="Carrera:").grid(row=5, column=1)
carreraEntry = Entry(root, textvariable=carrera)
carreraEntry.grid(row=5, column=2)

year = IntVar()
yearLabel = Label(root, background='#b3e6ff', text="Año en curso:").grid(row=6, column=1)
yearEntry = Entry(root, textvariable=year)
yearEntry.grid(row=6, column=2)

""" numrand1 = StringVar()
numrand1.set(random.randint(0,9))
numrand2 = StringVar()
numrand2.set(random.randint(0,9))

numrand = StringVar()
numrand.set(numrand1.get() + numrand2.get()) """

genButton = Button(root, text='Generar Matrícula', command=setMatricula).grid(row=7, column=2)

root.mainloop()