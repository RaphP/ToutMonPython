import numpy as numpy
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
import math
import random

FFMpegWriter = manimation.writers['mencoder']
metadata = dict(title='Movie Test', artist='Matplotlib',
        comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)


X = 200
Y = 200
N = 1000

carte = numpy.zeros( (Y,X) )


fig = plt.figure()
image = plt.imshow(carte, interpolation  = 'none', vmax = N)

dt = 1
R = 10
cercle = []
for i in range(R):
    for j in range(R):
        if (i**2 + j**2) < R:
            cercle += [(i,j),(-i,j),(i,-j),(-i,-j)]

class Individu(object):
    
    def __init__(self, color):
        self.posx = random.random()*X
        self.posy = random.random()*Y

        teta = random.random()*2*math.pi
        self.angle = teta
        self.vx = math.cos(teta)
        self.vy = math.sin(teta)

        self.color = color

        self.poids = 5

    def avance(self):
        self.posx = (self.posx + self.vx*dt )% X
        self.posy = (self.posy + self.vy*dt) % Y

    def change_direction(self):
        self.vx = math.cos(self.angle)
        self.vy = math.sin(self.angle)

    def position(self):
        return [self.posx, self.posy]

    def encarte(self):
        global carte
        carte[self.posy][self.posx] = self.color

    def colision(self):
        return [ population[int(j)] for j in [ carte[ (self.posx + i[0])%Y ][(self.posy + i[1])%X ] for i in cercle if (carte[ (self.posx + i[0])%Y ][(self.posy + i[1])%X ] != 0) ] if j != self.color]  

    def reoriente(self, autres):
        self.angle = ( sum([individu.angle for individu in autres])/len(autres) + self.poids*self.angle )/(self.poids + 1)
        self.change_direction()
        


population = [Individu(i) for i in range (N)]

with writer.saving(fig, "writer_test.mp4", 100):
    for n in range(100):
            carte = numpy.zeros( (Y,X) )
            for individu in population :
                if individu.colision() != [] :
                    individu.reoriente(individu.colision())
            
                individu.avance()
                individu.encarte()

    image.set_array(carte)
    writer.grab_frame()
