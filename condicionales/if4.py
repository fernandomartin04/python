#Ejercicio 4 con if
#Crear un programa que ompare dos nombres y verificar
#si hay conincidencia o no, si es que ambos nombres
#empiezan o terminan con la misma letra 

print("Escribe dos palabras y las compararé.")

p1=input("Escribe la primera palabra: ")
p2=input("Escribe la segunda palabra: ")

#Comparo la primera letra
if p1.lower()[0] == p2.lower()[0]:
    print("La primera letra es igual")

#Comparo la última letra

elif p1.lower()[-1] == p2.lower()[-1]:
    print("La última letra es igual")

else:
    print("No hay coincidencia ")