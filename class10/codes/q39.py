# q39.py  --  CBSE Class 10 Maths (Standard) 30/C/3
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
# CBSE 30/C/3 Q39: f(x) = 3x^4 - 9x^3 + x^2 + 15x + k divisible by 3x^2 - 5; find k and two zeros
#                  (OR) all zeros of x^4 - 8x^3 + 23x^2 - 28x + 12 if two zeros are 2 and 3
g = np.array([3.0, 0.0, -5.0])
q0, r0 = np.polydiv(np.array([3.0, -9.0, 1.0, 15.0, 0.0]), g)   # f with k = 0
k = -r0[-1]                                    # remainder is r0 + k = 0
f = np.array([3.0, -9.0, 1.0, 15.0, k])
q, r = np.polydiv(f, g)
print("remainder (k=0) =", r0, " => k = %.1f" % k)
print("quotient =", q, " remainder =", r)
dq = np.polyder(q)
z1 = newton(lambda x: np.polyval(q, x), lambda x: np.polyval(dq, x), 0.0)
z2 = newton(lambda x: np.polyval(q, x), lambda x: np.polyval(dq, x), 3.0)
print("zeros from quotient: %.6f, %.6f" % (z1, z2))
print("zeros of 3x^2-5: +-%.6f" % np.sqrt(5 / 3))

# (OR)
p = np.array([1.0, -8.0, 23.0, -28.0, 12.0])
g2 = np.convolve([1.0, -2.0], [1.0, -3.0])     # (x-2)(x-3)
q2, r2 = np.polydiv(p, g2)
dq2 = np.polyder(q2)
y1 = newton(lambda x: np.polyval(q2, x), lambda x: np.polyval(dq2, x), 0.0)
y2 = newton(lambda x: np.polyval(q2, x), lambda x: np.polyval(dq2, x), 3.0)
print("(OR) quotient =", q2, " remainder =", r2, " zeros: 2, 3, %.6f, %.6f" % (y1, y2))

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
x = np.linspace(-2, 3.2, 300)
ax[0].plot(x, np.polyval(f, x))
zs = np.array([-np.sqrt(5 / 3), np.sqrt(5 / 3), z1, z2]); ax[0].plot(zs, np.zeros(4), 'ro')
ax[0].set_title('f(x), k = %.0f' % k)
x = np.linspace(0.3, 3.5, 300)
ax[1].plot(x, np.polyval(p, x)); ax[1].plot([y1, y2, 2, 3], np.zeros(4), 'ro')
ax[1].set_title('x^4-8x^3+23x^2-28x+12')
for a_ in ax: a_.axhline(0, color='k', lw=0.5); a_.grid(True)
savefig('q39.png')
