# Instalar 'psycopg2' desde http://www.stickpeople.com/projects/python/win-psycopg/ en Windows
# https://www.fullstackpython.com/blog/postgresql-python-3-psycopg2-ubuntu-1604.html para Linux
#
#Crear la Base de Datos mediante script adjunto

import os
import psycopg2, psycopg2.extras
import Persona

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

def leerBase(conexion, registros):
    cur = conexion.cursor()
    cur.execute("SELECT * FROM persona LIMIT " + str(registros))
    
    for row in cur:
        print("\nID: " + str(row[0]) + "\nNOMBRE: " + str(row[1]) + "\nApellido Paterno: " + str(row[2]) +  "\nApellido Materno: " + str(row[3]) + "\nRut: " + str(row[4]) +  "\nObservación: " + str(row[5]))
    
    cur.close()
    conexion.close()
    

def editarBase(conexion, idPersona):
    cur = conexion.cursor()
    queryEditar = "UPDATE persona SET per_nombre = , per_apellidomaterno = , per_apellidopaterno = , per_rut character = , per_observacion =  WHERE per_id = "  + idPersona 
    cur.execute(queryEditar)
    return 0

def eliminarBase(conexion, idPersona):
    cur = conexion.cursor()
    queryEditar = "DELETE FROM persona WHERE per_id = " + idPersona
    cur.execute(queryEditar)
    return 0

def crearRegistroBase(conexion, persona):
    persona.setIdPersona(getNextId(conexion))
    
    cur = conexion.cursor()
    queryCrear = "INSERT INTO persona (per_id, per_nombre, per_apellidomaterno, per_apellidopaterno, per_rut, per_observacion) VALUES (" + persona.getIdPersona() + "::bigint, '" + persona.getNombre() +  "'::character varying,'" + persona.getApellidoPaterno() + "'::character varying,'" + persona.getApellidoMaterno() + "'::character varying,'" + persona.getRut() + "'::character varying,'" + persona.getObservacion() + "'::character varying);"
    print (queryCrear)
    cur.execute(queryCrear)    
    conexion.commit()
    cur.close()
    conexion.close()

def getNextId(conexion):
    cur =  conexion.cursor()
    cur.execute("SELECT MAX(per_id) FROM persona")
    for row in cur:
        retorno = str(int(row[0]) + 1)
    
    return retorno
    
# INICIO DE PROGRAMA

at = Persona.Persona(1,'as', 'as', 'as', 'as', 'as')
opcion = 0

conexion = getConectionPostgres(
            'localhost', 
            'crudPython', 
            'postgres',
            'postgres',
            '1680')

personas = []

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
    
    #OPCIONES

    if(opcion == 1):
        print("LEERÁ LA BASE DE DATOS")
        print("======================\n\n")
        registros = int(input("Ingrese cantidad de registros a mirar: "))
        
        leerBase(conexion, registros)

        input("\nTecla para continuar.... \n") 

    elif (opcion == 2):
        print("ESCRIBIRÁ NUEVO REGISTRO EN LA BASE")
        print("===================================\n\n")
        nombre = str(input("Ingrese nombre: ")).upper()        
        apellidoPaterno = str(input("Ingrese apellido Paterno: ")).upper()
        apellidoMaterno = str(input("Ingrese apellido Materno: ")).upper()
        rut = str(input("Ingrese rut: ")).upper()
        observacion = str(input("Ingrese observacion: ")).upper()

        nuevaPersona = Persona.Persona(0, nombre, apellidoPaterno, apellidoMaterno, rut, observacion)
        crearRegistroBase(conexion, nuevaPersona)

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

# FIN DE PROGRAMA