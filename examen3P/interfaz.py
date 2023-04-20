from tkinter import *
from tkinter import ttk #importamos ttk para usar NoteBook
import tkinter as tk
from logica import * #1. Presentamos los archivos Controlador y Vista

#2. Creamos 1 objeto de la clase controladorBD
controlador = logica() #Como en las otras prácticas, creamos un objeto de la clase

def ejecutaInsert():
    controlador.guardarExportacion(varTransporteNew.get(), varAduanaNew.get())

def ejecutaSelectExpo():
    exportacion = controlador.consultarExportacion(varbus.get())

    for expo in exportacion:
        cadena = "Id: " + str(expo[0])+ "\n" + " Transporte: " + str(expo[1])+ "\n" + " Aduana: " + expo[2]
    
    if (exportacion):
        print(cadena)
        #actualizar textEnc
        textEnc.delete("1.0", END)
        textEnc.insert(END, cadena)

    else:
        messagebox.showinfo("Error", "No se encontró la exportación")

def allSelect():
    #limpiar el TreeView
    tabla.delete(*tabla.get_children())
    exportaciones = controlador.consultarTodasExportaciones()
    for expo in exportaciones:
        cadena = "Id: " + str(expo[0])+ "\n" + " Transporte: " + expo[1]+ "\n" + " Aduana: " + expo[2]
        print(cadena)
        #colocar en el TreeView los datos de la consulta
        tabla.insert('',0, values=(expo[0],expo[1], expo[2]))

""" def ejecutaActualizacion():
    controlador.actualizarExportacion(varID.get(), varTransporte.get(), varAduana.get()) """

def ejecutaEliminar():
    controlador.eliminarExportacion(varDeleteID.get())

ventana = Tk()
ventana.title("CRUD de exportaciones - Examen 3P")
ventana.geometry("1024x400")

panel = ttk.Notebook(ventana) #creamos el panel de pestañas
panel.pack(fill='both', expand='yes') #lo empaquetamos

pestana1 = ttk.Frame(panel) #creamos la primera pestaña
pestana2 = ttk.Frame(panel) #creamos la segunda pestaña
pestana3 = ttk.Frame(panel) #creamos la tercera pestaña
pestana4 = ttk.Frame(panel) #creamos la cuarta pestaña

#Pestaña 1
panel.add(pestana1, text='Insertar') #agregamos la pestaña al panel
panel.add(pestana2, text='Consultar') #agregamos la pestaña al panel
panel.add(pestana3, text='Todos los registros') #agregamos la pestaña al panel
panel.add(pestana4, text='Eliminar') #agregamos la pestaña al panel

#Pestaña 1
#Etiquetas
lblTransporteNew = Label(pestana1, text="Transporte: ")
lblTransporteNew.grid(column=0, row=0)
lblAduanaNew = Label(pestana1, text="Aduana: ")
lblAduanaNew.grid(column=0, row=1)

#Cajas de texto
varTransporteNew = StringVar()
txtTransporteNew = Entry(pestana1, width=10, textvariable=varTransporteNew)
txtTransporteNew.grid(column=1, row=0)
varAduanaNew = StringVar()
txtAduanaNew = Entry(pestana1, width=10, textvariable=varAduanaNew)
txtAduanaNew.grid(column=1, row=1)

#Botón
btnInsertar = Button(pestana1, text="Insertar", command=ejecutaInsert)
btnInsertar.grid(column=1, row=2)

#Pestaña 2
#Etiquetas
lblbus = Label(pestana2, text="Buscar: ")
lblbus.grid(column=0, row=0)

#Cajas de texto
varbus = StringVar()
txtbus = Entry(pestana2, width=10, textvariable=varbus)
txtbus.grid(column=1, row=0)

#Botón
btnBuscar = Button(pestana2, text="Buscar", command=ejecutaSelectExpo)
btnBuscar.grid(column=1, row=1)

#Resultado de la búsqueda
subBus=Label(pestana2, text="Resultado de la busqueda: ", fg='blue', font=("Modern", 18)).grid(column=0, row=2)
textEnc = tk.Text(pestana2, width=52, height=10)
textEnc.grid(column=0, row=3)

#Pestaña 3
#Botón
btnTodos = Button(pestana3, text="Mostrar todos", command=allSelect)
btnTodos.grid(column=0, row=0)

#Tabla
tabla = ttk.Treeview(pestana3, columns=(1,2,3), show="headings", height="5")
tabla.grid(column=0, row=1)
tabla.heading(1, text="Id")
tabla.heading(2, text="Transporte")
tabla.heading(3, text="Aduana")

#Pestaña 4
#Etiquetas
lblDeleteID = Label(pestana4, text="Id: ")
lblDeleteID.grid(column=0, row=0)

#Cajas de texto
varDeleteID = StringVar()
txtDeleteID = Entry(pestana4, width=10, textvariable=varDeleteID)
txtDeleteID.grid(column=1, row=0)

#Botón
btnEliminar = Button(pestana4, text="Eliminar", command=ejecutaEliminar)
btnEliminar.grid(column=1, row=1)

ventana.mainloop()

