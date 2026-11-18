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
def newton(f, df, x0, n=8):
  x = [x0]
  for _ in range(n):
    x.append(x[-1] - f(x[-1])/df(x[-1]))
  return np.array(x)

# discriminant of 3x^2 - kx + 3 is D(k) = k^2 - 36 ; equal roots <=> D(k) = 0
D  = lambda k: k**2 - 4*3*3
dD = lambda k: 2*k
for k0 in [10.0, -10.0]:
  k = newton(D, dD, k0)
  print("k0 =", k0, "->", np.round(k[:6], 6))
  assert np.isclose(k[-1], np.sign(k0)*6)

# plot of D(k) with the Newton iterates from k0 = 10
k = newton(D, dD, 10.0)[:4]
kk = np.linspace(-11, 11, 200)
plt.figure(figsize=(7, 5))
plt.plot(kk, D(kk), 'b', label=r'$D(k) = k^2 - 36$')
for i in range(3):
  P1 = np.array([[k[i]], [D(k[i])]])
  P2 = np.array([[k[i+1]], [0.0]])
  s = line_gen(P1, P2)
  plt.plot(s[0, :], s[1, :], 'r--', linewidth=0.9)       # tangent at k_n
  s = line_gen(P2, np.array([[k[i+1]], [D(k[i+1])]]))
  plt.plot(s[0, :], s[1, :], 'g:', linewidth=0.9)        # vertical to the curve
pts = np.block([[np.array([[k[0], k[1], k[2], 6.0, -6.0], [D(k[0]), D(k[1]), D(k[2]), 0.0, 0.0]])]])
plt.scatter(pts[0, :], pts[1, :], color='k', zorder=3)
for i, (t, off) in enumerate(zip(['(10, 64)', '(6.8, 10.24)', '(6.05, 0.57)', '(6, 0)', '(-6, 0)'],
                                 [(-30, 0), (38, 8), (45, -14), (0, -16), (0, -16)])):
  plt.annotate(t, (pts[0, i], pts[1, i]), textcoords="offset points", xytext=off, ha='center')
plt.axhline(0, color='k', linewidth=0.8)
plt.axvline(0, color='k', linewidth=0.8)
plt.xlabel('$k$')
plt.ylabel('$D(k)$')
plt.legend(loc='upper center')
plt.grid(True)
plt.savefig(os.path.join(FIG, 'q8a_newton.png'), bbox_inches='tight')
#plt.show()
