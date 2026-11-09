# q8.py  --  CBSE Class 10 Maths (Standard) 30/C/3
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
# CBSE 30/C/3 Q8: (a) k for which 3x^2 - kx + 3 = 0 has equal roots
#                 (OR) discriminant of 3*sqrt(3) x^2 + 10 x + sqrt(3) = 0
# (a) D(k) = k^2 - 4(3)(3) = k^2 - 36 = 0, solve by Newton-Raphson
D = lambda k: k**2 - 4 * 3 * 3
dD = lambda k: 2 * k
k1 = newton(D, dD, 10.0)
k2 = newton(D, dD, -10.0)
print("k = %.6f and %.6f   -> option (C) +-6" % (k1, k2))

# (OR) discriminant b^2 - 4ac
a2, b2, c2 = 3 * np.sqrt(3), 10.0, np.sqrt(3)
disc = b2**2 - 4 * a2 * c2
print("discriminant = %.6f -> option (D) 64" % disc)

k = np.linspace(-9, 9, 200)
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(k, D(k)); ax[0].plot([k1, k2], [0, 0], 'ro')
ax[0].set_xlabel('$k$'); ax[0].set_ylabel('$D(k)=k^2-36$'); ax[0].grid(True)
x = np.linspace(-1, 3, 200)
ax[1].plot(x, 3 * x**2 - 6 * x + 3, label='k=6, double root at x=1')
ax[1].plot([1], [0], 'ro'); ax[1].legend(); ax[1].set_xlabel('$x$'); ax[1].grid(True)
savefig('q8.png')
