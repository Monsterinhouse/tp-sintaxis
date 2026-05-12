from os import system
from TADInvestigadores import*
from datetime import datetime, time

close = 0
ListaInv = []

while (close==0):
    system("cls")
    print ("##### MENU DE OPCIONES ##### \n")
    print("[1] Cargar nuevo investigador")
    print("[2] Ver Investigador")
    print("[3] Modificar Investigador")
    print("[4] Eliminar Investigador")
    print("[5] Visualizar Plantel Cientifico")
    print("[6] Reasignacion Masiva Por Año de Ingreso")
    print("[7] Depuracion por Jubilacion (30 años)")
    print("[8] Generar cola de investigadores de un area especifica")
    print("[9] Salir")

    opcion=int(input("Opcion: "))

    match opcion :
        case 1 : 
            system("cls")
            inv = crearInvestigador()
            # nombre = input("Ingrese su Nombre: ")
            # if (nombre.isdigit()) :
            #         print ("Caracter no valido!\nLa carga ha sido cancelada\n")
            #         input ("Volviendo al menu")
            #         break
            nombre = verificarInputStr("Ingrese su Nombre: ")
            apellido = verificarInputStr("Ingrese su Apellido: ")
            legajo = verificarInputInt("Ingrese su Legajo: ")
            fechIng = input("Ingrese su Fecha de Ingreso (DD/MM/AAAA): ")
            feching = formateoFecha(fechIng)
            controlFecha(fechIng[:2], fechIng[3:5], fechIng[-4:])
            numLab = verificarInputInt("Ingrese su numero de Laboratorio: ")
            area = verificarInputInt("Ingrese su area: \n1) Area 1\n2) Area 2\n3) Area 3\nOpcion: ")
            if (area == 1) :
                area == 'Area1'
            elif (area == 2) :
                area == 'Area2'
            elif (area == 3) :
                area == 'Area3'
            cargarInvestigador(inv,nombre,apellido,legajo,fechIng,numLab,area)
            sumarInvestigador(ListaInv,inv)
            system ("cls")
            print(f'''Se ha cargado satisfactoriamente el Investigador: \n
                    Nombre: {nombre}
                    Apellido: {apellido}
                    Legajo: {legajo}
                    Fecha de Ingreso: {fechIng}
                    Numero de Laboratorio: {numLab}
                    Area: {area}
                ''')
            input("Presione una tecla para continuar...")
            
        case 2:
            system("cls")
            x=input("Ingrese Legajo del Investigador que desea ver:")
            for z in range(len(ListaInv)):
                if (verLegajo(recuperarInvestigador(ListaInv,z))==x):
                    print("##### Investigador ##### \n")
                    print("Nombre:", verNombre(recuperarInvestigador(ListaInv,z)))
                    print("Apellido:", verApellido(recuperarInvestigador(ListaInv,z)))
                    print("Legajo:", verLegajo(recuperarInvestigador(ListaInv,z)))
                    print("Fecha de Ingreso:", verFecha(recuperarInvestigador(ListaInv,z)))
                    print("Numero de Laboratorio:", verLaboratorio(recuperarInvestigador(ListaInv,z)))
                    print("Area:", verArea(recuperarInvestigador(ListaInv,z)))
                    input("Presione una tecla para continuar...")
                else :
                    print("Investigador no encontrado\n")
                    input("Presione una tecla para continuar...")
        
        case 3:
            system("cls")
            x=input("Ingrese legajo del investigador que desea modificar:")
            for z in range(len(ListaInv)):
                legMod=verLegajo(recuperarInvestigador(ListaInv,z))
                if (legMod==x):
                    nuevoNom=input("Ingrese nombre:")
                    nuevoApe=input("Ingrese apellido:")
                    nuevoLeg=input("Ingrese legajo:")
                    nuevaFecha=input("Ingrese fecha de ingreso:")
                    nuevoLab=input("Ingrese Numero de laboratorio:")
                    nuevaArea = input ("Ingrese su area: \n1) Area 1\n2) Area 2\n3) Area 3\nOpcion: ")
                    if (area == 1) :
                        area == 'Area1'
                    elif (area == 2) :
                        area == 'Area2'
                    elif (area == 3) :
                        area == 'Area3'
                    modNombre(recuperarInvestigador(ListaInv,z),nuevoNom)
                    modApellido(recuperarInvestigador(ListaInv,z),nuevoApe)
                    modLegajo(recuperarInvestigador(ListaInv,z),nuevoLeg)
                    modFecha(recuperarInvestigador(ListaInv,z),nuevaFecha)
                    modLab(recuperarInvestigador(ListaInv,z),nuevoLab)
                    modArea(recuperarInvestigador(ListaInv,z),nuevaArea)
                    print("Investigador modificado con exito")
                    input("Presione una tecla para continuar...")
            
                else :
                    print("No se ha encontrado Investigador!\n")
                    input("Presione una tecla para continuar...")

        case 4:
            system("cls")
            x=input("Ingrese legajo del Investigador que desea modificar:")
            z=0
            while(z<len(ListaInv)):
                legEli=verLegajo(recuperarInvestigador(ListaInv,z))
                if (legEli==x):
                    print("Desea eliminar el siguiente Investigador?:\n")
                    print("Nombre:", verNombre(recuperarInvestigador(ListaInv,z)))
                    print("Apellido:", verApellido(recuperarInvestigador(ListaInv,z)))
                    print("Legajo:", verLegajo(recuperarInvestigador(ListaInv,z)))
                    print("Fecha de Ingreso:", verFecha(recuperarInvestigador(ListaInv,z)))
                    print("Numero de Laboratorio:", verLaboratorio(recuperarInvestigador(ListaInv,z)))
                    print("Area:", verArea(recuperarInvestigador(ListaInv,z)))
                    print("\n")
                    opcEli=int(input("[1] Si\n[2] No\nOpcion: "))
                    if (opcEli==1):
                        eliminarInvestigador(ListaInv,recuperarInvestigador(ListaInv,z))
                        print("Investigador eliminado")
                        input("Presione una tecla para continuar...")
                    
                    elif (opcEli==0):
                        print("Se cancela la eliminacion de investigador")
                        input("Presione una tecla para continuar...")
                
                else :
                    z=z+1

        case 5:
            if (esVacia(ListaInv)) :
                system("cls")
                print("No hay elementos cargados en la lista!\nProba ca6rgando un Investigador con la Opcion 1 en el menu")
                input("Presione una tecla para continuar...")
            else :
                system("cls")
                print ("##### Lista de Investigadores ##### \n")
                for z in range(len(ListaInv)):
                    print("Nombre:", verNombre(recuperarInvestigador(ListaInv,z)))
                    print("Apellido:", verApellido(recuperarInvestigador(ListaInv,z)))
                    print("Legajo:", verLegajo(recuperarInvestigador(ListaInv,z)))
                    print("Fecha de Ingreso:", verFecha(recuperarInvestigador(ListaInv,z)))
                    print("Numero de Laboratorio:", verLaboratorio(recuperarInvestigador(ListaInv,z)))
                    print("Area:", verArea(recuperarInvestigador(ListaInv,z)))
                    print("##############################")
                input("Presione una tecla para continuar...")
            
        case 9:
            system("cls")
            print("Adios!")
            exit(0)
        
        case _:
            system ("cls")
            print("Ingrese una opcion valida!")
            input("Presione una tecla para continuar...")
        