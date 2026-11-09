# q26.py  --  CBSE Class 12 Mathematics 65/C/3
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
# CBSE 65/C/3 Q26: x dy/dx = x + y.   Put x = e^t:  dy/dt - y = e^t.
# Laplace:  s Y - y0 - Y = 1/(s-1)  ->  Y(s) = y0/(s-1) + 1/(s-1)^2  ->  y = (y0 + t) e^t = x (C + log x)
C = 0.5                                        # assumed y0 = y(x = 1)
y_t = lambda t: (C + t) * np.exp(t)
for s in (3.0, 4.0):
    num = laplace(y_t, s, T=30.0, N=300000)
    Y = C / (s - 1) + 1 / (s - 1)**2
    print("s=%.0f  L{(C+t)e^t} = %.8f   Y(s) from the ODE = %.8f" % (s, num, Y))
# Euler forward method for dy/dx = (x + y)/x, y(1) = C
F = lambda x, y: (x + y) / x
xe, ye = euler_ode(F, 1.0, C, 4.0, 300)
y_x = lambda x: x * (C + np.log(x))
print("Euler forward at x = 4: %.5f, exact %.5f" % (ye[-1], y_x(4.0)))

x = np.linspace(0.3, 4, 300)
for Cc in (-1, 0, 0.5, 1):
    plt.plot(x, x * (Cc + np.log(x)), label='$C=%g$' % Cc)
plt.plot(xe[::15], ye[::15], 'ko', ms=3, label='Euler forward ($C=0.5$)')
plt.xlabel('$x$'); plt.ylabel('$y=x(C+\\log x)$'); plt.ylim(-3, 6); plt.legend(); plt.grid(True)
savefig('q26.png')
