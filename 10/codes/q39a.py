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

# Newton-Raphson: x_{n+1} = x_n - f(x_n)/f'(x_n)
def newton(f, df, x0, n=6):
  x = [x0]
  for _ in range(n):
    x.append(x[-1] - f(x[-1])/df(x[-1]))
  return np.array(x)

# Part (a): f(x) = (3x^2 - 5)(x^2 + b x + c) = 3x^4 + 3b x^3 + (3c - 5) x^2 - 5b x - 5c
b = -9/3                                              # x^3 : 3b = -9
c = (1 + 5)/3                                         # x^2 : 3c - 5 = 1
assert np.isclose(-5*b, 15)                           # x   : -5b = 15 (consistent)
k = -5*c                                              # x^0 : -5c = k
print("b, c, k =", b, c, k)
assert np.isclose(k, -10)
# check by multiplying out
assert np.allclose(np.polymul([3, 0, -5], [1, b, c]), [3, -9, 1, 15, k])
h = np.array([1.0, b, c])

# zeroes of the quotient q(x) = x^2 - 3x + 2 by Newton-Raphson
q  = lambda x: np.polyval(h, x)
dq = lambda x: np.polyval(np.polyder(h), x)
for x0 in [5.0, 0.0]:
  print("x0 =", x0, ":", np.round(newton(q, dq, x0), 4))
assert np.isclose(newton(q, dq, 5.0)[-1], 2) and np.isclose(newton(q, dq, 0.0)[-1], 1)

# plot of q(x) with the Newton iterates from x0 = 5
xs = newton(q, dq, 5.0)
xx = np.linspace(-0.3, 5.5, 200)
plt.figure(figsize=(7, 5))
plt.plot(xx, q(xx), 'b', label=r'$q(x) = x^2 - 3x + 2$')
for i in range(3):
  P1 = np.array([[xs[i]], [q(xs[i])]])
  P2 = np.array([[xs[i+1]], [0.0]])
  s = line_gen(P1, P2)
  plt.plot(s[0, :], s[1, :], 'r--', linewidth=0.9)         # tangent at x_n
  s = line_gen(P2, np.array([[xs[i+1]], [q(xs[i+1])]]))
  plt.plot(s[0, :], s[1, :], 'g:', linewidth=0.9)
pts = np.array([[xs[0], xs[1], xs[2], 2.0, 1.0],
                [q(xs[0]), q(xs[1]), q(xs[2]), 0.0, 0.0]])
plt.scatter(pts[0, :], pts[1, :], color='k', zorder=3)
labels = [f"({xs[0]:.0f}, {q(xs[0]):.0f})", f"({xs[1]:.2f}, {q(xs[1]):.2f})",
          f"({xs[2]:.2f}, {q(xs[2]):.2f})", '(2, 0)', '(1, 0)']
for i, (t, off) in enumerate(zip(labels, [(-35, 5), (-45, 10), (38, -18), (10, -16), (0, 12)])):
  plt.annotate(t, (pts[0, i], pts[1, i]), textcoords="offset points", xytext=off, ha='center')
plt.axhline(0, color='k', linewidth=0.8)
plt.axvline(0, color='k', linewidth=0.8)
plt.xlabel('$x$')
plt.ylabel('$q(x)$')
plt.legend(loc='upper center')
plt.grid(True)
plt.savefig(os.path.join(FIG, 'q39a_quotient.png'), bbox_inches='tight')
#plt.show()
