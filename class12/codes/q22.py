# q22.py  --  CBSE Class 12 Mathematics 65/C/3
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
# CBSE 65/C/3 Q22: 2i - j + k, i - 3j - 5k, 3i - 4j - 4k form a right-angled triangle
A = col(2, -1, 1)
B = col(1, -3, -5)
C = col(3, -4, -4)
AB, BC, CA = B - A, C - B, A - C
sides = [dot(AB, AB), dot(BC, BC), dot(CA, CA)]
print("AB^2 = %.0f, BC^2 = %.0f, CA^2 = %.0f" % tuple(sides))
print("AB.BC = %.0f, BC.CA = %.0f, CA.AB = %.0f" % (dot(AB, BC), dot(BC, CA), dot(CA, AB)))
print("BC^2 + CA^2 = %.0f = AB^2 = %.0f" % (sides[1] + sides[2], sides[0]))
print("right angle at C (CB.CA = %.0f)" % dot(B - C, A - C))
