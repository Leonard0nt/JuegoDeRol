import mysql.connector

from Models.getById import *
from Models.Personaje import *
from Models.conexionBDD import *



def listarPersonajes():
    try:
        connection = conex()
        cursor = connection.cursor()
        query = "SELECT * from personaje"
        cursor.execute(query)
        tuplas = cursor.fetchall()
        listaPersonajes=[]
        for row in tuplas:
            personaje = Personaje()
            personaje.setNombre(row[1])
            personaje.setHabilidad(row[2])
            personaje.setEquipamiento(row[3])
            personaje.setEstado(row[4])
            personaje.setRaza(row[5])
            personaje.setNivel(row[6])
            listaPersonajes.append(personaje)

        close_connection(connection)
        return listaPersonajes
    except (Exception, mysql.connector.Error) as error:
        exceptionE = "Error en la conexión a la BDD", error
        return exceptionE

def agregarPersonaje():
    try:
        NvoNombre = revisarInNombres()
        NvaHabilidad = getIdByNombreHabilidad()
        NvoEquipamiento = getIdByNombreEquipamiento()
        NvaRaza = getIdByNombreRaza()
        query = "INSERT INTO personaje (id_personaje, nombre_personaje, habilidad_fk, equipamientos_fk, estado_fk, raza_fk, nivel) VALUES(0,%s,%s,%s,1,%s,1)"

        connection = conex()
        cursor = connection.cursor()
        cursor.execute(query, (NvoNombre, NvaHabilidad, NvoEquipamiento, NvaRaza))
        connection.commit()

        filas = cursor.rowcount
        if filas > 0:
            print("Nuevo personaje agregado")
            return getIdByNombrePersonaje2(NvoNombre)
        else:
            print("No se pudo agregar el personaje")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexión a la BDD", error
        return ExceptionE


def eliminarPersonaje(id):
    try:
        query = "DELETE FROM personaje WHERE id_personaje = %s"
        connection = conex()
        cursor = connection.cursor()
        cursor.execute(query, (id,))
        connection.commit()
        print("personaje eliminado correctamente")
        try:
            query = "UPDATE jugador SET personajes_fk = 0 WHERE personajes_fk = %s"
            connection = conex()
            cursor = connection.cursor()
            cursor.execute(query, (id,))
            connection.commit()
            close_connection()
        except (Exception, mysql.connector.Error) as error:
            ExceptionE = "Error en la conexion a la BDD", error
            return ExceptionE
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexion a la BDD", error
        return ExceptionE

"""
Metodos exclusivos de Gm
"""
def cambiarEstadoPersonaje(nombre,estado):
    if estado != None :
        try:
            query = "UPDATE personaje SET estado_fk = %s WHERE nombre_personaje = %s"
            connection = conex()
            cursor = connection.cursor()
            cursor.execute(query, (estado, nombre))
            connection.commit()
            print("estado cambiado correctamente")
            close_connection()
        except (Exception, mysql.connector.Error) as error:
            ExceptionE = "Error en la conexion a la BDD", error
            return ExceptionE
    else:
        print("el estado ingresado no existe en sistema de momento")
        return cambiarEstadoPersonaje(nombre)

def cambiarEquipamientoPersonaje(nombre,equipamiento):
        try:
            query = "UPDATE personaje SET equipamientos_fk = %s WHERE nombre_personaje = %s"
            connection = conex()
            cursor = connection.cursor()
            cursor.execute(query, (equipamiento, nombre))
            connection.commit()
            print("equipo cambiado correctamente")
            close_connection()
        except (Exception, mysql.connector.Error) as error:
            ExceptionE = "Error en la conexion a la BDD", error
            return ExceptionE


def cambiarNivelPersonaje(nombre):
    nvoNivel = int(input("Ingrese nuevo nivel "))
    if nvoNivel > 0 :
        try:
            query = "UPDATE personaje SET nivel = %s WHERE nombre_personaje = %s"
            connection = conex()
            cursor = connection.cursor()
            cursor.execute(query, (nvoNivel, nombre))
            connection.commit()
            print("nivel cambiado correctamente")
            close_connection()
        except (Exception, mysql.connector.Error) as error:
            ExceptionE = "Error en la conexion a la BDD", error
            return ExceptionE
    else:
        print("el nivel debe ser mayor o igual a 1")
        return cambiarNivelPersonaje(nombre)

def eliminarPersonajeGm():
    nombre = (input("Ingrese el nombre del personaje a eliminar "),)
    try:
        query = "DELETE FROM personaje WHERE nombre_personaje = %s"
        connection = conex()
        cursor = connection.cursor()
        cursor.execute(query, nombre)
        connection.commit()
        filas = cursor.rowcount
        if filas > 1:
            print("personaje eliminado correctamente")
        else:
            print("el personaje no existe")
        close_connection()
        try:
            query = "UPDATE jugador SET personajes_fk = 0 WHERE personajes_fk = (SELECT id_personaje FROM personaje WHERE nombre_personaje = %s)"
            connection = conex()
            cursor = connection.cursor()
            cursor.execute(query, nombre)
            connection.commit()
            close_connection()
        except (Exception, mysql.connector.Error) as error:
            ExceptionE = "Error en la conexion a la BDD", error
            return ExceptionE
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexion a la BDD", error
        return ExceptionE


