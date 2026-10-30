import numpy as np
import numpy.linalg as LA

# matgeo style: points as column vectors
A = np.array([2, 3, -4]).reshape(-1, 1)
B = np.array([3, -4, -5]).reshape(-1, 1)
C = np.array([3, 2, -3]).reshape(-1, 1)

S = A + B + C                       # a + b + c
norm_S = np.sqrt(S.T @ S).item()    # sqrt(S^T S)

print("a+b+c =", S.flatten())       # [ 8  1 -12]
print("S^T S =", (S.T @ S).item())  # 209
print("|a+b+c| =", norm_S)          # 14.4568...
print("LA.norm =", LA.norm(S))

for opt, v in {'A': 113, 'B': 185, 'C': 203, 'D': 209}.items():
    print(opt, np.sqrt(v), "<-- correct" if np.isclose(norm_S, np.sqrt(v)) else "")
