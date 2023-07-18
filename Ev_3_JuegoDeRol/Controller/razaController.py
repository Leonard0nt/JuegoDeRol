import mysql.connector

from Models.conexionBDD import *
from Models.Raza import *

def listarRazas():
    try:
        connection = conex()
        cursor = connection.cursor()
        query = "SELECT * from razas"
        cursor.execute(query)
        tuplas = cursor.fetchall()
        listaRazas=[]
        for row in tuplas:
            raza = Raza()
            raza.setNombreRaza(row[1])
            raza.setDescripcionRaza(row[2])
            listaRazas.append(raza)

        close_connection(connection)
        return listaRazas
    except (Exception, mysql.connector.Error) as error:
        exceptionE = "Error en la conexión a la BDD", error
        return exceptionE

def agregarRaza():
    try:
        NvoNombre = input("Ingrese nombre de la nueva raza ")
        NvoDescripcion = input("Ingrese descripcion para la nueva raza ")
        query = "INSERT INTO razas (id_raza, nombre_raza, descripcion_raza) VALUES(0,%s,%s)"

        connection = conex()
        cursor = connection.cursor()
        cursor.execute(query, (NvoNombre, NvoDescripcion))
        connection.commit()
        filas = cursor.rowcount
        if filas > 0:
            print("Nueva raza agregada")
        else:
            print("No se pudo agregar la nueva raza")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexión a la BDD", error
        return ExceptionE

def eliminarRaza():
    nombre= (input("Ingrese el nombre de la raza a eliminar "),)
    try:
        query = "DELETE FROM razas WHERE nombre_raza = %s"
        connection = conex()
        cursor = connection.cursor()
        cursor.execute(query, nombre)
        connection.commit()
        print("raza eliminada correctamente")
        close_connection()
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexion a la BDD", error
        return ExceptionE
