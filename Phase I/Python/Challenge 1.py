import numpy as np
import math
import timeit
import time

A = np.arange(1, (1 + 10 ** 6), 1)


A = np.array([i for i in range(1,10**6) if i % 3 == 0 or i % 5 == 0], dtype=np.int64).sum()

print(A)
#


# timing method 1
code_block = """
import numpy as np
import math

A = np.arange(0,10**6,1)

math.fsum(A[np.where( (A % 3 == 0) | (A % 5 == 0))])
"""
elapsed_time = timeit.timeit(code_block, number=10)
print(np.mean(elapsed_time))




# timing method?
def main():
    A = np.arange(0,10**6,1)
    # A = np.asarray(range(0,10**6,1))

    print(math.fsum(A[np.where( (A % 3 == 0) | (A % 5 == 0))]))
# timing method two
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))