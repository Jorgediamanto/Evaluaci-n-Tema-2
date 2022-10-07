class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        print("Alumno creado con éxito")

    def __str__(self):

        cadena = "Nombre: "+str(self.nombre) + " . Nota: "+str(self.nota)
        return cadena


    def calificacion(self):
        if self.nota<5:
            print("Este alumno ha suspendido la asignatura")

        else:
            print("Este alumno ha aprobado la asignatura")


A = Alumno("Jorge",0)
B = Alumno("Daniel",10)
C = Alumno("Francisco",5)

A.calificacion()
B.calificacion()
C.calificacion()


print(A)
print(B)
print(C)
