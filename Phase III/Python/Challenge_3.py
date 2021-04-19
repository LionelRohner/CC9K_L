###################################################################################################################
# Modules

import numpy as np
import random as rd
import BenchPress as bp


###################################################################################################################
# BenchMarkus

data = {
    "A1"     : [],
    "A2"    : [],
    "A3"    : [],
    "A3.1"  : [],
    "A4"    : [],
    "A4.1"  : [],
    "A4.2"  : [],
    "A_flex": [],
    "AlgoNenad": []
}

benchMarkus = bp.BenchPress(data=data, benchMeth="Lionel")

###################################################################################################################
# Algo 1

# Idea: create a numpy array of dim(x,80) with uniformly drawn random floats between 0 and 1. Create a 4 boolean masks
#       for A, T, G and C. All floats between 0 and 0.25 are A and so on. np.where is used to project boolean mask onto
#       float matrix.

algoN = "A1"
algo = """
import numpy as np


c = 80
it = 4
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

benchMarkus.getDaReps(algo = algo, algoN = algoN, nIter=10)


###################################################################################################################
# Algo 2

# IDEA: Same as above, but instead of using np.savetxt, I first use np.save, which saves bytes rather than text thus
#       formatting. In a second step, the npy file is converted to a txt file
# algoN = "A2"
# algo = """
# import numpy as np
#
#
# c = 80
# total = 8000000
# r = (total // c)
#
# # preallocate numbers
# preAlloc = np.random.random(total).reshape(r,c)
#
# # Create boolean masks
# A = preAlloc < 0.25
# T = ((preAlloc > 0.25) & (preAlloc < 0.5))
# G = ((preAlloc > 0.5) & (preAlloc < 0.75))
# C = ((preAlloc > 0.75) & (preAlloc < 1))
#
# # Project boolean mask to random number array
# seqs = np.where(A,"A",np.where(T,"T", np.where(G, "G", np.where(C,"C",0))))
# np.save("HG2.fasta", seqs)
#
# # data = np.load('C:/Users/stryc/OneDrive/GitHub/Projects/CC9K/Phase III/Python/HG2.fasta.npy')
# # f=open('HG2.fasta','w')
# # np.savetxt(f, np.squeeze(data), delimiter="", fmt="%s")
#
# """
#
# benchMarkus.getDaReps(algo=algo, algoN=algoN, nIter=10)


###################################################################################################################
# Algo 3

algoN = "A3"
algo = """
import numpy as np

f=open('HG3.fasta','a')
for i in range(1,100000):
    np.savetxt(f, np.random.choice(["A", "T", "G", "C"], 80).reshape(1,80), delimiter="", fmt="%s")

"""

benchMarkus.getDaReps(algo=algo, algoN=algoN, nIter=10)

###################################################################################################################
# Algo 3.1

algoN = "A3.1"
algo = """
import numpy as np

f=open('HG3_1.fasta','a')
np.savetxt(f, np.random.choice(["A", "T", "G", "C"], 8000000).reshape(100000,80), delimiter="", fmt="%s")

"""

benchMarkus.getDaReps(algo=algo, algoN=algoN, nIter=10)

###################################################################################################################
# Algo 4

algoN = "A4"
algo = """
import itertools
import numpy as np

d ={'1':['A','C','T','G'],
    '2':['A','C','T','G'],
    '3':['A','C','T','G'],
    '4':['A','C','T','G']}
tetramer = []
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    tetramer.append(''.join(combo))

f=open('HG4.fasta','a')
np.savetxt(f, np.random.choice(tetramer, 8000000//4).reshape(100000,80//4), delimiter="", fmt="%s")
"""

benchMarkus.getDaReps(algo=algo, algoN=algoN, nIter=10)

###################################################################################################################
# Algo 4

algoN = "A4.1"
algo = """
import itertools
import numpy as np

d ={'1':['A','C','T','G'],
    '2':['A','C','T','G'],
    '3':['A','C','T','G'],
    '4':['A','C','T','G'],
    '5': ['A', 'C', 'T', 'G'],
    '6': ['A', 'C', 'T', 'G'],
    '7': ['A', 'C', 'T', 'G'],
    '8': ['A', 'C', 'T', 'G']
    }
tetramer = []
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    tetramer.append(''.join(combo))

f=open('HG4.fasta','a')
np.savetxt(f, np.random.choice(tetramer, 8000000//8).reshape(100000,80//8), delimiter="", fmt="%s")

"""

benchMarkus.getDaReps(algo=algo, algoN=algoN, nIter=10)


###################################################################################################################
# Algo 4

algoN = "A4.2"
algo = """
import itertools
import numpy as np

d ={'1':['A','C','T','G','A','C','T','G','A','C','T','G','A','C','T','G'],
    '2':['A','C','T','G','A','C','T','G','A','C','T','G','A','C','T','G'],
    '3':['A','C','T','G','A','C','T','G','A','C','T','G','A','C','T','G'],
    '4':['A','C','T','G','A','C','T','G','A','C','T','G','A','C','T','G']}
tetramer = []
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    tetramer.append(''.join(combo))

f=open('HG4.fasta','a')
np.savetxt(f, np.random.choice(tetramer, 8000000//8).reshape(100000,80//8), delimiter="", fmt="%s")

"""

benchMarkus.getDaReps(algo=algo, algoN=algoN, nIter=10)


###################################################################################################################
# Algo Flex

# algoN = "A_Flex"
# algo = """
# import numpy as np
#
# # funcs
# def float2base(preAlloc):
#     # Create boolean masks
#     A = preAlloc < 0.25
#     T = ((preAlloc > 0.25) & (preAlloc < 0.5))
#     G = ((preAlloc > 0.5) & (preAlloc < 0.75))
#     C = ((preAlloc > 0.75) & (preAlloc < 1))
#     return(A,T,G,C)
#
# # variables
# total = 8000000
# mudolo = total % 80
# r = (total // 80)
#
# f = open('HG_flex.fasta', 'a')
#
# # preallocate numbers
# preAlloc = np.random.random(r*80).reshape(r, 80)
#
# # Create boolean masks
# A,T,G,C = float2base(preAlloc)
#
# # Project boolean mask to random number array
# seqs = np.where(A, "A", np.where(T, "T", np.where(G, "G", np.where(C, "C", 0))))
# np.savetxt(f, seqs, delimiter="", fmt="%s")
#
# # repeat for remained
#
# # preallocate numbers
# preAlloc = np.random.random(mudolo).reshape(1, mudolo)
#
# # Create boolean masks
# A,T,G,C = float2base(preAlloc)
# seqs = np.where(A, "A", np.where(T, "T", np.where(G, "G", np.where(C, "C", 0))))
# np.savetxt(f, seqs, delimiter="", fmt="%s")
# """


benchMarkus.getDaReps(algo=algo, algoN=algoN, nIter=10)


benchMarkus.plotBP()