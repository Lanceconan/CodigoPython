import os
from os import scandir, getcwd
    
def sortNumerosEntrada(a):
    return sorted(a)

def leerArchivo():
    archivoEntrada = open('Entrada.txt', 'r') 
    lista = []
    
    for linea in archivoEntrada.readlines():         
        lista.append(int(linea))
    
    print (str(lista))
    
    archivoEntrada.close()
    return lista

def escribirArchivo(lista):
    archivoSalida = open('Salida.txt', 'w') 
    for i in range(0, len(lista)):
        archivoSalida.write(str(lista[i]) + "\n")
    archivoSalida.close()
    return lista

arrayPrueba = [1,2,12,-3,22]

os.system('cls')
print("OPERACIÓN DE ARREGLO DE NUMEROS EN UN ARCHIVO DE TEXTO Y ESCRIBINDO A LA SALIDA LOS NUMEROS ORDENADOS")
print("TEST DE METODO ORDENAMIENTO ORIGINAL" + str(arrayPrueba))
print("TEST DE METODO DE ORDENAMIENTO ORDENADO: " + str(sortNumerosEntrada(arrayPrueba)))

input("\n\nTecla para continuar.... \n")
os.system('cls')

listaArchivoEntrada = sortNumerosEntrada(leerArchivo())
escribirArchivo(listaArchivoEntrada)

print("SE ESCRIBIÓ: " + str(listaArchivoEntrada))