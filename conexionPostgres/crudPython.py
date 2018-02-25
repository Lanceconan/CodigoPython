#Instalar 'psycopg2' desde http://www.stickpeople.com/projects/python/win-psycopg/
#Crear la Base de Datos mediante script adjunto

import os
import psycopg2, psycopg2.extras

#METODOS

def getConectionPostgres(
    host, 
    database, 
    usuario, 
    password,
    port
): 
    stringConexion = "dbname = '" + database + "' user = '" + usuario + "' password = '" + password + "' port = " + port + "' host = '" + host + "'"        
    connexion = psycopg2.connect(stringConexion)
    return connexion

def leerBase():
    return 0

def editarBase(id):
    return 0

def eliminarBase(id):
    return 0

def crearRegistroBase():
    return 0

opcion = 0

while (opcion != 5):
    
    os.system('cls')
    print("CONEXION A BASE DE DATOS POSTGRES")
    print("================================\n")
    print("1. Leer Base de Datos")
    print("2. Escribir nuevo Registro")
    print("3. Editar Registro")
    print("4. Eliminar Registro")
    print("5. Salir")

    opcion = int(input("Ingrese Opcion: "))

    os.system('cls')    

    #opciones

    if(opcion == 1):
        print("LEERÁ LA BASE DE DATOS")
        print("======================\n\n")
        
        conexion = getConectionPostgres(
            'localhost', 
            'crudPython', 
            'postgres',
            'postgres',
            '1680')

        cur = conexion.cursor()
        cur.execute("SELECT * FROM persona")
        rows=cur.fetchall()
        print (rows)
        input("\nTecla para continuar.... \n") 

    elif (opcion == 2):
        print("ESCRIBIRÁ NUEVO REGISTRO EN LA BASE")
        print("===================================\n\n")

        input("\nTecla para continuar.... \n") 

    elif (opcion == 3):
        print("EDITARÁ UN REGISTRO EN LA BASE DE DATOS")
        print("======================================\n\n")

        input("\nTecla para continuar.... \n") 

    elif (opcion == 4):
        print("ELIMINARÁ UN REGISTRO")
        print("===================\n\n")

        input("\nTecla para continuar.... \n") 
        
    elif (opcion == 5):
        print("USTED SALIÓ")
        break
    
    else:
        print("OPCION NO VÁLIDA") 
        input("\nTecla para continuar.... \n")       
        