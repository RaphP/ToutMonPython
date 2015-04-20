import numpy
import matplotlib.pyplot as plt
from pyhull.delaunay import DelaunayTri
import mayavi.mlab as mlab
import random as r

N = 300
pts = numpy.array([  [i,j, ((N/2-i)**2 + (N/2 - j)**2 )/100 ] for i in range(N) for j in range(N)])
tri = DelaunayTri(pts[:,0:2])

z = numpy.random.rand(N*N)

colors = range(N*N)
r.shuffle(colors)
mlab.triangular_mesh(pts[:,0], pts[:,1], pts[:,2], tri.vertices, scalars = colors )
mlab.show()
'''

N = 10
x = numpy.random.rand(N+3)
y = numpy.random.rand(N+3)
x[N:] = [0,1,0.5]
y[N:] = [0, 0, 1]
z = numpy.zeros(N)

distances2 = []    
for i in range(N):
    distances2 += [[( (x[i] - x[j])**2 + (y[i] - y[j])**2  )  for j in range(N+3)]]
    
voisins = numpy.argsort(distances2)[:,1:4]

for i,voisins in enumerate(voisins):
    for j in voisins:
        plt.plot([x[i], x[j]], [y[i], y[j]])

plt.plot(x,y, 'ro')
plt.show()
'''
