# CBSE 65-C-3 (Class 12) -- Q21: y = sqrt(a + sqrt(a + x)), find dy/dx
# Check: if dy/dx is right, Euler's method applied to it must give back y
import numpy as np

a = 1.0
y = lambda x: np.sqrt(a + np.sqrt(a + x))
dy = lambda x: 1/(4*np.sqrt(a + x)*np.sqrt(a + np.sqrt(a + x)))

h = 1e-4
x = np.arange(0, 2, h)
Y = np.zeros_like(x)
Y[0] = y(0)
for n in range(len(x) - 1):
    Y[n+1] = Y[n] + h*dy(x[n])

print(np.abs(Y - y(x)).max())    # about 1e-5
