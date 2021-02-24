import numpy as np


x = 255
y = 140
m = 15


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
