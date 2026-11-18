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

#Labeling points
def label_pts(G_v, vert_labels):
  for i, txt in enumerate(vert_labels):
    plt.annotate(txt,                       # this is the text
                 (G_v[0, i], G_v[1, i]),    # this is the point to label
                 textcoords="offset points",
                 xytext=(0, 10),            # distance from text to points (x,y)
                 ha='center')

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

# vertices as column vectors
A = np.array([2, -1, 1]).reshape(-1, 1)
B = np.array([1, -3, -5]).reshape(-1, 1)
C = np.array([3, -4, -4]).reshape(-1, 1)

# side vectors as columns of D, Gram matrix G = D^T D
D = np.block([B - A, C - B, A - C])
G = D.T @ D
print("D =\n", D)
print("G =\n", G)
assert G[1, 2] == 0                       # (C-B)^T (A-C) = 0 : right angle at C
assert G[0, 0] == G[1, 1] + G[2, 2]       # Pythagoras

# 2D plot in the plane of the triangle: C at origin, CB along x-axis, CA along y-axis
# (side lengths from the diagonal of G, right angle at C)
C2 = np.array([0.0, 0.0]).reshape(-1, 1)
B2 = np.array([np.sqrt(G[1, 1]), 0.0]).reshape(-1, 1)
A2 = np.array([0.0, np.sqrt(G[2, 2])]).reshape(-1, 1)
assert np.isclose(LA.norm(A2 - B2)**2, G[0, 0])

x_AB = line_gen(A2, B2)
x_BC = line_gen(B2, C2)
x_CA = line_gen(C2, A2)
plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')
plt.plot(x_BC[0, :], x_BC[1, :], label='$BC$')
plt.plot(x_CA[0, :], x_CA[1, :], label='$CA$')

tri_coords = np.block([[A2, B2, C2]])
plt.scatter(tri_coords[0, :], tri_coords[1, :])
vert_labels = ['A', 'B', 'C']
offsets = [(48, -12), (0, 10), (-42, -8)]
for i, txt in enumerate(vert_labels):
  plt.annotate(f'{txt}\n({tri_coords[0, i]:.2f}, {tri_coords[1, i]:.2f})',
               (tri_coords[0, i], tri_coords[1, i]),
               textcoords="offset points", xytext=offsets[i], ha='center')
# mark the right angle at C
plt.plot([0.4, 0.4, 0], [0, 0.4, 0.4], 'k-', linewidth=1)

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.ylim(-0.5, 6.8)
plt.savefig(os.path.join(FIG, 'q22_tri.png'), bbox_inches='tight')
#plt.show()
