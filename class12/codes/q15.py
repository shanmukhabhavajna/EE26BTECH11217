# q15.py  --  CBSE Class 12 Mathematics 65/C/3
# Uses only numpy and matplotlib; helper functions follow matgeo / CoordGeo and are written inline.
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

# ---- trapezoidal rule ----
def trapz(y, x):
    return float(np.sum(0.5 * (y[1:] + y[:-1]) * (x[1:] - x[:-1])))

# ---- Laplace transform (numerical, trapezoidal rule) ----
#  F(s) = int_0^T exp(-s t) f(t) dt
def laplace(f, s, T=40.0, N=400000):
    t = np.linspace(0, T, N + 1)
    return trapz(np.exp(-s * t) * f(t), t)

#  derivative property:  L{f'}(s) = s F(s) - f(0) + exp(-sT) f(T)   (last term -> 0 for large T)
def lap_first(f, df, s, T=40.0, N=400000):
    lhs = laplace(df, s, T, N)
    rhs = s * laplace(f, s, T, N) - f(0.0) + np.exp(-s * T) * f(T)
    return lhs, rhs

#  L{f''}(s) = s^2 F(s) - s f(0) - f'(0) + exp(-sT) (s f(T) + f'(T))
def lap_second(f, df, d2f, s, T=40.0, N=400000):
    lhs = laplace(d2f, s, T, N)
    rhs = s**2 * laplace(f, s, T, N) - s * f(0.0) - df(0.0) + np.exp(-s * T) * (s * f(T) + df(T))
    return lhs, rhs

# ---- Euler forward difference ----
def euler_diff(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h

def euler_diff2(f, x, h=1e-4):
    return (f(x + 2 * h) - 2 * f(x + h) + f(x)) / h**2

# ---------------- solution ----------------
# CBSE 65/C/3 Q15: y = log x. Find d^2y/dx^2.
# Laplace with t = x - 1:  y(t) = log(1 + t), y(0) = 0, y'(0) = 1,  y' = 1/(1+t), y'' = -1/(1+t)^2
y = lambda t: np.log(1 + np.asarray(t, dtype=float))
dy = lambda t: 1 / (1 + np.asarray(t, dtype=float))
d2y = lambda t: -1 / (1 + np.asarray(t, dtype=float))**2
for s in (2.0, 3.0, 5.0):
    a, b = lap_first(y, dy, s)
    c, d = lap_second(y, dy, d2y, s)
    print("s=%.0f  L{y'}=%.8f  sY-y(0)=%.8f   L{y''}=%.8f  s^2Y-sy(0)-y'(0)=%.8f" % (s, a, b, c, d))
# Euler forward differences in x
for x0 in (1.0, 2.0, 4.0):
    print("x=%.0f  Euler 2nd difference = %.5f   -1/x^2 = %.5f" % (x0, euler_diff2(np.log, x0), -1 / x0**2))

x = np.linspace(0.4, 4, 300)
xe = np.linspace(0.6, 4, 12)
plt.plot(x, np.log(x), label='$y=\\log x$')
plt.plot(x, 1 / x, label="$y'=1/x$")
plt.plot(x, -1 / x**2, label="$y''=-1/x^2$")
plt.plot(xe, [euler_diff2(np.log, v, 1e-3) for v in xe], 'ko', ms=3, label='Euler 2nd difference')
plt.ylim(-4, 2.5); plt.xlabel('$x$'); plt.legend(); plt.grid(True)
savefig('q15.png')
