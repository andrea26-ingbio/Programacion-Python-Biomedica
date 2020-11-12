# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 22:54:49 2020

@author: 1
"""

#Algoritmo de deteccion de colores
#Detecta objetos rojo, azul y amarillo elimina el ruido y busca su centro
 
import cv2
import numpy as np
 
#Iniciamos la camara
captura = cv2.VideoCapture(0)
 
while(1):
     
    #Capturamos una imagen y la convertimos de RGB -> HSV
    _, imagen = captura.read()
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 
    #Establecemos el rango de colores que vamos a detectar
    #En este caso de verde oscuro a verde-azulado claro
    rojo_bajos1=np.array([0,100,20], dtype=np.uint8)
    rojo_altos1=np.array([8,255,255], dtype=np.uint8)
    rojo_bajos2=np.array([175,100,20], dtype=np.uint8)
    rojo_altos2=np.array([179,255,255], dtype=np.uint8)
    azul_bajos=np.array([110,100,100], dtype=np.uint8)
    azul_altos=np.array([130,255,255], dtype=np.uint8)
    amarillo_bajos=np.array([25,100,100], dtype=np.uint8)
    amarillo_altos=np.array([35,255,255], dtype=np.uint8)
 
    #Crear una mascara con solo los pixeles dentro del rango de verdes
    mask1 = cv2.inRange(hsv, rojo_bajos1, rojo_altos1)
    mask2 =cv2.inRange(hsv,rojo_bajos2,rojo_altos2)
    mask3 = cv2.inRange(hsv, azul_bajos, azul_altos)
    mask4 = cv2.inRange(hsv, amarillo_bajos, amarillo_altos)
    
    mask5 =cv2.bitwise_or(mask1, mask2)
    mask6 =cv2.bitwise_or(mask5, mask3)
    mask =cv2.bitwise_or(mask6, mask4)
 
    #Encontrar el area de los objetos que detecta la camara
    moments = cv2.moments(mask)
    area = moments['m00']
 
    #Descomentar para ver el area por pantalla
    #print area
    if(area > 2000000):
         
        #Buscamos el centro x, y del objeto
        x = int(moments['m10']/moments['m00'])
        y = int(moments['m01']/moments['m00'])
         
        #Mostramos sus coordenadas por pantalla
        print ("x = ", x)
        print ("y = ", y)
 
        #Dibujamos una marca en el centro del objeto
        cv2.rectangle(imagen, (x, y), (x+2, y+2),(0,0,255), 2)
     
     
    #Mostramos la imagen original con la marca del centro y
    #la mascara
    cv2.imshow('Detector de colores', mask)
    cv2.imshow('Camara', imagen)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
 
cv2.destroyAllWindows()