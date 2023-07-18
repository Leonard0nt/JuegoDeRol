import mysql.connector

from Models.conexionBDD import *
from Models.Habilidad import *

def listarHabilidades():
    try:
        connection = conex()
        cursor = connection.cursor()
        query = "SELECT * from habilidades"
        cursor.execute(query)
        tuplas = cursor.fetchall()
        listaHabilidades=[]
        for row in tuplas:
            habilidad = Habilidad()
            habilidad.setNombreHabilidad(row[1])
            habilidad.setDescripcionHabilidad(row[2])
            listaHabilidades.append(habilidad)

        close_connection(connection)
        return listaHabilidades
    except (Exception, mysql.connector.Error) as error:
        exceptionE = "Error en la conexión a la BDD", error
        return exceptionE

def agregarHabilidad():
    try:
        NvoNombre = input("Ingrese nombre de la nueva habilidad ")
        NvoDescripcion = input("Ingrese descripcion para la nueva habilidad ")
        query = "INSERT INTO habilidades (id_habilidad, nombre_habilidad, descripcion_habilidad) VALUES(0,%s,%s)"

        connection = conex()
        cursor = connection.cursor()
        cursor.execute(query, (NvoNombre, NvoDescripcion))
        connection.commit()
        filas = cursor.rowcount
        if filas > 0:
            print("Nueva habilidad agregada")
        else:
            print("No se pudo agregar la habilidad")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexión a la BDD", error
        return ExceptionE

def eliminarHabilidad():
    nombre= (input("Ingrese el nombre de la habilidad a eliminar "),)
    try:
        query = "DELETE FROM habilidades WHERE nombre_habilidad = %s"
        connection = conex()
        cursor = connection.cursor()
        cursor.execute(query, nombre)
        connection.commit()
        print("habilidad eliminada correctamente")
        close_connection()
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexion a la BDD", error
        return ExceptionE

