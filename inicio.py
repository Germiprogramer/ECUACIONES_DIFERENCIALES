from ecuaciones.ecuacion1 import *
from ecuaciones.ecuacion2 import *
from ecuaciones.ecuacion3 import *
from ecuaciones.ecuacion4 import *
from ecuaciones.funciones import limpiar_pantalla


def iniciar():
    while True:
        limpiar_pantalla()

        print("========================")
        print("  Bienvenido al Gestor  ")
        print("========================")
        print("[1] Ecuación 1")
        print("[2] Ecuación 2")
        print("[3] Ecuación 3")
        print("[4] Ecuación 4")
        print("========================")

        opcion = input("> ")
        limpiar_pantalla()

        if opcion == '1':
            problema1(3)

        elif opcion == '2':
           problema2()

        elif opcion == '3':
           problema3()

        elif opcion == '4':
           problema4()
        
        input("\nPresiona ENTER para continuar...")