import itertools
import numpy as np

d ={'1':['A','C','T','G'],
    '2':['A','C','T','G'],
    '3':['A','C','T','G'],
    '4':['A','C','T','G']}
tetramer = []
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    tetramer.append(''.join(combo))



f=open('HGtest.fasta','a')
np.savetxt(f, np.random.choice(tetramer, 8000//4).reshape(100,80//4), delimiter="", fmt="%s")


