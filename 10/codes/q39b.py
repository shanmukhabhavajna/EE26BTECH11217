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

# Part (b): p(x) = x^4 - 8x^3 + 23x^2 - 28x + 12 with zeroes 2 and 3
p = np.array([1.0, -8.0, 23.0, -28.0, 12.0])
# p(x) = (x^2 - 5x + 6)(x^2 + b x + c)
#      = x^4 + (b - 5) x^3 + (c - 5b + 6) x^2 + (6b - 5c) x + 6c
b = -8 + 5                                            # x^3 : b - 5 = -8
c = 23 + 5*b - 6                                      # x^2 : c - 5b + 6 = 23
assert np.isclose(6*b - 5*c, -28) and np.isclose(6*c, 12)   # last two are consistent
print("b, c =", b, c)
h = np.array([1.0, b, c])
assert np.allclose(np.polymul([1, -5, 6], h), p)      # multiply out to check

# remaining zeroes: zeroes of q(x) = x^2 - 3x + 2 by Newton-Raphson
q  = lambda x: np.polyval(h, x)
dq = lambda x: np.polyval(np.polyder(h), x)
for x0 in [0.0, 5.0]:
  print("x0 =", x0, ":", np.round(newton(q, dq, x0), 4))
assert np.isclose(newton(q, dq, 0.0)[-1], 1) and np.isclose(newton(q, dq, 5.0)[-1], 2)
print("zeroes of p:", np.sort(np.roots(p)))

# plot of p(x) and its zeroes (x = 2 appears twice)
P = lambda x: np.polyval(p, x)
xx = np.linspace(0.4, 3.6, 300)
plt.figure(figsize=(7, 5))
plt.plot(xx, P(xx), 'b', label=r'$p(x) = x^4 - 8x^3 + 23x^2 - 28x + 12$')
pts = np.array([[1.0, 2.0, 3.0], [0.0, 0.0, 0.0]])
plt.scatter(pts[0, :], pts[1, :], color='k', zorder=3)
for i, (t, off) in enumerate(zip(['(1, 0)', '(2, 0)', '(3, 0)'], [(0, 12), (0, 12), (0, 12)])):
  plt.annotate(t, (pts[0, i], pts[1, i]), textcoords="offset points", xytext=off, ha='center')
plt.axhline(0, color='k', linewidth=0.8)
plt.axvline(0, color='k', linewidth=0.8)
plt.xlabel('$x$')
plt.ylabel('$p(x)$')
plt.legend(loc='upper center')
plt.grid(True)
plt.savefig(os.path.join(FIG, 'q39b_quartic.png'), bbox_inches='tight')
#plt.show()
