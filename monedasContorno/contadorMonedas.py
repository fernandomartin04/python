#Contador de monedas con imagen
import cv2
import numpy as np 
original=cv2.imread('monedasContorno/monedassoles.jpg')
gris=cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)

#Ahora para mejorar la imagen, es decir quitar los ruidos de la imagen vamos a aplicar
#un nuevo proceso de suavizado, los valores de los () deben de ser siempre iguales...3,3;5,5...
valorGauss=1
valorKernel=33
gauss=cv2.GaussianBlur(gris,(valorGauss,valorGauss),0)

#Segunda eliminacion de ruidos, con canny
canny = cv2.Canny(gauss,60,100)

#Elijo el contorno que me interesa, el de fuera
kernel = np.ones((valorKernel,valorKernel),np.uint8) #Matriz
cierre = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)

contornos, jerarquia = cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#Cuento las monedas y dibujo sus contornos finales
print("monedas encontradas: {}".format(len(contornos)))
cv2.drawContours(original,contornos,-1,(0,0,255),2)

#Mostrar resultados
cv2.imshow("Grises",gris)
cv2.imshow("Gauss",gauss)
cv2.imshow("Canny",canny)
cv2.imshow("Cierre",cierre)
cv2.imshow("Resultado", original) #Ya con los contornos dibujados
cv2.waitKey(0)