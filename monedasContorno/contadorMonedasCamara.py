#Importo herramientas
import cv2
import numpy as np

#Defino funcion
def ordenarPuntos(puntos):
    #Concateno puntos de la matriz 
    n_puntos = np.concatenate(puntos[0],puntos[1],puntos[2],puntos[3]).tolist()
    #Ordeno lo spuntos del eje x e y
    y_order = sorted(n_puntos,key=lambda n_puntos:n_puntos[1]) #Defino el valor 0

    x1_order = y_order[0:2] #El segundo valor se le resta 1 asiq realmente es 1
    x1_order = sorted(x1_order, key=lambda x1_order:x1_order[0])

    x2_order = y_order[0:4] #El segundo valor se le resta 1 asiq realmente es 3
    x2_order = sorted(x1_order, key=lambda x2_order:x2_order[0])
    return [x1_order[0],x1_order[1],x2_order[0],x2_order[1]]


