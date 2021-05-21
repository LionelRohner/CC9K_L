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
cBase = np.random.choice([65,67,85,71],80)

c = 80
it = 1
total = 3456895
mudolo = total % 80
r = (total // c) // it

print(mudolo)
print(r)
print((r*80)+mudolo)

quit()

def float2base(preAlloc):
    # Create boolean masks
    A = preAlloc < 0.25
    T = ((preAlloc > 0.25) & (preAlloc < 0.5))
    G = ((preAlloc > 0.5) & (preAlloc < 0.75))
    C = ((preAlloc > 0.75) & (preAlloc < 1))
    return(A,T,G,C)

f=open('HG1.fasta','a')

# preallocate numbers
preAlloc = np.random.random(r*80).reshape(r, 80)



# Project boolean mask to random number array
seqs = np.where(A, "A", np.where(T, "T", np.where(G, "G", np.where(C, "C", 0))))

np.savetxt(f, seqs, delimiter="", fmt="%s")

# f = open('HG1.fasta', 'a')
# for i in range(0, it):


algoN = "A1"
algo = """
import numpy as np


c = 80
it = 1
total = 8000000
r = (total // c) // it

f=open('HG1.fasta','a')
for i in range(0, it):
    # preallocate numbers
    preAlloc = np.random.random(total//it).reshape(r,80)

    # Create boolean masks
    A = preAlloc < 0.25
    T = ((preAlloc > 0.25) & (preAlloc < 0.5))
    G = ((preAlloc > 0.5) & (preAlloc < 0.75))
    C = ((preAlloc > 0.75) & (preAlloc < 1))
    
    # Project boolean mask to random number array
    seqs = np.where(A,"A",np.where(T,"T", np.where(G, "G", np.where(C,"C",0))))
    np.savetxt(f, seqs, delimiter="", fmt="%s")

"""

benchMarkus.getDaReps(algo = algo, algoN = algoN, nIter=2)

#############

# IDEA: Same as above, but instead of using np.savetxt, which goes

algoN = "A2"
algo = """
import numpy as np

c = 80
it = 1
total = 8000000
r = (total // c) // it

for i in range(0, it):
    # preallocate numbers
    preAlloc = np.random.random(total//it).reshape(r,c)

    # Create boolean masks
    A = preAlloc < 0.25
    T = ((preAlloc > 0.25) & (preAlloc < 0.5))
    G = ((preAlloc > 0.5) & (preAlloc < 0.75))
    C = ((preAlloc > 0.75) & (preAlloc < 1))

    # Project boolean mask to random number array
    seqs = np.where(A,"A",np.where(T,"T", np.where(G, "G", np.where(C,"C",0))))
    np.save("HG2.fasta", seqs)

data = np.load('C:/Users/stryc/OneDrive/GitHub/Projects/CC9K/Phase III/Python/HG2.fasta.npy')
f=open('HG2.fasta','w')
np.savetxt(f, np.squeeze(data), delimiter="", fmt="%s")

"""

benchMarkus.getDaReps(algo = algo, algoN = algoN, nIter=2)


##################

algoN = "A3"
algo = """
import numpy as np

cBase = np.random.choice(["A","T","G","C"],80)

f=open('HG3.fasta','a')
for i in range(1,100000):
    np.savetxt(f, np.random.choice(["A", "T", "G", "C"], 80).reshape(1,80), delimiter="", fmt="%s")

"""

benchMarkus.getDaReps(algo = algo, algoN = algoN, nIter=2)
quit()
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
