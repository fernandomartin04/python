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

def alinemiento(imagen,ancho,alto):
    imagen_alineada = None
    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) #Grises
    tipo_umbral, umbral = cv2.threshold(grises, 150, 255, cv2.THRESH_BINARY) #Umbral
    cv2.imshow("Umbral", umbral) #Muestro Umbral
    contorno, jerarquía = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] #Contornos
    contorno = sorted(contorno, key=cv2.contourArea, reverse=True) #Ordeno las matrices (los puntos) de menor a mayor
    #Con este bucle recorro todos los contornos encontrados
    for c in contorno:
        epsilon = 0.01*cv2.arcLength(c, True) #Cierro los contornos encontrados y recorridos
        aproximacion = cv2.approxPolyDP(c, epsilon, True) #Aproximacion
        if len(aproximacion)==4: #Si ha encontrado la aproximacion 4 puntos del circulo...
            puntos = ordenarPuntos(aproximacion)
            puntos1 = np.float32(puntos)
            puntos2 = np.float32([[0,0],[ancho,0],[0,alto],[ancho,alto]])
            #Perspectiva, por si muevo la camara o algo
            M = cv2.getPerspectiveTransform(puntos1, puntos2)
            imagen_alineada = cv2.warpPerspective(imagen, M, (ancho,alto))
    return imagen_alineada

capturaVideo = cv2.VideoCapture(0)

while True:
    tipocamara, camara = capturaVideo.read()
    if tipocamara==False:
        break
    imagen_A6 = alinemiento(camara,ancho=480,alto=677)
    if imagen_A6 is not None:
        puntos=[]
        imagen_gris=cv2.cvtColor(imagen_A6,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(imagen_gris,(5,5),1)
        _,umbral2=cv2.threshold(blur,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)
        cv2.imshow("Umbral", umbral2)
        contorno2,jerarquia=cv2.findContours(umbral2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(imagen_A6, contorno2, -1, (255,0,0), 2)
        suma1=0.0
        suma2=0.0
        for c_2 in contorno2:
            area=cv2.contourArea(c_2)
            momentos = cv2.moments(c_2)
            if(momentos["m00"]==0):
                momentos["m00"]=1.0
            x=int(momentos["m10"]/momentos["m00"])
            y=int(momentos["m01"]/momentos["m00"])

            if 