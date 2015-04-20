import numpy
import matplotlib.pyplot as plt

N = 600

X = 256
Y = X


F = 0.035
k = 0.06
Du = 0.10
Dv = 0.05




for k in numpy.arange(0, 0.1, 0.005):
    for F in numpy.arange(0, 0.1, 0.005):
        
        U = numpy.ones((Y,X))
        V = numpy.zeros((Y,X))
        U[100:120,100:120] = 0.5 
        V[100:120,100:120] = 0.25

        for fabien in range(N):
                U[1:-1, 1:-1] += Du*(U[0:-2, 1:-1]+U[1:-1, 0:-2]+U[2:, 1:-1]+U[1:-1, 2:]-4*U[1:-1, 1:-1]) - (U*V*V)[1:-1, 1:-1] + ((1 - U)*F)[1:-1, 1:-1]
                V[1:-1, 1:-1] += Dv*(V[0:-2, 1:-1]+V[1:-1, 0:-2]+V[2:, 1:-1]+V[1:-1, 2:]-4*V[1:-1, 1:-1]) + (U*V*V)[1:-1, 1:-1] - ((F + k)*V)[1:-1, 1:-1]
    
        plt.imsave('F=' +str(F)+ '-k=' + str(k) +'-N=' + str(N)+'.png' , U, vmin = 0, vmax = 1)
