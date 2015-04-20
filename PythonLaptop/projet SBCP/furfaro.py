import numpy
import numpy.random as random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

X = 30
Y = X


U = numpy.ones((Y,X))
V = numpy.zeros((Y,X))
U[14:17,14:17] = 0.5 
V[14:17,14:17] = 0.25
'''
U = numpy.random.rand(Y,X)
V = numpy.random.rand(Y,X)/2.0
'''

fig = plt.figure()
image = plt.imshow(U, interpolation  = 'none', vmin = 0, vmax = 1)


F = 0.02
k = 0.05
Du = 0.10
Dv = 0.05


#U -= 0.1*random.rand(X,Y)


def updatefig(*args):
    global U, V
    
    for fabien in range(10):
        
        U[1:-1, 1:-1] += Du*(U[0:-2, 1:-1]+U[1:-1, 0:-2]+U[2:, 1:-1]+U[1:-1, 2:]-4*U[1:-1, 1:-1]) - (U*V*V)[1:-1, 1:-1] + ((1 - U)*F)[1:-1, 1:-1]
        V[1:-1, 1:-1] += Dv*(V[0:-2, 1:-1]+V[1:-1, 0:-2]+V[2:, 1:-1]+V[1:-1, 2:]-4*V[1:-1, 1:-1]) + (U*V*V)[1:-1, 1:-1] - ((F + k)*V)[1:-1, 1:-1]

    
    image.set_array(U)
    return image,

ani = animation.FuncAnimation(fig, updatefig, interval=10)


plt.show()

#numpy.log(numpy.abs(numpy.fft.fftshift(numpy.fft.fft2(U)))**2)
