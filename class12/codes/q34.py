# q34.py  --  CBSE Class 12 Mathematics 65/C/3
# Uses only numpy; helper functions follow matgeo / CoordGeo and are written inline.
import numpy as np

# ---- trapezoidal rule ----
def trapz(y, x):
    return float(np.sum(0.5 * (y[1:] + y[:-1]) * (x[1:] - x[:-1])))

# ---------------- solution ----------------
# CBSE 65/C/3 Q34: int_1^3 (x^2 + 1 + e^x) dx  (as a limit of sums)
f = lambda x: x**2 + 1 + np.exp(x)
exact = (3**3 / 3 + 3 + np.exp(3)) - (1 / 3 + 1 + np.exp(1))     # [x^3/3 + x + e^x]_1^3
print("N        trapezoidal rule")
for N in (4, 16, 64, 256, 1024, 4096, 16384):
    x = np.linspace(1, 3, N + 1)
    print("%6d   %.8f" % (N, trapz(f(x), x)))
print("limit of sums: 32/3 + e^3 - e = %.8f" % exact)
