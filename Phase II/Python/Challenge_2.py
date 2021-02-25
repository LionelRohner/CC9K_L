import numpy as np
import math
import decimal
import pandas as pd
import timeit as tmt

res = pd.DataFrame({
    "Algo1": [],
    "Algo2": [],
    "Algo3": []
})

import numpy as np

A = np.array([1, 1, 1, 0], dtype=object).reshape(2, 2)

F_i =  0
i = 0
while F_i <= 4000000:
    F_i += (np.linalg.matrix_power(A, i)[0, 1])
    i += 3
print(F_i)

quit()

# 4 F(n-3) + F(n-6)
#
import numpy as np

# A = np.array([1, 1, 1, 0], dtype=object).reshape(2, 2)
#
# i = 34
#
# (np.linalg.matrix_power(A, (i+1))[0,1] - 1)//2
#
# print(F_i)
# print(4613732)


algo1 = """
import numpy as np

A = np.array([1, 1, 1, 0], dtype=object).reshape(2, 2)


F_i = 0
i = 0
while F_i <= 4000000:
    F_i +=  np.linalg.matrix_power(A, i)[0,1]
    i += 3
# print(F_i)
"""

# tst1 = [tmt.timeit(stmt=algo1, number=i) for i in range(5000)]
# res["Algo1"] = tst1
# print(np.mean(tst1))

nIter = 10000

elapsed_time = tmt.timeit(algo1, number=nIter)
print("algo1 ", (elapsed_time / nIter))
print("Loop Done.")


algo2 = """
import numpy as np

A = np.array([1, 1, 1, 0], dtype=object).reshape(2, 2)

F_i = []
i = 0
while F_i < 4000000:
    F_i.append(np.linalg.matrix_power(A,i)[0,1])
    i += 3
    
sum(F_i)
"""

# tst1 = [tmt.timeit(stmt=algo1, number=i) for i in range(5000)]
# res["Algo1"] = tst1
# print(np.mean(tst1))

nIter = 10000

elapsed_time = tmt.timeit(algo2, number=nIter)
print("algo2 ", (elapsed_time / nIter))
print("Loop Done.")


algoCheat = """
import numpy as np

# A = np.array([1, 1, 1, 0], dtype=object).reshape(2, 2)

(np.linalg.matrix_power([[1,1],[1,0]], (35))[0,1] - 1)//2

"""
# tst2 = [tmt.timeit(stmt=algo2, number=i) for i in range(5000)]
# res["Algo2"] = tst2
# print(np.mean(tst2))

elapsed_time = tmt.timeit(algoCheat, number=nIter)
print("algoCheat: ", elapsed_time / nIter)
print("Loop Done.")


algoCheat2 = """
import numpy as np

sum([np.linalg.matrix_power([[1,1],[1,0]], i)[0,1] for i in range(0,36,3)])

"""
# tst2 = [tmt.timeit(stmt=algo2, number=i) for i in range(5000)]
# res["Algo2"] = tst2
# print(np.mean(tst2))

elapsed_time = tmt.timeit(algoCheat2, number=nIter)
print("algoCheat2: ", elapsed_time / nIter)
print("Loop Done.")

algoCheat2 = """
from numpy.linalg import matrix_power as m

(m([[1,1],[1,0]], (35))[0,1] - 1)//2
"""
# tst2 = [tmt.timeit(stmt=algo2, number=i) for i in range(5000)]
# res["Algo2"] = tst2
# print(np.mean(tst2))

elapsed_time = tmt.timeit(algoCheat2, number=nIter)
print("algoCheat2: ", elapsed_time / nIter)
print("Loop Done.")



algoComp = """
sum = 0
f1, f2 = 0, 1
while f2 <= 4000000:
    if f2 % 2 == 0:
        sum += f2
    f1, f2 = f2, f1 + f2
# print(sum)
"""
# tst2 = [tmt.timeit(stmt=algo2, number=i) for i in range(5000)]
# res["Algo2"] = tst2
# print(np.mean(tst2))

elapsed_time = tmt.timeit(algoComp, number=nIter)
print("algoComp: ", elapsed_time / nIter)
print("Loop Done.")

quit()

algoBF = """
import numpy as np

def fibMatrix(n):
    lst = []
    # sum = 0

    A = np.array([1, 1, 1, 0], dtype=object).reshape(2, 2)

    # standard loop over each Fibonacci Number up to 4 Mio
    for i in range(0,n,3):

        # each new number in the sequence is found in the right corner of the matrix X
        # Since it is indexed right away, the x is in lower case
        lst.append(np.linalg.matrix_power(A,i)[0,1])

    return(sum(lst))

fibMatrix(4*10**6)

print("done")
"""

print(res)