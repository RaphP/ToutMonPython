import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L = 200


carte = numpy.ones((L,L))

fig = plt.figure()
image = plt.imshow(carte, interpolation  = 'none', vmin = -1, vmax = 1)


pos = numpy.asarray([L/2, L/2])
deplacement = [[1,0] , [0,1] , [-1,0], [0,-1]]
direction = 0

c = 0

def updatefig(*args):
    global carte, pos, direction, c, deplacement
    c+= 1

        
    for n in range(10):
        if carte[pos[0],pos[1]] == -1:
            direction = (direction + 1)%4
        else:
            direction = (direction - 1)%4

        carte[pos[0], pos[1]] *= -1
        pos += deplacement[direction]
    

    if c == 1172 :
        carte[pos[0], pos[1]] *= -1
        pos -= deplacement[direction]
        #deplacement = [ [0,-1], [-1,0], [0,1] , [1,0]]


    
    image.set_array(carte)
    return image, 

ani = animation.FuncAnimation(fig, updatefig, interval=1)


plt.show()
