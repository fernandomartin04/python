#Ejercicio 2 de if
#Pedir dos números y obtener cual es par o si los dos lo son
#Para ello lo haré con el módulo %(el resto de la division)
print("Ingresa dos números y adivinaré cuá o cuáles es par")
numero1=int(input("Ingresa el primer numero: "))
numero2=int(input("Ingresa el segundo numero: "))

if numero1%2==0 and numero2%2==0:
    print("Los dos números son pares")
elif numero1%2==0 and numero2%2!=0:
    print("El primer número es par, el segundo no")
elif numero1%2!=0 and numero2%2==0:
    print("El segundo número es par, el primero no")
else:
    print("Ninguno de los números es par")
