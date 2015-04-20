import numpy
import numpy.random as random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

X = 256
Y = X

dx = 1
dy =1


B = numpy.zeros((Y,X))
N = numpy.ones((Y,X))
B[Y/2-10:Y/2+10,X/2-10:X/2+10] = 1



fig = plt.figure()
image = plt.imshow(B, interpolation  = 'none', vmin = 0, vmax = 1)



Dn = 0.10
Db = 0.15*0
Datt = 0.15
Tr = 0.01
Tc = 2*Tr



def laplacien(U):
    return (numpy.roll(U, -1, axis =0) +numpy.roll(U, 1, axis=0) -2*U )/(dx**2) + (numpy.roll(U, 1, axis = 1) +  numpy.roll(U, -1, axis=1) - 2*U )/(dy**2)  

def produit_nablas(U,V):
    return    ( ( numpy.roll(U, 1, axis=0) - numpy.roll(U,-1, axis=0) )/(2*dx) * (numpy.roll(V, 1, axis=0) - numpy.roll(V, -1, axis=0))/(2*dx) )   +  ( (numpy.roll(U, 1, axis=1) - numpy.roll(U,-1, axis=1) )/(2*dy) * (numpy.roll(V, 1, axis=1) - numpy.roll(V, -1, axis=1))/(2*dy) )  

def updatefig(*args):
    global N, B
               
    for fabien in range(10):
        B+= Db*laplacien(B) + Tr*B*N - Datt*(B*laplacien(N) + produit_nablas(N,B))
        N += Dn*laplacien(N) - Tc*N*B 


    image.set_array(B)
    return image,

ani = animation.FuncAnimation(fig, updatefig, interval=10)


plt.show()

#numpy.log(numpy.abs(numpy.fft.fftshift(numpy.fft.fft2(U)))**2)
