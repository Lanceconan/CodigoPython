import os
from math import floor
from math import ceil
import math
os.system('cls')

print ("Operaciones Básicas")
print ("====================\n")

array = [2, "tres", True, ["uno", 10]]

a = int(input("ingresa primer numero: \n"))
b = int(input("ingresa segundo numero: \n"))

suma = a + b
resta = a - b
multiplicacion = a * b
division = a // b

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
print ("OPERACIONES MAS AVANZADAS")
print ("====================================\n")
input = float(input("ingresa numero decimal: \n"))

redondearBajo = floor(input)
redondearArriba = ceil(input)
redondear = round(input)

print("\n\nmetodo round: " + str(redondear))
print("metodo floor: " + str(redondearBajo))
print("metodo ceil: " + str(redondearArriba))