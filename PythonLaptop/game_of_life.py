import matplotlib.pyplot as plt
import numpy
import matplotlib.animation as animation

N = 100





def updateGrid(grid):
    gridPasseAuKernel = numpy.zeros((N,N))
    for d in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]:
        gridPasseAuKernel += numpy.roll(numpy.roll(grid, d[0], axis=0), d[1], axis=1)
    return ((gridPasseAuKernel == 2) + (gridPasseAuKernel == 3))*grid

TPS = []
TPSvar = []
TPSmin = []
TPSmax = [] 
P = numpy.linspace(0,1,30)
for p in P:
    T = []
    for i in range(100):
        grid = (numpy.random.random((N,N)) > p)*1
        for t in range(1000):
            grid2 = updateGrid(grid)
            if (grid == grid2).all():
                break
            else:
                grid = grid2
        T += [t]
    TPS += [numpy.mean(T)]
    TPSvar += [numpy.var(T)]
    TPSmin += [numpy.min(T)]
    TPSmax += [numpy.max(T)]
    
plt.plot(P,TPS)
plt.plot(P,TPSmin)
plt.plot(P,TPSmax)
plt.show()
    

'''
fig = plt.figure()
image = plt.imshow(grid, interpolation  = 'none', vmin = 0, vmax = 1, cmap ='gray')

def updatefig(*args):
    global grid
    grid = updateGrid(grid) 
    image.set_array(grid)
    return image,

ani = animation.FuncAnimation(fig, updatefig, interval=3)
plt.show()
'''
