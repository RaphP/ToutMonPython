# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 18:41:59 2015

@author: raphael
"""


'''
import Image
import numpy
import matplotlib.pyplot as plt

img = Image.open('/home/raphael/Images/G00'+str(10030)+'.JPG')

fond = numpy.zeros((3000,4000))

for n in range(10030,10060):
    img = Image.open('/home/raphael/Images/G00'+str(n)+'.JPG')
    image = numpy.array(img)
    imagegris = 0.299*image[:,:,0] + 0.587*image[:,:,1] + 0.114*image[:,:,2] 
    fond = (imagegris < fond)*fond + (imagegris >= fond)*imagegris 
    

trace = numpy.zeros(img.size)

def barycentre(image):
    Y,X = numpy.where(image == 1)
    if numpy.isnan(Y.mean() + X.mean()):
        return 1,1
    else :
        return X.mean(), Y.mean()

X = []
Y = []

for n in range(10030,10060):
    img = Image.open('/home/raphael/Images/G00'+str(n)+'.JPG')
    image = numpy.array(img)
    imagegris = 0.299*image[:,:,0] + 0.587*image[:,:,1] + 0.114*image[:,:,2] 
    stack = numpy.array(imagegris - fond)
    plt.imshow(stack)
    plt.figure()
  
    
    
'''


from time import sleep
from time import time
import urllib2

t = time()


for n in range(60):
    sleep(0.9357356977462769)
    urllib2.urlopen ("http://10.5.5.9/bacpac/SH?t=motdepasse&p=%01") 
    

    

print time() -t