from os import system
from TADInvestigadores import *
from FuncionesAuxiliares import *

close = 0
ListaInv = []

while (close==0):
    system("cls")
    print ("====== SISTEMA DE GESTION DE INVESTIGADORES ======\n")
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
            nombre = verificarInputStr("Ingrese su Nombre: ")
            apellido = verificarInputStr("Ingrese su Apellido: ")
            legajo = verificarInputLegajo("Ingrese su Legajo: ", ListaInv)
            fechIng = verificarInputFecha("Ingrese su Fecha de Ingreso (DD/MM/AAAA): ")
            numLab = verificarInputInt("Ingrese su numero de Laboratorio: ")
            area = int(verificarInputInt("Ingrese su area: \n1) Biotecnologia\n2) IA\n3) Energias Renovables\nOpcion: "))
            if (area == 1) :
                area = "Biotecnologia"
            elif (area == 2) :
                area = "IA"
            elif (area == 3) :
                area = "Energia Renovables"
            else :
                area = "Area Desconocida"
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
            x=input("Ingrese Legajo del Investigador que desea ver: ")
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
            x=input("Ingrese legajo del investigador que desea modificar: ")
            for z in range(len(ListaInv)):
                legMod=verLegajo(recuperarInvestigador(ListaInv,z))
                if (legMod==x):
                    nuevoNom=verificarInputStr("Ingrese el nuevo Nombre: ")
                    nuevoApe=verificarInputStr("Ingrese el nuevo Apellido: ")
                    nuevoLeg=verificarInputInt("Ingrese el nuevo Legajo: ")
                    nuevaFecha=verificarInputFecha("Ingrese fecha de ingreso:")
                    nuevoLab=verificarInputInt("Ingrese el nuevo numero de Laboratorio: ")
                    nuevaArea = verificarInputInt ("Ingrese su area: \n1) Biotecnologia\n2) IA\n3) Energias Renovables\nOpcion: ")
                    if (area == 1) :
                        area == 'Biotecnologia'
                    elif (area == 2) :
                        area == 'IA'
                    elif (area == 3) :
                        area == 'Energia Renovables'
                    modNombre(recuperarInvestigador(ListaInv,z),nuevoNom)
                    modApellido(recuperarInvestigador(ListaInv,z),nuevoApe)
                    modLegajo(recuperarInvestigador(ListaInv,z),nuevoLeg)
                    modFecha(recuperarInvestigador(ListaInv,z),nuevaFecha)
                    modLab(recuperarInvestigador(ListaInv,z),nuevoLab)
                    modArea(recuperarInvestigador(ListaInv,z),nuevaArea)
                    print("Investigador modificado con exito!")
                    input("Presione una tecla para continuar...")
            
                else :
                    print("No se ha encontrado Investigador!\n")
                    input("Presione una tecla para continuar...")

        case 4:
            system("cls")
            x = verificarInputInt("Ingrese el Legajo del Investigador que desea Eliminar:")
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
                print("No hay elementos cargados en la lista!\nProba cargando un Investigador con la Opcion 1 en el menu.")
                input("Presione una tecla para continuar...")
            else :
                system("cls")
                print ("##### Lista de Investigadores ##### \n")
                verTodo(ListaInv)
                print("=================================\n")
                input("Presione una tecla para continuar...")
        
        case 6: 
            system ("cls")
            print("#### Reasignacion Masiva de Personal ####")
            nuevaArea = verificarInputStr("Ingrese el año de los investigadores a cambiar el area: ")
        
        case 8:
            cola=CrearCola()
            area = int(verificarInputInt("Ingrese el area que desea generar cola: \n1) Biotecnologia\n2) IA\n3) Energias Renovables\nOpcion: "))
            if (area == 1) :
                area = "Biotecnologia"
            elif (area == 2) :
                area = "IA"
            elif (area == 3) :
                area = "Energia Renovables"
            else :
                area = "Area Desconocida"
            
            for z in range(len(ListaInv)):
                inv=recuperarInvestigador(ListaInv,z)
                if(area==verArea(inv)):
                    Encolar(cola,inv)
            
            if(not esVacia(cola)):
                print("### COLA INVESTIGADORES ###\n")
                while(not esVacia(cola)):
                    imp=Desencolar(cola)
                    print("Nombre:", verNombre(imp))
                    print("Apellido:", verApellido(imp))
                    print("Legajo:", verLegajo(imp))
                    print("Fecha de Ingreso:", verFecha(imp))
                    print("Numero de Laboratorio:", verLaboratorio(imp))
                    print("Area:", verArea(imp))
                    print("=================================\n")
            
            else :
                print("No se encontraron investigadores en esa area")

            input("Presione una tecla para continuar...")

        case 9:
            system("cls")
            print("Adios!")
            exit(0)
        
        case _:
            system ("cls")
            print("Ingrese una opcion valida!")
            input("Presione una tecla para continuar...")
