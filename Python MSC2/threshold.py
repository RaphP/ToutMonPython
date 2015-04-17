# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 19:01:11 2015

@author: raul
"""
import time 



import Image, ImageChops

import Tkinter, tkFileDialog, os #selectione le repertoire de fichiers d'entree
root = Tkinter.Tk()
root.withdraw()
repertoire = tkFileDialog.askdirectory(parent=root,initialdir="/home/raul/Desktop/Experiences",title='Selectionez le repertoire entree M. Chaussette')
fichiers = [os.path.join(repertoire, f) for f in sorted(os.listdir(repertoire))]


sortie = repertoire + '/../Propre'
#os.makedirs(repertoire + '/../Propre')

root = Tkinter.Tk()
root.withdraw()
fichfond = tkFileDialog.askopenfilename(parent=root,initialdir="/home/raul/Desktop/Experiences",title='Selectionez le fond M. Chaussette')
Fond = Image.open(fichfond)

def temps(stringTM):
    return int(str.split(str.split(str.split(stringTM, '/')[-1], '.')[0], '-')[1])*1000*1000000 + int(str.split(str.split(str.split(stringTM, '/')[-1], '.')[0], '-')[2])*1000 + int(str.split(str.split(str.split(stringTM, '/')[-1], '.')[0], '-')[3])
    

t0 = temps(fichiers[0])

t = time.time()
for n in range(100000000):
    ImageChops.difference(Fond, Image.open(fichiers[n])).save(sortie+'/'+str(temps(fichiers[n]) - t0)+'.jpg')
    #ImageChops.difference(Fond, Image.open(fichiers[n])).save(fichiers[n])
    
print time.time() - t