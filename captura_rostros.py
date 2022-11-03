import cv2
import os
import imutils
#Ingresamos el nombre de la persona a registrar
entrada=input("Ingrese el nombre de la persona a registrar: ")
nombre_Persona=entrada
#Accedemos a la carpeta donde almacenaremos los datos
arch_Datos="C:\\Users\\tom_4\\Documents\\Python\\clases\\tesis\\Datos_Rostros"
#Creamos la carpeta con los datos de la persona
arch_Person=arch_Datos+"\\"+nombre_Persona
if not os.path.exists(arch_Person):
    print("Carpeta creada: ",arch_Person)
    os.makedirs(arch_Person)
#Declaramos el clasificador Haar Cascade
clasific=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
cont=0
#Encendemos la cámara
captura=cv2.VideoCapture(0)

while True:
    ret,frame=captura.read()
    if ret==False: break
    #redimensionamos la captura para su almacenamiento
    frame=imutils.resize(frame,width=640)
    #Convertimos en escala de grises
    esc_Grises=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    copia_Frame=frame.copy()
    #aplicamos el reconocimiento a las imagenes capturadas
    faces=clasific.detectMultiScale(esc_Grises,1.3,5,minSize=(50,50),maxSize=(200,200))
    #Almacenamos los rostros 
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        rostro=copia_Frame[y:y+h,x:x+w]
        rostro=cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(arch_Person+"\\rostro_{}.JPG".format(cont),rostro)
        cont+=1
    #mostramos la cámara    
    cv2.imshow("frame",frame)    
    
    k=cv2.waitKey(1)
    if k==27 or cont==300:
        break
captura.release()
cv2.destroyAllWindows()

