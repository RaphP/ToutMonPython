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

def temps(stringTM): #attention au changement de mois
    date = str.split(str.split(stringTM, '/')[-1], '.')[0]
    return int(date[16:19]) + 1000*( int(date[13:15]) + 60*( int(date[11:13]) + 60*( int(date[9:11]) + 24*int(date[6:8]) ) ) )
    

t0 = temps(fichiers[0])

t = time.time()
for n in range(100000000):
    ImageChops.difference(Fond, Image.open(fichiers[n])).save(sortie+'/'+str(temps(fichiers[n]) - t0)+'.jpg')
    #ImageChops.difference(Fond, Image.open(fichiers[n])).save(fichiers[n])
    
print time.time() - t