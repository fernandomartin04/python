#Practicando el while
import math
numero=int(input("Escriba un numero: "))
while numero<=0:
    print("Porfavor ingresa un numero positivo distinto de 0")
    numero=int(input("Vuelva a ingresar un numero: "))
print(f"El resultado de la raiz cuadrada es: {math.sqrt(numero):.2f}")

