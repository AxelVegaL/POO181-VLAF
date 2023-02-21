#1. Importar la clase
from Personaje import * # Importa todo lo que hay en el archivo Personaje.py

#2. Instanciar un objeto
Heroe = Personaje() # Instancia un objeto de la clase Personaje

#3. Acceder a los atributos
print("ATRIBUTOS DEL PERSONAJE")
print("El personaje es un " + Heroe.especie) # Accede al atributo especie del objeto Heroe
print("Este distinguido caballero se llama " + Heroe.nombre) # Accede al atributo nombre del objeto Heroe
print("El personaje mide " + str(Heroe.altura) + " metros") # Accede al atributo altura del objeto Heroe

#4. Acceder a los métodos
print("\n\n\nMÉTODOS DEL PERSONAJE")
Heroe.correr(True) # Accede al método correr del objeto Heroe
Heroe.lanzarGranada() # Accede al método lanzarGranada del objeto Heroe
Heroe.recargarArma(3) # Accede al método recargarArma del objeto Heroe
#el 3 es el argumento que se le pasa al método recargarArma
