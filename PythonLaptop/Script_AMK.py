
fichier = file('TP271114.TXT')

###################################################
import matplotlib.pyplot as plt
import numpy

ScanNum = []
MeVo = []
ReVo = []
CoVo = []
Cu = []
CuEr = []
ThCu = []

line = fichier.readline() #la comande readline va a la ligne
while line[0:4] != 'Scan' : #Il va chercher la ligne ou il y a Scan Num etc...
    line = fichier.readline() 

print line

line = fichier.readline()
while line != '': #lit jusque la fin
    line = line.replace(',', '.') #change les virgules en points
    line = line.split() #separe la chaine de caractere au endroit ou il y a un espace

    ScanNum += [float(line[0])]
    MeVo += [float(line[1])]
    ReVo += [float(line[2])]
    CoVo += [float(line[3])]
    Cu += [float(line[4])]
    CuEr += [float(line[5])]
    ThCu += [float(line[6])]

    line = fichier.readline()


################################################################################



# ce sont tes tableaux de donnes, Mesured Voltage etc..
#pour acceder a un element c'est MeVo[3] si tu veux le 4 eme element (ca commence a 0)
# pour acceder aux elements du 1er (indice 0) au 5 eme (indice 4) c'est : MeVo[0:5]

MeVo = numpy.asarray(MeVo)
ReVo = numpy.asarray(ReVo)
CoVo = numpy.asarray(CoVo)
Cu = numpy.asarray(Cu)
CuEr = numpy.asarray(CuEr)
ThCu = numpy.asarray(ThCu)




## Un exemple : Le tracer de la puissance (U*I)
fig, ax = plt.subplots()


for spine in ['left', 'bottom']:
    ax.spines[spine].set_position('zero')

# Hide the other spines...  
for spine in ['right', 'top']:
    ax.spines[spine].set_color('none')

ax.axis([-60, 40, -2, 12])
ax.grid()


ax.plot(CoVo, Cu)
ax.set_title('Caracteristique courant tension')

ax.set_xlabel('potentiel (V)')
ax.set_ylabel('courant (mA)')


plt.show()
#comme tu peux le voir tu manipule les tableaux comme si c'etait des nombres :)
#ca marche aussi avec les fonctions ( cos(MeVo) c'est possible)
# c'est la librairie numpy qui permet ca, regarde sur google si tu as des questions

 





    
