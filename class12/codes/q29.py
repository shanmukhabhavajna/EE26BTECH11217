import os
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

c = np.array([120, 150]).reshape(-1, 1)
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8]).reshape(-1, 1)

# corner points: origin, the two axis intercepts, and where the two lines meet
P = LA.solve(A, b)
x_int = b[0, 0]/A[0, 0]              # silver line on the x-axis
y_int = b[1, 0]/A[1, 1]              # gold line on the y-axis
corners = np.array([[0, x_int, P[0, 0], 0],
                    [0, 0, P[1, 0], y_int]])
assert (A @ corners <= b + 1e-9).all()      # all four lie in the feasible region

Z = (c.T @ corners).ravel()
best = Z.argmax()
print(Z, corners[:, best])           # [0 360 690 600] and (2, 3)

