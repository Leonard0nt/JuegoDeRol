import mysql.connector

from Models.conexionBDD import *
from Models.Estado import *

def listarEstados():
    try:
        connection = conex()
        cursor = connection.cursor()
        query = "SELECT * from estados"
        cursor.execute(query)
        tuplas = cursor.fetchall()
        listaEstados=[]
        for row in tuplas:
            estado = Estado()
            estado.setNombreEstado(row[1])
            estado.setDescripcionEstado(row[2])
            listaEstados.append(estado)

        close_connection(connection)
        return listaEstados
    except (Exception, mysql.connector.Error) as error:
        exceptionE = "Error en la conexión a la BDD", error
        return exceptionE

def agregarEstado():
    try:
        NvoNombre = input("Ingrese nombre del nuevo estado ")
        NvoDescripcion = input("Ingrese descripcion para el nuevo estado ")
        query = "INSERT INTO estados (id_estado, nombre_estado, descripcion_estado) VALUES(0,%s,%s)"

        connection = conex()
        cursor = connection.cursor()
        cursor.execute(query, (NvoNombre, NvoDescripcion))
        connection.commit()
        filas = cursor.rowcount
        if filas > 0:
            print("Nuevo estado agregado")
        else:
            print("No se pudo agregar el nuevo estado")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexión a la BDD", error
        return ExceptionE

def eliminarEstado():
    nombre= (input("Ingrese el nombre de la habilidad a eliminar "),)
    try:
        query = "DELETE FROM estados WHERE nombre_estado = %s"
        connection = conex()
        cursor = connection.cursor()
        cursor.execute(query, nombre)
        connection.commit()
        print("estado eliminado correctamente")
        close_connection()
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexion a la BDD", error
        return ExceptionE
