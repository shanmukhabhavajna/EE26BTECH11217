# CBSE 65-C-3 (Class 12) -- Q6
# sec^-1((1+x)/(1-y)) = a, find dy/dx.  Check each option with Euler's method
import numpy as np

a = 1.0
k = 1/np.cos(a)
y_exact = lambda x: 1 - (1 + x)/k            # exact curve from the relation

opts = {'A': lambda x, y: (x-1)/(y-1),
        'B': lambda x, y: (x-1)/(y+1),
        'C': lambda x, y: (y-1)/(x+1),
        'D': lambda x, y: (y+1)/(x-1)}

h = 0.01
x = np.arange(0, 0.9 + h/2, h)               # stay away from x = 1 (option D)
for name, f in opts.items():
    y = np.zeros_like(x)
    y[0] = y_exact(x[0])                     # y0 on the curve
    for n in range(len(x) - 1):
        y[n+1] = y[n] + h*f(x[n], y[n])      # Euler: y_{n+1} = y_n + h f(x_n, y_n)
    err = np.max(np.abs(y - y_exact(x)))
    print("Q6: option %s  max error = %.5f %s" % (name, err, "<-- correct" if err < 1e-3 else ""))
