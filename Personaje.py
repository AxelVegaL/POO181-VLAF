
class Personaje: # Clase Personaje
    #Atributos del Personaje
    especie = "Humano"
    nombre = "Leon Scott Kennedy"
    altura = 1.78

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
        print("Se han recargado " + municiones + " municiones. Ahora el cargador tiene " + cargador + " municiones")