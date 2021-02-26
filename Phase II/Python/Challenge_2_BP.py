import numpy as np
import pandas as pd
import timeit as tmt
import matplotlib.pyplot as plt
import BenchPress as bp


# INIT BenchPress

data = {
    "Algo1": [],
    "Algo2": [],
    "Algo3": [],
    "Algo4": [],
    "AlgoCheat1": [],
    "AlgoCheat2": [],
    "AlgoCheat3": [],
    "AlgoComp1": [],
    "s3": []
}

benchMarkus = bp.BenchPress(data, "Nenad")
# benchMarkus = bp.BenchPress(data = data, benchMeth = "Lionel")


#######################################################################################################################

algoN = "Algo1"

algo = """
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


benchMarkus.getDaReps(algo = algo, algoN = algoN)


#######################################################################################################################

algoN = "Algo2"

algo = """
import numpy as np

A = np.array([1, 1, 1, 0], dtype=object).reshape(2, 2)

F_i = [0]
i = 0

while F_i[-1] < 4000000:
    F_i.append(np.linalg.matrix_power(A,i)[0,1])
    i += 3

sum(F_i[:-1])

# print(sum(F_i[:-1]))
"""

benchMarkus.getDaReps(algo = algo, algoN = algoN)

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

benchMarkus.getDaReps(algo = algo, algoN = algoN)

#######################################################################################################################

algoN = "Algo4"

algo = """
sqrt5 = (5)**0.5
phi = (sqrt5+1)/2
i = 0
F_i = 0
# sum = 0


while F_i <= 4000000:
    # sum += F_i 
    F_i += ((phi**i)-(-phi)**-i)//sqrt5

    i += 3

# print(F_i)
"""

benchMarkus.getDaReps(algo = algo, algoN = algoN)

#######################################################################################################################

algoN = "AlgoCheat1"

algo = """
import numpy as np

# A = np.array([1, 1, 1, 0], dtype=object).reshape(2, 2)

(np.linalg.matrix_power([[1,1],[1,0]], (4000000))[0,1] - 1)//2
"""

benchMarkus.getDaReps(algo = algo, algoN = algoN)

#######################################################################################################################

algoN = "AlgoCheat2"

algo = """
import numpy as np

sum([np.linalg.matrix_power([[1,1],[1,0]], i)[0,1] for i in range(0,35,3)])
"""

benchMarkus.getDaReps(algo = algo, algoN = algoN)

#######################################################################################################################

algoN = "AlgoCheat3"

algo = """
from numpy.linalg import matrix_power as m

(m([[1,1],[1,0]], (35))[0,1] - 1)//2
"""

benchMarkus.getDaReps(algo = algo, algoN = algoN)

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

benchMarkus.getDaReps(algo = algo, algoN = algoN)

########################################################################################################################

# algoN = "AlgoComp2"
#
# algo = """
# from sympy import fibonacci
#
# F_i = 0
# i = 0
#
# while F_i <= 4000000:
#
#     F_i += fibonacci(i)
#
#     i += 3
#
# # print(F_i)
# """
#
# benchMarkus.getDaReps(algo = algo, algoN = algoN)


########################################################################################################################
algoN = "s3"

s3 = """
def get_fib_even_sum3():
    import functools
    @functools.lru_cache(None)
    def fib2(n):
        if n < 1:
            return n
        if n == 1:
            return 2
        return (4 * (fib2(n-1))) + fib2(n-2)

    f_sum = 0
    i = 0
    tmp_fib = 0
    while tmp_fib < 4000000:
        f_sum += tmp_fib
        tmp_fib = fib2(i)

        i += 1
    return f_sum
"""

benchMarkus.getDaReps(algo=s3,algoN = algoN)

########################################################################################################################
# benchmark plot
print(benchMarkus.returnRes())

benchMarkus.dickPic()

benchMarkus.saveCSV()