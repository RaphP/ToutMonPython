import numpy
import numpy.random as random
import matplotlib.pyplot as plt
import matplotlib.animation as animation



N = 200 #racine du nombre de points
R = 1

phi = numpy.array([numpy.linspace(0, numpy.pi , N) for i in range(N)])
teta = numpy.array([[x for n in range(N)] for x in numpy.linspace(0, 2*numpy.pi, N)])

dteta = 1
dphi = 1
dt = 1

U = numpy.ones((N,N)) #coord phi teta
V = numpy.zeros((N,N))
U[N/2-10:N/2+10,N/2-10:N/2+10] = 0.5 
V[N/2-10:N/2+10,N/2-10:N/2+10] = 0.25

fig = plt.figure()
image = plt.imshow(U, interpolation  = 'none', vmin = 0, vmax = 1)


F = 0.01 
k = 0.05
Du = 0.10
Dv = 0.05


#U -= 0.1*random.rand(Y,X)

def laplacien(U):
    return 1/R**2 * ( numpy.roll(U, -1, axis =1) +numpy.roll(U, 1, axis=1) - 2*U )/(dteta**2)

def updatefig(*args):
    global U, V
    
    for fabien in range(10):
        U += (Du*laplacien(U) - U*V*V + (1 - U)*F)*dt
        V += (Dv*laplacien(V) + U*V*V- (F + k)*V)*dt

    image.set_array(U)
    return image,

ani = animation.FuncAnimation(fig, updatefig, interval=1)
plt.show()
