import matplotlib.pyplot as plt
import numpy


k = 1
n = 2
vitesse = 1.

def proba(A, B):
    return [ (A + k)**n / ( (A+k)**n + (B+k)**n )  , (B + k)**n / ( (A+k)**n + (B+k)**n ) ]


    
t = numpy.linspace(0, 15,  1000)  

A = [1]
B = [10]

for tp in t:
    A, B = numpy.append(A, A[-1] + vitesse*proba(A[-1],B[-1])[0]), numpy.append(B, B[-1] + vitesse*proba(A[-1],B[-1])[1])
    
plt.plot(A)
plt.plot(B)
plt.show()