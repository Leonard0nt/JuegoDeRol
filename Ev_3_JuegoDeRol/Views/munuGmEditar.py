from Controller.personajeController import *
from Views.menuGm import *

def menuGmEditar():
    nombre = input("ingrese nombre del personaje que desea editar ")
    while True:
        print("-------Seleccione--------")
        print("1........Estado..........")
        print("2........Nivel...........")
        print("3.......Equipamiento.....")
        print("4.Volver")
        op2 = int(input())
        if op2 == 1:
            cambiarEstadoPersonaje(nombre, getIdByNombreEstado())
        elif op2 == 2:
            cambiarNivelPersonaje(nombre)
        elif op2 == 3:
            cambiarEquipamientoPersonaje(nombre, getIdByNombreEquipamiento())
        elif op2 == 4:
            break
        else:
            print("ingrese una opcion valida")
