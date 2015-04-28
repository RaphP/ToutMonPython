# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 14:22:21 2015

@author: raphael
"""
X = numpy.load('NDLPX.npy')
for i,x in enumerate(X):
   if x == 1:
       n = 1
       while X[i-n] == 1:
           n += 1
       X[i] = X[i-n]
       
numpy.save('NDLPX.npy',X)       
     
Y = numpy.load('NDLPY.npy')
for i,y in enumerate(Y):
   if y == 1:
       n = 1
       while Y[i-n] == 1:
           n += 1
       Y[i] = Y[i-n]       
       
numpy.save('NDLPY.npy',Y)