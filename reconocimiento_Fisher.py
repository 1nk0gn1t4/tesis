import cv2
import os
from imutils.video import FPS
#Accedemos a la carpeta
arch_Datos="C:\\Users\\1mk0gn1t4\\Documents\\Python\\clases\\tesis\\Datos_Rostros"
nombres=os.listdir(arch_Datos)
#Eigenfaces
face_recognizer=cv2.face.FisherFaceRecognizer_create()
#leemos el modelo
face_recognizer.read("C:\\Users\\1mk0gn1t4\\Documents\\Python\\clases\\tesis\\modeloFisherFace.XML")
#Clasificador de rostro Haarcascade
clasificador=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
#fps=FPS().start()
#Encendemos la camara
captura=cv2.VideoCapture(0)
while True:
    ret,frame=captura.read()
    if ret==False: break
    #transformamos la captura en escala de grises y copiamos
    escala_Grises=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_Copia=escala_Grises.copy()
    #clasificamos el rostro
    rostros_Detectados=clasificador.detectMultiScale(escala_Grises,1.3,5)
    #Aplicamos el reconocimiento Facial Eigenfaces
    for (x,y,w,h) in rostros_Detectados:
        rostro=frame_Copia[y:y+h,x:x+w]
        rostro=cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
        resultado=face_recognizer.predict(rostro)
        cv2.putText(frame,"{}".format(resultado),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
        if resultado[1]<2:
            cv2.putText(frame,"{}".format(nombres[resultado[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.putText(frame,"Desconocido",(x,y-25),2,1.1,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow("frame",frame)
    k=cv2.waitKey(1)
    if k==27:
        break
    #fps.update()
#fps.stop()
#print("Tiempo de Reproduccion: {:.2f}".format(fps.elapsed()))
#print("FPS aproximado: {:.2f}".format(fps.fps()))
captura.release()
cv2.destroyAllWindows()
