import numpy
from scipy import sparse
from pyhull.delaunay import DelaunayTri
import mayavi.mlab as mlab

##############################
                ####triangulation

   ####creation de la surface par elevation d'un plan selon une fonction
    ### et triangulation de Delaunay


N = 40
def f(i,j): return ((N/2-i)**2)/20. 
def g(i,j):return 1 #delaunauy ne veux pas travailler avec z!=int..... mystere.
pts = numpy.asarray([  [i,j, g(i,j)] for i in range(N)  for j in range(N) ])
tri = DelaunayTri(pts[:,0:2])
pts = numpy.asarray([  [i,j, f(i,j)] for i in range(N)  for j in range(N) ])



#########################################
             ### classe triangle permetant d'avoir les valeurs sur les
            ### triangles necessaires a la construction de la matrice gerant
            ## la diffusion entre les triangles

class Triangles:
    
    def __init__(self, point, triangle, n): #n le numero du triangle.

        a, b, c = triangle[n] #indices des 3 sommets du triangle dans la liste des points
        vj = point[b] - point[a]  #le triangle a 3 voisins j,k,l
        vk = point[c] - point[b] #ces vecteurs representent les cotes
        vl = point[a] - point[c] 

        surface = numpy.linalg.norm(abs(numpy.cross(vj,vk)/2.0))
        self.surface = surface
        
        centre = (point[a]+point[b]+point[c])/3.0
        self.centre = centre
        
        self.interface_j = numpy.linalg.norm(vj) #la longueur des cotes
        self.interface_k = numpy.linalg.norm(vk)
        self.interface_l = numpy.linalg.norm(vl)


        self.voisin_j = n  ## si il est en bordure il n'echange pas
        self.voisin_k = n  ## c'est a dire il echange avec lui meme
        self.voisin_l = n  ## le numero du voisin est donc initialise a lui meme
            
        for i, trii in enumerate(triangle) : 
            if i != n:
                if a in trii and b in trii :
                    self.voisin_j = i
                if b in trii and c in trii :
                    self.voisin_k = i
                if c in trii and a in trii :
                    self.voisin_l = i
   
        self.valU = 0.5 if abs(N/2 - centre[0]) <= 4 and abs(N/2 - centre[1]) <=4  else 1.
        self.valV = 0.25 if   abs(N/2 - centre[0]) <= 4 and abs(N/2 - centre[1]) <=4 else 0.
        

        self.distance_j = 100 #on ne peux calculer les distances aux voisins
        self.distance_k = 100 #qu'une fois apres avoir initialise tout les objets
        self.distance_l = 100

    def init_distances_centres(self, triangles):

        if numpy.linalg.norm(self.centre - triangles[self.voisin_j].centre) != 0 :
            self.distance_j = numpy.linalg.norm(self.centre - triangles[self.voisin_j].centre) 
        if numpy.linalg.norm(self.centre - triangles[self.voisin_k].centre) != 0:
            self.distance_k = numpy.linalg.norm(self.centre - triangles[self.voisin_k].centre) 
        if numpy.linalg.norm(self.centre - triangles[self.voisin_l].centre) != 0:
            self.distance_l = numpy.linalg.norm(self.centre - triangles[self.voisin_l].centre) 


#on cree les objets de la classe Triangles, stocke dans le tableau triangles
triangles = [Triangles(pts, tri.vertices, i) for i in range(len(tri.vertices))]


#on calcul les distances aux proches voisins
for triangle in triangles:
    triangle.init_distances_centres(triangles)


#############################################
    ## on calcule une matrice qui applique sur le vecteur contenant les valeurs
    ## des concentrations des differents triangles de notre discretisation
    ## va renvoye la variation des concentration au temps d+dt

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


#########################################


dt = .1

F = 0.02
k = 0.05
Du = 0.10/6
Dv = 0.05/6

U = numpy.array([triangle.valU for triangle in triangles])
V = numpy.array([triangle.valV for triangle in triangles])

centres = numpy.asarray([triangle.centre for triangle in triangles] + [[0,0,0],[0,0,0]])

plt = mlab.points3d(centres[:,0], centres[:,1], centres[:,2], numpy.concatenate((U,[1,0])), scale_mode = 'none')   
msplt = plt.mlab_source

@mlab.animate(delay=10)
def anim():
    
    while True:

        global U, V
        for foo in range(100):
            U,V =  U+ (Du*matrice_diffusion.dot(U) - U*V*V + F*(1 - U))*dt, V+(Dv*matrice_diffusion.dot(V) + U*V*V- (F + k)*V)*dt 
        
        msplt.scalars = numpy.concatenate((U,[1,0]))
        yield  

anim()
mlab.show()
