import random
import string
from tkinter import messagebox, Entry, Label
lettersmay = string.ascii_letters.upper()
lettersmin = string.ascii_letters.lower()
special_chars = string.digits + string.punctuation

class passwords:
    def __init__(self): #Bob el constructor
        self.__password = "" #Contraseña por defecto
        self.__len = 8 #Longitud de la contraseña por defecto

    def createPass(self,length, mayus, special):
        if length > 0:
            self.__len = length #Aquí se cambia la longitud de la contraseña por la que se introdujo
        else:
            pass #Si no se cambia o se introduce un valor negativo, se usa la lenght por defecto
        if mayus == True and special == True:
            passPool= lettersmay+lettersmin+special_chars
        elif mayus == True and special == False:
            passPool= lettersmay+lettersmin
        elif mayus == False and special == True:
            passPool= lettersmin+special_chars
        else:
            passPool= lettersmin
        self.__password =  "".join(random.choices(passPool,k=self.__len)) #Aquí se crea la contraseña
        messagebox.showinfo("Contraseña creada",self.__password) #Aquí se muestra la contraseña en un messagebox
        pEntry = Entry() #Aquí se crea un entry para copypastear la contraseña
        pEntry.insert(0, self.__password) #Aquí se inserta la contraseña en el entry
        pEntry.pack()
        return self.__password
    
        
    
    #Getters y Setters
    def getLen(self): #Este es el getter de la longitud de la contraseña
        return self.__len
    
    """ def setLen(self):
        self.__len = length """