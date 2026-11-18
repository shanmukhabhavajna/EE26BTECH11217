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

# Problem: log(dy/dx) = a x + b y, i.e. dy/dx = e^{a x + b y}, y(0) = 0
a, b, u0 = 2.0, -1.0, 1.0        # u0 = e^{-b y(0)} = 1

# Laplace: u = e^{-b y} satisfies u' = -b e^{a x}, so
# U(s) = u0/s - b/(s(s-a))  =>  u(x) = u0 + (b/a)(1 - e^{a x}),  y = -ln(u)/b
u_lap = lambda x: u0 + (b/a)*(1 - np.exp(a*x))
y_lap = lambda x: -np.log(u_lap(x))/b

# check the Laplace transform of u(x) at s = 3 against the formula for U(s)
s = 3.0
U_num = quad(lambda x: u0*np.exp(-s*x) + (b/a)*(np.exp(-s*x) - np.exp((a - s)*x)), 0, np.inf)[0]
U_formula = u0/s - b/(s*(s - a))
assert np.isclose(U_num, U_formula)

# Euler forward difference: y_{n+1} = y_n + h e^{a x_n + b y_n}
h, n = 0.001, 1000
x = h*np.arange(n+1)
y_eul = np.zeros(n+1)
for i in range(n):
  y_eul[i+1] = y_eul[i] + h*np.exp(a*x[i] + b*y_eul[i])

# compare at x = 0, 0.1, ..., 1.0 (every 100th Euler step)
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
m1.set_label('Laplace: $y=\\ln\\frac{e^{2x}+1}{2}$')
m2.set_label('Euler forward, $h=0.001$')

# baseline using line_gen
base = line_gen(np.array([-0.05, 0.0]).reshape(-1, 1), np.array([1.05, 0.0]).reshape(-1, 1))
ax.plot(base[0, :], base[1, :], 'k-', linewidth=1)

# label the end points
end_pts = np.block([[x[-1]], [y_ex[-1]]])
label_pts(end_pts, [f'{y_ex[-1]:.4f}'])
ax.annotate(f'{y_eul[-1]:.4f}', (x[-1] + d, y_eul[-1]), textcoords="offset points",
            xytext=(14, -4), ha='left')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xlim(-0.05, 1.15)
ax.set_ylim(-0.1, 1.7)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left')

plt.tight_layout()
plt.savefig(os.path.join(FIG, 'q17_stem.png'))
#plt.show()
