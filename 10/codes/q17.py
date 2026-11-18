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

#Generate points on a circle
def circ_gen(O, r):
  len = 50
  theta = np.linspace(0, 2*np.pi, len)
  x_circ = np.zeros((2, len))
  x_circ[0, :] = r*np.cos(theta)
  x_circ[1, :] = r*np.sin(theta)
  x_circ = (x_circ + O)
  return x_circ

O = np.array([4, 4]).reshape(-1, 1)
P = np.array([4, 0]).reshape(-1, 1)

# other end of the diameter: Q = 2O - P
Q = 2*O - P
print("Q =", Q.flatten())
r = LA.norm(P - O)
print("||P-O|| =", r, " ||Q-O|| =", LA.norm(Q - O), " ||Q-P|| =", LA.norm(Q - P))
assert np.allclose(Q, [[4], [8]])
assert np.isclose(LA.norm(Q - O), r) and np.isclose(LA.norm(Q - P), 2*r)

# plot
fig, ax = plt.subplots(figsize=(6, 6))
x_circ = circ_gen(O, r)
ax.plot(x_circ[0, :], x_circ[1, :], label='circle')
x_PQ = line_gen(P, Q)
ax.plot(x_PQ[0, :], x_PQ[1, :], label='diameter $PQ$')

pts = np.block([[O, P, Q]])
ax.scatter(pts[0, :], pts[1, :], color='k', zorder=3)
offs = [(30, 0), (0, -26), (0, 10)]
for i, txt in enumerate(['O', 'P', 'Q']):
  ax.annotate(f'{txt}\n({pts[0, i]:.0f}, {pts[1, i]:.0f})', (pts[0, i], pts[1, i]),
              textcoords="offset points", xytext=offs[i], ha='center')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_aspect('equal')
ax.set_xlim(-1.5, 9.5)
ax.set_ylim(-1.5, 9.5)
ax.legend(loc='upper left')
ax.grid(True)
plt.savefig(os.path.join(FIG, 'q17_diameter.png'), bbox_inches='tight')
#plt.show()
