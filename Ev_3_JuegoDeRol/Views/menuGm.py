from Models.getById import *
from Controller.equipamientoController import *
from Controller.estadoController import *
from Controller.habilidadController import *
from Controller.razaController import *
from Controller.personajeController import *
from Controller.jugadorController import *
from Views.menuGmAdm import *
from Views.munuGmEditar import *
from Models.getById import *
def menuGm(id_Jugador):
    while True:
        print("-----Menu Gm------")
        print("1.Agregar Personaje")
        print("2.Eliminar Personaje")
        print("3.Editar Personajes")
        print("4.Aministrar caracteristicas")
        print("5.Mostrar personajes")
        print("6.Salir")
        op = int(input())
        if op == 1:
            agregarPersonajeJugador(id_Jugador)
        elif op == 2:
            eliminarPersonajeGm()
        elif op == 3:
            menuGmEditar()
        elif op == 4:
            menuADM()
        elif op == 5:
            miListaPj = listarPersonajes()
            for personaje in miListaPj:
                print(personaje.toString())
        elif op == 6:
            break
        else:
            print("ingrese una opcion valida")














