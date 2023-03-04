from tkinter import Tk, ttk, Button, messagebox
from tkinter import *
from login import *

def userWelcome():
    messagebox.showinfo("¡Bienvenido!","Has iniciado sesión correctamente")

def userRejected():
    messagebox.showerror("ERROR","Un parámetro no es válido. Los patámetros no pueden ser vacíos")

validate = False

#ma=input("Mail: ")
#passw=input('Password: ')

ventana = Tk()
ventana.configure(background="#ccf2ff")
ventana.title("Práctica 12 - Login")
ventana.geometry("600x400")

""" def maValidation(ma):
    print("Correo :", ma.get())
    return login(ma)
def passwValidation(passw):
    print("Contraseña :", passw.get())
    return login(passw) """

""" if loginValidation() == False:
    userRejected()
else:
    userWelcome() """

#user=login(ma, passw)



emailLabel = Label(ventana, text="Correo").grid(row=0, column=0)
email = StringVar()
ttk.emailEntry = Entry(ventana, textvariable=email).grid(row=0, column=1)

passwordLabel = Label(ventana,text="Contraseña").grid(row=1, column=0)  
password = StringVar()
ttk.passwordEntry = Entry(ventana, textvariable=password, show='*').grid(row=1, column=1)

#Boton
def mandar():
    if password.get() == "" or email.get() == "":
        messagebox.showinfo("Error","No puedes mandar vacíos")
    else:
        messagebox.showinfo("Bienvenido!","Has iniciado sesión")

log = ttk.Button(ventana, text="Iniciar sesión", command=mandar)
log.grid(row=4, column=3)

ventana.mainloop()



