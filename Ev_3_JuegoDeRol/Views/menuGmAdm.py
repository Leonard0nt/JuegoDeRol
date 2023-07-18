from Views.menuGm import *
from Controller.razaController import *

def menuGmADMEliminar():
    while True:
        print("-------Seleccione--------")
        print("1........Estado..........")
        print("2........Habilidad.......")
        print("3.......Equipamiento.....")
        print("4.........Raza...........")
        print("5.Volver")
        op2 = int(input())
        if op2 == 1:
            eliminarEstado()
        elif op2 == 2:
            eliminarHabilidad()
        elif op2 == 3:
            eliminarEquipamiento()
        elif op2 == 4:
            eliminarRaza()
        elif op2 == 5:
            break
        else:
            print("ingrese una opcion valida")
def menuGmADMAgregar():
    while True:
        print("-------Seleccione--------")
        print("1........Estado..........")
        print("2........Habilidad.......")
        print("3.......Equipamiento.....")
        print("4.........Raza...........")
        print("5.Volver")
        op2 = int(input())
        if op2 == 1:
            agregarEstado()
        elif op2 == 2:
            agregarHabilidad()
        elif op2 == 3:
            agregarEquipamiento()
        elif op2 == 4:
            agregarRaza()
        elif op2 == 5:
            break
        else:
            print("ingrese una opcion valida")

def menuADM():
    while True:
        print("1.Eliminar")
        print("2.agregar")
        print("3.volver")
        op = int(input("ingrese una opcion "))
        if op == 1:
            menuGmADMEliminar()
        elif op == 2:
            menuGmADMAgregar()
        elif op == 3:
            break
        else:
            print("ingrese una opcion valida")