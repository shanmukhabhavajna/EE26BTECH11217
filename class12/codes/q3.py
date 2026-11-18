# q3.py  --  CBSE Class 12 Mathematics 65/C/3
# Uses only numpy; helper functions follow matgeo / CoordGeo and are written inline.
import numpy as np

# ---- vector helpers (column vectors, as in matgeo / CoordGeo) ----
def dot(u_, v_):
    return (u_.T @ v_).item()

def norm(u_):
    return np.sqrt(dot(u_, u_))

def col(*a):
    return np.array(a, dtype=float).reshape(-1, 1)

# ---------------- solution ----------------
# CBSE 65/C/3 Q3: distance between the planes 4x - 4y + 2z + 5 = 0 and 2x - 2y + z + 6 = 0
n1, c1 = col(4, -4, 2), -5.0                  # n^T x = c  form
n2, c2 = col(2, -2, 1), -6.0
lam = dot(n1, n2) / dot(n2, n2)               # n1 = lam n2 ?
print("n1 = %.1f n2, residual %.2e -> planes are parallel" % (lam, norm(n1 - lam * n2)))
# bring the second plane to the normal n1:  lam n2^T x = lam c2
c2s = lam * c2
d = abs(c1 - c2s) / norm(n1)
print("distance = |c1 - c2'| / |n1| = %.6f, 7/6 = %.6f" % (d, 7 / 6))
for lab, v in zip("ABCD", [1 / 6, 7 / 6, 11 / 6, 16 / 6]):
    print("(%s) %.6f %s" % (lab, v, "<-- answer" if np.isclose(d, v) else ""))
