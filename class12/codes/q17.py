# CBSE 65-C-3 (Class 12) -- Q17
# log(dy/dx) = ax + by   =>   dy/dx = e^{ax+by}
# Separating variables:  e^{-by} dy = e^{ax} dx  =>  e^{ax}/a + e^{-by}/b = C
# Check with Euler's method: y_{n+1} = y_n + h f(x_n, y_n)
import numpy as np

a, b = 2.0, 1.0
f = lambda x, y: np.exp(a*x + b*y)

h = 1e-5
x = np.arange(0, 0.5 + h/2, h)
y = np.zeros_like(x)                          # y(0) = 0
for n in range(len(x) - 1):
    y[n+1] = y[n] + h*f(x[n], y[n])

I = np.exp(a*x)/a + np.exp(-b*y)/b            # should stay constant
C = I[0]
y_exact = -np.log(b*(C - np.exp(a*x)/a))/b    # solve the relation for y


print("solution  e^{ax}/a + e^{-by}/b = C")
