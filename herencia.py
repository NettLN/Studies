#Programacion Orientada a objetos
class Persona():
    #CONTRUCTOR
    def __init__(self, nombre, apepat, apemat):
        self.nombre = nombre
        self.apepat = apepat
        self.apemat = apemat

    def MostrarNombreCompleto(self):
        txt = "{0}, {1}, {2}"
        return txt.format(self.nombre, self.apepat, self.apemat)
    
class Estudiante(Persona):
    def __init__(self, nombre, apepat, apemat, profesion):
        super().__init__(nombre, apepat, apemat) #REferenciamos el constructor de la clase padre
        self.profecion = profesion

    def MostrarNombreCompleto(self):
        return super().MostrarNombreCompleto()

#Instanciar el objeto estudiante1
estudiante1 = Estudiante("Carlos", "Perez", "Gomez", "Ingeniero en Sistemas" )
print(estudiante1.MostrarNombreCompleto())
print(estudiante1.profecion)
estudiante1.MostrarNombreCompleto()