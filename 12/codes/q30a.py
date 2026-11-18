import numpy as np
import numpy.linalg as LA

# shortest distance between skew lines
a1 = np.array([1, -1, 0]).reshape(-1, 1)
m1 = np.array([2, 3, 1]).reshape(-1, 1)
a2 = np.array([-1, 2, 2]).reshape(-1, 1)
m2 = np.array([5, 1, 0]).reshape(-1, 1)

n = np.cross(m1.T, m2.T).reshape(-1, 1)
d = abs(n.T @ (a2 - a1)).item()/LA.norm(n)
print("n =", n.flatten(), " d =", d, " 9/sqrt(195) =", 9/np.sqrt(195))

# check: minimise |(a1 + l m1) - (a2 + u m2)| over l, u by least squares
M = np.block([m1, -m2])
lu = LA.lstsq(M, a2 - a1, rcond=None)[0]
d_ls = LA.norm(M @ lu - (a2 - a1))
print("least-squares distance =", d_ls)
assert np.isclose(d, d_ls) and d > 1e-9          # d != 0, lines do not intersect
