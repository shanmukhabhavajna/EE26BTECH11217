import numpy as np
import numpy.linalg as LA

# planes n1^T x = c1 and n2^T x = c2 written as 4x - 4y + 2z = -5 and 2x - 2y + z = -6
n1, c1 = np.array([4.0, -4.0, 2.0]), -5.0
n2, c2 = np.array([2.0, -2.0, 1.0]), -6.0

# normalised equations: divide by the norm of the normal vector
nh1, d1 = n1/LA.norm(n1), c1/LA.norm(n1)
nh2, d2 = n2/LA.norm(n2), c2/LA.norm(n2)
print("unit normals =", nh1, nh2, " offsets =", d1, d2)
assert np.allclose(nh1, nh2)                 # parallel planes with the same unit normal

# distance between the planes = |d1 - d2|
dist = abs(d1 - d2)
print("distance =", dist, " 7/6 =", 7/6)
assert np.isclose(dist, 7/6)
