from tkinter import messagebox
import sqlite3

class logica:

    def __init__(self):
        pass

    #Método para crear conexiones
    def conexionBD(self):
        try: #lo que intentamos hacer
            conexion = sqlite3.connect("C:/Users/axelv/Desktop/GitPoo/POO181/examen3P/BDExportaciones.db")
            print ("Conexión exitosa")
            return conexion
        except sqlite3.OperationalError:
        #si hay un error, qué hacer
            print ("Error al conectar a la base de datos")

    #Método para guardar Exportaciones
    def guardarExportacion(self, trans, adua): #recibe los datos de exportación
        #1. Conectar a la base de datos
        conx = self.conexionBD() #llamamos al método de conexión
        #2. Validar que no hayan campos vacíos
        if (trans == "" or adua == ""):
            messagebox.showwarning("Campos vacíos", "Procura incluir todos los datos")
        else:
            #3. Preparamos Cursor, Datos, QuerySQL
            cursor = conx.cursor() #cursor permite insertar datos a la BD con SQLite
            datos = (trans, adua)
            qrInsert = "INSERT INTO TBPedimentos(Transporte, Aduana) VALUES(?,?)"
            #qrInsert mete los datos en la tabla y los values serán incógnitas

            #4. Ejecutamos Insert y cerramos la conexión
            cursor.execute(qrInsert, datos)
            conx.commit() #commit es para guardar los cambios
            conx.close() #cerramos la conexión
            messagebox.showinfo("Registro exitoso", "Exportación registrada con éxito")

    #Método para buscar Exportaciones
    def consultarExportacion(self,adu):
        #1. Preparamos la conexión
        conx = self.conexionBD()

        #2. Verificar si ID no está vacío
        if (adu == ""): #También se puede validar datos numéricos con isdigit()
            messagebox.showwarning("Campos vacíos", "Procura incluir todos los datos")
            conx.close()
        else:
            try:
                #3. Preparamos Cursor, Datos, QuerySQL
                cursor = conx.cursor()
                qrSelect = "SELECT * FROM TBPedimentos WHERE Aduana = ?"
                #4. Ejecutamos Select y cerramos la conexión
                cursor.execute(qrSelect, adu)
                rsExport = cursor.fetchall()
                conx.close()
                return rsExport
            except sqlite3.OperationalError:
                messagebox.showwarning("Error", "No se encontró el registro")
                conx.close()

    #Método para consultar todas las exportaciones
    def consultarTodasExportaciones(self):
        #1. Preparamos la conexión
        conx = self.conexionBD()
        try:
            #2. Preparamos Cursor, Datos, QuerySQL
            cursor = conx.cursor()
            qrSelect = "SELECT * FROM TBPedimentos"
            #3. Ejecutamos Select y cerramos la conexión
            cursor.execute(qrSelect)
            registros = cursor.fetchall()
            conx.close()
            return registros
        except sqlite3.OperationalError:
            messagebox.showwarning("Error", "No se encontró el registro")
            conx.close()

    #Método para eliminar Exportaciones
    def eliminarExportacion(self, id):
        #1. Preparamos la conexión
        conx = self.conexionBD()

        #2. Verificar si ID no está vacío
        if (id == ""):
            messagebox.showwarning("Campos vacíos", "Procura incluir todos los datos")
            conx.close()
        else:
            validar = messagebox.askquestion("Eliminar", "¿Estás seguro de eliminar el registro?")
            if validar:
                try:
                    rsExport = self.consultarExportacion(id)
                    if (rsExport == []):
                        messagebox.showwarning("Error", "No se encontró el registro")
                        conx.close()
                    else:
                        #3. Preparamos Cursor, Datos, QuerySQL
                        cursor = conx.cursor()
                        qrDelete = "DELETE FROM TBPedimentos WHERE IDExpo = ?"
                        #4. Ejecutamos Delete y cerramos la conexión
                        cursor.execute(qrDelete, id)
                        conx.commit()
                        conx.close()
                        messagebox.showinfo("Eliminación exitosa", "Exportación eliminada con éxito")
                except sqlite3.OperationalError:
                    messagebox.showwarning("Error", "No se encontró el registro")
                    conx.close()
            else:
                conx.close()
                messagebox.showinfo("Eliminación cancelada", "No se eliminó el registro")