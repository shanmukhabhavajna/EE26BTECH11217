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

#Labeling points
def label_pts(G_v, vert_labels):
  for i, txt in enumerate(vert_labels):
    plt.annotate(txt,                       # this is the text
                 (G_v[0, i], G_v[1, i]),    # this is the point to label
                 textcoords="offset points",
                 xytext=(0, 10),            # distance from text to points (x,y)
                 ha='center')

A = np.array([0, 0]).reshape(-1, 1)
C = np.array([3, 6]).reshape(-1, 1)

def rank_for(m):
  B = np.array([2*m, -4]).reshape(-1, 1)
  M = np.block([B - A, C - A])        # columns B-A, C-A
  return LA.matrix_rank(M)

for m in [-1, 0, 1, 2, -2.5]:
  print("m =", m, " rank =", rank_for(m))

assert rank_for(-1) == 1                                       # collinear
assert all(rank_for(m) == 2 for m in [0, 1, 2, -2.5])          # not collinear

# plot for m = -1: B = (-2, -4)
B = np.array([2*(-1), -4]).reshape(-1, 1)
x_BC = line_gen(B, C)
plt.figure(figsize=(7, 5))
plt.plot(x_BC[0, :], x_BC[1, :], label='line through $A$, $B$, $C$')

pts = np.block([[A, B, C]])
plt.scatter(pts[0, :], pts[1, :], color='k', zorder=3)
vert_labels = ['A', 'B', 'C']
for i, txt in enumerate(vert_labels):
  plt.annotate(f'{txt}\n({pts[0, i]:.0f}, {pts[1, i]:.0f})', (pts[0, i], pts[1, i]),
               textcoords="offset points", xytext=[(22, -22), (-28, 0), (-28, 0)][i], ha='center')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper left')
plt.grid(True)
plt.axis('equal')
plt.savefig(os.path.join(FIG, 'q14_collinear.png'), bbox_inches='tight')
#plt.show()
