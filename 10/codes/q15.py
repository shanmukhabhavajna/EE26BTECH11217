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

f  = lambda x: 2*x**2 - 5*x - 4
df = lambda x: 4*x - 5

xa = newton(f, df, 4.0)
xb = newton(f, df, -2.0)
print("x0 =  4 ->", np.round(xa[:6], 4))
print("x0 = -2 ->", np.round(xb[:6], 4))
alpha, beta = xa[-1], xb[-1]
print("alpha =", alpha, " beta =", beta)

S = 1/alpha + 1/beta
print("1/alpha + 1/beta =", S)
assert np.isclose(S, -5/4)

# plot: y = f(x), its zeros and the Newton iterates
x = np.linspace(-2.2, 4.2, 200)
fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(x, f(x), label='$y = 2x^2 - 5x - 4$')

base = line_gen(np.array([-2.2, 0.0]).reshape(-1, 1), np.array([4.2, 0.0]).reshape(-1, 1))
ax.plot(base[0, :], base[1, :], 'k-', linewidth=1)

ax.scatter(xa[:4], f(xa[:4]), color='g', zorder=3, label='Newton iterates')
ax.scatter(xb[:4], f(xb[:4]), color='g', zorder=3)

# mark the coordinates of the first Newton iterates
offs_a = [(-38, 0), (48, 20), (-45, 50)]
offs_b = [(38, 0), (-55, 22), (60, 50)]
arrow = dict(arrowstyle='-', color='gray')
for k in range(3):
  ax.annotate(f'({xa[k]:.4f}, {f(xa[k]):.4f})', (xa[k], f(xa[k])), textcoords="offset points",
              xytext=offs_a[k], ha='center', fontsize=8, arrowprops=arrow)
  ax.annotate(f'({xb[k]:.4f}, {f(xb[k]):.4f})', (xb[k], f(xb[k])), textcoords="offset points",
              xytext=offs_b[k], ha='center', fontsize=8, arrowprops=arrow)

roots = np.block([[alpha, beta], [0.0, 0.0]])
ax.scatter(roots[0, :], roots[1, :], color='r', zorder=4)
for i, txt in enumerate(['$\\alpha$', '$\\beta$']):
  ax.annotate(f'{txt}\n({roots[0, i]:.4f}, 0)', (roots[0, i], 0),
              textcoords="offset points", xytext=[(0, -34), (-10, -34)][i], ha='center')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_ylim(-9, 28)
ax.legend(loc='upper center')
ax.grid(True)
plt.savefig(os.path.join(FIG, 'q15_newton.png'), bbox_inches='tight')
#plt.show()
