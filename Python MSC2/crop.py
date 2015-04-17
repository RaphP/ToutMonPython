# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 13:57:00 2015

@author: raul
"""


from scipy import misc

import Tkinter, tkFileDialog, os #selectione le repertoire de fichiers d'entree
root = Tkinter.Tk()
root.withdraw()
repertoire = tkFileDialog.askdirectory(parent=root,initialdir="/home/raul/Desktop/",title='Selectionez le repertoire entree M. Chaussette')
fichiers = [os.path.join(repertoire, f) for f in sorted(os.listdir(repertoire))]

root = Tkinter.Tk()
root.withdraw()
sortie = tkFileDialog.askdirectory(parent=root,initialdir="/home/raul/Desktop/",title='Selectionez le repertoire Sortie M. Chaussette')



for n, f in enumerate(fichiers):
    misc.imsave(sortie+'/'+str(n)+'.jpg', misc.imread(f)[594:594+650,837:837+612])
