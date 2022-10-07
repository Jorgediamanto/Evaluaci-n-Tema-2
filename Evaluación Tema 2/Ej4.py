

try:
	numero = 7/0
except ZeroDivisionError:
	print("Error causado por tratar de dividir por 0.")

lista = [4, 7, 30, 23, 5]

try:
    lista[10]
except IndexError:
    print("Índice fuera de rango de lista.")


paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 

try:
    paises["alemania"]
except KeyError:
    print("Esta llave no se encuentra dentro del diccionario")


try:
    resultado = "2" + 10
except TypeError:
    print("No se puede sumar un string a un entero!!")