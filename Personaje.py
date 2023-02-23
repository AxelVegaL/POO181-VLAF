
class Personaje: # Clase Personaje
    #Atributos del Personaje
    #Bob el Constructor
    def __init__(self, esp, nom, alt): # El constructor siempre lleva el self
        self.especie = esp
        self.nombre = nom
        self.altura = alt #Hey, en JS se ve eso xD


    #Métodos del Personaje
    def correr(self, status): # Método correr. Siempre lleva el self xd
        if (status):
            print("El personaje " + self.nombre + " está corriendo")
        else:
            print("El personaje " + self.nombre + " está quieto")
    
    def lanzarGranada(self):
        print("Se ha lanzado una granada... o un cohetazo, ahre")
    
    def recargarArma(self, municiones):
        cargador = 5
        cargador = cargador + municiones
        print("Se han recargado " + str(municiones) + " municiones. Ahora el cargador tiene " + str(cargador) + " municiones")
         