#Contador de monedas con la cámara
import cv2
capturaVideo = cv2.VideoCapture(0) #Detecta camara del ordenador

#caso de error
if not capturaVideo.isOpened(): #Si no funciona la captura de video...
    print("No he encontrado ninguna cámara. ")
    exit()

while True: #Mientras que funcione...
    tipoCamara, camara = capturaVideo.read() #Que ejecute la variable de la captura de video
    grises = cv2.cvtColor(camara, cv2.COLOR_BGR2GRAY) #grises

    cv2.imshow("Camara", grises) #Muestro
    if cv2.waitKey(1)==ord("l"): #Si presiono la l se detiene el imshow del vídeo
        break
capturaVideo.release() #Detenemos el vídeo
cv2.destroyAllWindows() #Cerramos ventanas
