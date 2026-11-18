# q23.py  --  CBSE Class 10 Maths (Standard) 30/C/3
# Uses only numpy and matplotlib; helper functions are copied inline from matgeo / CoordGeo.
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figs')
def savefig(name):
    os.makedirs(FIG, exist_ok=True)
    plt.savefig(os.path.join(FIG, name), dpi=200, bbox_inches='tight')
    plt.close()

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
# CBSE 30/C/3 Q23: solve 9x^2 - 6 a^2 x + a^4 - b^4 = 0 by the quadratic formula
def roots(a, b):
    A, B, Cc = 9.0, -6 * a**2, a**4 - b**4
    D = B**2 - 4 * A * Cc                    # = 36 b^4
    return float((-B + np.sqrt(D)) / (2 * A)), float((-B - np.sqrt(D)) / (2 * A))

a, b = 2.0, 1.0                              # assumed values
x1, x2 = roots(a, b)
print("a=%.1f b=%.1f  roots = %.6f, %.6f  (a^2+b^2)/3 = %.6f, (a^2-b^2)/3 = %.6f"
      % (a, b, x1, x2, (a**2 + b**2) / 3, (a**2 - b**2) / 3))

# check with Newton-Raphson
f = lambda x: 9 * x**2 - 6 * a**2 * x + a**4 - b**4
df = lambda x: 18 * x - 6 * a**2
print("Newton-Raphson roots: %.6f, %.6f" % (newton(f, df, 3.0), newton(f, df, 0.0)))
for a, b in [(1, 2), (3, 1), (2.5, 0.5)]:
    print("a=%.1f b=%.1f roots =" % (a, b), roots(a, b), " expected", ((a**2 + b**2) / 3, (a**2 - b**2) / 3))

a, b = 2.0, 1.0
x = np.linspace(0, 3, 200)
plt.plot(x, f(x)); plt.plot([x1, x2], [0, 0], 'ro')
plt.xlabel('$x$'); plt.ylabel('$f(x)$'); plt.grid(True)
savefig('q23.png')
