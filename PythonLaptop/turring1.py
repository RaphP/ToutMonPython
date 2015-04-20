import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 61
teta = numpy.linspace(0,2*numpy.pi,N)
pX = 10*numpy.cos(teta)
pY = 10*numpy.sin(teta)

I = 0

#a, b, c, d, mu, nu, dt  = 1, 1, 1, 1, .25, .25, .05

#a, b, c, d, mu, nu, dt  = 2, 1, -1, 2, .25, .25 , 0.5

#a, b ,c ,d, mu, nu, dt = I-1, 1, -1, I, 0, 1, 0.5

a, b ,c ,d, mu, nu, dt = I - 2, 2.5, -1.25, I+1.5, (N/2/numpy.pi)**2, (N/2/numpy.pi)**2*0.5, 0.01



X = numpy.zeros(N)  + (numpy.random.random(N) - 0.5)/100000.
Y = numpy.zeros(N)  + (numpy.random.random(N)-0.5)/100000.

X[15] = 0.0001
Y[15] = 0.00013

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=False, sharey=False)
ax1.scatter(pX, pY, c=X, s= 100)
ax2.scatter(pX, pY, c=Y, s= 100)
ax3.plot(X)
ax4.plot(Y)

def laplacien(X):
    return (numpy.roll(X,1) + numpy.roll(X,-1) - 2*X)


def onclick(event):
    global X,Y, Xmem, dt
    
    for n in range(100):
        dt = min(min(abs(X/10./(a*X + b*Y + mu*laplacien(X)))), min(abs(Y/10./(c*Y + d*Y + nu*laplacien(Y)))) )
        X, Y = X + (a*X + b*Y + mu*laplacien(X))*dt, Y + (c*Y + d*Y + nu*laplacien(Y))*dt

    ax3.clear()
    ax4.clear()
    ax1.scatter(pX, pY, c=X, s= 100)
    ax2.scatter(pX, pY, c=Y, s= 100)
    ax3.plot(range(0,N),X)
    ax4.plot(range(0,N),Y)
    f.canvas.draw()

    

cid = f.canvas.mpl_connect('key_press_event', onclick)

plt.show()



