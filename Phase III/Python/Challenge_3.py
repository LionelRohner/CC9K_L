###################################################################################################################
# Modules

import numpy as np
import random as rd
import BenchPress as bp


###################################################################################################################
# BenchMarkus

data = {
    "A1": [],
    "A2": [],
    "A3": [],
    "A4": []
}

benchMarkus = bp.BenchPress(data = data, benchMeth = "Lionel")

preAlloc = np.random.random(10).reshape(1, 10)

# Create boolean masks
A = preAlloc < 0.25
T = ((preAlloc > 0.25) & (preAlloc < 0.5))
G = ((preAlloc > 0.5) & (preAlloc < 0.75))
C = ((preAlloc > 0.75) & (preAlloc < 1))

# Project boolean mask to random number array
seq = np.where(A,"A",np.where(T,"T", np.where(G, "G", np.where(C,"C",0))))
print(seq)


quit()
# dists[(np.where((dists >= r) & (dists <= r + dr)))]


seqs = np.where(preAlloc < 0.25, "A", preAlloc)
print(seqs)
seqs2 = np.where(seqs < 0.5 , "T", seqs)
print(seqs)
seqs3 = np.where(seqs2 < 0.75, "G", "C")
print(seqs)
quit()
# import numpy as np
# c = 80
# it = 2
# total = 8000
# r = (total // c) // it
#
# f=open('HG1.fasta','a')
# for i in range(0, it):
#     preAlloc = np.random.random(total//it).reshape(r,c)
#     seqs = np.where(preAlloc < 0.5, rd.choice("AT"), rd.choice("GC"))
#     np.savetxt(f, seqs, delimiter="", fmt="%s")
# quit()

algoN = "A1"
algo = """
import numpy as np
import random as rd

c = 80
it = 1
total = 8000
r = (total // c) // it

f=open('HG1.fasta','a')
for i in range(0, it):
    preAlloc = np.random.random(total//it).reshape(r,c)
    seqs = np.where(preAlloc < 0.5, rd.choice("AT"), rd.choice("GC"))
    np.savetxt(f, seqs, delimiter="", fmt="%s")

"""

benchMarkus.getDaReps(algo = algo, algoN = algoN)

#############

algoN = "A2"
algo = """
import numpy as np
import random as rd

c = 80
it = 2
total = 8000
r = (total // c) // it

f=open('HG2.fasta','a')
for i in range(0, it):
    preAlloc = np.random.random(total//it).reshape(r,c)
    seqs = np.where(preAlloc < 0.5, rd.choice("AT"), rd.choice("GC"))
    np.savetxt(f, seqs, delimiter="", fmt="%s")
"""

benchMarkus.getDaReps(algo = algo, algoN = algoN)

##################

algoN = "A3"
algo = """
import numpy as np
import random as rd

c = 80
it = 4
total = 8000
r = (total // c) // it

f=open('HG3.fasta','a')
for i in range(0, it):
    preAlloc = np.random.random(total//it).reshape(r,c)
    seqs = np.where(preAlloc < 0.5, rd.choice("AT"), rd.choice("GC"))
    np.savetxt(f, seqs, delimiter="", fmt="%s")

"""

benchMarkus.getDaReps(algo = algo, algoN = algoN)

#####################

algoN = "A4"
algo = """
import numpy as np
import random as rd

c = 80
it = 8
total = 8000
r = (total // c) // it

f=open('HG4.fasta','a')
for i in range(0, it):
    preAlloc = np.random.random(total//it).reshape(r,c)
    seqs = np.where(preAlloc < 0.5, rd.choice("AT"), rd.choice("GC"))
    np.savetxt(f, seqs, delimiter="", fmt="%s")

"""

benchMarkus.getDaReps(algo = algo, algoN = algoN)
