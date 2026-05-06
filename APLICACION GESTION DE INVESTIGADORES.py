from os import system
from TADInvestigadores import*
from datetime import datetime, time

x=0
i = []

while (x==0):
    system("cls")
    print ("##### MENU DE OPCIONES ##### \n")
    print("[1]:Cargar nuevo investigador")
    print("[2]:Ver informacion de Investigador")
    print("[3]:Modificar Investigador")
    print("[4]:Eliminar Investigador")
    print("[5]:Visualizar Plantel Cientifico")
    print("[6]:Reasignacion Masiva Por Año de Ingreso")
    print("[7]:Depuracion por Jubilacion (30 años)")
    print("[8]:Generar cola de investigadores de un area especifica")
    print("[9]:Salir")

    opcion=int(input("Res:"))

    match opcion :
        case 1 : 
            system("cls")
            inv = crearInvestigador()
            nombre = input("Ingrese su Nombre: ")
            apellido = input("Ingrese su Apellido: ")
            legajo = input("Ingrese su Legajo: ")
            fechIng = input("Ingrese su Fecha de Ingreso (DD/MM/AAAA): ")
            print (f"len:{len(fechIng)}")
            if (fechIng.rfind("-")) :
                fechIng = fechIng.replace("-","/")
            elif (len(fechIng) <= 0 | len(fechIng) > 10) :
                print ("Ingrese una fecha valida!")
            numLab = input ("Ingrese su numero de Laboratorio: ")
            area = input ("Ingrese su area: \n1) Area 1\n2) Area 2\n3) Area 3\nOpcion: ")
            if (area == 1) :
                area == 'Area1'
            elif (area == 2) :
                area == 'Area2'
            elif (area == 3) :
                area == 'Area3'
            cargarInvestigador(inv,nombre,apellido,legajo,fechIng,numLab,area)
            sumarInvestigador(i,inv)
            print(f"Se ha cargado satisfactoriamente el investigador: \n{inv}")
            input()
        
        case 5:
            if (esVacia(i)) :
                system("cls")
                print("No hay elementos cargados en la lista!\nProba ca6rgando un Investigador con la Opcion 1 en el menu")
                input("Presione una tecla para continuar...")
            else :
                system("cls")
                mostrarLista(i)
                input("Presione una tecla para continuar...")
            
        case 9:
            system("cls")
            print("Adios!")
            x=1
        
        case _:
            system ("cls")
            print("Ingrese una opcion valida!")
            input("Presione una tecla para continuar...")
        