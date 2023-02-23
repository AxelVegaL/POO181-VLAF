#1. Importar la clase
from Personaje import * # Importa todo lo que hay en el archivo Personaje.py

#2.1 Solicitar atributos para el objeto
print("\n\n### SOLICITUD DE DATOS DEL HEROE ###\n")
espH = input("Especie del personaje: ")
nomH = input("Nombre del personaje: ")
altH = float(input("Altura del personaje: "))
cargaH = int(input("Balas a recargar: "))

#2.2 Datos de villano
print("\n\n### SOLICITUD DE DATOS DEL VILLANO ###\n")
espV = input("Especie del villano: ")
nomV = input("Nombre del villano: ")
altV = float(input("Altura del villano: "))
cargaV = int(input("Balas a recargar para el villano: "))

#3. Creamos 2 objetos
Heroe = Personaje(espH, nomH, altH) # Instancia un objeto de la clase Personaje (Héroe)
Villano = Personaje(espV, nomV, altV) # Instancia un objeto de la clase Personaje (Villano)
#No se toma la de recarga, ya que se lleva desde Persona.py como municiones

#4. Acceder a los atributos y métodos de cada objeto
print("\n\nATRIBUTOS Y MÉTODOS DEL PERSONAJE\n")
print("El personaje es un " + Heroe.especie) # Accede al atributo especie del objeto Heroe
print("Este distinguido caballero se llama " + Heroe.nombre) # Accede al atributo nombre del objeto Heroe
print("El personaje mide " + str(Heroe.altura) + " metros\n") # Accede al atributo altura del objeto Heroe
Heroe.correr(True) # Accede al método correr del objeto Heroe
Heroe.lanzarGranada() # Accede al método lanzarGranada del objeto Heroe
Heroe.recargarArma(cargaH) # Accede al método recargarArma del objeto Heroe


print("\n\nATRIBUTOS Y MÉTODOS DEL VILLANO\n")
print("El villano es un " + Villano.especie)
print("El enemigo lleva por nombre '" + Villano.nombre + "'") 
print("El malo mide " + str(Villano.altura) + " metros\n\n")

Villano.correr(False) 
Villano.lanzarGranada()
Villano.recargarArma(cargaV)
 