from Models.getById import *
from Controller.jugadorController import *

def menuJg(id_Jugador):
    while True:
        print("-----Menu Jg------")
        print("1.Agregar Personaje")
        print("2.Eliminar Personaje")
        print("3.Editar Equipamiento")
        print("4.Salir")
        op = int(input())
        if op == 1:
            agregarPersonajeJugador(id_Jugador)
        elif op == 2:
            eliminarPersonaje(id_Jugador)
        elif op == 3:
            nombre = getNombreByIdNombrePersonaje(getIdPersonaje(id_Jugador))
            equipamiento = getIdByNombreEquipamiento()
            cambiarEquipamientoPersonaje(nombre, equipamiento)
        elif op == 4:
            break
        else:
            print("ingrese una opcion valida")









