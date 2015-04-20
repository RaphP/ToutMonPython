import numpy
from pyhull.delaunay import DelaunayTri
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


N = 5
def f(i,j): return ((N/2-i)**2 + (N/2 - j)**2 )/N
def g(i,j): return 1
pts = numpy.array([  [i,j, g(i,j) ] for i in range(N) for j in range(N)])





class Triangles:
    
    def __init__(self, point, triangle, n): #n le numero du triangle.
        point = numpy.array(point)
        triangle = numpy.array(triangle)
        a, b, c = triangle[n]
        vj = point[b] - point[a] 
        vk = point[c] - point[b] 
        vl = point[a] - point[c] 

        self.surface = numpy.linalg.norm(abs(numpy.cross(vj,vk)/2.0))

        self.centre = (point[a]+point[b]+point[c])/3.0

        self.interface_j = numpy.linalg.norm(vj)
        self.interface_k = numpy.linalg.norm(vk)
        self.interface_l = numpy.linalg.norm(vl)

        self.voisin_j = n  ## si il est en bordure il n'echange pas
        self.voisin_k = n  ## c'est a dire il echange avec lui meme 
        self.voisin_l = n
            
        for i, trii in enumerate(triangle) : #on dirait qu'il y a un probleme.... voir triangles[8].val() ==> deux fois le meme voisin....
            if i != n:
                if a in trii and b in trii :
                    self.voisin_j = i
                if b in trii and c in trii :
                    self.voisin_k = i
                if c in trii and a in trii :
                    self.voisin_l = i

    def val(self):
        print 'surface = '+ str(self.surface)
        print 'interfaces = ' + str([self.interface_j, self.interface_k, self.interface_l])
        print 'voisins = ' + str([self.voisin_j, self.voisin_k, self.voisin_l])

tri = DelaunayTri(pts[:,0:2])
triangles = [Triangles(pts, tri.vertices, i) for i in range(len(tri.vertices))]


dt = 1
D = 1

matrice_laplacien = numpy.zeros((len(tri.vertices), len(tri.vertices)))

for i, triangle in enumerate(triangles):
    matrice_laplacien[i,i] += 1 - D*dt/triangle.surface*(triangle.interface_j + triangle.interface_k + triangle.interface_l)
    matrice_laplacien[i, triangle.voisin_j] += D*dt*(triangle.interface_j/triangles[triangle.voisin_j].surface)
    matrice_laplacien[i, triangle.voisin_k] += D*dt*(triangle.interface_k/triangles[triangle.voisin_k].surface)
    matrice_laplacien[i, triangle.voisin_l] += D*dt*(triangle.interface_l/triangles[triangle.voisin_l].surface)

U = numpy.ones(len(matrice_laplacien))
V = numpy.zeros(len(matrice_laplacien))
F = 0
k = 0

centres = numpy.asarray([triangle.centre for triangle in triangles])


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(pts[:,0], pts[:,1], tri.vertices, pts[:,2] ) #si je supprime tri.vertice il triangule tout seul
ax.scatter(centres[:,0], centres[:,1], color = 'r')
plt.show()


