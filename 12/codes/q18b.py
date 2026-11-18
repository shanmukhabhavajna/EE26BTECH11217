import numpy as np
import numpy.linalg as LA

# Function below is taken from CoordGeo (G. V. V. Sharma, GNU GPL),
# copied here so that no CoordGeo module has to be imported.

#Angle between two direction vectors
def ang_vec(m1, m2):
  num = m1 @ m2
  den = LA.norm(m1)*LA.norm(m2)
  return np.degrees(np.arccos(num/den))

# G = [[1,k],[k,1]], c = M(1,2), d = M(5,-4), c^T d = 6k - 3 = 0
p, q = np.array([1, 2]), np.array([5, -4])
# c^T d = k*(p0*q1 + p1*q0) + (p0*q0 + p1*q1) = 6k - 3
k = -(p @ q)/(p[0]*q[1] + p[1]*q[0])
print("k = cos(theta) =", k)

# verify with explicit unit vectors at that angle
th = np.arccos(k)
ah = np.array([1.0, 0.0])
bh = np.array([np.cos(th), np.sin(th)])
c, d = ah + 2*bh, 5*ah - 4*bh
print("c.d =", c @ d, " theta =", ang_vec(ah, bh), "deg")
assert np.isclose(c @ d, 0) and np.isclose(ang_vec(ah, bh), 60)
