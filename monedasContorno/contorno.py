#Empezamos a trabajar con contornos
import cv2
imagen=cv2.imread('monedasContorno/contorno.jpg')
#Lo pongo a escala de grises
grises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY) 

#Para ahora el umbral, ponemos _, delante del nombre de la variable, esto es
#porque el umbrla devuelve dos valores y a nosotros nos interesa e segundo 
#entonces para el primero ponemos eso, una variable vacía, tambien puedo ponerle nombre
_,umbralizado=cv2.threshold(grises,100,255,cv2.THRESH_BINARY)

#Contorno
contorno, jerarquia = cv2.findContours(umbralizado,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

#Dibujamos el contorno en la imagen original, para mostrar todos, ponemos el -1. 
#el 3 es el grosor del contorno
cv2.drawContours(imagen,contorno,-1,(0,255,0),3)

#Mostrar la imagen en grises, para la normal ponemos la variable de la imagen
cv2.imshow('Imagen en normal',imagen)
#cv2.imshow('Imagen en grises',grises)
#cv2.imshow('Imagen en umbralizado',umbralizado)

cv2.waitKey(0)
cv2.destroyAllWindows() #Se cierran todas las ventanas a iertas pulsando una tecla