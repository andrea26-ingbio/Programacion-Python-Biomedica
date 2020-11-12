# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 20:56:50 2020

@author: 1
"""

from math import*
from numpy import*
from pylab import*
from matplotlib.pylab import *

def f1(x):
    y=sin(x)
    return y

def f2(x):
    y=sin(x) + sin(5.0*x)
    return y

def f3(x):
    y=sin(x) * exp(-x/10.)
    return y

#array de valores a representar
x=linspace(2,10*pi,800)

p1, p2, p3=plt.plot(x,f1(x),x,f2(x),x,f3(x))

#Añado leyenda, tamaño de letra 10, en esquina superior
legend(('Funcion 1','Funcion 2', 'Funcion 3'),
prop={'size':10}, loc='upper right')

xlabel('Tiempo / s')
ylabel('Amplitud / cm')
title('Representacion de tres funciones')

#Creo una figura (ventana), pero indico el tamaño (x,y) en pulgadas
figure(figsize=(18,8))

show()