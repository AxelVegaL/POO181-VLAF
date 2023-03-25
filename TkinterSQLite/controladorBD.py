from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:

    def __init__(self):
        pass

    #Método para crear conexiones
    def conexionBD(self):
        try: #lo que intentamos hacer
            conexion = sqlite3.connect("C:/Users/axelv/Desktop/GitPoo/POO181/TkinterSQLite/DBUsuarios.db")
            print ("Conexión exitosa")
            return conexion
        except sqlite3.OperationalError:
        #si hay un error, qué hacer
            print ("Error al conectar a la base de datos")


    #Método para guardar usuarios
    def guardarUsuario(self, nom, cor, con): #recibe los datos del usuario

        #1. Conectar a la base de datos
        conx = self.conexionBD() #llamamos al método de conexión
        #2. Validar que no hayan campos vacíos
        if (nom == "" or cor == "" or con == ""):
            messagebox.showwarning("Campos vacíos", "Cuidaito Wasaoski, falta llenar campos")
        else:
            #3. Preparamos Cursor, Datos, QuerySQL
            cursor = conx.cursor() #cursor permite insertar datos a la BD con SQLite
            conH = self.encriptarCon(con) #llamamos al método para encriptar la contraseña
            datos = (nom, cor, conH)
            qrInsert = "INSERT INTO TBRegistrados(nombre, correo, contra) VALUES(?,?,?)"
            #qrInsert mete los datos en la tabla y los values serán incógnitas

            #4. Ejecutamos Insert y cerramos la conexión
            cursor.execute(qrInsert, datos)
            conx.commit() #commit es para guardar los cambios
            conx.close() #cerramos la conexión
            messagebox.showinfo("Registro exitoso", "Usuario registrado con éxito")

    def encriptarCon(self,con): #recibe la contraseña para encriptar
        conPlana = con
        #Convertimso la cadena de caracteres planos en bytes
        conPlana = conPlana.encode('utf-8') #utf-8 es el formato de codificación
        sal = bcrypt.gensalt() #generamos la "sal" xd?
        conHa = bcrypt.hashpw(conPlana, sal) #encriptamos la contraseña
        print (conHa)

        #enviamos la contraseña encriptada
        return conHa