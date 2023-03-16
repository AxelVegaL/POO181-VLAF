class Matriculador:
    def __init__(self):
        self.matricula = ""
        self.nombre = ""
        self.nacimiento = 0
        self.year = 2023
        self.carrera = ""
        self.aleatorio = ""
        self.apellido_paterno =""
        self.apellido_materno = ""

    def matriculaData(self,nombre, apellido_p, apellido_m, nacimiento, carrera, year, aleatorio):
        self.nombre = nombre
        self.apellido_paterno = apellido_p
        self.apellido_materno = apellido_m
        self.nacimiento = nacimiento
        self.carrera = carrera
        self.year = year
        self.aleatorio = aleatorio
        self.matricula = self.nombre[0] + self.apellido_paterno[0] + self.apellido_paterno [1] + self.apellido_materno[0] + self.apellido_materno[1] + str(self.nacimiento)[-2] + str(self.nacimiento)[-1] + str(self.year)[-2] + str(self.year)[-1] + self.carrera[0] + self.carrera[1] + self.carrera[2] + self.aleatorio
        self.matricula = self.matricula.upper()
        #print(self.matricula)
        return self.matricula