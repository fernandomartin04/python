#Ejercicio 3
import math
r=float(input("Ingrersa el radio: "))
area=math.pi*r**2
longitud=2*math.pi*r
#Ahora al mostrar el resultado pongo :. seguido del numero de decimales que quiero y una f
print(f"El area es: {area:.3f} y la longitud es {longitud:.2f}")