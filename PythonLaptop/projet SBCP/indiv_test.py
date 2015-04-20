import random
import numpy
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation
import time

X = 100
Y = 100
N = 400

carte = numpy.zeros( (Y,X) )

carte[0,0] = N
fig = plt.figure()
image = plt.imshow(carte, interpolation  = 'none')
carte[0,0] = 0

R = 5
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
        self.vx = math.cos(teta)
        self.vy = math.sin(teta)

        self.color = color

        self.poids = 1

    def avance(self):
        self.posx = (self.posx + self.vx )% X
        self.posy = (self.posy + self.vy) % Y

    def change_direction(self, angle):
        self.vx = math.cos(angle)
        self.vy = math.sin(angle)

    def position(self):
        return [self.posx, self.posy]

    def encarte(self):
        global carte
        carte[self.posy][self.posx] = self.color

    def colision(self):
        return [ population[int(j)] for j in [ carte[ (self.posx + i[0])%Y ][(self.posy + i[1])%X ] for i in cercle if (carte[ (self.posx + i[0])%Y ][(self.posy + i[1])%X ] != 0) ] if j != self.color]  

    def reoriente(self, autres):
        self.vx = ( sum([individu.vx for individu in autres])/len(autres) + self.poids*self.vx )/(self.poids + 1)
        self.vy = ( sum([individu.vy for individu in autres])/len(autres) + self.poids*self.vy )/(self.poids + 1)
        


population = [Individu(i) for i in range (N)]

a = time.time()
c = 0

for k in range(1002):
    c+= 1
    if c == 1000:
        print time.time() - a
    carte = numpy.zeros( (Y,X) )
    for individu in population :
        if individu.colision() != [] :
            individu.reoriente(individu.colision())
            
        individu.avance()
        individu.encarte()


#ani = animation.FuncAnimation(fig, updatefig, interval=0, blit=True)


plt.show()
