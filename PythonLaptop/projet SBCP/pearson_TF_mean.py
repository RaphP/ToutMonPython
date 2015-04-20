import numpy
import numpy.random as random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

X = 256
Y = X

kern = [ [] for n in range(int(numpy.sqrt(X**2 + Y**2))) ]
for x in range(X):
    for y in range(Y):
        kern[int(numpy.sqrt(x**2 + y**2))] += [(y,x)]


U = numpy.ones((Y,X))
V = numpy.zeros((Y,X))
U[100:120,100:120] = 0.5 
V[100:120,100:120] = 0.25

TF = numpy.log(numpy.abs(numpy.fft.fftshift(numpy.fft.fft2(U)))**2)
f = [ sum ([TF[pos[0], pos[1]] for pos in R]) for R in kern ]

fig = plt.figure()
plt.plot(f)


F = 0.01
k = 0.05
Du = 0.10
Dv = 0.05



for t in range(100):
    
    for fabien in range(10):
        U[1:-1, 1:-1] += Du*(U[0:-2, 1:-1]+U[1:-1, 0:-2]+U[2:, 1:-1]+U[1:-1, 2:]-4*U[1:-1, 1:-1]) - (U*V*V)[1:-1, 1:-1] + ((1 - U)*F)[1:-1, 1:-1]
        V[1:-1, 1:-1] += Dv*(V[0:-2, 1:-1]+V[1:-1, 0:-2]+V[2:, 1:-1]+V[1:-1, 2:]-4*V[1:-1, 1:-1]) + (U*V*V)[1:-1, 1:-1] - ((F + k)*V)[1:-1, 1:-1]

    TF = numpy.log(numpy.abs(numpy.fft.fftshift(numpy.fft.fft2(U)))**2)
    f = [ sum ([TF[pos[0], pos[1]] for pos in R]) for R in kern ]

    plt.plot(f)









