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

# Part (a): x + 2y = 6, 2x - 5y = 12 by Gauss elimination on the augmented matrix
Mr = np.array([[1, 2, 6],
               [2, -5, 12]], dtype=float)
Mr[1] = Mr[1] - 2*Mr[0]          # R2 -> R2 - 2 R1
Mr[1] = Mr[1]/(-9)               # R2 -> R2/(-9)
Mr[0] = Mr[0] - 2*Mr[1]          # R1 -> R1 - 2 R2
print(Mr)
assert np.allclose(Mr, [[1, 0, 6], [0, 1, 0]])
x = Mr[:, 2].reshape(2, 1) + 0.0
print("x, y =", x.flatten())

# plot of the two lines
A1, B1 = np.array([[-2.0], [4.0]]), np.array([[8.0], [-1.0]])      # on x + 2y = 6
A2, B2 = np.array([[-2.0], [-3.2]]), np.array([[8.0], [0.8]])      # on 2x - 5y = 12
x_1 = line_gen(A1, B1)
x_2 = line_gen(A2, B2)
plt.figure(figsize=(7, 5))
plt.plot(x_1[0, :], x_1[1, :], label=r'$L_1$: $\mathbf{n}_1^{\top}\mathbf{x} = 6$')
plt.plot(x_2[0, :], x_2[1, :], label=r'$L_2$: $\mathbf{n}_2^{\top}\mathbf{x} = 12$')

# intercepts and the solution
pts = np.block([[np.array([[0.0], [3.0]]), np.array([[0.0], [-2.4]]), x]])
plt.scatter(pts[0, :], pts[1, :], color='k', zorder=3)
for i, txt in enumerate(['(0, 3)', '(0, -2.4)', '(6, 0)']):
  plt.annotate(txt, (pts[0, i], pts[1, i]), textcoords="offset points",
               xytext=[(30, 5), (32, -5), (0, 12)][i], ha='center')

plt.axhline(0, color='k', linewidth=0.8)
plt.axvline(0, color='k', linewidth=0.8)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid(True)
plt.savefig(os.path.join(FIG, 'q30_lines.png'), bbox_inches='tight')
#plt.show()
