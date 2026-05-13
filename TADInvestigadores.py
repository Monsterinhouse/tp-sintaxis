from datetime import date

### FUNCIONES DE CARGA DE INVESTIGADORES ###
investigador = ["","",0,"",0,""]

def crearInvestigador():
    #crea un investigador vacio
    investigador = ["","",0,"",0,""]
    return investigador

def cargarInvestigador(investigador,nom,ape,leg,fecha,lab,area):
    #carga los datos de un nuevo investigador
    #[Nombre,Apellido,Legajo,Fecha de ingreso, Numero de lab, Area]
    investigador[0] = nom
    investigador[1] = ape
    investigador[2] = leg
    investigador[3] = fecha
    investigador[4] = lab
    investigador[5] = area

def sumarInvestigador (lista, investigador):
    lista.append(investigador)

def asignarInvestigador(investigador1,investigador2):
    #copia los datos del investigador1 al investigador2
    investigador1[0] = investigador2[0]
    investigador1[1] = investigador2[1]
    investigador1[2] = investigador2[2]
    investigador1[3] = investigador2[3]
    investigador1[4] = investigador2[4]
    investigador1[5] = investigador2[5]

### FUNCIONES DE VISTA ###

def verNombre(investigador):
    #retorna el nombre del investigador
    return investigador[0]

def verApellido(investigador):
    return investigador[1]

def verLegajo(investigador):
    return investigador[2]

def verFecha(investigador):
    return investigador[3]

def verLaboratorio(investigador):
    return investigador[4]

def verArea(investigador):
    return investigador[5]


### FUNCIONES DE MODIFICACION ###
def modNombre(investigador,nuevonomb):
    #modifica el nombre del investigador
    investigador[0]= nuevonomb

def modApellido(investigador,nuevoapellido):
    investigador[1]= nuevoapellido

def modLegajo(investigador,nuevolegajo):
    investigador[2]= nuevolegajo

def modFecha(investigador,nuevafecha):
    investigador[3]= nuevafecha

def modLab(investigador,nuevolab):
    investigador[4] = nuevolab

def modArea(investigador,nuevoarea):
    investigador[5]= nuevoarea

### FUNCIONES DE VERIFICACION

def esVacia(lista) :
    return len(lista) == 0

### FUNCIONES DE AYUDA ###
def eliminarInvestigador(lista,inv):
    lista.remove(inv)

def recuperarInvestigador(lista,investigador):
    return lista[investigador]

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

def asignacionMasiva (yearInvestigadores, areaCambio, listaInvestigadores) :
    for i in range(len(listaInvestigadores)) :
        year = verFecha(recuperarInvestigador(listaInvestigadores,i))
        if (year[-4:] == yearInvestigadores) :
            modArea(i,areaCambio)


### VERIFICACIONES DE INPUTS ###

def verificarInputStr(mensajeInput) :
        while True:
            valor = input(mensajeInput)
            if (valor.isdigit()) :
                print ("Error: No se permiten Numeros. Ingrese caracteres validos")
            elif len(valor.strip()) == 0 :
                print ("Error: El campo no puede estar vacio")
            else :
                return valor

def verificarInputInt(mensajeInput) :
        while True:
            valor = input(mensajeInput)
            if (valor.isalpha()) :
                print ("Error: No se permiten Letras. Ingrese caracteres validos")
            elif len(valor.strip()) == 0 :
                print ("Error: El campo no puede estar vacio")
            else :
                return valor

def verificarLegajo (mensajeInput, listaInvestigadores) :
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
                
def niam () :
    print ("ñam")