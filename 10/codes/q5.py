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

#Angle between two vectors (degrees)
def ang_deg(m1, m2):
  return np.degrees(np.arccos(((m1.T @ m2)/(LA.norm(m1)*LA.norm(m2))).item()))

# Construction: circle of radius 1 centred at O, P on the x-axis with angle APB = 80 deg.
# sin(40 deg) = r/OP  =>  OP = 1/sin(40 deg);  angle AOP = 50 deg
r = 1.0
O = np.array([0.0, 0.0]).reshape(-1, 1)
P = np.array([1/np.sin(np.radians(40)), 0.0]).reshape(-1, 1)
A = np.array([np.cos(np.radians(50)), np.sin(np.radians(50))]).reshape(-1, 1)
B = np.array([np.cos(np.radians(50)), -np.sin(np.radians(50))]).reshape(-1, 1)

# tangent is perpendicular to the radius:  (A-O)^T (P-A) = 0,  (B-O)^T (P-B) = 0
print("(A-O)^T(P-A) =", ((A - O).T @ (P - A)).item())
print("(B-O)^T(P-B) =", ((B - O).T @ (P - B)).item())
assert np.isclose(((A - O).T @ (P - A)).item(), 0)
assert np.isclose(((B - O).T @ (P - B)).item(), 0)

# angles
print("angle APB =", ang_deg(A - P, B - P))
print("angle AOB =", ang_deg(A - O, B - O))
assert np.isclose(ang_deg(A - P, B - P), 80)
assert np.isclose(ang_deg(A - O, B - O), 100)

# plot
fig, ax = plt.subplots(figsize=(8, 6))
x_circ = circ_gen(O, r)
ax.plot(x_circ[0, :], x_circ[1, :], label='circle')
for (X, Y, lab) in [(O, A, '$OA$'), (O, B, '$OB$'), (A, P, '$PA$'), (B, P, '$PB$')]:
  x_XY = line_gen(X, Y)
  ax.plot(x_XY[0, :], x_XY[1, :], label=lab)

pts = np.block([[O, A, B, P]])
ax.scatter(pts[0, :], pts[1, :], color='k', zorder=3)
labels = ['O', 'A', 'B', 'P']
offs = [(-25, -12), (0, 10), (0, -22), (22, 4)]
for i, txt in enumerate(labels):
  ax.annotate(f'{txt}\n({pts[0, i]:.2f}, {pts[1, i]:.2f})', (pts[0, i], pts[1, i]),
              textcoords="offset points", xytext=offs[i], ha='center')
ax.annotate('$80^\\circ$', (P[0, 0], 0), textcoords="offset points", xytext=(-38, 3), ha='center')
ax.annotate('$100^\\circ$', (0, 0), textcoords="offset points", xytext=(22, 3), ha='center')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.legend(loc='upper right')
ax.grid(True)
ax.set_aspect('equal')
ax.set_xlim(-1.6, 2.4)
plt.savefig(os.path.join(FIG, 'q5_tangents.png'), bbox_inches='tight')
#plt.show()
