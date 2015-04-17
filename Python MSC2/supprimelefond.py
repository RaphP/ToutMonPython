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
#os.makedirs(repertoire + '/../Propre')

'''root = Tkinter.Tk()
root.withdraw()
fichfond = tkFileDialog.askopenfilename(parent=root,initialdir="/home/raul/Desktop/Experiences",title='Selectionez le fond M. Chaussette')
Fond = Image.open(fichfond)
'''


def temps(stringTM):
    return int(str.split(str.split(str.split(stringTM, '/')[-1], '.')[0], '-')[1])*1000*1000000 + int(str.split(str.split(str.split(stringTM, '/')[-1], '.')[0], '-')[2])*1000 + int(str.split(str.split(str.split(stringTM, '/')[-1], '.')[0], '-')[3])
    
    
def fond(premiere, derniere, pas=1):
    image = misc.imread(fichiers[premiere])
    fond = numpy.zeros(image.shape)
    for n in range(premiere,derniere,pas):
        image = misc.imread(fichiers[n])
        fond = (image < fond)*fond + (image >= fond)*image 
    return Image.fromarray(fond).convert('L')

    

t0 = temps(fichiers[0])

Fond = fond(606,3180,100)
for n,f in enumerate(fichiers[604:3180]):
    ImageChops.difference(Fond, Image.open(f)).save(sortie+'/'+str(temps(f) - t0)+'.jpg')
    

for n,f in enumerate(fichiers[3180:]):
    if n%3026 == 0:
        Fond = fond(n+3180+26,n+3000+3180,100)
    ImageChops.difference(Fond, Image.open(f)).save(sortie+'/'+str(temps(f) - t0)+'.jpg')
    


