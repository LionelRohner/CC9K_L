import numpy as np
import math
import timeit
import time

# Algo 1 - numpy + math
code_block = """
import numpy as np
import math

A = np.arange(1,10**6,1)

print(math.fsum(A[np.where( (A % 3 == 0) | (A % 5 == 0))]))
"""
elapsed_time = timeit.timeit(code_block, number=10)
timeAlgo1 = np.mean(elapsed_time)


# Algo 2 - numpy only
code_block = """
import numpy as np


A = np.arange(1,10**6,1, dtype = np.int64)

print(np.sum(A[np.where( (A % 3 == 0) | (A % 5 == 0))]))
"""
elapsed_time = timeit.timeit(code_block, number=10)
timeAlgo2 = np.mean(elapsed_time)


# Algo 3 aka the one-line-killer
code_block = """
import numpy as np

print(np.array([i for i in range(1,10**6) if i % 3 == 0 or i % 5 == 0], dtype=np.int64).sum())
"""
elapsed_time = timeit.timeit(code_block, number=10)
timeAlgo3 = np.mean(elapsed_time)


# benchmark
print("\n\n\n")
print("############################################################")
print("{:>30}".format("BENCHMARK"))
print("############################################################")

print("Mean Speed (Algo1): ", timeAlgo1)
print("Mean Speed (Algo2): ", timeAlgo2)
print("Mean Speed (Algo3): ", timeAlgo3)