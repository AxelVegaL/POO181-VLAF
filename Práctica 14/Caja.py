from tkinter import *
from tkinter import Tk, messagebox, Button
class Caja:
    def __init__(self):
        self.__edad = 18
    
    def accountData(self, cuenta, titular, edad, saldo):
        self.__cuenta = cuenta
        self.__titular = titular
        self.__edad = edad
        self.__saldo = saldo
        bal = float(self.__saldo)
        if self.__edad < 18:
            messagebox.showerror("Error", "No se puede crear una cuenta a nombre de un menor de edad")
        else:
            messagebox.showinfo("Cuenta creada", "La cuenta ha sido creada exitosamente con un saldo de: " + str(bal) + " pesos")
            self.accountWindow(bal)
            

    def accountWindow(self, bal):        
        subwindow = Tk()
        subwindow.configure(background='#b3e6ff')
        subwindow.title("Manejo de cuenta")
        subwindow.geometry("600x400")
        Label(subwindow, background='#b3e6ff', text="No. Cuenta: ").grid(row=0, column=0)
        Label(subwindow, background='#b3e6ff', text=self.__cuenta).grid(row=0, column=1)
        Label(subwindow, background='#b3e6ff', text="Titular: ").grid(row=1, column=0)
        Label(subwindow, background='#b3e6ff', text=self.__titular).grid(row=1, column=1)
        Label(subwindow, background='#b3e6ff', text="Edad: ").grid(row=2, column=0)
        Label(subwindow, background='#b3e6ff', text=self.__edad).grid(row=2, column=1)
        Label(subwindow, background='#b3e6ff', text="Saldo: ").grid(row=3, column=0)
        Label(subwindow, background='#b3e6ff', text=bal).grid(row=3, column=1)

        def consultar():
            messagebox.showinfo("Saldo", "El saldo actual es de: " + str(bal))
            nose()

        def depositar():
            deposito_num = float(deposito.get())
            messagebox.showinfo("Depósito", "Depósito de " + str(deposito.get()) + " realizado con éxito")
            nonlocal bal
            bal = bal + deposito_num

        def retirar():
            nonlocal bal
            retiro_num = float(retiro.get())
            if bal < retiro_num:
                messagebox.showerror("Error", "No se puede retirar una cantidad mayor al saldo actual")
            else:
                bal = bal - retiro_num
                Label(subwindow, background='#b3e6ff', text=bal).grid(row=3, column=1) # Actualizar el valor del Label correspondiente
                messagebox.showinfo("Retiro", "Retiro de " + str(retiro_num) + " realizado con éxito")
                
        Button(subwindow, text="Consultar saldo", command=consultar).grid(row=4, column=0)
        depLabel = Label(subwindow, background='#b3e6ff', text="Depósito: ").grid(row=5, column=0)
        deposito = DoubleVar()
        depEntry = Entry(subwindow, textvariable=deposito).grid(row=5, column=1)
        Button(subwindow, text="Depositar", command=depositar).grid(row=5, column=2)
        retLabel = Label(subwindow, background='#b3e6ff', text="Retiro: ").grid(row=6, column=0)
        retiro = DoubleVar()
        retEntry = Entry(subwindow, textvariable=retiro).grid(row=6, column=1)
        Button(subwindow, text="Retirar", command=retirar).grid(row=6, column=2)

        def nose():
            print(deposito.get())
            print(retiro.get())
            print(bal)
        subwindow.mainloop()



"""def getSaldo(self):
        return self.__saldo
    def getCuenta(self):
        return self.__cuenta
    def getTitular(self):
        return self.__titular
    def getEdad(self):
        return self.__edad
    
    def setSaldo(self, bal):
        self.__saldo = bal
    def setCuenta(self, acc):
        self.__cuenta = acc
    def setTitular(self, name):
        self.__titular = name
    def setEdad(self, age):
        self.__edad = age """