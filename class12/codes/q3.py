import numpy as np
import numpy.linalg as LA

n1 = np.array([4, -4, 2]).reshape(-1, 1);  c1 = -5   # 4x-4y+2z+5=0
n2 = np.array([2, -2, 1]).reshape(-1, 1);  c2 = -6   # 2x-2y+z+6=0
n2s, c2s = 2*n2, 2*c2                                # same normal as plane 1
print("same normal:", np.allclose(n1, n2s))          # True

d = abs(c1 - c2s) / LA.norm(n1)
print("distance =", d, "= 7/6 =", 7/6)               # 1.1666...

# check: point on plane 1, distance to plane 2
P = np.array([0, 0, c1/2]).reshape(-1, 1)
print("check =", abs((n2.T @ P).item() - c2) / LA.norm(n2))   # 1.1666...
