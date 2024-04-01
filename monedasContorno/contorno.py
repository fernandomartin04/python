#Empezamos a trabajar con contornos
import cv2
imagen=cv2.imread('monedasContorno/contorno.jpg')
cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()