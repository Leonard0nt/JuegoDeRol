import mysql.connector

from Models.conexionBDD import *
from Models.Equipamiento import *

def listarEquipamientos():
    try:
        connection = conex()
        cursor = connection.cursor()
        query = "SELECT * from equipamiento"
        cursor.execute(query)
        tuplas = cursor.fetchall()
        listaEquipamientos=[]
        for row in tuplas:
            equipamiento = Equipamiento()
            equipamiento.setNombreEquipamiento(row[1])
            equipamiento.setDescripcionEquipamiento(row[2])
            listaEquipamientos.append(equipamiento)

        close_connection(connection)
        return listaEquipamientos
    except (Exception, mysql.connector.Error) as error:
        exceptionE = "Error en la conexión a la BDD", error
        return exceptionE

def agregarEquipamiento():
    try:
        NvoNombre = input("Ingrese nombre del nuevo equipamiento ")
        NvoDescripcion = input("Ingrese descripcion para el nuevo equipamiento ")
        query = "INSERT INTO equipamiento (id_equipamiento, nombre_equipamiento, descripcion_equipamiento) VALUES(0,%s,%s)"

        connection = conex()
        cursor = connection.cursor()
        cursor.execute(query, (NvoNombre, NvoDescripcion))
        connection.commit()
        filas = cursor.rowcount
        if filas > 0:
            print("Nuevo equipamiento agregado")
        else:
            print("No se pudo agregar el nuevo equipamiento")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexión a la BDD", error
        return ExceptionE
def eliminarEquipamiento():
    nombre= (input("Ingrese el nombre del equipamiento a eliminar "),)
    try:
        query = "DELETE FROM equipamiento WHERE nombre_equipamiento = %s"
        connection = conex()
        cursor = connection.cursor()
        cursor.execute(query, nombre)
        connection.commit()
        print("equipamiento eliminado correctamente")
        close_connection()
    except (Exception, mysql.connector.Error) as error:
        ExceptionE = "Error en la conexion a la BDD", error
        return ExceptionE


