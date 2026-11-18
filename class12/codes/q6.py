# q6.py  --  CBSE Class 12 Mathematics 65/C/3
# Uses only numpy; helper functions follow matgeo / CoordGeo and are written inline.
import numpy as np

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
# CBSE 65/C/3 Q6: sec^{-1}((1+x)/(1-y)) = a. Find dy/dx.
# (1+x)/(1-y) = sec a = k  =>  y = 1 - (1 + x)/k.   Take a = 1 rad (assumed), x -> t.
k = 1 / np.cos(1.0)
y = lambda t: 1 - (1 + t) / k
dy = lambda t: -np.ones_like(np.asarray(t, dtype=float)) / k   # claimed derivative -1/k

# Laplace:  L{y'}(s) = s Y(s) - y(0)
for s in (1.0, 2.0, 3.0):
    lhs, rhs = lap_first(y, dy, s)
    print("s=%.0f  L{y'} = %.8f   sY - y(0) = %.8f" % (s, lhs, rhs))
# Euler forward difference
x0 = 0.5
print("Euler forward difference at x=0.5: %.6f,  -1/k = %.6f" % (euler_diff(y, x0), -1 / k))
# compare with the options
yv = y(x0)
opts = {'A': (x0 - 1) / (yv - 1), 'B': (x0 - 1) / (yv + 1), 'C': (yv - 1) / (x0 + 1), 'D': (yv + 1) / (x0 - 1)}
for lab, v in opts.items():
    print("(%s) %.6f %s" % (lab, v, "<-- answer" if np.isclose(v, -1 / k) else ""))
