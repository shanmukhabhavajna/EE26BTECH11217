# q10.py  --  CBSE Class 12 Mathematics 65/C/3
# Uses only numpy; helper functions follow matgeo / CoordGeo and are written inline.
import numpy as np

# ---- Newton-Raphson ----
def newton(f, df, x0, tol=1e-12, maxit=100):
    x = x0
    for _ in range(maxit):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# ---- determinants by cofactor expansion (only for evaluating |A|, never to solve equations) ----
def det2(M):
    return M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]

def det3(M):
    s = 0.0
    for j in range(3):
        minor = np.delete(np.delete(M, 0, axis=0), j, axis=1)
        s += (-1) ** j * M[0, j] * det2(minor)
    return s

# ---------------- solution ----------------
# CBSE 65/C/3 Q10: roots of | x 0 8 ; 4 1 3 ; 2 0 x | = 0
def D(x):
    return det3(np.array([[x, 0, 8], [4, 1, 3], [2, 0, x]], dtype=float))

# expanding along the second column: D(x) = x^2 - 16
for x in (-3.0, 0.5, 2.0, 7.0):
    print("x = %5.1f  |.| = %9.4f   x^2 - 16 = %9.4f" % (x, D(x), x**2 - 16))
r1 = newton(lambda x: x**2 - 16, lambda x: 2 * x, 5.0)
r2 = newton(lambda x: x**2 - 16, lambda x: 2 * x, -5.0)
print("Newton-Raphson roots: %.6f, %.6f   |.| at roots: %.2e, %.2e" % (r1, r2, D(r1), D(r2)))
print("-> option (A) -4, 4")
