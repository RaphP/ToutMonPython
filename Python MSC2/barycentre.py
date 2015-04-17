# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 15:19:36 2015

@author: raphael
"""
import numpy
from scipy import misc


import Tkinter, tkFileDialog, os #selectione le repertoire de fichiers d'entree
root = Tkinter.Tk()
root.withdraw()
repertoire = tkFileDialog.askdirectory(parent=root,initialdir="/home/raul/Desktop",title='Selectionez le repertoire M. Chaussette')
fichiers = [os.path.join(repertoire, f) for f in sorted(os.listdir(repertoire))]

import shutil #cree le repertoire de sortie, vide l'ancien si besoin
sortie = repertoire + '/../Barycentre'
#if os.path.exists(repertoire + '/../Barycentre'): shutil.rmtree(repertoire + '/../Barycentre')
#os.makedirs(repertoire + '/../Barycentre')



def barycentre(image):
    Y,X = numpy.where(image == 1)
    if numpy.isnan(Y.mean() + X.mean()):
        return 1,1
    else :
        return X.mean(), Y.mean()


image = misc.imread(fichiers[1])
trace = numpy.zeros(image.shape) 
X = []
Y = []

for i,f in enumerate(fichiers[:14671]):
    x,y = barycentre(misc.imread(f) > 29)
    X+=[x]
    Y+=[y]
    trace[int(y),int(x)] = 1
    if i%1000 == 0:
        print i 
    
    
numpy.save(sortie+"/X", X)
numpy.save(sortie+"/Y", Y)
shutil.copy2(fichiers[1], sortie+'/image.jpg')