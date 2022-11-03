import cv2
import os
import numpy as np
import time
#Accedemos al archivo de datos
arch_Datos="C:\\Users\\1mk0gn1t4\\Documents\\Python\\clases\\tesis\\Datos_Rostros"
Lista_personas=os.listdir(arch_Datos)
#Declaramos las variables a usar en el entrenador
labels=[]
faces_Data=[]
label=0
#Llenamos las matrices con los imagenes del archivo de datos
for nameDir in Lista_personas:
    personPath=arch_Datos+"\\"+nameDir
    print("Leyendo datos")
    for fileName in os.listdir(personPath):
        #print("Rostros: ",nameDir+"\\"+fileName)
        labels.append(label)
        faces_Data.append(cv2.imread(personPath+"\\"+fileName,0))
        imagen=cv2.imread(personPath+"\\"+fileName,0)
    label+=1
#Fissherfaces:
face_recognizer=cv2.face.FisherFaceRecognizer_create()
#Entrenando el reconocedor de rostros:
print("Entrenando...")
#inicio=time.time()
face_recognizer.train(faces_Data,np.array(labels))
#tiempo_Entrenamiento=time.time()-inicio
#print("Tiempo de entrenamiento: ",tiempo_Entrenamiento)
#Almacenando el modelo obtenido:
face_recognizer.write("C:\\Users\\1mk0gn1t4\\Documents\\Python\\clases\\tesis\\modeloFisherFace.XML")
print("modelo almacenado")
