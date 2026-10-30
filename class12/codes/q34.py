
import numpy as np

a = 1
b = 3

def f(x):
    return x**2 + 1 + np.exp(x)

# sum f(a + i*h) * h for i = 1..n, where h = (b - a)/n
for n in [10, 100, 1000, 100000]:
    h = (b - a) / n
    total = 0
    for i in range(1, n + 1):
        total = total + f(a + i * h) * h

# exact answer: [x^3/3 + x + e^x] from 1 to 3 = 32/3 + e^3 - e
exact = 32 / 3 + np.exp(3) - np.exp(1)
print("exact =", exact)
