# q17.py  --  CBSE Class 12 Mathematics 65/C/3
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

# ---- Euler forward method for dy/dx = F(x, y) ----
def euler_ode(F, x0, y0, x1, n):
    x = np.linspace(x0, x1, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    h = x[1] - x[0]
    for i in range(n):
        y[i + 1] = y[i] + h * F(x[i], y[i])
    return x, y

# ---------------- solution ----------------
# CBSE 65/C/3 Q17: log(dy/dx) = a x + b y.  dy/dx = e^{ax+by}  ->  e^{-by} dy = e^{ax} dx
#   e^{ax}/a + e^{-by}/b + C = 0
# Numerical check with a = b = 1 (assumed) and y(0) = 0:  e^x + e^{-y} = 2
a_, b_ = 1.0, 1.0
y_exact = lambda x: -np.log(2 - np.exp(x))      # from e^x + e^{-y} = 2
F = lambda x, y: np.exp(a_ * x + b_ * y)
xe, ye = euler_ode(F, 0.0, 0.0, 0.5, 500)         # Euler forward method
print("Euler forward at x = 0.5: %.5f, exact %.5f" % (ye[-1], y_exact(0.5)))

# Laplace (derivative property on [0, 0.5]):  L{y'} = s Y - y(0) + e^{-sT} y(T)
dy = lambda t: np.exp(t + y_exact(t))
for s in (1.0, 2.0, 4.0):
    lhs, rhs = lap_first(y_exact, dy, s, T=0.5, N=100000)
    print("s=%.0f  L{e^{x+y}} = %.8f   sY - y(0) + e^{-sT}y(T) = %.8f" % (s, lhs, rhs))
# the relation e^{ax}/a + e^{-by}/b is constant along the solution
xs = np.linspace(0, 0.5, 6)
print("e^x + e^-y along the solution:", np.round(np.exp(xs) + np.exp(-y_exact(xs)), 8))

x = np.linspace(0, 0.5, 200)
plt.plot(x, y_exact(x), 'b', label='$e^x+e^{-y}=2$')
plt.plot(xe[::25], ye[::25], 'ro', ms=3, label='Euler forward')
plt.xlabel('$x$'); plt.ylabel('$y$'); plt.legend(); plt.grid(True)
savefig('q17.png')
