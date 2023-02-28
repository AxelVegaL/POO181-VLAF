from tkinter import Tk, Frame, Button

#1. Instanciamos un Objeto Ventana
ventana = Tk()
ventana.title("Práctica 11:3 Frames")
ventana.geometry("600x400")
#Tenemos que llamar al main de esta clase con el metodo mainloop()

#2. Definimos Secciones de la ventana
seccion1 = Frame(ventana, bg="#00bfff")
seccion1.pack(expand=True, fill="both") #Activa expandir, rellenar a ambos lados
seccion2 = Frame(ventana,bg="#ffffff")
seccion2.pack(expand=True, fill="both") 
seccion3 = Frame(ventana, bg="#00394d")
seccion3.pack(expand=True, fill="both")

#3. Creamos los botones
botonAzul = Button(seccion1, text="Botón Azul Cielo", fg="#00bbff", bg="white") #seccion1 es el padre, Button la clase
botonAzul.place(x=60, y=60) #x e y son las coordenadas del botón, place es el método
botonBlanco = Button(seccion2, text="Botón Blanco", fg="white", bg="gray") #seccion1 es el padre, Button la clase
botonBlanco.grid(row=0, column=0) #row y column son las coordenadas del botón, grid es el método
botonAzulF = Button(seccion2, text="Botón Azul Fuerte", fg="blue", bg="white") #seccion1 es el padre, Button la clase
botonAzulF.grid(row=1, column=1) 
botonVerde = Button(seccion3, text="Botón Verde", fg="green", bg="white") #seccion1 es el padre, Button la clase
botonVerde.pack() #pack es el método, no necesita coordenadas porque se pone al final de la ventana


ventana.mainloop()
#el main siempre queda al final del código, porque es el que te dibuja la ventana con toooodo lo ya escrito