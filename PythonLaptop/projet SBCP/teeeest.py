import numpy
from scipy import sparse
from pyhull.delaunay import DelaunayTri
from scipy.spatial import ConvexHull
import mayavi.mlab as mlab



pi = numpy.pi

N = 20

pts = []
R = 10.
dt = .1

for t in numpy.linspace(-pi/N,pi+pi/N,N):
    for p in numpy.linspace(0,2*pi, numpy.sin(t)*N*2):
        pts += [[R*numpy.sin(t)*numpy.cos(p),R*numpy.sin(t)*numpy.sin(p),R*numpy.cos(t)]]

pts = numpy.array(pts)

hull = ConvexHull(pts)




class Triangles:
    
    def __init__(self, point, triangle, n): #n le numero du triangle.
        #point = numpy.array(point)
        #triangle = numpy.array(triangle)
        a, b, c = triangle[n]
        vj = point[b] - point[a] 
        vk = point[c] - point[b] 
        vl = point[a] - point[c] 

        surface = numpy.linalg.norm(abs(numpy.cross(vj,vk)/2.0))
        self.surface = surface
        
        centre = (point[a]+point[b]+point[c])/3.0
        self.centre = centre
        
        self.interface_j = numpy.linalg.norm(vj) 
        self.interface_k = numpy.linalg.norm(vk)
        self.interface_l = numpy.linalg.norm(vl)


        self.voisin_j = n  ## si il est en bordure il n'echange pas
        self.voisin_k = n  ## c'est a dire il echange avec lui meme 
        self.voisin_l = n
            
        for i, trii in enumerate(triangle) : 
            if i != n:
                if a in trii and b in trii :
                    self.voisin_j = i
                if b in trii and c in trii :
                    self.voisin_k = i
                if c in trii and a in trii :
                    self.voisin_l = i

        self.valU = 0.5 if centre[0] >= 0.9*R  else 1.
        self.valV = 0.25 if   centre[0] >= 0.9*R else 0.

        self.distance_j = 100
        self.distance_k = 100
        self.distance_l = 100

    def init_distances_centres(self, triangles):

        if numpy.linalg.norm(self.centre - triangles[self.voisin_j].centre) != 0 :
            self.distance_j = numpy.linalg.norm(self.centre - triangles[self.voisin_j].centre) 
        if numpy.linalg.norm(self.centre - triangles[self.voisin_k].centre) != 0:
            self.distance_k = numpy.linalg.norm(self.centre - triangles[self.voisin_k].centre) 
        if numpy.linalg.norm(self.centre - triangles[self.voisin_l].centre) != 0:
            self.distance_l = numpy.linalg.norm(self.centre - triangles[self.voisin_l].centre) 




    def val(self):
        print 'surface = '+ str(self.surface)
        print 'interfaces = ' + str([self.interface_j, self.interface_k, self.interface_l])
        print 'voisins = ' + str([self.voisin_j, self.voisin_k, self.voisin_l])

'''
tri = DelaunayTri(pts[:,0:2])
triangles = [Triangles(pts, tri.vertices, i) for i in range(len(tri.vertices))]
'''

triangles = [Triangles(pts, hull.simplices, i) for i in range(len(hull.simplices))]





for triangle in triangles:
    triangle.init_distances_centres(triangles)


I= []
J = []
V = []

for i, triangle in enumerate(triangles):
    I += [i]
    J += [i] 
    V +=  [-1/triangle.surface*(triangle.interface_j/triangle.distance_j + triangle.interface_k/triangle.distance_k + triangle.interface_l/triangle.distance_l)]

    I += [i]
    J += [triangle.voisin_j] 
    V += [(triangle.interface_j/triangle.distance_j)/triangle.surface]

    I += [i]
    J += [triangle.voisin_k] 
    V += [(triangle.interface_k/triangle.distance_k)/triangle.surface]

    I += [i]
    J += [triangle.voisin_l] 
    V += [(triangle.interface_l/triangle.distance_l)/triangle.surface]

matrice_diffusion = sparse.coo_matrix((V,(I,J)), shape=(len(triangles),len(triangles)))



U = numpy.array([triangle.valU for triangle in triangles])
U += numpy.random.rand(len(U))*0.1
V = numpy.array([triangle.valV for triangle in triangles])
F = 0.038
k = 0.061
Du = 0.10
Dv = 0.05

centres = numpy.asarray([triangle.centre for triangle in triangles] + [[0,0,0],[0,0,0]])
surfaces = numpy.array([tri.surface for tri in triangles])

plt = mlab.points3d(centres[:,0], centres[:,1], centres[:,2], numpy.concatenate((U,[1,0])), scale_mode = 'none')   
msplt = plt.mlab_source

@mlab.animate(delay=10)
def anim():
    
    while True:

        global U, V
        for foo in range(100):
            U,V =  U+ (Du*matrice_diffusion.dot(U) - U*V*V + F*(1 - U))*dt, V+(Dv*matrice_diffusion.dot(V) + U*V*V- (F + k)*V)*dt
            #U,V =  U+ (Du*matrice_diffusion.dot(U))*dt, V+(Dv*matrice_diffusion.dot(V))*dt 
        
        msplt.scalars = numpy.concatenate((U,[1,0]))
        yield  

anim()
mlab.show()


def affiche_triangles():
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(pts[:,0], pts[:,1], tri.vertices, pts[:,2] ) #si je supprime tri.vertice il triangule tout seul
    ax.scatter(centres[:,0], centres[:,1], color = 'r')
    plt.show()
    
