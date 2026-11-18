import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# figures are saved in ../figs, whichever folder the script is run from
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figs')
os.makedirs(FIG, exist_ok=True)

# Function below is taken from CoordGeo (G. V. V. Sharma, GNU GPL),
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

# coefficient vector (A, B, C) of 9x^2 - 6a^2 x + a^4 - b^4 for a = 2, b = 1
a, b = 2.0, 1.0
v = np.array([9.0, -6*a**2, a**4 - b**4])

# quadratic formula: D = B^2 - 4AC = 36 b^4
D = v[1]**2 - 4*v[0]*v[2]
print("D =", D, " 36 b^4 =", 36*b**4)
assert np.isclose(D, 36*b**4)
roots = np.array([(a**2 + b**2)/3, (a**2 - b**2)/3])
print("quadratic formula roots =", roots)

# Newton-Raphson on f(x) = 9x^2 - 6a^2 x + a^4 - b^4, starting on each side of the vertex x = a^2/3
f  = lambda x: v[0]*x**2 + v[1]*x + v[2]
df = lambda x: 2*v[0]*x + v[1]
for x0 in [3.0, 0.0]:
  x = newton(f, df, x0)
  print("x0 =", x0, "->", np.round(x[:7], 4))
  assert np.isclose(x[-1], roots).any()
assert np.isclose(newton(f, df, 3.0)[-1], roots[0])
assert np.isclose(newton(f, df, 0.0)[-1], roots[1])

# plot: y = f(x) for a = 2, b = 1, its roots and the Newton iterates
xa = newton(f, df, 3.0)
xb = newton(f, df, 0.0)
x = np.linspace(-0.6, 3.4, 200)
fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(x, f(x), label='$y = 9x^2 - 24x + 15$')

base = line_gen(np.array([-0.6, 0.0]).reshape(-1, 1), np.array([3.4, 0.0]).reshape(-1, 1))
ax.plot(base[0, :], base[1, :], 'k-', linewidth=1)

ax.scatter(xa[:4], f(xa[:4]), color='g', zorder=3, label='Newton iterates')
ax.scatter(xb[:4], f(xb[:4]), color='g', zorder=3)

# coordinates of the first Newton iterates
offs_a = [(-40, 0), (50, 28), (78, 8)]
offs_b = [(40, 0), (45, 20), (-55, 40)]
arrow = dict(arrowstyle='-', color='gray')
for k in range(3):
  ax.annotate(f'({xa[k]:.4f}, {f(xa[k]):.4f})', (xa[k], f(xa[k])), textcoords="offset points",
              xytext=offs_a[k], ha='center', fontsize=8, arrowprops=arrow)
  ax.annotate(f'({xb[k]:.4f}, {f(xb[k]):.4f})', (xb[k], f(xb[k])), textcoords="offset points",
              xytext=offs_b[k], ha='center', fontsize=8, arrowprops=arrow)

pts = np.block([[roots[0], roots[1]], [0.0, 0.0]])
ax.scatter(pts[0, :], pts[1, :], color='r', zorder=4)
ax.annotate(f'({pts[0, 0]:.4f}, 0)', (pts[0, 0], 0), textcoords="offset points", xytext=(30, -22), ha='center')
ax.annotate(f'({pts[0, 1]:.4f}, 0)', (pts[0, 1], 0), textcoords="offset points", xytext=(-30, -22), ha='center')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_ylim(-5, 27)
ax.legend(loc='upper left')
ax.grid(True)
plt.savefig(os.path.join(FIG, 'q23_newton.png'), bbox_inches='tight')
#plt.show()
