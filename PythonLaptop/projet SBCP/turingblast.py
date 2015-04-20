import numpy
import numpy.random as random
import mayavi.mlab as mlab




N = 20 #racine du nombre de points
R = 1

phi = numpy.array([numpy.linspace(0.01, numpy.pi, N) for i in range(N)]) ##attention c'est la colatitude
teta = numpy.array([[x for n in range(N)] for x in numpy.linspace(0, 2*numpy.pi, N)])

dteta = 1 
dphi = 1
dt = 0.01

U = numpy.zeros((N,N)) + numpy.random.random((N,N))/100. #coord phi teta
V = numpy.zeros((N,N)) + numpy.random.random((N,N))/100.





a, b, c, d , mu, nu = -4, -8, 4, 7, 2, 1


#U -= 0.1*random.rand(Y,X)

def laplacien(U):
    #return 1/R**2 * 1/numpy.sin(phi)**2 * ( numpy.roll(U, -1, axis =0) +numpy.roll(U, 1, axis=0) - 2*U )/(dteta**2) + 1/R**2 * (  numpy.vstack( (numpy.ones(N), U[2:,:] +  U[:-2,:] - 2*U[1:-1,:], numpy.ones(N))  )   )/(dphi**2) #+ 1/R**2 * 1/numpy.tan(phi)*(U - numpy.roll(U, -1, axis=1) )/(dphi)   
    return   1/R**2 * (numpy.roll(U, 1, axis = 1) +  numpy.roll(U, -1, axis=1) - 2*U )/(dteta**2) 



x = R*numpy.sin(phi.flatten())*numpy.cos(teta.flatten())
y = R*numpy.sin(phi.flatten())*numpy.sin(teta.flatten())
z = R*numpy.cos(phi.flatten())


plt = mlab.points3d(x, y, z, U.flatten(), scale_mode = 'none')   
msplt = plt.mlab_source
@mlab.animate(delay=500)
def anim():
    global U, V
    while True:
    
        for fabien in range(10):
            U, V = U + ( a*U + b*V + mu*laplacien(U) )*dt, V + (c*U + d*V + nu*laplacien(V))
        
        msplt.scalars = U.flatten()
        yield  

anim()
mlab.show()
