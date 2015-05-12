# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 17:22:48 2015

@author: raul
"""

import time


import numpy, Image, ImageChops
from scipy import misc

###fonctions

def CalculFond(fichiers):
    image = misc.imread(fichiers[0])
    fond = numpy.zeros(image.shape)
    for n in numpy.linspace(0,len(fichiers)-1,100).astype('uint32'):
        image = misc.imread(fichiers[n])
        fond = (image < fond)*fond + (image >= fond)*image 
    return Image.fromarray(fond).convert('L')


def barycentre(image):
    Y,X = numpy.where(image == 1)
    if numpy.isnan(Y.mean() + X.mean()):
        return 1,1
    else :
        return X.mean(), Y.mean()

def GetXY(fichiers,n):
    X, Y = [], []
    fond = CalculFond(fichiers)
    for f in fichiers:
        propre = numpy.array(ImageChops.difference(fond, Image.open(f)))
        threshold = propre.max() - 30
        x,y = barycentre(propre > threshold)
        X+=[x]
        Y+=[y]
    misc.imsave(sortie+'/image'+str(n)+'.jpg',propre > threshold)
    return X,Y    
        

####Script

import Tkinter, tkFileDialog, os #selectione le repertoire de fichiers d'entree
root = Tkinter.Tk()
root.withdraw()
repertoire = tkFileDialog.askdirectory(parent=root,initialdir="/home/raul/Desktop/Experiences",title='Selectionez le repertoire entree M. Chaussette')
fichiers = [os.path.join(repertoire, f) for f in sorted(os.listdir(repertoire))]

sortie = repertoire+'/../position'
if not(os.path.exists(sortie)): os.makedirs(sortie)

n = 0

X = [1]
Y = [1]
numpy.save(sortie+"/X", X)
numpy.save(sortie+"/Y", Y) 

while 1:
    #time.sleep(1800)
    fichiers = [os.path.join(repertoire, f) for f in sorted(os.listdir(repertoire))][:-1]
    Xp,Yp = numpy.array(GetXY(fichiers, n))        
    X = numpy.load(sortie+'/X.npy')
    Y = numpy.load(sortie+'/Y.npy')
    numpy.save(sortie+"/X", numpy.append(X,Xp))
    numpy.save(sortie+"/Y", numpy.append(Y,Yp))        
    n+=1
    for f in fichiers:
        os.remove(f)    
    time.sleep(3600*2)



'''
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
im = plt.imshow(misc.imread(fichiers[301]), cmap='gray', vmax=1)

i = 0

def updatefig(*args):
    global i
    f = fichiers[i]
    propre = numpy.array(ImageChops.difference(fond, Image.open(f)))
    threshold = propre.max() - 30
    ima = propre > threshold
    im.set_array(ima)
    i+=10
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=10, blit=True)
plt.show()
'''
