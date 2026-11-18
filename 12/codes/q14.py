import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

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

# Problem:  x dy/dx - y = ln x,  y(1) = 0
# Laplace solution: y(t) = t - ln t - 1
y_lap = lambda x: x - np.log(x) - 1

# check: Laplace transform of y_lap at s = 2 against (gamma + ln s - 1)/s + 1/s^2
g, s = np.euler_gamma, 2.0
Y_num = quad(lambda t: np.exp(-s*t)*y_lap(t), 0, np.inf)[0]
Y_formula = (g + np.log(s) - 1)/s + 1/s**2
assert np.isclose(Y_num, Y_formula)

# Euler forward difference: y_{n+1} = y_n + h f(x_n, y_n), f = (y + ln x)/x
h, n = 0.001, 1000
x = 1 + h*np.arange(n+1)
y_eul = np.zeros(n+1)
for i in range(n):
  y_eul[i+1] = y_eul[i] + h*(y_eul[i] + np.log(x[i]))/x[i]

# compare at x = 1.0, 1.1, ..., 2.0 (every 100th Euler step)
k = np.arange(0, n+1, 100)
x, y_eul = x[k], y_eul[k]
y_ex = y_lap(x)
print("  x      Euler      Laplace    error")
for i in range(len(x)):
  print(f"{x[i]:.1f}  {y_eul[i]:.6f}  {y_ex[i]:.6f}  {y_ex[i]-y_eul[i]:.6f}")

# stem plot: Laplace (exact) and Euler, offset slightly so both are visible
fig, ax = plt.subplots(figsize=(8, 6))
d = 0.012
m1, s1, b1 = ax.stem(x - d, y_ex, linefmt='b-', markerfmt='bo', basefmt=' ')
m2, s2, b2 = ax.stem(x + d, y_eul, linefmt='r-', markerfmt='rs', basefmt=' ')
m1.set_label('Laplace: $y=x-\\ln x-1$')
m2.set_label('Euler forward, $h=0.001$')

# baseline using line_gen
base = line_gen(np.array([0.95, 0.0]).reshape(-1, 1), np.array([2.05, 0.0]).reshape(-1, 1))
ax.plot(base[0, :], base[1, :], 'k-', linewidth=1)

# label the end points
end_pts = np.block([[x[-1]], [y_ex[-1]]])
label_pts(end_pts, [f'{y_ex[-1]:.4f}'])
ax.annotate(f'{y_eul[-1]:.4f}', (x[-1] + d, y_eul[-1]), textcoords="offset points",
            xytext=(14, -4), ha='left')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xlim(0.95, 2.15)
ax.set_ylim(-0.02, 0.34)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend()

plt.tight_layout()
plt.savefig(os.path.join(FIG, 'q14_stem.png'))
#plt.show()
