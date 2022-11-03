from codecs import utf_8_encode
from datetime import datetime
import os
from datetime import datetime
nombre=input("ingrese su nombre: ")
#Accedemos a la carpeta donde almacenaremos los datos
arch_Lib="C:\\Users\\tom_4\\Documents\\Python\\clases\\tesis\\Gestion Biblioteca"

#accedemos a la carpeta de libros 
carpeta_Libros=(arch_Lib+"\\"+"Libros.txt")
libros=open(carpeta_Libros,"r",encoding="utf-8")

#mostramos los libros que tenemos
#print(libros.read())
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
            historia.write(nombre+";"+reg['titulo']+";"+str(datetime.today())+"\n")
            historia.close()
            break
        else:
            print("el libro no se encuentra disponible en estos momentos")
            reg=lineas
            break
if len(reg)==0:
    print("no contamos con el libro")


          


