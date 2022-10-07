import os
import helpers
import Ej1,Ej2,Ej3,Ej4,Ej5 as Ej1,Ej2,Ej3,Ej4,Ej5

def iniciar():
    while True:
        helpers.limpiar_pantalla()

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
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("ejecutando ejercicio 1...")
            os.system("Ej1.py 1")

        elif opcion == '2':
            print("ejecutando ejercicio 1...")
            os.system("Ej2.py 1")

        elif opcion == '3':
            print("ejecutando ejercicio 1...")
            os.system("Ej3.py 1")

        elif opcion == '4':
            print("ejecutando ejercicio 1...")
            os.system("Ej4.py 1")

        elif opcion == '5':
            print("ejecutando ejercicio 1...")
            os.system("Ej5.py 1")

        elif opcion == '6':
            print("saliendo...")
            break

        input("\nPresiona ENTER para continuar...")
