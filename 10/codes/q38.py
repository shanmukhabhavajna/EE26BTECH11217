import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# figures are saved in ../figs, whichever folder the script is run from
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figs')
os.makedirs(FIG, exist_ok=True)

# Functions below are taken from CoordGeo (G. V. V. Sharma, GNU GPL),
# copied here so that no CoordGeo module has to be imported.

#Generate line points
def line_gen(A, B):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim, len))
  lam_1 = np.linspace(0, 1, len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B - A)
    x_AB[:, i] = temp1.T
  return x_AB

# B takes x days, A takes x - 16 days: 1/(x - 16) + 1/x = 1/15
#   -> f(x) = x^2 - 46 x + 240 = 0
f  = lambda x: x**2 - 46*x + 240
df = lambda x: 2*x - 46

# Newton-Raphson: x_{n+1} = x_n - f(x_n)/f'(x_n)
def newton(f, df, x0, n=6):
  x = [x0]
  for _ in range(n):
    x.append(x[-1] - f(x[-1])/df(x[-1]))
  return np.array(x)

xs = newton(f, df, 50.0)
print("x0 = 50 :", np.round(xs, 4))
print("x0 = 0  :", np.round(newton(f, df, 0.0), 4))
assert np.isclose(xs[-1], 40)
assert np.isclose(newton(f, df, 0.0)[-1], 6)

# A takes x - 16 days, which must be positive, so x = 6 is rejected
x = xs[-1]
print("B takes", x, "days, A takes", x - 16, "days; joint rate =", 1/(x - 16) + 1/x, " 1/15 =", 1/15)
assert np.isclose(1/(x - 16) + 1/x, 1/15)

# plot of f(x) with the Newton iterates from x0 = 50
xx = np.linspace(-2, 52, 300)
plt.figure(figsize=(7, 5))
plt.plot(xx, f(xx), 'b', label=r'$f(x) = x^2 - 46x + 240$')
for i in range(3):
  P1 = np.array([[xs[i]], [f(xs[i])]])
  P2 = np.array([[xs[i+1]], [0.0]])
  s = line_gen(P1, P2)
  plt.plot(s[0, :], s[1, :], 'r--', linewidth=0.9)         # tangent at x_n
  s = line_gen(P2, np.array([[xs[i+1]], [f(xs[i+1])]]))
  plt.plot(s[0, :], s[1, :], 'g:', linewidth=0.9)          # vertical to the curve
pts = np.array([[xs[0], xs[1], xs[2], 40.0, 6.0],
                [f(xs[0]), f(xs[1]), f(xs[2]), 0.0, 0.0]])
plt.scatter(pts[0, :], pts[1, :], color='k', zorder=3)
labels = [f"({xs[0]:.0f}, {f(xs[0]):.0f})", f"({xs[1]:.2f}, {f(xs[1]):.2f})",
          f"({xs[2]:.2f}, {f(xs[2]):.2f})", '(40, 0)', '(6, 0)']
for i, (t, off) in enumerate(zip(labels, [(-35, 5), (-45, 10), (45, 20), (0, -16), (0, 12)])):
  plt.annotate(t, (pts[0, i], pts[1, i]), textcoords="offset points", xytext=off, ha='center')
plt.axhline(0, color='k', linewidth=0.8)
plt.axvline(0, color='k', linewidth=0.8)
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.legend(loc='upper center')
plt.grid(True)
plt.savefig(os.path.join(FIG, 'q38_quad.png'), bbox_inches='tight')
#plt.show()
