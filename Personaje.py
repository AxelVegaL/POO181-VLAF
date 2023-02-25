
class Personaje: # Clase Personaje
    #Atributos del Personaje
    #Bob el Constructor
    def __init__(self, esp, nom, alt): # El constructor siempre lleva el self
        self.__especie = esp #es público sin los "__", pero no se debe acceder a él desde fuera de la clase, por eso se usa el "__"
        self.__nombre = nom
        self.__altura = alt #Hey, en JS se ve eso xD


    #Métodos del Personaje
    def correr(self, status): # Método correr. Siempre lleva el self xd
        if (status):
            print("El personaje " + self.__nombre + " está corriendo")
        else:
            print("El personaje " + self.__nombre + " está quieto")
    
    def lanzarGranada(self):
        print("Se ha lanzado una granada... o un cohetazo, ahre")
    
    def recargarArma(self, municiones):
        cargador = 5
        cargador = cargador + municiones
        print("Se han recargado " + str(municiones) + " municiones. Ahora el cargador tiene " + str(cargador) + " municiones")
    #Ejemplo de método privado
    def __pensar(self):
        print("Toy pensando... ( ͡° ͜ʖ ͡°) ")
    
    #getters y setters'

    def getEspecie(self):
        return self.__especie #Retorna el valor del atributo especie
    
    def getNombre(self):
        return self.__nombre
    
    def getAltura(self):
        return self.__altura
    
    def setEspecie(self, esp):
        self.__especie = esp #Asigna un valor al atributo especie
    
    def setNombre(self, nom):
        self.__nombre = nom

    def setAltura(self, alt):
        self.__altura = alt