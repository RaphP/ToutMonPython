# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:10:11 2015

@author: bernard
"""
dx = 1.
dt = 1.0
dm = 1.
mu = 0.00
T = 1.

import numpy

x = numpy.linspace(0,2*numpy.pi,500)

y = numpy.sin(x)
y[-1] = 0

Y = [y,y]


def iteration(F):
    y = F[-1]
    F.append(  ( T*dt/dx*(numpy.roll(y,1) + numpy.roll(y,-1) - 2*y) +  mu*y  - dm/dt*F[-2] + 2*dm/dt*y )/( dm/dt + mu )  )
    return F
    
    
    
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


line, = ax.plot(x, y)

def animate(i):
    global Y
    Y = iteration(Y)
    Y[-1][-1] = 0
    Y[-1][0] = 0
    line.set_ydata(Y[-1])
    return line,


ani = animation.FuncAnimation(fig, animate, interval = 2)
plt.show()