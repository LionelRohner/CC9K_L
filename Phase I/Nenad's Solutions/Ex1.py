#!/usr/bin/env python


# Ex 1: get sum of all numbers divisible by 3 or 5 up to 1'000'000
import timeit as tmt
import pandas as pd
import numpy as np

res = pd.DataFrame({
    "Loop": [],
    "NumPy_Loop": [],
    "NumPy_Array": []
})

# Try 1: Just loop
s1 = """
l = 1000001
n = 0
for i in range(1, l):
    if i % 3 == 0 or i % 5 ==0:
        n += i
"""

tst1 = [tmt.timeit(stmt=s1, number=i) for i in range(11)]
res["Loop"] = tst1
print("Loop Done.")

# Try 2: NumPy Loop
s2 = """
import numpy as np
l = 1000001
arr = np.arange(start=1,
                stop=l,
                dtype='int64').reshape(1000, 1000)
n = 0
with np.nditer(arr) as it:
    for x in it:
        if x % 3 == 0 or x % 5 == 0:
            n += x
"""
tst2 = [tmt.timeit(stmt=s2, number=i) for i in range(11)]
res["NumPy_Loop"] = tst2
print("NumPy Loop Done.")

# Try 3: NumPy PreAlloc
import numpy as np
s3 = """
import numpy as np
l = 1000001
arr = np.arange(start=1,
                stop=l,
                dtype='int64').reshape(1000, 1000)

div3 = np.full((1000, 1000), 3)
res3 = np.mod(arr, div3)
id3 = res3 == 0

div5 = np.full((1000, 1000), 5)
res5 = np.mod(arr, div5)
id5 = res5 == 0

tmp = arr[id3]
arr2 = np.concatenate((tmp, arr[id5]))

np.sum(arr2)

res5 = np.mod(arr, div5)
"""
tst3 = [tmt.timeit(stmt=s3, number=i) for i in range(11)]
res["NumPy_Array"] = tst3
print("NumPy Arrays Done.")

print(res)