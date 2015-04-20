import numpy
from mayavi import mlab



t = numpy.linspace(0, 4 * numpy.pi, 20)
cos = numpy.cos
sin = numpy.sin
x = sin(2 * t)
y = cos(t)
z = cos(2 * t)
s = 2 + sin(t)

plt = mlab.points3d(x, y, z, s, scale_mode = 'none')

    


msplt = plt.mlab_source
@mlab.animate(delay=100)
def anim():
    while True:
        msplt.scalars =  numpy.roll(msplt.scalars, 1)
        yield
    
anim()
mlab.show()
