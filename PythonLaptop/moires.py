import matplotlib.pyplot as plt
import numpy

N = 200

carte = numpy.zeros((N,N))

for y in range(N):
    for x in range(N):
        carte[y,x] = 1- int(x%5==0 or y%5==0)

plt.imshow(carte, cmap='gray', interpolation = 'none')

plt.show()
