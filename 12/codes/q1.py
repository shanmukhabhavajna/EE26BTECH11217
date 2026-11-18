import numpy as np

# position vectors of A, B, C as the columns of M
a = np.array([2, 3, -4])
b = np.array([3, -4, -5])
c = np.array([3, 2, -3])
M = np.block([[a.reshape(-1, 1), b.reshape(-1, 1), c.reshape(-1, 1)]])

# Gram matrix G = M^T M
G = M.T @ M
print("G =\n", G)

# |a + b + c|^2 = 1^T G 1
one = np.ones((3, 1))
s2 = (one.T @ G @ one).item()
print("|a + b + c|^2 =", s2, " |a + b + c| =", np.sqrt(s2))
assert s2 == 209
assert np.isclose(np.linalg.norm(M @ one), np.sqrt(209))     # direct check
