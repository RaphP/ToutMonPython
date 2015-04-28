# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 18:44:47 2015

@author: raphael
"""
import os

for i in range(1,407871+1):
    os.rename('/home/raphael/Bureau/Week2/weekend2/weekend'+str(i).zfill(4)+'.jpg', '/home/raphael/Bureau/Week2/weekend2/weekend'+str(i).zfill(6)+'.jpg')
    if i%1000 == 0:
        print i 
    

