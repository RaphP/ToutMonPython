# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:23:24 2015

@author: raphael
"""

import numpy
from scipy import misc
import matplotlib.pyplot as plt
import time

import Tkinter, tkFileDialog, os #selectione le repertoire de fichiers d'entree
root = Tkinter.Tk()
root.withdraw()
repertoire = tkFileDialog.askdirectory(parent=root,initialdir="/home/raphael/Bureau",title='Selectionez le repertoire Images M. Chaussette')
fichiers = [os.path.join(repertoire, f) for f in sorted(os.listdir(repertoire))]
X = numpy.load(repertoire+'/../Barycentre/X.npy')
Y = numpy.load(repertoire+'/../Barycentre/Y.npy')
V = ( (X[301:]- X[300:-1])**2 + (Y[301:]- Y[300:-1])**2 )**0.5 

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(V)

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)


i = 0
im = []

def ouvre_image(x):
    if x > len(fichiers) - 1:
        return  
    global i, im
    i = x
    ax2.clear()
    im = ax2.imshow(misc.imread(fichiers[int(i)]))
    fig2.canvas.draw()
  

def loop():
    global i
    
  
def change_image(key):
    global i
    if key == 'right':
        i+=1
        im.set_array(misc.imread(fichiers[int(i)]))
        fig2.canvas.draw()
    if key == 'left':
        i+=-1
        im.set_array(misc.imread(fichiers[int(i)]))
        fig2.canvas.draw()
    if key == 'up':
        i+=10
        im.set_array(misc.imread(fichiers[int(i)]))
        fig2.canvas.draw()
    if key == 'down':
        i+=-10
        im.set_array(misc.imread(fichiers[int(i)]))
        fig2.canvas.draw()
    
    if key == ' ':
        for t in range(50):
            time.sleep(1)
            i+=1
            im.set_array(misc.imread(fichiers[int(i)]))
            fig2.canvas.draw()
            

    


def onclick1(event):
    if event.button == 3:
        ouvre_image(event.xdata)

cid1 = fig1.canvas.mpl_connect('button_press_event', onclick1)

def onclick2(event):
    change_image(event.key)

        
cid2 = fig1.canvas.mpl_connect('key_press_event', onclick2)

