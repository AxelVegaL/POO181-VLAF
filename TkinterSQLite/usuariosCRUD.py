from tkinter import *
from tkinter import ttk #importamos ttk para usar NoteBook
import tkinter as tk
from controladorBD import * #1. Presentamos los archivos Controlador y Vista

#2. Creamos 1 objeto de la clase controladorBD
controlador = controladorBD() #Como en las otras prácticas, creamos un objeto de la clase

#3. Función para disparar el botón
def ejecutaInsert():
    controlador.guardarUsuario(varNombre.get(), varCor.get(), varCon.get())

#Aquí hacemos un def para la selección de datos
def ejecutaSelectU():
    usuario = controlador.consultarUsuario(varbus.get()) #Aquí se manda el id a la función de la clase controladorBD. Variable Buscar: varbus
    #Mandando "usuario" ya no se pierde en el limbro el valor de la consulta :D porque así de delicado es esto =(
    
    for usu in usuario:
        cadena = "Id: " + str(usu[0])+ "\n" + " Nombre: " + usu[1]+ "\n" + " Correo: " + usu[2]+ "\n" + " Contraseña: " + str(usu[3])
    
    if (usuario):
        print(cadena)
        #actualizar textEnc
        textEnc.delete("1.0", END)
        textEnc.insert(END, cadena)


    else:
        messagebox.showinfo("Error", "No se encontró el usuario")

def allSelect():
    #limpiar el TreeView
    tabla.delete(*tabla.get_children())
    usuarios = controlador.consultarTodosUsuarios()
    for usu in usuarios:
        cadena = "Id: " + str(usu[0])+ "\n" + " Nombre: " + usu[1]+ "\n" + " Correo: " + usu[2]+ "\n" + " Contraseña: " + str(usu[3])
        print(cadena)
        #colocar en el TreeView los datos de la consulta
        tabla.insert('',0, values=(usu[0],usu[1], usu[2], usu[3]))


ventana = Tk()
ventana.title("CRUD de usuarios - Práctica 15")
ventana.geometry("1024x400")
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

btnGuardar = Button(pestana1, text="Guardar Usuario", command=ejecutaInsert).pack()

panel.add(pestana1, text='Formulario de usuarios') #le damos un nombre a la pestaña
panel.add(pestana2, text='Buscar usuarios')
panel.add(pestana3, text='Consultar usuarios')
panel.add(pestana4, text='Actualizar usuarios')

#Pestaña 2. Buscar usuarios

titulo2= Label(pestana2, text="Buscar usuarios", fg = 'green', font = ("Modern",18)).pack()

varbus=tk.StringVar()
lblid=Label(pestana2, text="Id: ").pack() #Label ID
txtid=Entry(pestana2, textvariable=varbus).pack() #Entry ID
btnBuscar=Button(pestana2, text="Buscar", command=ejecutaSelectU).pack() #Botón buscar}

subBus=Label(pestana2, text="Resultado de la busqueda: ", fg='blue', font=("Modern", 18)).pack() #Subtítulo
textEnc = tk.Text(pestana2, width=52, height=10)
textEnc.pack()
#Este pequeño malnacido fue el causante de todos mis males en las últimas 2 horas

#Pestaña 3. Consultar usuarios
titulo3= Label(pestana3, text="Consultar usuarios:", fg = 'red', font = ("Modern",18))
titulo3.pack()

tabla = ttk.Treeview(pestana3, columns=('#1', '#2', '#3', '#4'), show='headings', height=10)
tabla.heading('#1', text='Id')
tabla.heading('#2', text='Nombre')
tabla.heading('#3', text='Correo')
tabla.heading('#4', text='Contraseña')
tabla.pack()

botonconsulta = Button(pestana3, text="Consultar", command=allSelect).pack()


#Pestaña 4. Actualizar usuarios
titulo4= Label(pestana4, text="Actualizar usuarios", fg = 'orange', font = ("Modern",18)).pack()




ventana.mainloop()