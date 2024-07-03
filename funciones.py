import os
import csv

pedidos=[]


def opc_1():
    print("Registrar Pedido")
    print("")
    contador_5=0
    contador_15=0

    
    print("Ingrese su Nombre:")
    nombre=input("> ")
    rut=input("Ingrese su Rut (con puntos y guion):\n> ")


    direccion=input("Ingrese su direccion(ejemplo: Las calles 1234):\n> ")

    while True:
        print("""Seleccione comuna
              1. Puente Alto
              2. San Bernardo
              3. La Pintana
              
              Ingrese numero: """)
        while True:
            try:
                opc_comuna=int(input("> "))
                if opc_comuna in(1,2,3):
                    break
                else:
                    print("Error, ingrese un numero valido")
            except:
                print("Error, ingrese opcion en numero Entero")
        if opc_comuna in(1,2,3):
            break
    
    if opc_comuna==1:
        comuna="puente alto"
    elif opc_comuna==2:
        comuna="san bernardo"
    elif opc_comuna==3:
        comuna="la pintana"
    


    while True:
        print(""" Ingrese su Pedido:
            
            1.Galon 5kg..............$12.500
            2.Galon 15kg.............$25.500

            3.Contiunar compra
                        """)
        try:
            opc_galon=int(input("> "))
            if opc_galon in(1,2,3):
                if opc_galon==1:
                    print("Cuantos Galones de 5kg llevara?")
                    while True:
                        try:
                            cantidad_5=int(input("> "))
                            if cantidad_5>0:
                                
                                contador_5=contador_5+cantidad_5
                                break
                            else:
                                print("Error, Ingrese un valor superior a 0")
                        except:
                            print("Error, ingrese un valor en numeros Enteros!")

                elif opc_galon==2:
                    print("Cuantos Galones de 15kg llevara?")
                    while True:
                        try:
                            cantidad_15=int(input("> "))
                            if cantidad_15>0:
                                
                                contador_15=contador_15+cantidad_15
                                break
                            else:
                                print("Error, Ingrese un valor superior a 0")
                        except:
                            print("Error, ingrese un valor en numeros Enteros!")
                elif opc_galon==3:
                    break
                            
            else:
                print("Error, ingrese un numero valido")
            
            print("")
        except:
            print("Error, ingrese opcion en numero Entero")

        total_5=contador_5*12500
        total_15=contador_15*25000
        total=total_15+total_5

        
        pedido={"nombre":nombre,
                "rut":rut,
                "direccion":direccion,
                "comuna":comuna,
                "cilindro 5kg": contador_5,
                "cilindro 15kg": contador_15,
                "total":total}
        
        pedidos.append(pedido)

def opc_2():
    print("Nombre      Rut      Direccion      Comuna      Cil.5kg     Cil.15kg      Total")
    for x in pedidos:
        
        print(f"{x['nombre']}    {x['rut']}    {x['direccion']}    {x['comuna']}    {x['cilindro 5kg']}    {x['cilindro 15kg']}    {x['total']}")

def opc_3():
    print("Ingrese rut para buscar:")
    busca=input("> ")

    for x in pedidos:
        if pedidos[x]["rut"]==busca:
            print("Nombre      Rut      Direccion      Comuna      Cil.5kg     Cil.15kg      Total")
            print(f"{x['nombre']}    {x['rut']}    {x['direccion']}    {x['comuna']}    {x['cilindro 5kg']}    {x['cilindro 15kg']}    {x['total']}")
            break
        if x==len(pedidos) and pedidos[x]["rut"]==busca:
            break
        elif x==len(pedidos) and pedidos[x]["rut"]!=busca:
            print("Rut no encontrado!")

def opc_4():
    print("Seleccione comuna a imprimir:")
    print("1. Puente Alto")
    print("2. San Bernardo")
    print("3. La Pintana")

    while True:
        try:
            menu=int(input("> "))
            if menu in(1,2,3):
                break
            else:
                print("Error!, ingrese opcion valida")
        except:
            print("Error!, ingrese opcion en numero entero!")
   
    print("ingrese nombre del archivo a extraer:")
    nombre=input("> ")
    nombre=nombre+(".csv")

   
   
   

    if menu==1:
        for x in pedidos:    
            if x['comuna']=="puente alto":
                imprime(f"""
Nombre      Rut      Direccion      Comuna      Cil.5kg     Cil.15kg      Total
{x['nombre']}    {x['rut']}    {x['direccion']}    {x['comuna']}    {x['cilindro 5kg']}    {x['cilindro 15kg']}    {x['total']}""")             
                with open(nombre,"w",newline="") as archivo:
                    escritor=csv.writer(archivo)
                    escritor.writerow(imprime)


                
    elif menu==2:
        for x in pedidos:
            if x['comuna']=="san bernardo":
                imprime=(f"""
Nombre      Rut      Direccion      Comuna      Cil.5kg     Cil.15kg      Total
{x['nombre']}    {x['rut']}    {x['direccion']}    {x['comuna']}    {x['cilindro 5kg']}    {x['cilindro 15kg']}    {x['total']}""")      
                with open(nombre,"w",newline="") as archivo:
                    escritor=csv.writer(archivo)
                    escritor.writerow(imprime)              
    elif menu==3:
        for x in pedidos:
            if x['comuna']=="la pintana":
                imprime=(f"""
Nombre      Rut      Direccion      Comuna      Cil.5kg     Cil.15kg      Total
{x['nombre']}    {x['rut']}    {x['direccion']}    {x['comuna']}    {x['cilindro 5kg']}    {x['cilindro 15kg']}    {x['total']}""")    
                with open(nombre,"w",newline="") as archivo:
                    escritor=csv.writer(archivo)
                    escritor.writerow(imprime)