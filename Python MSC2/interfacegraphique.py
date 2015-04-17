# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 17:36:04 2015

@author: raphael
"""

import numpy
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation
from scipy import misc

import Tkinter, tkFileDialog #selectione le repertoire de fichiers d'entree
root = Tkinter.Tk()
root.withdraw()
repertoire = tkFileDialog.askdirectory(parent=root,initialdir="/home/raul/Bureau/Experiences",title='Selectionez le repertoire M. Chaussette')


X = numpy.load(repertoire+'/X.npy')
Y = numpy.load(repertoire+'/Y.npy')
V = ( (X[301:]- X[300:-1])**2 + (Y[301:]- Y[300:-1])**2 )**0.5 
trace = numpy.zeros((misc.imread(repertoire+'/image.jpg').shape))

dt = 1

class SubplotAnimation(animation.TimedAnimation):
    def __init__(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 2, 1)
        ax2 = fig.add_subplot(2, 2, 2)


        ax1.set_xlabel('position of the ant')
        self.im = ax1.imshow(trace, cmap='gray', vmax=1)


        ax2.set_xlabel('time')
        ax2.set_ylabel('vitesse')
        self.line2 = Line2D([], [], color='black')
        self.line2e = Line2D([], [], color='red', marker='o', markeredgecolor='r')
        ax2.add_line(self.line2)
        ax2.add_line(self.line2e)
        ax2.set_xlim(0, 1000)
        ax2.set_ylim(0, 30)


        animation.TimedAnimation.__init__(self, fig, interval=50, blit=True)

    def _draw_frame(self, framedata):
        global trace
        i = framedata
        for j in range(i,i+dt):
            trace[Y[j], X[j]] += 1



        self.im.set_array(trace)

        self.line2.set_data(range(i+dt), V[:i+dt])
        self.line2e.set_data(i+dt,V[i+dt])


        self._drawn_artists = [ self.im, self.line2,  self.line2e]

    def new_frame_seq(self):
        return iter(range(300,407870,dt))

    def _init_draw(self):
        lines =  [self.line2,  self.line2e]
        self.im.set_array(trace)
        for l in lines:
            l.set_data([], [])

ani = SubplotAnimation()

plt.show()