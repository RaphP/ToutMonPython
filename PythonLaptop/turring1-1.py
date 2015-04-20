import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

e = 0.000001

X1 = 1 +3*e
Y1 = 1 + e
X2 = 1 - 3*e
Y2 = 1 - e
x = [[X1],[X2]]
y = [[Y1],[Y2]]

dt = 1

for t in range(3):
    X1, X2, Y1, Y2 = X1+ (5*X1 - 6*Y1 +1 + 0.5*(X2-X1))*dt,X2 + (5*X2 - 6*Y2 +1 - 0.5*(X2-X1))*dt, Y1+ (6*X1 - 7*Y1 +1 + 4.5*(Y2 - Y1))*dt, Y2+ (6*X2 -7*Y2 +1 + 4.5*(Y1-Y2))*dt
    X1, X2, Y1, Y2 = max(0,X1), max(0,X2), max(0,Y1), max(0,Y2)
    x[0] += [X1]
    x[1] += [X2]
    y[0] += [Y1]
    y[1] += [Y2]

plt.plot(x[0])
plt.plot(x[1])
plt.show()

