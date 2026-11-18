# q20.py  --  CBSE Class 12 Mathematics 65/C/3
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
# CBSE 65/C/3 Q20: distance of the point (a, b, c) from the x-axis
e1 = col(1, 0, 0)
for a, b, c in [(2, 3, 6), (1, -4, 3), (5, 0, -2)]:
    P = col(a, b, c)
    foot = dot(P, e1) * e1                      # foot of the perpendicular on the x-axis
    d = norm(P - foot)
    print("P = (%g, %g, %g): foot = %s, distance = %.6f, sqrt(b^2 + c^2) = %.6f"
          % (a, b, c, foot.flatten(), d, np.sqrt(b**2 + c**2)))
