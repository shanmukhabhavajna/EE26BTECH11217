# q9.py  --  CBSE Class 12 Mathematics 65/C/3
# Uses only numpy; helper functions follow matgeo / CoordGeo and are written inline.
import numpy as np

# ---- trapezoidal rule ----
def trapz(y, x):
    return float(np.sum(0.5 * (y[1:] + y[:-1]) * (x[1:] - x[:-1])))

# ---------------- solution ----------------
# CBSE 65/C/3 Q9: int_0^1 tan(sin^{-1} x) dx
# x = sin(theta):  tan(theta) cos(theta) d theta = sin(theta) d theta,  theta in [0, pi/2]
# (the integrand tan(asin x) = x / sqrt(1-x^2) is infinite at x = 1, so the substitution is used)
theta = np.linspace(0, np.pi / 2, 10001)
x = np.sin(theta[1:-1])
print("check tan(asin x) cos(theta) = sin(theta):", np.allclose(np.tan(np.arcsin(x)) * np.cos(theta[1:-1]), np.sin(theta[1:-1])))
for N in (10, 100, 1000, 10000):
    th = np.linspace(0, np.pi / 2, N + 1)
    print("N = %5d  trapezoidal rule = %.8f" % (N, trapz(np.sin(th), th)))
I = trapz(np.sin(theta), theta)
print("integral = %.6f -> option (D) 1" % I)
