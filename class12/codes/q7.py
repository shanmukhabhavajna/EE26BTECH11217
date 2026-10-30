# CBSE 65-C-3 (Class 12) -- Q7
# int (cos8x+1)/(tan2x-cot2x) dx = lambda*cos8x + c, find lambda
import numpy as np

def trap(y, x):
    return np.sum((y[1:] + y[:-1]) * np.diff(x)) / 2

f = lambda x: (np.cos(8*x) + 1) / (np.tan(2*x) - 1/np.tan(2*x))
a, b = 0.05, 0.3                      # interval with no singularity
x = np.linspace(a, b, 200001)
I = trap(f(x), x)                     # definite integral
lam = I / (np.cos(8*b) - np.cos(8*a)) # I = lambda (cos8b - cos8a)
print("Q7: lambda =", lam, "= 1/16 =", 1/16)
for opt, v in {'A': 1/16, 'B': 1/8, 'C': -1/16, 'D': -1/8}.items():
    print("Q7: option", opt, v, "<-- correct" if np.isclose(lam, v, atol=1e-6) else "")
