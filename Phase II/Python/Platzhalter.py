import numpy as np
#
# for i in np.arange(1,4*10**6, dtype = np.int64):
#     print(i)

def fibo(niter):

    fiboSeq = []
    fiboSum = 0
    cnt = 0

    n1 = 0
    n2 = 1

    while cnt < niter:
        fiboSeq.append(n1)

        fiboSum = fiboSum + n1

        nth = n1 + n2


        # update values
        n1 = n2
        n2 = nth
        cnt += 1


    # return fiboSeq
    return fiboSum

print(fibo(10))

print({0:0})
quit()

def fib(n, computed = {0: 0, 1: 1}):
     if n not in computed:
         computed[n] = fib(n-1, computed) + fib(n-2, computed)
     return computed[n]

print(fib(10))

def fib_to(n):
     fibs = [0, 1]
     for i in range(2, n+1):
             fibs.append(fibs[-1] + fibs[-2])
     return fibs

print(fib_to(10))

def fib(n):
     a, b = 0, 1
     for _ in range(n):
         a, b = b, a+b
     return a

print(fib(10))

def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2

print(fib(10))