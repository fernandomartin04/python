#Vamos a trabajar las funciones en las listas
array=["futbol","Pc",16.6,18,[6,7,10.4],True,False,"Pc"]
array.append(50) #Añade un valor al final del array
array.insert(1,80) #Añade un valor en la posicion elegida del array
array.extend([5,55,True]) #Añade varios valores al final del array
array1=["perro",2,True]
array2=[7,"gato",False]
array3=array1+array2 #Concateno 2 arrays
arrayNum=[4,2,-11,37,5]

print(array)
print(array3)
print("Pc" in array) #Busca la palabra Pc en la variable array (devuelve un true)
print(array.index("Pc")) #Nos dice la ubicacion que tiene Pc en el array
print(array.count("Pc")) #Me cuenta la cantidad de veces que esta Pc en el array
array.remove(True) #Quita el valor True del array
array.clear() #Vacia el array
array.reverse() #Cambia el orden de array
arrayNum.sort() #Ordena el array numericamente