import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

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

from fractions import Fraction

# figures are saved in ../figs, whichever folder the script is run from
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figs')
os.makedirs(FIG, exist_ok=True)

# cross product of plane vectors: u x v = u1 v2 - u2 v1
def cross2(u, v):
  return u[0]*v[1] - u[1]*v[0]

def tri_area(A, B, C):
  return Fraction(abs(cross2(B - A, C - A)), 2)

# quadrilateral ABCD split by the diagonal AC
A = np.array([-4, -3]); B = np.array([3, -1]); C = np.array([0, 5]); D = np.array([-4, 2])
a1, a2 = tri_area(A, B, C), tri_area(A, C, D)
print("ar(ABC) =", a1, " ar(ACD) =", a2, " ar(ABCD) =", a1 + a2)
assert (a1, a2, a1 + a2) == (24, 10, 34)

# plot of the quadrilateral and the diagonal AC
V = np.block([[A.reshape(2, 1), B.reshape(2, 1), C.reshape(2, 1), D.reshape(2, 1)]]).astype(float)
plt.figure(figsize=(6, 5))
for i, j in [(0, 1), (1, 2), (2, 3), (3, 0)]:
  s = line_gen(V[:, i:i+1], V[:, j:j+1])
  plt.plot(s[0, :], s[1, :], 'b')
s = line_gen(V[:, 0:1], V[:, 2:3])
plt.plot(s[0, :], s[1, :], 'r--', linewidth=0.9)
plt.scatter(V[0, :], V[1, :], color='k', zorder=3)
for i, (n, off) in enumerate(zip(['A', 'B', 'C', 'D'], [(42, -14), (22, -12), (25, 5), (-25, 5)])):
  plt.annotate(f"{n}({V[0, i]:.0f}, {V[1, i]:.0f})", (V[0, i], V[1, i]),
               textcoords="offset points", xytext=off, ha='center')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axis('equal')
plt.grid(True)
plt.savefig(os.path.join(FIG, 'q28a_quad.png'), bbox_inches='tight')
#plt.show()
