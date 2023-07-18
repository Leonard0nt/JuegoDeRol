from Models.conexionBDD import *

from Controller.habilidadController import *
from Controller.estadoController import *
from Controller.equipamientoController import*
from Controller.razaController import *
from Controller.personajeController import *


"""
Metodos para obtener nombre del atributo mediante el id
"""
def getNombreByIdEquipamiento(id):
    try:
        sql = "SELECT nombre_equipamiento FROM equipamiento WHERE id_equipamiento = %s"
        connection = conex()
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        aux = cursor.fetchone()
        aux = aux[0]

        return aux
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexion a la BDD", error
        return ExceptionE

def getNombreByIdRaza(id):
    try:
        sql = "SELECT nombre_raza FROM razas WHERE id_raza = %s"
        connection = conex()
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        aux = cursor.fetchone()
        aux = aux[0]
        return aux
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexion a la BDD", error
        return ExceptionE

def getNombreByIdEstado(id):
    try:
        sql = "SELECT nombre_estado FROM estados WHERE id_estado = %s"
        connection = conex()
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        aux = cursor.fetchone()
        aux = aux[0]
        return aux
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexion a la BDD", error
        return ExceptionE
def getNombreByIdNombrePersonaje(id):
    try:
        sql = "SELECT nombre_personaje FROM personaje WHERE id_personaje = %s"
        connection = conex()
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        aux = cursor.fetchone()
        aux = aux[0]
        return aux
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexion a la BDD", error
        return ExceptionE

def getNombreByIdHabilidad(id):
    try:
        sql = "SELECT nombre_habilidad FROM habilidades WHERE id_habilidad = %s"
        connection = conex()
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        aux = cursor.fetchone()
        aux = aux[0]
        return aux
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexion a la BDD", error
        return ExceptionE


""" 
Metodos para obtener id mediante nombre
"""

def getIdByNombreEquipamiento():
    print("Los equipamientos disponibles son los siguientes")
    printEquipamiento()
    try:
        nombre = input("ingrese nombre equipamiento: ")
        sql = "SELECT id_equipamiento FROM equipamiento WHERE nombre_equipamiento = %s"
        connection = conex()
        cursor = connection.cursor()
        cursor.execute(sql, (nombre,))
        aux = cursor.fetchone()
        if aux is None:
            print("el equipamiento no existe en sistema ingrese una valida")
            return getIdByNombreEquipamiento()
        else:
            return aux[0]
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexion a la BDD", error
        return ExceptionE


def getIdByNombreRaza():
    print("Las razas disponibles son las siguientes")
    printRaza()
    try:
        nombre = input("ingrese nombre raza: ")
        sql = "SELECT id_raza FROM razas WHERE nombre_raza = %s"
        connection = conex()
        cursor = connection.cursor()
        cursor.execute(sql, (nombre,))
        aux = cursor.fetchone()
        if aux is None:
            print("La raza no existe en sistema ingrese una valida")
            return getIdByNombreRaza()
        else:
            return aux[0]
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexion a la BDD", error
        return ExceptionE

def getIdByNombreEstado():
    print("Los estados disponibles son los siguientes")
    printEstado()
    try:
        nombre = input("ingrese nombre estado: ")
        sql = "SELECT id_estado FROM estados WHERE nombre_estado = %s"
        connection = conex()
        cursor = connection.cursor()
        cursor.execute(sql, (nombre,))
        aux = cursor.fetchone()
        if aux is None:
            print("el estado no existe en sistema ingrese una valida")
            return getIdByNombreEstado()
        else:
            return aux[0]
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexion a la BDD", error
        return ExceptionE


def getIdByNombreHabilidad():
    print("Las habilidades actuales son las siguientes")
    printHabilidades()
    try:
        nombre = input("ingrese nombre habilidad: ")
        sql = "SELECT id_habilidad FROM habilidades WHERE nombre_habilidad = %s"
        connection = conex()
        cursor = connection.cursor()
        cursor.execute(sql, (nombre,))
        aux = cursor.fetchone()
        if aux is None:
            print("La habilidad no existe en sistema ingrese una valida")
            return getIdByNombreHabilidad()
        else:
            return aux[0]
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexion a la BDD", error
        return ExceptionE


def getIdByNombrePersonaje():
    try:
        nombre = input("ingrese nombre personaje: ")
        sql = "SELECT id_personaje FROM personaje WHERE nombre_personaje = %s"
        connection = conex()
        cursor = connection.cursor()
        cursor.execute(sql, (nombre,))
        aux = cursor.fetchone()
        if aux is None:
            print("No existe ningun personaje con este nombre")
            return getIdByNombrePersonaje()
        else:
            return aux[0]
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexion a la BDD", error
        return ExceptionE

def getIdByNombrePersonaje2(nombre):
    try:
        sql = "SELECT id_personaje FROM personaje WHERE nombre_personaje = %s"
        connection = conex()
        cursor = connection.cursor()
        cursor.execute(sql, (nombre,))
        aux = cursor.fetchone()
        return aux[0]
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexion a la BDD", error
        return ExceptionE

def revisarInNombres():
    nombre = input("ingrese nombre del nuevo personaje: ")
    try:
        sql = "SELECT nombre_personaje FROM personaje"
        connection = conex()
        cursor = connection.cursor()
        cursor.execute(sql)
        tupla = cursor.fetchall()
        tupla = [x[0] for x in tupla]
        if nombre in tupla:
            print("el nombre ingresado ya se encuentra registrado ingrese uno distinto")
            return revisarInNombres()
        else:
            return nombre

    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexion a la BDD", error
        return ExceptionE

"""
Metodos print para las caracterisitcas de personaje
"""


def printHabilidades():
    miListaHabilidades = listarHabilidades()
    for habilidad in miListaHabilidades:
        print(habilidad.toString())


def printEquipamiento():
    miListaEquipamientos = listarEquipamientos()
    for equipamiento in miListaEquipamientos:
        print(equipamiento.toString())


def printEstado():
    miListaEstado = listarEstados()
    for estado in miListaEstado:
        print(estado.toString())


def printRaza():
    miListaRaza = listarRazas()
    for raza in miListaRaza:
        print(raza.toString())

