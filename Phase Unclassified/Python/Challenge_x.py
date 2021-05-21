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

A = np.array([1,1,1,0], dtype=object).reshape(2,2)


def fibMatrixEven(n):
    lst = []
    # sum = 0
    # standard loop over each Fibonacci Number up to 4 Mio
    for i in range(0,n,3):

        # each new number in the sequence is found in the right corner of the matrix X
        # Since it is indexed right away, the x is in lower case
        lst.append(np.linalg.matrix_power(A,i)[0,1])

    return(lst)


n = 10
print(fibMatrixEven(n))
print(sum(fibMatrixEven(n)))

# find n
k = (11//3)+2


A = np.array([1,1,1,0], dtype=object).reshape(2,2)
I = np.array([1,0,1,0], dtype=object).reshape(2,2)

F3n_3 = np.linalg.matrix_power(A,n+2)



# print((np.matmul((F3n_3-I),(F3n_3-I))//2)[1,1])
print((F3n_3[1,1]-1)//2)

# my algo 1
quit()
A = np.array([1,1,1,0], dtype=object).reshape(2,2)
Fk = np.linalg.matrix_power(A, ((n+1)))

# F_k        F_k+1      F_k
print(((Fk[0,1]*(2*Fk[0, 0] - Fk[0, 1]))-1)//2)


quit()

algo1 = """
import numpy as np
A = np.array([1,1,1,0], dtype=object).reshape(2,2)
Fk = np.linalg.matrix_power(A, (1999999))

# F_k        F_k+1      F_k
(Fk[0,1]*(2*Fk[0, 0] - Fk[0, 1]))-1
"""

# tst1 = [tmt.timeit(stmt=algo1, number=i) for i in range(5000)]
# res["Algo1"] = tst1
# print(np.mean(tst1))

nIter = 11

elapsed_time = tmt.timeit(algo1, number=nIter)
print("algo1 ", (elapsed_time/nIter))
print("Loop Done.")


# algo2 = """
# import numpy as np
#
# A = np.array([1,1,1,0], dtype=object).reshape(2,2)
# np.linalg.matrix_power(A, 7999996)[0, 1] - 1
# """
#
# # tst2 = [tmt.timeit(stmt=algo2, number=i) for i in range(5000)]
# # res["Algo2"] = tst2
# # print(np.mean(tst2))
#
# elapsed_time = tmt.timeit(algo2, number=nIter)
# print("algo2: ", (elapsed_time/nIter))
# print("Loop Done.")

# algoCrap = """
# import numpy as np
# A = np.array([1,1,1,0], dtype=object).reshape(2,2)
# F2k = np.linalg.matrix_power(A, (2*10**6))[0, 1]*(2*np.linalg.matrix_power(A, (2*10**6) + 1)[0, 1] - np.linalg.matrix_power(A, (2*10**6))[0, 1])
# # print("done")
# """
# # tst2 = [tmt.timeit(stmt=algoCrap, number=i) for i in range(5000)]
# # res["algoCrap"] = tst2
# # print(np.mean(tst2))
#
# elapsed_time = tmt.timeit(algoCrap, number=nIter)
# print("algo4: ", elapsed_time/nIter)
# print("Loop Done.")



algo3 = """
import numpy as np

def karatsuba(x , y, m):
    # 1.)
    xlow = x % m
    xhigh = x//m

    # 2.)
    ylow = y % m
    yhigh = y//m

    # 3.)
    a = xhigh*yhigh
    b = (xlow + xhigh)*(ylow + yhigh)
    c = xlow*ylow

    # Result
    return(a*m**2+(b-a-c)*m+c)


A = np.array([1,1,1,0], dtype=object).reshape(2,2)
Fk = np.linalg.matrix_power(A, 1999999)

karatsuba(x = Fk[0,1], y = (2*Fk[0, 0] - Fk[0, 1]), m = 20000) - 1 
"""
# tst2 = [tmt.timeit(stmt=algo2, number=i) for i in range(5000)]
# res["Algo2"] = tst2
# print(np.mean(tst2))

elapsed_time = tmt.timeit(algo3, number=nIter)
print("algo3: ", elapsed_time/nIter)
print("Loop Done.")


karatsuba(np.matmul(Fk[0,0:1],[[2],[-1]]),Fk, )

algo4 = """
import numpy as np
A = np.array([1,1,1,0], dtype=object).reshape(2,2)
Fk = np.linalg.matrix_power(A, 1999999)


# F_k        F_k+1      F_k
(Fk[0,1]*(2*Fk[0, 0] - Fk[0, 1]))-1
"""

# tst1 = [tmt.timeit(stmt=algo1, number=i) for i in range(5000)]
# res["Algo1"] = tst1
# print(np.mean(tst1))

nIter = 11

elapsed_time = tmt.timeit(algo1, number=nIter)
print("algo1 ", (elapsed_time/nIter))
print("Loop Done.")

algoComp = """
#### Comparison
#
# Fast doubling Fibonacci algorithm (Python)
#
# Copyright (c) 2015 Project Nayuki
# All rights reserved. Contact Nayuki for licensing.
# https://www.nayuki.io/page/fast-fibonacci-algorithms

# (Public) Returns F(n).

def fibonacci(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]


# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

(fibonacci(7999996)-1)

"""
# tst2 = [tmt.timeit(stmt=algo2, number=i) for i in range(5000)]
# res["Algo2"] = tst2
# print(np.mean(tst2))

elapsed_time = tmt.timeit(algoComp, number=nIter)
print("algoComp: ", elapsed_time/nIter)
print("Loop Done.")


algoComp2 = """

import numpy as np

# Karatsuba fast multiplication algorithm (Python)
# 
# Copyright (c) 2020 Project Nayuki
# All rights reserved. Contact Nayuki for licensing.
# https://www.nayuki.io/page/karatsuba-multiplication
# 


# Requirement: _CUTOFF >= 64, or else there will be infinite recursion.
_CUTOFF = 1536


def multiply(x, y):
    if x.bit_length() <= _CUTOFF or y.bit_length() <= _CUTOFF:  # Base case
        return x * y
    
    else:
        n = max(x.bit_length(), y.bit_length())
        half = (n + 32) // 64 * 32
        mask = (1 << half) - 1
        xlow = x & mask
        ylow = y & mask
        xhigh = x >> half
        yhigh = y >> half
        
        a = multiply(xhigh, yhigh)
        b = multiply(xlow + xhigh, ylow + yhigh)
        c = multiply(xlow, ylow)
        d = b - a - c
        return (((a << half) + d) << half) + c


A = np.array([1,1,1,0], dtype=object).reshape(2,2)
Fk = np.linalg.matrix_power(A, 1999999)

multiply(x = Fk[0,1], y = (2*Fk[0, 0] - Fk[0, 1])) - 1 
"""
elapsed_time = tmt.timeit(algoComp2, number=nIter)
print("algoComp2: ", elapsed_time/nIter)
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