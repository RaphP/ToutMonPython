import random
import numpy
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation
import time

X = 20
Y = 20


carte = numpy.zeros( (Y,X) )

for y,line in enumerate(carte):
    for x,pix in enumerate(carte):
        if random.random() > 0.5:
            carte[y][x] = 1
        else :
            carte[y][x] = -1



fig = plt.figure()
image = plt.imshow(carte, interpolation  = 'none')




def updatefig(*args):
    global carte
    x = int(random.random()*X)
    y = int(random.random()*Y)
    c = carte[y][x] + carte[(y-1)%Y][x] + carte[y][(x-1)%X] + carte[(y+1)%Y][x] + carte[y][(x+1)%X] 
    if random.random() < 0.1 and abs(c) <2 :
        carte[y][x] = carte[y][x]*-1
    else:
        if c > 0:
            carte[y][x] = 1
        else:
            carte[y][x] = -1


    
    
    image.set_array(carte)
    return image,

ani = animation.FuncAnimation(fig, updatefig, interval=0, blit=True)


plt.show()
