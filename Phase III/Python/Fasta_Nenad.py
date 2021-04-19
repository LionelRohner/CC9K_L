'''
Generate FASTA File with 8'000'000 basepairs (ATGC)
'''
import timeit as tmt

b = 'ATGC'
cnt = 0
l = 0
it = 0

out = ''

# Adapt path in order to write the file; timeit will reference this from the global variables
fasta = "E:\\Programming\\Python\\Python Projects\\01_Coding Challenge 9k\\data\\fasta_ex3.txt"

s1 = """
import numpy as np
n_max = 8000000
n_lst = range(80)
def bricks(b_l=80,
           n=1):
    global cnt
    global l
    global out
    global it
    if (cnt + b_l) <= n:
        cnt += b_l
        l += b_l
    else:
        b_l = (n - cnt)
        cnt += b_l
        l += b_l
    it += 1
    out += ''.join([b[idx] for idx in np.random.randint(0, 4, b_l)])
    if l >= 80:
        ofs = len(out) - (len(out) % 80) + it
        out = ''.join([out[:ofs], '\\n', out[ofs:]])
        l -= 80
    if cnt < n:
        bricks(b_l, n)
# ---------------------------------------------------
def reset():
    global out
    out = ""
    global cnt
    cnt = 0
    global l
    l = 0
# ---------------------------------------------------
def build_seq(blk=80, n=80, n_max=80):
    n_it = n_max/n
    it = 1
    with open("HGNenad.fasta", "a") as f:
        while it != n_it:
            bricks(blk, n)
            f.write(out)
            reset()
            it += 1
            #print(round((float(it) / n_it) * 100, ndigits=2), "%", end="\\r", flush=True)
    f.close()
build_seq(n=8000, n_max=80000000)
"""

tst1 = tmt.timeit(stmt=s1, number=10, globals=globals())

print(tst1)