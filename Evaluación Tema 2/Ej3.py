class Producto:
    def __init__(self,codigo,nombre,precio,tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print("El producto se ha creado con éxito")

    def __str__(self):

        cadena = "Codigo: "+str(self.codigo) + " . Nombre: "+str(self.nombre) +". Precio: "+str(self.precio)+". Tipo: "+str(self.tipo)
        return cadena


A = Producto("A312","Jorge",50,"A")
B = Producto("B222","Daniel",50,"B")

print(A)
print(B)

A.precio = 100

print(A)