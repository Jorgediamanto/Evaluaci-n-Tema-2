import os
import Ej1
import Ej2
import Ej3
import Ej4
import Ej5


def iniciar():
    while True:
        

        print("========================")
        print("  Bienvenido al Menu  ")
        print("========================")
        print("[1] Ejecutar Ejercicio 1 ")
        print("[2] Ejecutar Ejercicio 2 ")
        print("[3] Ejecutar Ejercicio 3 ")
        print("[4] Ejecutar Ejercicio 4 ")
        print("[5] Ejecutar Ejercicio 5 ")
        print("[6] Cerrar el Menu       ")
        print("========================")

        opcion = input("> ")
        

        if opcion == '1':
            print("ejecutando ejercicio 1...")
            os.system("Ej1.py")

        elif opcion == '2':
            print("ejecutando ejercicio 1...")
            os.system("Ej2.py")

        elif opcion == '3':
            print("ejecutando ejercicio 1...")
            os.system("Ej3.py")

        elif opcion == '4':
            print("ejecutando ejercicio 1...")
            os.system("Ej4.py")

        elif opcion == '5':
            print("ejecutando ejercicio 1...")
            os.system("Ej5.py")

        elif opcion == '6':
            print("saliendo...")
            break

        input("\nPresiona ENTER para continuar...")
