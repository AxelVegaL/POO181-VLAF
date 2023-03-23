from tkinter import *
from tkinter import ttk #importamos ttk para usar NoteBook
import tkinter as tk

ventana = Tk()
ventana.title("CRUD de usuarios - Práctica 15")
ventana.geometry("600x400")
#ventana.configure(background='#b3e6ff')

panel = ttk.Notebook(ventana) #creamos el panel de pestañas
panel.pack(fill='both', expand='yes') #lo empaquetamos

pestana1 = ttk.Frame(panel) #creamos la primera pestaña
pestana2 = ttk.Frame(panel) #creamos la segunda pestaña
pestana3 = ttk.Frame(panel) #creamos la tercera pestaña
pestana4 = ttk.Frame(panel) #creamos la cuarta pestaña


#Pestaña 1: Formulario de usuarios
titulos = Label(pestana1, text="Registro de usuarios", fg = 'blue', font = ("Modern",18)).pack()

varNombre = tk.StringVar()
lblNom = Label(pestana1, text="Nombre: ").pack()
txtNom = Entry(pestana1, textvariable=varNombre).pack()

varCor = tk.StringVar()
lblCor = Label(pestana1, text="Correo: ").pack()
txtCor = Entry(pestana1, textvariable=varCor).pack()

varCon = tk.StringVar()
lblCon = Label(pestana1, text="Contraseña: ").pack()
txtCon = Entry(pestana1, textvariable=varCon).pack()

btnGuardar = Button(pestana1, text="Guardar Usuario").pack()


panel.add(pestana1, text='Formulario de usuarios') #le damos un nombre a la pestaña
panel.add(pestana2, text='Buscar usuarios')
panel.add(pestana3, text='Consultar usuarios')
panel.add(pestana4, text='Actualizar usuarios')

ventana.mainloop()