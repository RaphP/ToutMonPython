import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

X =  256
Y = X

U = numpy.ones((Y,X))
V = numpy.zeros((Y,X))

U[10:80,10:80] = 0.5
U[12,13] = 0.6
V[10:80,10:80] = 0.3

fig = plt.figure()
image = plt.imshow(U, interpolation  = 'none', vmin = 0, vmax = 1)


F = 0.0002
k = 0.0005
Du = 2*10**-1
Dv = 10**-1

def updatefig(*args):
    global U, V

    cU = numpy.copy(U)
    cV = numpy.copy(V)
    for i in range(Y):
        for j in range(X):
            U[i,j] += Du*(cU[(i+1)%Y,j]+cU[i,(j+1)%X]+cU[(i-1)%Y,j]+cU[i,(j-1)%X] - 4*cU[i,j]) - cU[i,j]*cV[i,j]**2 + F*(1-cU[i,j])
            V[i,j] += Dv*(cV[(i+1)%Y,j]+cV[i,(j+1)%X]+V[(i-1)%Y,j]+cV[i,(j-1)%X] - 4*cV[i,j]) - cU[i,j]*cV[i,j]**2 - cV[i,j]*(F + k)
    
    image.set_array(U)
    return image,

ani = animation.FuncAnimation(fig, updatefig, interval=0, blit=True)


plt.show()
