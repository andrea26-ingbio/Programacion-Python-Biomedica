# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:12:20 2020

@author: 1
"""

import numpy as np
import cv2

#Cargamos la imagen
original=cv2.imread("aguila.jpg")
cv2.imshow("original", original)

#Convertimos a escala de grises
gris=cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

#Aplicar suavizado Guassiano
gauss=cv2.GaussianBlur(gris, (5,5), 0)
cv2.imshow("suavizado", gauss)

#Detectamos los bordes con canny
canny=cv2.Canny(gauss,50,150)
cv2.imshow("modulo canny", canny)

#Buscamos los contornos
(contornos,_)=cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Mostramos el numero de monedas por consolas
print("He encontrado {} objetos".format(len(contornos)))

cv2.drawContours(original,contornos,-1,(1,1,1),2)
cv2.imshow("Contornos", original)

cv2.waitKey(0)