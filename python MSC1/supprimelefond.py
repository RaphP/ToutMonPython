# -*- coding: utf-8 -*-
"""
Created on Fri Jan 09 16:46:47 2015

@author: Utilisateur
"""

import numpy
from scipy import misc

import Tkinter, tkFileDialog, os #selectione le repertoire de fichiers d'entree
root = Tkinter.Tk()
root.withdraw()
repertoire = tkFileDialog.askdirectory(parent=root,initialdir="/home/raphael/Bureau",title='Selectionez le repertoire M. Chaussette')
fichiers = [os.path.join(repertoire, f) for f in sorted(os.listdir(repertoire))]

import shutil #cree le repertoire de sortie, vide l'ancien si besoin
sortie = repertoire + '/../Propre'
if os.path.exists(repertoire + '/../Propre'): shutil.rmtree(repertoire + '/../Propre')
os.makedirs(repertoire + '/../Propre')


def fond(premiere, derniere, pas=1):
    image = misc.imread(fichiers[premiere])
    fond = numpy.zeros(image.shape)
    for n in range(premiere,derniere,pas):
        image = misc.imread(fichiers[n])
        fond = (image < fond)*fond + (image >= fond)*image 
    return fond


Fond = fond(1000,10000,100)

for n in range(100,407870):
    misc.imsave(sortie+'/no'+str(n).zfill(6)+'.jpg', misc.imread(fichiers[n]) - Fond)
