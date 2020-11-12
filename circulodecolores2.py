# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 22:34:19 2020

@author: 1
"""

import cv2
import numpy as np

img=cv2.imread('CirculoColores.jpg')
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

rojo_bajos=np.array([0,100,20])
rojo_altos=np.array([8,255,255])

rojo_bajos1=np.array([175,100,20])
rojo_altos1=np.array([179,255,255])

morado_bajos=np.array([130,100,100])
morado_altos=np.array([160,255,255])

azul_bajos=np.array([110,100,100])
azul_altos=np.array([130,255,255])

verde_bajos=np.array([40,100,100])
verde_altos=np.array([70,255,255])

amarillo_bajos=np.array([25,100,100])
amarillo_altos=np.array([35,255,255])

mask_rojo=cv2.inRange(hsv,rojo_bajos,rojo_altos)
mask_rojo1=cv2.inRange(hsv,rojo_bajos1,rojo_altos1)

mask_morado=cv2.inRange(hsv,morado_bajos,morado_altos)

mask_azul=cv2.inRange(hsv,azul_bajos,azul_altos)

mask_verde=cv2.inRange(hsv,verde_bajos,verde_altos)

mask_amarillo=cv2.inRange(hsv,amarillo_bajos,amarillo_altos)

mask_rojo2=cv2.bitwise_or(mask_rojo, mask_rojo1)

mask_union=cv2.bitwise_or(mask_rojo2, mask_morado)

mask_union1=cv2.bitwise_or(mask_azul, mask_verde)

mask_union2=cv2.bitwise_or(mask_union, mask_union1)

mask_union3=cv2.bitwise_or(mask_union2, mask_amarillo)

cv2.imshow('Imagen Original',img)
cv2.imshow('Morado+Naranj+Verde', mask_union3)
print("\nPulsa cualquier tecla para cerrar las ventanas\n")

cv2.waitKey(0)
cv2.destroyAllWindows()