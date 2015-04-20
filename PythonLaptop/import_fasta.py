f = open('chx.fasta')
f.seek(0)
data = f.read()
datap = [x  for x in data if x in ['A','T','C','G']]


fp = open('cp.txt','w')
fp.write(''.join(datap))



fp.close()

