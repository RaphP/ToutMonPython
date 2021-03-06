import numpy
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import Tkinter, tkFileDialog, os #selectione le repertoire de fichiers d'entree
root = Tkinter.Tk()
root.withdraw()
repertoireIm = tkFileDialog.askdirectory(parent=root,initialdir="/home/raul/Desktop",title='Selectionez le repertoire images M. Chaussette')
fichiers = [os.path.join(repertoireIm, f) for f in sorted(os.listdir(repertoireIm))]

root = Tkinter.Tk()
root.withdraw()
repertoireBar = tkFileDialog.askdirectory(parent=root,initialdir="/home/raul/Desktop",title='Selectionez le repertoire barycentre M. Chaussette')


X = numpy.load(repertoireBar+'/X.npy')
Y = numpy.load(repertoireBar+'/Y.npy')



fig = plt.figure()
im = plt.imshow(misc.imread(fichiers[301]), cmap='gray')

i = 1000

def updatefig(*args):
    global i
    ima = misc.imread(fichiers[i])
    ima[Y[i-1000]:Y[i-1000]+10,X[i-1000]:X[i-1000]+10] = 100
    im.set_array(ima)
    i+=1
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=1, blit=True)
plt.show()
