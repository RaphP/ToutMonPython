# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 11:30:31 2015

@author: raphael
"""

import time
import Tkinter

log = open('production', 'a')


fenetre = Tkinter.Tk()
fenetre.title("Travaille tête de pioche !")


def pression(nom):
    log.write(str(nom)+':'+str(time.time()) + ';')
    
boutons = []
for nom, r,c in zip(['RBPI', 'XY', 'Biblio', 'Pause','Bon','Mauvais'],[0,0,0,0,1,1], [1,2,3,4,2,3] ) :
    boutons.append( Tkinter.Button(fenetre, text=nom, command=lambda n=nom: pression(n) ) ) 
    boutons[-1].grid(row= r, column = c)



fenetre.mainloop()

log.close()
