#Ejercicio 3 de if
#Un programa que pida 3 numeros y determine el mayor
print("Escribe 3 números y te diré el mayor.")

n1=int(input("Introduce el primer número: "))
n2=int(input("Introduce el segundo número: "))
n3=int(input("Introduce el tercer número: "))

if n1==n2 and n1==n3:
    print("Todos los número son iguales")
elif n1>=n2 and n1>=n3:
    print(f"El número mayor es: {n1}")
elif n2>=n1 and n2>=n3:
    print(f"El número mayor es: {n2}")
elif n3>=n1 and n3>=n2:
    print(f"El número mayor es: {n3}")
elif n1==n2 and n1==n3:
    print("Todos los número son iguales")