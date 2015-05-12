# -*- coding: utf-8 -*-
"""
Created on Fri Jan 09 16:46:47 2015

@author: Utilisateur
"""

import Image, ImageChops, numpy
from scipy import misc

import Tkinter, tkFileDialog, os #selectione le repertoire de fichiers d'entree
root = Tkinter.Tk()
root.withdraw()
repertoire = tkFileDialog.askdirectory(parent=root,initialdir="/home/raul/Desktop/Experiences",title='Selectionez le repertoire entree M. Chaussette')
fichiers = [os.path.join(repertoire, f) for f in sorted(os.listdir(repertoire))]


sortie = repertoire + '/../Propre'
if not(os.path.exists(sortie)): os.makedirs(sortie)

'''root = Tkinter.Tk()
root.withdraw()
fichfond = tkFileDialog.askopenfilename(parent=root,initialdir="/home/raul/Desktop/Experiences",title='Selectionez le fond M. Chaussette')
Fond = Image.open(fichfond)
'''


def temps(stringTM): #attention au changement de mois
    date = str.split(str.split(stringTM, '/')[-1], '.')[0]
    return int(date[16:19]) + 1000*( int(date[13:15]) + 60*( int(date[11:13]) + 60*( int(date[9:11]) + 24*int(date[6:8]) ) ) )
    
    
def fond(premiere, derniere, pas=1):
    image = misc.imread(fichiers[premiere])
    fond = numpy.zeros(image.shape)
    for n in range(premiere,derniere,pas):
        image = misc.imread(fichiers[n])
        fond = (image < fond)*fond + (image >= fond)*image 
    return Image.fromarray(fond).convert('L')

    

n0 = 650

t0 = temps(fichiers[n0])

Fond = fond(n0,n0+10000,100)
    

for n,f in enumerate(fichiers[n0:]):
    if (n+1+n0)%10000==0:    
        Fond = fond(n+n0,n+n0+10000,100)
    
    ImageChops.difference(Fond, Image.open(f)).save(sortie+'/'+str(temps(f) - t0)+'.jpg')
    