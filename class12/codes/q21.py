# q21.py  --  CBSE Class 12 Mathematics 65/C/3
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
# CBSE 65/C/3 Q21: y = sqrt(a + sqrt(a + x)). Find dy/dx.   Take a = 1 (assumed), x -> t.
# chain rule:  dy/dx = 1/(2 sqrt(a + sqrt(a+x))) * 1/(2 sqrt(a+x))
a = 1.0
y = lambda t: np.sqrt(a + np.sqrt(a + np.asarray(t, dtype=float)))
dy = lambda t: 1 / (4 * np.sqrt(a + np.sqrt(a + np.asarray(t, dtype=float))) * np.sqrt(a + np.asarray(t, dtype=float)))
# Laplace:  L{y'} = s Y(s) - y(0)
for s in (1.0, 2.0, 3.0):
    lhs, rhs = lap_first(y, dy, s)
    print("s=%.0f  L{y'} = %.8f   sY - y(0) = %.8f" % (s, lhs, rhs))
# Euler forward difference
for x0 in (0.5, 2.0, 5.0):
    print("x=%.1f  Euler = %.6f   formula = %.6f" % (x0, euler_diff(y, x0), dy(x0)))
