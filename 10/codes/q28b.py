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


# cross product of plane vectors: u x v = u1 v2 - u2 v1
def cross2(u, v):
  return u[0]*v[1] - u[1]*v[0]

# A(2,0), B(6,1), C(p,q): area 12 and 2p + q = 10
A = np.array([2, 0]); B = np.array([6, 1])
M = np.array([[2, 1], [-1, 4]], dtype=float)
print("det M =", np.linalg.det(M))
sol = []
for c in [22, -26]:
  p, q = np.linalg.solve(M, np.array([10.0, c]))
  C = np.array([p, q])
  area = abs(cross2(B - A, C - A))/2
  print("c =", c, " (p, q) =", (round(float(p), 4), round(float(q), 4)), " area =", area, " 2p+q =", 2*p + q)
  assert np.isclose(area, 12) and np.isclose(2*p + q, 10)
  sol.append(C)

# plot of the line 2p + q = 10 and the two triangles ABC
A2 = A.reshape(2, 1).astype(float); B2 = B.reshape(2, 1).astype(float)
plt.figure(figsize=(6, 5))
L = line_gen(np.array([[0.0], [10.0]]), np.array([[8.0], [-6.0]]))
plt.plot(L[0, :], L[1, :], 'g', label=r'$\mathbf{n}^{\top}\mathbf{x} = 10$')
for C, col in zip(sol, ['b', 'r']):
  Cc = C.reshape(2, 1)
  for P1, P2 in [(A2, B2), (B2, Cc), (Cc, A2)]:
    s = line_gen(P1, P2)
    plt.plot(s[0, :], s[1, :], col)
pts = np.block([[A2, B2, sol[0].reshape(2, 1), sol[1].reshape(2, 1)]])
plt.scatter(pts[0, :], pts[1, :], color='k', zorder=3)
labels = ['A(2, 0)', 'B(6, 1)', 'C$_1$(2, 6)', 'C$_2$(7.33, -4.67)']
for i, (t, off) in enumerate(zip(labels, [(-30, -5), (28, 5), (-35, 5), (45, 0)])):
  plt.annotate(t, (pts[0, i], pts[1, i]), textcoords="offset points", xytext=off, ha='center')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.axis('equal')
plt.grid(True)
plt.savefig(os.path.join(FIG, 'q28b_tri.png'), bbox_inches='tight')
#plt.show()
