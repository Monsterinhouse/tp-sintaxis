
investigador = ["","",0,0,0,""]

def crearinvestigador():
    #crea un investigador vacio
    investigador = ["","",0,0,0,""]
    return investigador

def cargarinvestigador(investigador,nom,ape,leg,fecha,lab,area):
    #carga los datos de un nuevo investigador
    #[Nombre,Apellido,Legajo,Fecha de ingreso, Numero de lab, Area]
    investigador[0]= nom
    investigador[1]= ape
    investigador[2]=leg
    investigador[3]=fecha
    investigador[4]=lab
    investigador[5]=area

def asignarinvestigador(investigador1,investigador2):
    #copia los datos del investigador1 al investigador2
    investigador1[0]= investigador2[0]
    investigador1[1]= investigador2[1]
    investigador1[2]= investigador2[2]
    investigador1[3]= investigador2[3]
    investigador1[4]= investigador2[4]
    investigador1[5]= investigador2[5]

def vernombre(investigador):
    #retorna el nombre del investigador
    return investigador[0]

def verapellido(investigador):
    return investigador[1]

def verlegajo(investigador):
    return investigador[2]

def verfecha(investigador):
    return investigador[3]

def verlaboratorio(investigador):
    return investigador[4]

def verarea(investigador):
    return investigador[5]

def modnombre(investigador,nuevonomb):
    #modifica el nombre del investigador
    investigador[0]= nuevonomb

def modapellido(investigador,nuevoapellido):
    investigador[1]= nuevoapellido

def modlegajo(investigador,nuevolegajo):
    investigador[2]= nuevolegajo

def modfecha(investigador,nuevafecha):
    investigador[3]= nuevafecha

def modlab(investigador,nuevolab):
    investigador[4] = nuevolab

def modarea(investigador,nuevoarea):
    investigador[5]= nuevoarea
