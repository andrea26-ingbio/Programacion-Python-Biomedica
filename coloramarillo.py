# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 08:16:19 2020

@author: 1
"""

import cv2
import numpy as np

img=cv2.imread('globo.jpg')
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

amarillo_bajo=np.array([20,50,50])
amarillo_alto=np.array([40,73,37])

mask=cv2.inRange(hsv,amarillo_bajo,amarillo_alto)

cv2.imshow('foto original',img)
cv2.imshow('foto amarillo extraida', mask)

cv2.waitKey(0)
cv2.destroyALLWindows()
