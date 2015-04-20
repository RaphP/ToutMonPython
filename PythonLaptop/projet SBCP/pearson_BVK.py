import numpy
import numpy.random as random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

X = 100
Y = 100
dx = 1.
dy = 1. #si ils sont trops petits on a des instabilites numeriques (dx=1 dy=X/Y X=256/ Y=505 c'est une limite d'instabilite... ) Si ils sont trop grands aussi...
dt = 1.
if dt/(dx**2) > 2 or dt/(dy**2) > 2:
    print 'il faut reduire dt'

U = numpy.ones((Y,X))
V = numpy.zeros((Y,X))
U[Y/2-2:Y/2 +2,X/2 -4:X/2 +4] = 0.5 
V[Y/2-2:Y/2 +2,X/2 -4:X/2 +4] = 0.25




fig = plt.figure()
image = plt.imshow(U, interpolation  = 'none', vmin = 0, vmax = 1, cmap ='gray')


F = 0.038
k = 0.061
Du = 0.10
Dv = 0.05


U -= 0.1*random.rand(Y,X)
#V += 0.1*random.rand(Y,X)

def laplacien(U):
    return (numpy.roll(U, -1, axis =0) +numpy.roll(U, 1, axis=0) -2*U )/(dx**2) + (numpy.roll(U, 1, axis = 1) +  numpy.roll(U, -1, axis=1) - 2*U )/(dy**2)  

def updatefig(*args):
    global U, V
    
    for fabien in range(100):
        U += (Du*laplacien(U) - U*V*V + (1 - U)*F)*dt
        U -= random.rand(Y,X)*0.001
        V += (Dv*laplacien(V) + U*V*V- (F + k)*V)*dt
        
    image.set_array(U)
    return image,

ani = animation.FuncAnimation(fig, updatefig, interval=1)


plt.show()
