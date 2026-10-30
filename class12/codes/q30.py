
import os
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

def line_gen(A, B):                          # points on the segment AB, as in matgeo
    return A + (B - A)*np.linspace(0, 1, 20)

def line_dir_pt(m, A, k1, k2):               # points A + k m, k in [k1, k2], as in matgeo
    return A + m*np.linspace(k1, k2, 20)

def norm_vec(M):                             # n with M n = 0, the last right singular vector
    return LA.svd(M)[2][-1].reshape(-1, 1)

# ---------------- (a) shortest distance ----------------
A1 = np.array([1, -1, 0]).reshape(-1, 1)     # point on line 1
m1 = np.array([2, 3, 1]).reshape(-1, 1)      # direction of line 1
A2 = np.array([-1, 2, 2]).reshape(-1, 1)     # point on line 2
m2 = np.array([5, 1, 0]).reshape(-1, 1)      # direction of line 2

M = np.block([m1, m2]).T                     # common perpendicular: n^T m1 = n^T m2 = 0
n = norm_vec(M)
n = np.round(-n/n[0, 0], 6)                  # scale so that n = (-1, 5, -13)^T
print("n =", n.ravel())                      # [-1, 5, -13]
print("check with cross product:", np.cross(m1.ravel(), m2.ravel()))

d = abs(n.T @ (A2 - A1))[0, 0]/LA.norm(n)
print("d =", d, " 9/sqrt(195) =", 9/np.sqrt(195))   # 0.6445
print("lines intersect" if np.isclose(d, 0) else "lines do not intersect (skew)")

# feet of the common perpendicular:  lam m1 - mu m2 + t n = A2 - A1
sol = LA.solve(np.block([m1, -m2, n]), A2 - A1)
lam, mu, t = sol.ravel()
P = A1 + lam*m1
Q = A2 + mu*m2
print("P =", P.ravel(), " Q =", Q.ravel(), " |PQ| =", LA.norm(P - Q))

# ---------------- (b) OR : the plane ----------------
n1 = np.array([1, 3, 0]).reshape(-1, 1); c1 = -6      # x + 3y + 6 = 0
n2 = np.array([3, -1, -4]).reshape(-1, 1); c2 = 0     # 3x - y - 4z = 0
# (n1 + lam n2)^T x = c1 + lam c2 ; distance from origin = 1 means |c|/||n|| = 1
# since c2 = 0, c = c1 and  ||n1 + lam n2||^2 = c1^2  gives a quadratic in lam
coef = [(n2.T @ n2)[0, 0], 2*(n1.T @ n2)[0, 0], (n1.T @ n1)[0, 0] - c1**2]
lams = np.roots(coef)
print("lambda =", lams)                      # [ 1, -1 ]
for l in lams:
    nn = n1 + l*n2
    print("plane:", nn.ravel(), "x =", c1 + l*c2, " distance from origin =", abs(c1 + l*c2)/LA.norm(nn))
