import numpy


L = 1000


carte = numpy.ones((L,L))



pos = numpy.asarray([L/2, L/2])
deplacement = [[1,0] , [0,1] , [-1,0], [0,-1]]
direction = 0

for n in range(10000):
    if carte[pos[0],pos[1]] == -1:
        direction = (direction + 1)%4
    else:
        direction = (direction - 1)%4

    carte[pos[0], pos[1]] *= -1
    pos += deplacement[direction]

