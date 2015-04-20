f= open('cp.txt')

data = f.read(10000)

f.close()

marcheur = [0]

for a in data:
        if a in ['A','G']:
                marcheur += [marcheur[-1] + 1]
        if a in ['C','T'] :
                marcheur += [marcheur[-1] -1]


import numpy

import random
import matplotlib.pyplot as plt
import math

Tmax = 10000
t = numpy.arange(Tmax)

#t va de 0 a Tmax par pas de dt

s = [0]


for i in range(Tmax):
        s += [s[-1] + (1 -2*random.randint(0,1)) ]

f = numpy.cos(t/200.0) + t/10*numpy.sin(t/300.0) 


def phi(a):
        return [2.0*t/a*math.exp(-(t/a)**2) for t in range(-100,100)] 


map = []

for a in range(1,1500):
	map += [numpy.convolve(marcheur,phi(1.0*a), mode = 'valid')]

plt.plot(marcheur)



fig, ax = plt.subplots()
#ax.set_yscale('log', basey=2)



ax.imshow(map, interpolation = 'none')

plt.show()
