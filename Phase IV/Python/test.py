import numpy as np
import decimal


import math

_1_50 = 1 << 50  # 2**50 == 1,125,899,906,842,624

def isqrt(x):
    """Return the integer part of the square root of x, even for very
    large integer values."""
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    if x < _1_50:
        return int(math.sqrt(x))  # use math's sqrt() for small parameters
    n = int(x)
    if n <= 1:
        return n  # handle sqrt(0)==0, sqrt(1)==1
    # Make a high initial estimate of the result (a little lower is slower!!!)
    r = 1 << ((n.bit_length() + 1) >> 1)
    while True:
        newr = (r + n // r) >> 1  # next estimate by Newton-Raphson
        if newr >= r:
            return r
        r = newr

def karatsuba(x , y, m):
    """

    :param x: some int
    :param y: some other int
    :param m: modulo, such that approx sqrt(x)
    :return: product of x and y
    """

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
Fk = np.linalg.matrix_power(A, 10+2)
print(Fk[0,0]-1)
print(Fk)
quit()
print((np.dot(Fk[0,:],[[2],[-1]])*Fk[0,0])-1)
# karatsuba(np.matmul(Fk[0,0:1],[[2],[-1]]),Fk[0,1])

quit()
blin = (2*Fk[0, 0] - Fk[0, 1])

print("printing")
d = decimal.Decimal(blin)
print(format(d, '.6e'))
print(blin%2)

print("printing sqrt")
sqrtBlin = isqrt(blin)
dd = decimal.Decimal(sqrtBlin)
print(format(dd, '.6e'))

# dude sqrt(Fn) is 3.433651e+208987.... that should be m for karatsuba
