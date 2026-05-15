from TADInvestigadores import *
from datetime import date

def verTodo(listaInvestigadores) :
    for z in range(len(listaInvestigadores)):
        print("Investigador N°: ", z+1)
        print("Nombre:", verNombre(recuperarInvestigador(listaInvestigadores,z)))
        print("Apellido:", verApellido(recuperarInvestigador(listaInvestigadores,z)))
        print("Legajo:", verLegajo(recuperarInvestigador(listaInvestigadores,z)))
        print("Fecha de Ingreso:", verFecha(recuperarInvestigador(listaInvestigadores,z)))
        print("Numero de Laboratorio:", verLaboratorio(recuperarInvestigador(listaInvestigadores,z)))
        print("Area:", verArea(recuperarInvestigador(listaInvestigadores,z)))
        print("=================================\n")

def asignacionMasiva (yearInvestigadores, areaCambio, listaInvestigadores) :
    for i in range(len(listaInvestigadores)) :
        year = verFecha(recuperarInvestigador(listaInvestigadores,i))
        if (year[-4:] == yearInvestigadores) :
            modArea(recuperarInvestigador(listaInvestigadores,i),areaCambio)

### FUNCIONES DE AYUDA ###
def eliminarInvestigador(lista,inv):
    lista.remove(inv)

def recuperarInvestigador(lista,investigador):
    return lista[investigador]

### VERIFICACIONES DE INPUTS ###
def verificarInputStr(mensajeInput) :
        while True:
            valor = input(mensajeInput)
            if (valor.isdigit()) :
                print ("Error: No se permiten Numeros. Ingrese caracteres validos")
            elif len(valor.strip()) == 0 :
                print ("Error: El campo no puede estar vacio")
            else :
                return valor.title()

def verificarInputInt(mensajeInput) :
        while True:
            valor = input(mensajeInput)
            if (valor.isalpha()) :
                print ("Error: No se permiten Letras. Ingrese caracteres validos")
            elif len(valor.strip()) == 0 :
                print ("Error: El campo no puede estar vacio")
            else :
                return valor

def verificarInputLegajo (mensajeInput, listaInvestigadores) :
    while True :
        legajo = verificarInputInt(mensajeInput)
        if (esVacia(listaInvestigadores)) :
            return legajo
        else: 
            for i in range (len(listaInvestigadores)) :
                if (legajo==verLegajo(recuperarInvestigador(listaInvestigadores,i))) :
                    print("El legajo ingresado ya existe!\nIntente nuevamente.")
                else :
                    return legajo
                

def verificarInputFecha(mensajeInput):
    while True:
        fecha = input(mensajeInput).strip()
        if len(fecha) == 0 or len(fecha) < 10:
            print("Error: Ingrese una fecha con el formato DD/MM/AAAA o DD-MM-AAAA.")
            continue

        fecha = fecha.replace("-", "/")

        dia  = fecha[:2]
        mes  = fecha[3:5]
        year = fecha[-4:]

        if not (dia.isdigit() and mes.isdigit() and year.isdigit()):
            print("Error: La fecha debe contener solo numeros y separadores ( / o -).")
            continue

        try:
            date(int(year), int(mes), int(dia))
            return fecha 
        except ValueError:
            print("Error: La fecha ingresada no existe. Intente nuevamente.")