# q15.py  --  CBSE Class 10 Maths (Standard) 30/C/3
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
# CBSE 30/C/3 Q15: alpha, beta zeros of 2x^2 - 5x - 4. Find 1/alpha + 1/beta
f = lambda x: 2 * x**2 - 5 * x - 4
df = lambda x: 4 * x - 5
alpha = newton(f, df, 3.0)                   # Newton-Raphson from two starting points
beta = newton(f, df, -1.0)
s = 1 / alpha + 1 / beta
print("alpha = %.6f, beta = %.6f" % (alpha, beta))
print("1/alpha + 1/beta = %.6f" % s)
print("(alpha+beta)/(alpha beta) = %.6f, (-b/a)/(c/a) = %.6f" % ((alpha + beta) / (alpha * beta), (5 / 2) / (-2)))

x = np.linspace(-1.5, 3.8, 200)
plt.plot(x, f(x)); plt.plot([alpha, beta], [0, 0], 'ro')
plt.annotate(r'$\alpha$', (alpha, 0), textcoords="offset points", xytext=(5, 8))
plt.annotate(r'$\beta$', (beta, 0), textcoords="offset points", xytext=(-12, 8))
plt.xlabel('$x$'); plt.ylabel('$f(x)$'); plt.grid(True)
savefig('q15.png')
