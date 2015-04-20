import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def laplacien(dx,y):
    return (numpy.roll(y,1) + numpy.roll(y,-1) - 2*y)/dx

#x = numpy.linspace(1,3,1000)
x = numpy.concatenate((numpy.linspace(1,2,100), numpy.linspace(2,3,10)))
y = (x-1.5)**2

dx =  numpy.roll(x,-1) - x
dx[-1] = dx[-2]

fig = plt.figure()
courbe, = plt.plot(x,y)


dt = 0.001
D = 0.1


def updatefig(*args):
    global y
    for i in range(1000) : y += D*laplacien(x,y)*dt
    courbe.set_ydata(y)
    return courbe,

ani = animation.FuncAnimation(fig, updatefig, interval=1)
plt.show()







