import numpy as np

v = np.array([[14], [10]])             # (Median, Mean)^T
w = np.array([[3, -2]])
mode = (w @ v).item()                  # Mode = (3 -2) (Median, Mean)^T
print("Mode =", mode)

options = {'A': 6, 'B': 22, 'C': 2, 'D': 20}
print("correct option:", [k for k, x in options.items() if x == mode])
assert mode == 22
