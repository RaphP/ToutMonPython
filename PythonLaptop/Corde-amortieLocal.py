# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:49:11 2015

@author: bernard
"""

dx = 1.
dt = 1.0
dm = 1.
mu = 1.
T = 1.

xMesure = 150

import numpy

x = numpy.linspace(0,2*numpy.pi,500)

y = numpy.sin(x) + numpy.sin(4*x)
y[-1] = 0

Y = [y,y]


def iteration(F):
    y = F[-1]
    F.append(   T*dt**2/dx/dm*(numpy.roll(y,1) + numpy.roll(y,-1) - 2*y) +   - F[-2] + 2*y  )
    F[-1][xMesure] = ( T*dt/dx*(y[xMesure+1] + y[xMesure - 1] - 2*y[xMesure]) +  mu*y[xMesure]  - dm/dt*F[-3][xMesure] + 2*dm/dt*y[xMesure] )/( dm/dt + mu ) 
    F[-1][-1] = 0
    F[-1][0] = 0    
    return F
    
    
    
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


line, = ax.plot(x, y)

def animate(i):
    global Y
    Y = iteration(Y)
    line.set_ydata(Y[-1])
    return line,


ani = animation.FuncAnimation(fig, animate, interval = 2)
