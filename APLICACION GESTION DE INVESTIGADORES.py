from TADInvestigadores import*
from datetime import datetime, time

x=0

while (x==0):
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
            print ("hola")
        case 9:
            print("Adios!")
            x=1
        