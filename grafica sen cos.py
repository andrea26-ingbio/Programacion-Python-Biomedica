# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 22:31:00 2020

@author: 1
"""

from math import*
from numpy import*
from pylab import*
from matplotlib.pylab import *

t=arange(0.1,20,0.1)

y1=sin(t)/t
y2=sin(t)*exp(-t)
p1,p2=plt.plot(t, y1, t, y2)

#Texto en la grafica en coordenadas (x,y)
texto1=text(2, 0,6, r'$\frac(\sin(x)}{x}$', fontsize=20)
texto2=text(13, 0.2, r'$\sin(x) \cdot e^{-x}$', fontsize=16)

#añado una malla al grafico
grid()

title('Representacion de dos funciones')
xlabel('Tiempo / s')
ylabel('Amplitud / cm')

show()