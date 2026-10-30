# Laplace gives y = x(ln x + C). Euler's method is used here to check it.
import numpy as np

f = lambda x, y: 1 + y/x             # dy/dx

h = 1e-4
x = np.arange(1, 3, h)
y = np.zeros_like(x)

for C in (-1, 0, 2):
    y[0] = C                         # y(1) = C
    for n in range(len(x) - 1):
        y[n+1] = y[n] + h*f(x[n], y[n])
    print(C, np.abs(y - x*(np.log(x) + C)).max())     # about 1e-4 each time
