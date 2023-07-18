from Controller.habilidadController import *
from Controller.equipamientoController import *
from Controller.personajeController import *
from Controller.jugadorController import *
from Views.menuGm import *
from Views.menuJg import *


def mainMenu():
    while True:
        print("---------Menu----------")
        print("1.-----Ingresar--------")
        print("2.----Registrarse------")
        print("3.------Salir..........")
        op = int(input())
        if op == 1:
            id_jugador = identificarJugador()
            print(identificarTipo(id_jugador))
            if identificarTipo(id_jugador) == "Gm":
                menuGm(id_jugador)
            else:
                menuJg(id_jugador)
        elif op == 2:
            agregarJugador()
        elif op == 3:
            break
        else:
            print("ingrese una opcion valida")

mainMenu()





