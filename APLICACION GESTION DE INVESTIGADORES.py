from TADInvestigadores import*
from datetime import date
from datetime import time

x=0

while (x==0):
    print ("##### MENU DE OPCIONES ##### \n")
    print("[1]:Para cargar nuevo investigador:")
    print("[2]:Para ver informacion de investigador:")
    print("[3]:Para modificar investigador:")
    print("[4]:Para eliminar investigador:")
    print("[5]:Para una lista detallade de todos los investigadores:")
    print("[6]:Cambiar area de investigacion:")
    print("[7]:Eliminar investigadores con antiguedad mayor a 30 años(Jubilacion):")
    print("[8]:Generar cola de investigadores de un area especifica:")
    opcion=int(input("Ingrese una opcion:"))
