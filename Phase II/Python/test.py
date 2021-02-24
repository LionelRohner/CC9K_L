import numpy as np


x = 255
y = 140
m = 15

# 1.)
xlow = x % m
xhigh = np.floor(x/m)

# 2.)
ylow = y % m
yhigh = np.floor(y/m)

# 3.)
a = xhigh*yhigh
b = (xlow + xhigh)*(ylow + yhigh)
c = xlow*ylow

# Result
xy = a*m**2+(b-a-c)*m+c

print(xy)

