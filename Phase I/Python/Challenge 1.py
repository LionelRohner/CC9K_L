import numpy as np
import timeit
import time

A = np.arange(0, (10 ** 6), 1)
# A = np.asarray(range(0,10**6,1))

print(sum(A[np.where((A % 3 == 0) | (A % 5 == 0))]))


# # timing method?
# def main():
#     A = np.arange(0,10**6,1)
#     # A = np.asarray(range(0,10**6,1))
#
#     print(np.sum(A[np.where( (A % 3 == 0) | (A % 5 == 0))]))
#
#
# # timing method 1
# code_block = """
# import numpy as np
# A = np.arange(0,10**6,1)
#
# print(np.sum(A[np.where( (A % 3 == 0) | (A % 5 == 0))]))
# """
# elapsed_time = timeit.timeit(code_block, number=10)
# print(np.mean(elapsed_time))
#
# # timing method two
# start_time = time.time()
# main()
# print("--- %s seconds ---" % (time.time() - start_time))