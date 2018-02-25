import os

#METODOS

def getConectionPostgres(host, database, usuario, password):
    return 0

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
        print("LEERA LA BASE DE DATOS")
        print("======================\n\n")

        input("\nTecla para continuar.... \n") 

    elif (opcion == 2):
        print("ESCRIBIRÁ NUEVO REGISTRO EN LA BASE")
        print("===================================\n\n")

        input("\nTecla para continuar.... \n") 

    elif (opcion == 3):
        print("EDITARA UN REGISTRO EN LA BASE DE DATOS")
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
        