import mysql.connector

from Controller.personajeController import *
from Models.conexionBDD import *
from Models.Jugador import *

def agregarJugador():
    try:
        NvoNombre = input("Ingrese nombre  de jugador ")
        NvoPassword = input("Ingrese password ")
        NvoTipo = input("Ingrese tipo de jugador (jugador o Gm) ")
        query = "INSERT INTO jugador (id_jugador, nombre_jugador, password, tipo) VALUES(0,%s,%s,%s)"

        if comprobarNombreJugador(NvoNombre) == False:
            return agregarJugador()

        connection = conex()
        cursor = connection.cursor()
        cursor.execute(query, (NvoNombre, NvoPassword, NvoTipo))
        connection.commit()
        filas = cursor.rowcount
        if filas > 0:
            print("Nuevo jugador agregado")
        else:
            print("No se pudo agregar al nuevo jugador")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexión a la BDD", error
        return ExceptionE

def identificarJugador():
    try:
        nombre = input("ingrese nombre de jugador ")
        password = input("ingrese password ")
        connection = conex()
        cursor = connection.cursor()
        query = "SELECT * from jugador"
        cursor.execute(query)
        tuplas = cursor.fetchall()
        for row in tuplas:
            if nombre == row[1] and password == row[2]:
                return row[0]
        print("datos incorrectos")
        return identificarJugador()
    except (Exception, mysql.connector.Error) as error:
        exceptionE = "Error en la conexión a la BDD", error
        return exceptionE

def comprobarNombreJugador(nombre):
    try:
        connection = conex()
        cursor = connection.cursor()
        query = "SELECT nombre_jugador from jugador"
        cursor.execute(query)
        tuplas = cursor.fetchall()
        for row in tuplas:
            if nombre == row[0]:
                print("El jugador ya existe")
                return False
        return True
    except (Exception, mysql.connector.Error) as error:
        exceptionE = "Error en la conexión a la BDD", error
        return exceptionE

def agregarPersonajeJugador(idJugador):
    try:
        idPersonaje = agregarPersonaje()
        connection = conex()
        cursor = connection.cursor()
        query = "UPDATE jugador SET personajes_fk = %s WHERE id_jugador = %s "
        cursor.execute(query, (idPersonaje, idJugador))
        connection.commit()

    except (Exception, mysql.connector.Error) as error:
        exceptionE = "Error en la conexión a la BDD", error
        return exceptionE

def eliminarPersonajeJugador(id):
    try:
        connection = conex()
        cursor = connection.cursor()
        query = "SELECT personajes_fk FROM jugador WHERE id_jugador = %s"
        cursor.execute(query, (id,))
        idPersonaje = cursor.fetchone()
        if idPersonaje[0] != 0:
            eliminarPersonaje(idPersonaje[0])
        else:
            print("el jugador no posee personaje a eliminar")

    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexión a la BDD", error
        return ExceptionE


def identificarTipo(id):
    try:
        connection = conex()
        cursor = connection.cursor()
        query = "SELECT tipo FROM jugador WHERE id_jugador = %s"
        cursor.execute(query, (id,))
        tipo = cursor.fetchone()
        return tipo[0]

    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexión a la BDD", error
        return ExceptionE

def getIdPersonaje(id):
    try:
        connection = conex()
        cursor = connection.cursor()
        query = "SELECT personajes_fk FROM jugador WHERE id_jugador = %s"
        cursor.execute(query, (id,))
        tipo = cursor.fetchone()
        return tipo[0]

    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexión a la BDD", error
        return ExceptionE