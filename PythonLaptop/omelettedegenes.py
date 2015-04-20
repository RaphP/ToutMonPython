import matplotlib.pyplot as plt


f= open('cp.txt')

data = f.read(10000000)

f.close()

marcheur = [0]

for a in data:
	if a in ['A','G']:
		marcheur += [marcheur[-1] + 1]
	if a in ['T','C'] :
		marcheur += [marcheur[-1] -1] 


plt.plot(marcheur)
plt.show()
