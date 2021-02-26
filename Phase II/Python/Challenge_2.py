import numpy as np
import pandas as pd
import timeit as tmt
import matplotlib.pyplot as plt
import BenchPress as bp


def FibMatrix(A,n):
    return(np.linalg.matrix_power(A,n)[0,1])

res = pd.DataFrame({
    "Algo1": [],
    "Algo2": [],
    "Algo3": [],
    "AlgoCheat1": [],
    "AlgoCheat2": [],
    "AlgoCheat3": [],
    "AlgoCheat4": [],
    "AlgoComp1": [],
    "AlgoComp2": []
})

nIter = 5000

# benchMeth = "Nenad"
benchMeth = "Lionel"

#######################################################################################################################

algoN = "Algo1"

algo= """
import numpy as np

A = np.array([1, 1, 1, 0], dtype=object).reshape(2, 2)

F_i = 0
i = 0
# sum = 0


while F_i < 4000000:
    # sum = sum + F_i
    
    F_i += np.linalg.matrix_power(A, i)[0,1]

    i += 3

# print(F_i)
"""

if benchMeth == "Nenad":
    nIter = 10
    tst = [tmt.timeit(stmt=algo, number=i) for i in range(nIter)]
    res[algoN] = tst
    print()
else:
    elapsed_time = tmt.timeit(algo, number=nIter)
    print(algoN,": ", elapsed_time / nIter)
    res[algoN] = [elapsed_time]
    print("Loop Done.")
    print()

#######################################################################################################################

algoN = "Algo2"

algo= """
import numpy as np

A = np.array([1, 1, 1, 0], dtype=object).reshape(2, 2)

F_i = [0]
i = 0

while F_i[-1] < 4000000:
    F_i.append(np.linalg.matrix_power(A,i)[0,1])
    i += 3
    
sum(F_i[:-1])

# print(sum(F_i[:-1])
"""
if benchMeth == "Nenad":
    nIter = 10
    tst = [tmt.timeit(stmt=algo, number=i) for i in range(nIter)]
    res[algoN] = tst
    print()
else:
    elapsed_time = tmt.timeit(algo, number=nIter)
    print(algoN,": ", elapsed_time / nIter)
    res[algoN] = [elapsed_time / nIter]
    print("Loop Done.")
    print()

#######################################################################################################################

algoN = "Algo3"

algo = """
sum = 0
F_n, F_np1 = 1, 1
F_np2 = F_n + F_np1

while F_np2 < 4000000:
    sum += F_np2
    F_n = F_np1 + F_np2
    F_np1 = F_np2 + F_n
    F_np2 = F_n + F_np1

# print(sum)
"""
if benchMeth == "Nenad":
    nIter = 10
    tst = [tmt.timeit(stmt=algo, number=i) for i in range(nIter)]
    res[algoN] = tst
    print()
else:
    elapsed_time = tmt.timeit(algo, number=nIter)
    print(algoN,": ", elapsed_time / nIter)
    res[algoN] = [elapsed_time / nIter]
    print("Loop Done.")
    print()

#######################################################################################################################

algoN = "AlgoCheat1"

algo = """

sqrt5 = (5)**0.5
phi = (sqrt5+1)/2
i = 0
F_i = 0
# sum = 0


while F_i <= 4000000:
    # sum += F_i 
    F_i = ((phi**i)-(-phi)**-i)//sqrt5

    i += 3
    
# print(sum)
"""
if benchMeth == "Nenad":
    nIter = 10
    tst = [tmt.timeit(stmt=algo, number=i) for i in range(nIter)]
    res[algoN] = tst
    print()
else:
    elapsed_time = tmt.timeit(algo, number=nIter)
    print(algoN,": ", elapsed_time / nIter)
    res[algoN] = [elapsed_time / nIter]
    print("Loop Done.")
    print()

#######################################################################################################################
#######################################################################################################################

algoN = "AlgoCheat2"

algo = """
import numpy as np

# A = np.array([1, 1, 1, 0], dtype=object).reshape(2, 2)

(np.linalg.matrix_power([[1,1],[1,0]], (35))[0,1] - 1)//2
"""
if benchMeth == "Nenad":
    nIter = 10
    tst = [tmt.timeit(stmt=algo, number=i) for i in range(nIter)]
    res[algoN] = tst
    print()
else:
    elapsed_time = tmt.timeit(algo, number=nIter)
    print(algoN,": ", elapsed_time / nIter)
    res[algoN] = [elapsed_time / nIter]
    print("Loop Done.")
    print()

#######################################################################################################################

algoN = "AlgoCheat3"

algo = """
import numpy as np

sum([np.linalg.matrix_power([[1,1],[1,0]], i)[0,1] for i in range(0,35,3)])
"""
if benchMeth == "Nenad":
    nIter = 10
    tst = [tmt.timeit(stmt=algo, number=i) for i in range(nIter)]
    res[algoN] = tst
    print()
else:
    elapsed_time = tmt.timeit(algo, number=nIter)
    print(algoN,": ", elapsed_time / nIter)
    res[algoN] = [elapsed_time / nIter]
    print("Loop Done.")
    print()


#######################################################################################################################

algoN = "AlgoCheat4"

algo = """
from numpy.linalg import matrix_power as m

(m([[1,1],[1,0]], (35))[0,1] - 1)//2
"""
if benchMeth == "Nenad":
    nIter = 10
    tst = [tmt.timeit(stmt=algo, number=i) for i in range(nIter)]
    res[algoN] = tst
    print()
else:
    elapsed_time = tmt.timeit(algo, number=nIter)
    print(algoN,": ", elapsed_time / nIter)
    res[algoN] = [elapsed_time / nIter]
    print("Loop Done.")
    print()

########################################################################################################################

algoN = "AlgoComp1"

algo = """
sum = 0
f1, f2 = 0, 1
while f2 <= 4000000:
    if f2 % 2 == 0:
        sum += f2
    f1, f2 = f2, f1 + f2

# print(sum)
"""
if benchMeth == "Nenad":
    nIter = 10
    tst = [tmt.timeit(stmt=algo, number=i) for i in range(nIter)]
    res[algoN] = tst
    print()
else:
    elapsed_time = tmt.timeit(algo, number=nIter)
    print(algoN,": ", elapsed_time / nIter)
    res[algoN] = [elapsed_time / nIter]
    print("Loop Done.")
    print()


########################################################################################################################

algoN = "AlgoComp2"

algo = """
from sympy import fibonacci

F_i = 0
i = 0

while F_i <= 4000000:

    F_i += fibonacci(i)

    i += 3

# print(F_i)    
"""
if benchMeth == "Nenad":
    nIter = 10
    tst = [tmt.timeit(stmt=algo, number=i) for i in range(nIter)]
    res[algoN] = tst
    print()
else:
    elapsed_time = tmt.timeit(algo, number=nIter)
    print(algoN,": ", elapsed_time / nIter)
    res[algoN] = [elapsed_time]
    print("Loop Done.")
    print()


########################################################################################################################
# benchmark plot

if benchMeth == "Nenad":
    res.plot(ylim = [min(res.min()),max(res.max())])

else:
    res.boxplot()

plt.show()