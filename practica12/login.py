class login:
    def __init__(self, ma, passw):
        self.__mail = ma
        self.__password = passw

    def welcome(self):
        print("El personaje " + self.__mail + " está corriendo")
        print("Su clave es " + self.__password)

    #Getters y Setters
    def getMail(self):
        return self.__mail
    
    def getPassword(self):
        return self.__password
    
    def setMail(self, ma):
        self.__mail = ma

    def setPassword(self, passw):
        self.__password = passw