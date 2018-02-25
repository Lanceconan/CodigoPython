import os
from math import floor
from math import ceil
import math

#METODOS DEFINIDOS
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def combinatoria(m, n):
    return factorial(m) / (factorial(n) * factorial(m - n))

def getMayor(a, b):
    if (a > b):
        mayor = a
    elif(a < b):
        mayor = b
    else:
        mayor = a
    return mayor

def convertirSegundos(segundos):
    horas = segundos / (60 * 60)
    minutos = (segundos / 60) % 60
    segundos = segundos % 60
    return horas, minutos, segundos

#INICIO PROGRAMA
os.system('cls')
print ("Operaciones Básicas")
print ("====================\n")

array = [2, "tres", True, ["uno", 10]]

a = int(input("ingresa primer numero: \n"))
b = int(input("ingresa segundo numero: \n"))

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
resto = a % b
potencia = pow(a,b)

mayor = (a > b)
menor = (a < b)
igual = True

if (a == b):
    igual = True
else:
    igual = False

print("SUMA: " + str(suma))
print("RESTA: " + str(resta))
print("MULTIPLICACION: " + str(multiplicacion))
print("DIVISION: " + str(division))
print("RESTO DIVISION: " + str(resto))
print("POTENCIA: " + str(potencia))
print("EL MAYOR ES: " + str(getMayor(a, b)))

print("\n\nPrimer numero mayor al segundo numero: " + str(mayor))
print("Primer numero menor al segundo numero: " + str(menor))
print("Primer numero igual al segundo numero: " + str(igual))

input("\n\nTecla para continuar.... \n")
os.system('cls')
print ("WHILE SUMATORIA PRIMEROS n NUMEROS")
print ("====================================\n")
n = int(input("ingresa n: \n"))

sumatoria = 0
contador = 0
while (contador <= n):   
   sumatoria = sumatoria + contador
   contador = contador + 1

print ("La suma es: " + str(sumatoria))

input("\n\nTecla para continuar.... \n")
os.system('cls')
print ("FOR PRODUCTORIA PRIMEROS n NUMEROS")
print ("====================================\n")
n = int(input("ingresa n: \n"))

productoria = 1
for i in range(1, n + 1):
    productoria *= i

print("La productoria de n es: " + str(productoria))

input("\n\nTecla para continuar.... \n")
os.system('cls')
print ("OPERACIONES REDONDEO")
print ("=========================\n")
entrada = float(input("ingresa numero decimal: \n"))

redondearBajo = floor(entrada)
redondearArriba = ceil(entrada)
redondear = round(entrada)

print("\n\nmetodo round: " + str(redondear))
print("metodo floor: " + str(redondearBajo))
print("metodo ceil: " + str(redondearArriba))

input("\n\nTecla para continuar.... \n")
os.system('cls')
print ("CONVERSION DE SEGUNDOS")
print ("=========================================\n")
numero = int(input("ingresa cantidad de segundos: \n"))

hora, minuto, segundo = convertirSegundos(numero)

print("\n\nhora: " + str(hora))
print("minuto: " + str(minuto))
print("segundo: " + str(segundo))

input("\n\nTecla para continuar.... \n")
os.system('cls')
print ("FACTORIAL y COMBINATORIA MEDIANTE FUNCION")
print ("=========================================\n")
numero = int(input("ingresa numero: \n"))

factorial = factorial(numero)
combinatorias = combinatoria(4, 3)

print ("La factorial es: " + str(factorial))
print ("La combinatoria es: " + str(combinatorias))