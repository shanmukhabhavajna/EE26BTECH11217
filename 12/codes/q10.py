import os
import numpy as np
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

#Labeling points
def label_pts(G_v, vert_labels):
  for i, txt in enumerate(vert_labels):
    plt.annotate(txt,                       # this is the text
                 (G_v[0, i], G_v[1, i]),    # this is the point to label
                 textcoords="offset points",
                 xytext=(0, 10),            # distance from text to points (x,y)
                 ha='center')

# Determinant of [[x,0,8],[4,1,3],[2,0,x]], expanded along column 2: x^2 - 16
def f(x):  return x**2 - 16
def df(x): return 2*x

def newton(x0, N=6):
    xs = [x0]
    for _ in range(N):
        xs.append(xs[-1] - f(xs[-1])/df(xs[-1]))      # x_{n+1} = x_n - f/f'
    return np.array(xs)

# check the determinant numerically at a few points
for x in [-3.0, 0.5, 2.0, 5.0]:
    M = np.array([[x, 0, 8], [4, 1, 3], [2, 0, x]])
    assert np.isclose(np.linalg.det(M), f(x))

for x0 in [6.0, -6.0]:
    print(f"x0 = {x0:+.0f}:", np.round(newton(x0), 6))

fig, ax = plt.subplots(figsize=(8, 6))

# curve f(x) = x^2 - 16
x_vals = np.linspace(-8, 8, 400)
ax.plot(x_vals, f(x_vals), 'b-', linewidth=2.5, label=r'$f(x) = x^2 - 16$')

# coordinate axes using line_gen
x_axis = line_gen(np.array([-8.0, 0.0]).reshape(-1, 1), np.array([8.0, 0.0]).reshape(-1, 1))
y_axis = line_gen(np.array([0.0, -20.0]).reshape(-1, 1), np.array([0.0, 60.0]).reshape(-1, 1))
ax.plot(x_axis[0, :], x_axis[1, :], color='black', linewidth=1)
ax.plot(y_axis[0, :], y_axis[1, :], color='black', linewidth=1)

# Newton steps: vertical line to the curve, then tangent down to the x-axis
for x0, c in [(6.0, 'r'), (-6.0, 'g')]:
    xs = newton(x0, 4)
    for a, b in zip(xs[:-1], xs[1:]):
        P = np.array([a, 0.0]).reshape(-1, 1)
        Q = np.array([a, f(a)]).reshape(-1, 1)
        R = np.array([b, 0.0]).reshape(-1, 1)
        x_PQ = line_gen(P, Q)
        x_QR = line_gen(Q, R)
        ax.plot(x_PQ[0, :], x_PQ[1, :], c + ':', linewidth=1)
        ax.plot(x_QR[0, :], x_QR[1, :], c + '-', linewidth=1)
    ax.plot(xs, np.zeros_like(xs), c + 'o', markersize=5, label=f'$x_0 = {x0:+.0f}$')

# roots and starting points
roots = np.block([np.array([-4.0, 0.0]).reshape(-1, 1),
                  np.array([4.0, 0.0]).reshape(-1, 1)])
ax.plot(roots[0, :], roots[1, :], 'ks', markersize=7, zorder=5, label='roots $x = \\pm 4$')
label_pts(roots, ['-4', '4'])

ax.set_xlim(-8.5, 8.5)
ax.set_ylim(-25, 60)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend()

plt.tight_layout()
plt.savefig(os.path.join(FIG, 'q10_newton.png'))
#plt.show()
