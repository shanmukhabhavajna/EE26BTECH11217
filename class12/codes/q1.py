# q1.py  --  CBSE Class 12 Mathematics 65/C/3
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
# CBSE 65/C/3 Q1: a, b, c position vectors of A(2,3,-4), B(3,-4,-5), C(3,2,-3). |a + b + c| = ?
a = col(2, 3, -4)
b = col(3, -4, -5)
c = col(3, 2, -3)
s = a + b + c
m2 = dot(s, s)
print("a + b + c =", s.flatten())
print("|a+b+c|^2 = %.1f, |a+b+c| = %.6f" % (m2, np.sqrt(m2)))
for lab, v in zip("ABCD", [113, 185, 203, 209]):
    print("(%s) sqrt(%d) %s" % (lab, v, "<-- answer" if np.isclose(m2, v) else ""))
