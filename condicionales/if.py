#Uso del condicional if

dato=int(input("Introduce un número: "))

if dato>0:
    print(f"El número {dato} es positivo")
elif dato==0:
    print("El número es 0")
else:
    print("El número es negativo")
