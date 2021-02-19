import numpy as np
import math
import decimal
import pandas as pd
import timeit as tmt



res = pd.DataFrame({
    "Algo1": [],
    "Algo2": []
})


# A = np.array([[1,1],
#               [1,0]],dtype=np.int64)

A = np.array([1,1,1,0], dtype=object).reshape(2,2)

F0 = np.array([[0],[1]])


#
# lst = []
# # sum = 0
# # standard loop over each Fibonacci Number up to 4 Mio
# for i in range(1,4*10**6):
#
#     # each new number in the sequence is found in the right corner of the matrix X
#     # Since it is indexed right away, the x is in lower case
#     x = np.linalg.matrix_power(A,i)[0,1]
#     if x % 2 == 0:
#        lst.append(x)
#        # sum += int(x)
#
# print(lst)
# print(math.sum(lst))



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
# print(math.fsum(lst))
# blin =  __builtins__.sum(fibMatrix(10**4))
# print(blin)
# d = decimal.Decimal(blin)
# print(format(d, '.6e'))
# quit()



# def fib_to(n):
#      fibs = [0, 1]
#      for i in range(2, n+1):
#          fibs.append(fibs[-1] + fibs[-2])
#      return fibs
#
algo1 = """
def fib_to(n):
     fibs = [0, 1]
     for i in range(2, n+1):
         fibs.append(fibs[-1] + fibs[-2])
     return fibs


fib_to(4*10**6)[-1]
print("done")
"""

tst1 = [tmt.timeit(stmt=algo1, number=i) for i in range(3)]
res["Algo1"] = tst1
print("Loop Done.")
print(np.mean(tst1))




algo2 = """
import numpy as np

n = 4*10**6
A = np.array([1,1,1,0], dtype=object).reshape(2,2)

np.linalg.matrix_power(A,n)[0,1]
print("done")
"""

tst2 = [tmt.timeit(stmt=algo2, number=i) for i in range(3)]
res["Algo2"] = tst2
print("Loop Done.")

print(res)
print(np.mean(tst2))

