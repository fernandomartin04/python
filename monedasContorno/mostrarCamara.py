import cv2
import numpy as np

capturaVideo = cv2.VideoCapture(0) #Captura la camara que haya en el ordenador

#Si no hay camara disponible...
if not capturaVideo.isOpened():
    print("No se encontro una camara")
    exit()

#Mientras funcione camara
while True:
    tipoCamara,camara = capturaVideo.read() #Capturo su imagen
    grises=cv2.cvtColor(camara, cv2.COLOR_BGR2GRAY) #Lo paso a grises si lo quiero en gris

    cv2.imshow("En vivo", grises) #Muestro la camara
    if cv2.waitKey(1)==ord("l"): #Si pulso la letra l acabo
        break
capturaVideo.release() #Dejo de mostrar el video
cv2.destroyAllWindows() #Cierro la ventana
