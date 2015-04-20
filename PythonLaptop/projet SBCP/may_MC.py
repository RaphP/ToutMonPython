import matplotlib.pyplot as plt 
import random
from numpy import *

Ninit =100
 
dt = 0.001
pnaissance = 1*dt
pmort = 0.5*dt/(Ninit)



Tps = 1000

for i in range(1):

    N = [Ninit]
    for t in range(int(Tps/dt)):
        nmorts = 0
        nnaissances = 0
        for individu in range(N[-1]):
            if random.random() < pnaissance:
                nnaissances += 1
            if random.random() < pmort*N[-1]:
                nmorts += 1
        N += [N[-1] + nnaissances - nmorts]

    plt.plot(linspace(0,Tps,len(N)),N)

plt.show()
