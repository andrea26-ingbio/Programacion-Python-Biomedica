# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 08:18:25 2020

@author: 1
"""

from PIL import Image

foto=Image.open('urticaria.jpg')

for x in range(255):
    for y in range(197):
        pixel=foto.getpixel((x,y))
        print(pixel)
        
foto.close()