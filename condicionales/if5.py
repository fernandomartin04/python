#Ejercicio 5 if
#Crea un programa que simule un cajero automático con
#un saldo inicial de $2000, con el siguiente menú:
#1.Ingreso de dinero
#2.Retirar dinero
#3.Mostrar dinero
#4.Salir
saldo=2000

print("Elija una de las siguientes opciones: \n 1.Ingreso de dinero. \n 2.Retirar dinero. \n 3.Mostrar dinero. \n 4.Salir")

numero=int(input("Introduce el número de la opción: "))

if numero==1:
    cantidad=float(input("¿Cuánto deseas ingresar?: "))
    saldo+=cantidad
    print(f"Ha sido correcto, usted tiene ahora {saldo} euros")
elif numero==2:
    cantidad=float(input("¿Cuánto deseas retirar?: "))
    if cantidad<=saldo:
        saldo-=cantidad
        print(f"Ha sido correcto, usted tiene ahora {saldo} euros")
    else:
        print(f"No puede retirar {cantidad} euros porque tiene {saldo} euros en la cuenta")
elif numero==3:
    print(f"Usted tiene {saldo} euros")
elif numero==4:
    print("Bye, hasta luego")
else:
    print("Número incorreto")