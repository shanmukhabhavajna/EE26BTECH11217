# q14.py  --  CBSE Class 12 Mathematics 65/C/3
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
# CBSE 65/C/3 Q14: integrating factor of  x dy/dx - y = log x
# Standard form dy/dx - y/x = (log x)/x, IF = exp(-int dx/x) = 1/x.
# Laplace: put x = e^t.  Then x dy/dx = dy/dt and  dy/dt - y = t  ->  s Y - y0 - Y = 1/s^2
# Y(s) = y0/(s-1) + 1/(s^2 (s-1)),  integrating factor in t is e^{-t} = 1/x.
C = 0.5                                       # assumed constant of the solution y = -(log x + 1) + C x
y_t = lambda t: -(t + 1) + C * np.exp(t)      # the same solution in t = log x
y0 = y_t(0.0)
for s in (3.0, 4.0):
    num = laplace(y_t, s, T=30.0, N=300000)
    Y = y0 / (s - 1) + 1 / (s**2 * (s - 1))
    print("s=%.0f  L{y(t)} = %.8f   Y(s) from the ODE = %.8f" % (s, num, Y))
# the IF 1/x makes the left side exact: d/dx (y/x) = (x y' - y)/x^2 = (log x)/x^2
xs = np.linspace(1, 5, 9)
yx = lambda x: -(np.log(x) + 1) + C * x
print("check d/dx(y/x) = log(x)/x^2 (Euler forward difference):")
print(np.round([euler_diff(lambda z: yx(z) / z, x) for x in xs], 5))
print(np.round(np.log(xs) / xs**2, 5))

# Euler forward method for the ODE  y' = y/x + (log x)/x ,  y(1) = C - 1
F = lambda x, y: y / x + np.log(x) / x
xe, ye = euler_ode(F, 1.0, C - 1, 5.0, 200)
x = np.linspace(1, 5, 200)
plt.plot(x, yx(x), 'b', label='$y=-(\\log x+1)+Cx$')
plt.plot(xe[::10], ye[::10], 'ro', ms=3, label='Euler forward')
plt.plot(x, 1 / x, 'g--', label='integrating factor $1/x$')
plt.xlabel('$x$'); plt.legend(); plt.grid(True)
savefig('q14.png')
