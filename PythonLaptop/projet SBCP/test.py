import numpy
from mayavi.mlab import *



x = [[0,1,2],[4,5,6]]
y = [[0,1,2] , [4,5,8] ]
z = [[0,0,0] , [0,0,0] ]
mesh(x, y, z)
show()
