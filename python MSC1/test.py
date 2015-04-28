# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 18:44:47 2015

@author: raphael
"""

import Tkinter, tkFileDialog, os #selectione le repertoire de fichiers d'entree
root = Tkinter.Tk()
root.withdraw()
repertoire = tkFileDialog.askdirectory(parent=root,initialdir="/home/raphael/Bureau",title='Selectionez le repertoire M. Chaussette')
fichiers = [os.path.join(repertoire, f) for f in sorted(os.listdir(repertoire))]
