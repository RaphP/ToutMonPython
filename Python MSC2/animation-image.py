# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 17:21:33 2015

@author: raphael
"""

import numpy 
import matplotlib.pyplot as plt
import matplotlib.animation as animation


X = numpy.load('NDLPX.npy')
Y = numpy.load('NDLPY.npy')
trace = numpy.zeros((1080, 1080))


f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
im = ax1.imshow(trace, cmap='gray', vmax=1)
lin, = ax2.plot(X[0:10])


i=0

def updatefig(*args):
    global trace, i
    x = X[i]
    y = Y[i]
    i+=1
    trace[y,x] = 1
    im.set_array(trace)
    ax2.plot(X[0:i])
    plt.cla()
    return im,

ani = animation.FuncAnimation(f, updatefig, interval=50, blit=True)
plt.show()