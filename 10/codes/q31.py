import os
import numpy as np
import numpy.linalg as LA
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

#Generate circle points
def circ_gen(O, r):
  len = 50
  theta = np.linspace(0, 2*np.pi, len)
  x_circ = np.zeros((2, len))
  x_circ[0, :] = r*np.cos(theta)
  x_circ[1, :] = r*np.sin(theta)
  x_circ = (x_circ.T + O).T
  return x_circ

# circle of radius 2.5 cm with centre O, point P at distance 7 cm
r = 2.5
O = np.array([0.0, 0.0])
P = np.array([7.0, 0.0])
w = P - O
g = w @ w - r**2                                   # g = |P - O|^2 - r^2 = 42.75

# pair of tangents: (x - P)^T M (x - P) = 0, M = w w^T - g I
M = np.outer(w, w) - g*np.eye(2)
lam, U = LA.eigh(M)                                # eigenvalues in ascending order
print("M =\n", M, "\neigenvalues =", lam)
assert np.allclose(sorted(lam), [-g, r**2])

# direction vectors m = U (sqrt(-lam_neg), +-sqrt(lam_pos))^T
neg, pos = np.argmin(lam), np.argmax(lam)
T = []
for s in [1, -1]:
  coef = np.zeros(2)
  coef[neg] = np.sqrt(lam[pos])                    # component along eigenvector of -g
  coef[pos] = s*np.sqrt(-lam[neg])                 # component along eigenvector of r^2
  m = U @ coef
  m = m/LA.norm(m)
  mu = -(m @ w)/(m @ m)                            # foot of perpendicular from O
  T.append(P + mu*m)
  print("m =", m, " T =", T[-1])
T1, T2 = T
for Ti in T:
  assert np.isclose(LA.norm(Ti - O), r)                   # on the circle
  assert np.isclose((Ti - O) @ (Ti - P), 0)               # OT perpendicular to PT
  assert np.isclose(LA.norm(P - Ti), np.sqrt(g))          # tangent length
print("PT =", np.sqrt(g))

# plot
x_circ = circ_gen(O, r)
plt.figure(figsize=(7, 4))
plt.plot(x_circ[0, :], x_circ[1, :], 'b')
for Ti in T:
  x_PT = line_gen(P, Ti)
  plt.plot(x_PT[0, :], x_PT[1, :], 'r')
x_OP = line_gen(O, P)
plt.plot(x_OP[0, :], x_OP[1, :], 'k--', linewidth=0.8)

pts = np.block([[O.reshape(2, 1), P.reshape(2, 1), T1.reshape(2, 1), T2.reshape(2, 1)]])
plt.scatter(pts[0, :], pts[1, :], color='k', zorder=3)
names = ['O', 'P', 'T$_1$', 'T$_2$']
offs = [(-10, -14), (10, 8), (-50, -16), (-50, 8)]
for i in range(4):
  plt.annotate(f"{names[i]}({pts[0, i]:.2f}, {pts[1, i]:.2f})", (pts[0, i], pts[1, i]),
               textcoords="offset points", xytext=offs[i], ha='center')

plt.xlabel('$x$ (cm)')
plt.ylabel('$y$ (cm)')
plt.axis('equal')
plt.grid(True)
plt.savefig(os.path.join(FIG, 'q31_tangents.png'), bbox_inches='tight')
#plt.show()
