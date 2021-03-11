###################################################################################################################
# Modules

import numpy as np
import random as rd
import BenchPress as bp


###################################################################################################################
# BenchMarkus

data = {
    "Algo1": [],
    "Algo2": []
}

# benchMarkus = bp.BenchPress(data, "Nenad")
benchMarkus = bp.BenchPress(data = data, benchMeth = "Lionel")


###################################################################################################################
# Algo 1


# x = 3272116950/80 = 40901461.875 ~ 40901462

# print(3272116950/80)

n = 80

np.random.random(4000000000).astype('f2').reshape(100000,40000)
quit()
# quit()
# preAlloc = np.random.random(80)
# seqs = np.where(preAlloc < 0.5, rd.choice("AT"), rd.choice("GC"))
# print(np.random.random(4))



algoN = "Algo1"

algo = """
import numpy as np

print(np.random.random(3272116950).reshape(40901462,80))
"""

benchMarkus.getDaReps(algo = algo, algoN = algoN)
print(benchMarkus.returnRes())

quit()

###################################################################################################################
# Algo 1

algoN = "Algo2"

algo = """
a = np.random.random(4)
print(np.where(a < 0.5, rd.choice("AT"), rd.choice("GC")))
print(np.random.random(4))
"""

benchMarkus.getDaReps(algo = algo, algoN = algoN)