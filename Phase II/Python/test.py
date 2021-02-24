import numpy as np
import decimal


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


# how bis is it
A = np.array([1,1,1,0], dtype=object).reshape(2,2)
blin = np.linalg.matrix_power(A, 3)[0,0]
print(blin)
quit()
A = np.array([1,1,1,0], dtype=object).reshape(2,2)
blin = np.linalg.matrix_power(A, (4*10**6-2))[0, 0]
print("printing")
# d = decimal.Decimal(blin)
# print(format(d, '.6e'))
print(blin%2)

print(4*10**6-2)