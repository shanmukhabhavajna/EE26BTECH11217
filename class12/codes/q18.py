# q18.py  --  CBSE Class 12 Mathematics 65/C/3
# Uses only numpy; helper functions follow matgeo / CoordGeo and are written inline.
import numpy as np

# ---- vector helpers (column vectors, as in matgeo / CoordGeo) ----
def dot(u_, v_):
    return (u_.T @ v_).item()

def norm(u_):
    return np.sqrt(dot(u_, u_))

def col(*a):
    return np.array(a, dtype=float).reshape(-1, 1)

# ---- Newton-Raphson ----
def newton(f, df, x0, tol=1e-12, maxit=100):
    x = x0
    for _ in range(maxit):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# ---------------- solution ----------------
# CBSE 65/C/3 Q18: a = 2i - j + 2k, b = 5i - 3j - 4k.  (proj of a on b)/(proj of b on a)
a = col(2, -1, 2)
b = col(5, -3, -4)
pab = dot(a, b) / norm(b)                       # projection of a on b
pba = dot(a, b) / norm(a)                       # projection of b on a
print("a.b = %.1f, |a| = %.4f, |b| = %.4f" % (dot(a, b), norm(a), norm(b)))
print("ratio = %.6f, |a|/|b| = %.6f, 3/(5 sqrt2) = %.6f" % (pab / pba, norm(a) / norm(b), 3 / (5 * np.sqrt(2))))

# (OR) unit vectors a^, b^ with c = a^ + 2 b^ and d = 5 a^ - 4 b^ perpendicular
#      c.d = 5 - 4 cos(t) + 10 cos(t) - 8 = -3 + 6 cos(t) = 0 : solve with Newton-Raphson
f = lambda t: -3 + 6 * np.cos(t)
df = lambda t: -6 * np.sin(t)
t = newton(f, df, 1.0)
ah = col(1, 0)
bh = col(np.cos(t), np.sin(t))
print("angle = %.6f deg" % np.degrees(t))
print("c.d = %.2e" % dot(ah + 2 * bh, 5 * ah - 4 * bh))
