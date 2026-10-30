# CBSE 65-C-3 (Class 12) -- Q31
# Find a unit vector perpendicular to each of (a + b) and (a - b),
# where a = i + j + k and b = i + 2j + 3k.   (matgeo style)
import os
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt



def norm_vec(M):                             # n with M n = 0, the last right singular vector
    return LA.svd(M)[2][-1].reshape(-1, 1)

a = np.array([1, 1, 1]).reshape(-1, 1)
b = np.array([1, 2, 3]).reshape(-1, 1)
p = a + b                                    # (2, 3, 4)
q = a - b                                    # (0, -1, -2)
print(p.ravel(), q.ravel())

# n^T p = 0 and n^T q = 0  ->  M n = 0
M = np.block([p, q]).T
n = norm_vec(M)                              # already of unit length
n = n*np.sign(-n[0, 0])                      # choose the sign with first entry -1/sqrt(6)
print("n =", n.ravel(), " ||n|| =", LA.norm(n))
print("1/sqrt(6)*(-1, 2, -1) =", np.array([-1, 2, -1])/np.sqrt(6))
print("n^T p, n^T q =", (n.T @ p)[0, 0], (n.T @ q)[0, 0])   # both 0
print("cross-product check:", np.cross(p.ravel(), q.ravel()), LA.norm(np.cross(p.ravel(), q.ravel())))  # (-2,4,-2), 2 sqrt(6)


