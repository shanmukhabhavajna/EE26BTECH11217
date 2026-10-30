# CBSE 65-C-3 (Class 12) -- Q9
# int_0^1 tan(sin^-1 x) dx.  With x = sin t:  tan(t) cos(t) dt = sin(t) dt, t in [0, pi/2]
import numpy as np

def trap(y, x):
    return np.sum((y[1:] + y[:-1]) * np.diff(x)) / 2

t = np.linspace(0, np.pi/2, 200001)
I = trap(np.sin(t), t)
print("Q9: integral =", I)               # 1.0
for opt, v in {'A': 2, 'B': 0, 'C': -1, 'D': 1}.items():
    print("Q9: option", opt, v, "<-- correct" if np.isclose(I, v, atol=1e-6) else "")
