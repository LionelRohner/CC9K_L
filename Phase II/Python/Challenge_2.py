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


def fibMatrix(n):
    lst = []
    # sum = 0
    # standard loop over each Fibonacci Number up to 4 Mio
    for i in range(0,n,3):

        # each new number in the sequence is found in the right corner of the matrix X
        # Since it is indexed right away, the x is in lower case
        lst.append(np.linalg.matrix_power(A,i)[0,1])

    return(lst)


# np.linalg.matrix_power uses binary exponentiation to compute the end result (the pure Python source is here), so it is just a smart sequence of calls to np.dot. If the arrays are of object dtype, np.dot uses the objects __mul__ and __add__ methods. So for the OP's use case, simply setting A = np.array([1, 1, 1, 0], dtype=object).reshape(2, 2) will take advantage of Python's arbitrary precision integers and never overflow. – Jaime Feb 1 '15 at 7:22

# n = 1000000
#
# print(np.linalg.matrix_power(A,n)[0,1])
#
# blin =  __builtins__.sum(fibMatrix(10**4))
# print(blin)
# d = decimal.Decimal(blin)
# print(format(d, '.6e'))
# quit()



algo1 = """
import numpy as np
A = np.array([1,1,1,0], dtype=object).reshape(2,2)
Fk = np.linalg.matrix_power(A, (2*10**6)+1)

(Fk[0,1]*(2*Fk[0, 0] - Fk[0, 1]))-1
# print("done")
"""

# tst1 = [tmt.timeit(stmt=algo1, number=i) for i in range(5000)]
# res["Algo1"] = tst1
# print(np.mean(tst1))

nIter = 11

elapsed_time = tmt.timeit(algo1, number=nIter)
print("algo1 ", (elapsed_time/nIter))
print("Loop Done.")

# Recursive


# algo2 = """
# import numpy as np
#
# A = np.array([1,1,1,0], dtype=object).reshape(2,2)
# np.linalg.matrix_power(A, 2*(4*10**6))[0, 1] - 1
# # print("done")
# """
#
# # tst2 = [tmt.timeit(stmt=algo2, number=i) for i in range(5000)]
# # res["Algo2"] = tst2
# # print(np.mean(tst2))
#
# elapsed_time = tmt.timeit(algo2, number=nIter)
# print("algo2: ", (elapsed_time/nIter))
# print("Loop Done.")

# algo3 = """
# import numpy as np
# n = 4000000
# A = np.array([1,1,1,0], dtype=object).reshape(2,2)
# np.linalg.matrix_power(A, n)[0, 1] - 1
# # print("done")
# """
#
# # tst2 = [tmt.timeit(stmt=algo2, number=i) for i in range(5000)]
# # res["Algo2"] = tst2
# # print(np.mean(tst2))
#
# elapsed_time = tmt.timeit(algo3, number=nIter)
# print("algo3: ", elapsed_time/nIter)
# print("Loop Done.")


# algo4 = """
# import numpy as np
# A = np.array([1,1,1,0], dtype=object).reshape(2,2)
# F2k = np.linalg.matrix_power(A, (2*10**6))[0, 1]*(2*np.linalg.matrix_power(A, (2*10**6) + 1)[0, 1] - np.linalg.matrix_power(A, (2*10**6))[0, 1])
# # print("done")
# """
# # tst2 = [tmt.timeit(stmt=algo2, number=i) for i in range(5000)]
# # res["Algo2"] = tst2
# # print(np.mean(tst2))
#
# elapsed_time = tmt.timeit(algo4, number=nIter)
# print("algo4: ", elapsed_time/nIter)
# print("Loop Done.")



algo5 = """
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
Fk = np.linalg.matrix_power(A, (2*10**6)+1)

karatsuba(x = Fk[0,1], y = (2*Fk[0, 0] - Fk[0, 1]), m = 2000) - 1
# print("done")
"""
# tst2 = [tmt.timeit(stmt=algo2, number=i) for i in range(5000)]
# res["Algo2"] = tst2
# print(np.mean(tst2))

elapsed_time = tmt.timeit(algo5, number=nIter)
print("algo5: ", elapsed_time/nIter)
print("Loop Done.")

print(res)

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

(fibonacci(2*(4*10**6))-1)

"""
# tst2 = [tmt.timeit(stmt=algo2, number=i) for i in range(5000)]
# res["Algo2"] = tst2
# print(np.mean(tst2))

elapsed_time = tmt.timeit(algo5, number=nIter)
print("algoComp: ", elapsed_time/nIter)
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


#

