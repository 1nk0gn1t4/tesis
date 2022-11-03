import cv2
import os
from imutils.video import FPS
from datetime import datetime
from codecs import utf_8_encode

#el acceso esta denegado
acceso=False
alumno=""
#Accedemos a la carpeta
arch_Datos="C:\\Users\\tom_4\\Documents\\Python\\clases\\tesis\\Datos_Rostros"
nombres=os.listdir(arch_Datos)
#encendemos el archivo de reconocimiento
face_recognizer=cv2.face.LBPHFaceRecognizer_create()
#leemos el modelo
face_recognizer.read("C:\\Users\\tom_4\\Documents\\Python\\clases\\tesis\\modeloLBPH.XML")
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
        if resultado[1]<50:
            cv2.putText(frame,"{}".format(nombres[resultado[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            alumno=nombres[resultado[0]]
            acceso=True
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

if acceso==True:
    #Accedemos a la carpeta donde almacenaremos los datos
    arch_Lib="C:\\Users\\tom_4\\Documents\\Python\\clases\\tesis\\Gestion Biblioteca"

    #accedemos a la carpeta de libros 
    carpeta_Libros=(arch_Lib+"\\"+"Libros.txt")
    libros=open(carpeta_Libros,"r",encoding="utf-8")

    #mostramos los libros que tenemos
    print(libros.read())
    libros.seek(0)
    lineas_libros=libros.readlines()
    libros.close()

    retirar=input("ingrese el nombre del libro al cual desea retirar: ")


    #organizamos los libros en una tabla llamada almacen
    almacen=[] #lista
    reg=[] #diccionario
    for linea in lineas_libros:
        campo=linea.replace("\n","").split(";")
        linea={"titulo":campo[0],"autor":campo[1],"cantidad":campo[2]}
        almacen.append(linea)

    #verificamos si el libro se encuentra accesible en el almacen
    for lineas in almacen:
        if lineas['titulo']==retirar:
            if int(lineas['cantidad'])>0:
                print("retire su voucher para recojer el libro en la biblioteca")
                reg=lineas
                carpeta_Historial=(arch_Lib+"\\"+"Historial.txt")
                historia=open(carpeta_Historial,"a")
                historia.write(str(alumno)+";"+reg['titulo']+";"+str(datetime.today())+"\n")
                historia.close()
                break
            else:
                print("el libro no se encuentra disponible en estos momentos")
                reg=lineas
                break
    if len(reg)==0:
        print("no contamos con el libro")