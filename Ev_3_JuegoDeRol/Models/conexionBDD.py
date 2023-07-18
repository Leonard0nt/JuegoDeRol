import mysql.connector


def conex():
    try:
        myConn = mysql.connector.connect(host="localHost", user="root", passwd="", db="juegoderol")
    except:
        print("Error")

    return myConn

def close_connection(connection):
    if connection:
        connection.close()
