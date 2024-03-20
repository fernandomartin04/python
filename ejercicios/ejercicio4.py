#Ejercicio 4
#Obtener el precio final que se tiene que pagar
#si se aplica el 36% de descuento del
#total de la compra

producto1=float(input("Precio del primer producto: "))
producto2=float(input("Precio del segundo producto: "))
producto3=float(input("Precio del tercer producto: "))
resultado=(producto1+producto2+producto3)*0.64

print(f"El precio final es de: {resultado:.2f} euros")
