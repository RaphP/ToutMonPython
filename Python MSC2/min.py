import numpy
import time
from scipy import misc

import Tkinter, tkFileDialog, os #selectione le repertoire de fichiers d'entree
root = Tkinter.Tk()
root.withdraw()
repertoire = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Selectionez le repertoire M. Chaussette')
fichiers = [os.path.join(repertoire, f) for f in sorted(os.listdir(repertoire))]

#import shutil #cree le repertoire de sortie, vide l'ancien si besoin
sortie = repertoire+'/../'
#if os.path.exists(sortie): shutil.rmtree(sortie)
#os.makedirs(sortie)


def fond(premiere, derniere, pas=1):
    image = misc.imread(fichiers[premiere])
    fond = numpy.ones(image.shape)*255
    for n in range(premiere,derniere,pas):
        image = misc.imread(fichiers[n])
        fond = (image > fond)*fond + (image <= fond)*image
    return fond

N = len(fichiers)

t = time.time()

for i in numpy.linspace(500,N,100, dtype= int):
	Fond = fond(i,i+int(N/100.),1)
	misc.imsave(sortie+'min'+str(i)+'.jpg', Fond)
	print i


print time.time() -t
