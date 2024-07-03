import os
import csv
from funciones import *

os.system("cls")

while True:

    print("Bienvenido al sistema de ventas Gaxplosive!")
    print("""Menu:
        1. Registrar Pedido
        2. Listar Pedidos
        3. Buscar pedido por rut
        4. Imprimir hoja de ruta
        5. Salir
        
        Ingrese opcion:""")
    while True:
        try:
            opc=int(input("> "))
            if opc in(1,2,3,4,5):
                break
            else:
                print("Error!, ingrese una opcion valida")
        except:
            print("Error!, ingrese una opcion en numero entero!")

    if opc==1:
        opc_1()
    elif opc==2:
        opc_2()
    elif opc==3:
        opc_3()
    elif opc==4:
        pass
    elif opc==5:
        break

