import itertools


class Vehiculo():

 

    def __init__(self, color, ruedas):

        self.color = color

        self.ruedas = ruedas

 

    def __str__(self):

        return "color {}, {} ruedas".format( self.color, self.ruedas )

    def catalogar(self,vehiculos,ruedas=4):
        a1=0
        for x in vehiculos:
            if x.ruedas == ruedas:
                a1+=1
                print("Nombre de clase: "+x.__class__.__name__)

                if x.__class__.__name__ == "Coche":
                    print("Color: "+x.color)
                    print("Ruedas: "+str(x.ruedas))
                    print("Velocidad: "+str(x.velocidad))
                    print("Cilindrada:"+str(x.cilindrada))

                if x.__class__.__name__ == "Vehiculo":
                    print("Color: "+x.color)
                    print("Ruedas: "+str(x.ruedas))

        print("Se han encontrado "+str(a1)+" vehículos con "+str(ruedas)+" ruedas:")
 

 

class Coche(Vehiculo):

 

    def __init__(self, color, ruedas, velocidad, cilindrada):

        Vehiculo.__init__(self, color, ruedas)

        self.velocidad = velocidad

        self.cilindrada = cilindrada

 

    def __str__(self):

        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

    

 

 
vehiculos = []

c = Coche("azul", 4, 150, 1200)
a = Vehiculo("amarillo chillón",4)

vehiculos.append(c)
vehiculos.append(a)

print(vehiculos)


c.catalogar(vehiculos)