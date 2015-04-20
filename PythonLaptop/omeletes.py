
import numpy
import random
import matplotlib.pyplot as plt
import math

dt = 1
Tmax = 1000

#t va de 0 a Tmax par pas de dt

s = [0]


for i in range(Tmax):
	s += [s[-1] + (1 -2*random.randint(0,1)) ]



def phi(t):
	return 2*t*math.exp(-t**2)


def T(b,a) :
	Dt = 3*a

	T = 0
	for t in range(b-Dt, b+Dt):
		T+= s[t]*phi( (t-b)/a )	
	
	return T


#plt.plot(f)
#plt.show()


map = numpy.empty([200,int(Tmax)])

for a in range(10, 200):
	print a 
	Dt = 3*a
	for b in range(0+Dt, Tmax - Dt):
		map[a-10][b] = T(b,a)


plt.imshow(map)

plt.show()




