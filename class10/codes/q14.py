# q14.py  --  CBSE Class 10 Maths (Standard) 30/C/3
# Uses only numpy and matplotlib; helper functions are copied inline from matgeo / CoordGeo.
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figs')
def savefig(name):
    os.makedirs(FIG, exist_ok=True)
    plt.savefig(os.path.join(FIG, name), dpi=200, bbox_inches='tight')
    plt.close()

# ---- params.py (CoordGeo) ----
omat = np.array([[0, 1], [-1, 0]])   # rotation by -90 degrees (normal vector)
I2 = np.eye(2)
e1 = I2[:, [0]]
e2 = I2[:, [1]]

# ---- Gauss elimination (used instead of determinants) ----
def gauss_solve(A, b):
    M = np.hstack([np.array(A, dtype=float), np.array(b, dtype=float).reshape(-1, 1)])
    n = M.shape[0]
    for i in range(n):                       # forward elimination, partial pivoting
        p = i + np.argmax(np.abs(M[i:, i]))
        M[[i, p]] = M[[p, i]]
        M[i] = M[i] / M[i, i]
        for j in range(i + 1, n):
            M[j] = M[j] - M[j, i] * M[i]
    x = np.zeros((n, 1))
    for i in range(n - 1, -1, -1):           # back substitution
        x[i] = M[i, n] - M[i, i + 1:n] @ x[i + 1:n]
    return x

# ---- line/funcs.py (CoordGeo) ----
def dot(u_, v_):
    return (u_.T @ v_).item()

def dir_vec(A, B):
    return B - A

def norm_vec(A, B):
    return omat @ dir_vec(A, B)

def line_gen(A, B):
    n = 10
    dim = A.shape[0]
    x_AB = np.zeros((dim, n))
    lam_1 = np.linspace(0, 1, n)
    for i in range(n):
        x_AB[:, i] = (A + lam_1[i] * (B - A)).flatten()
    return x_AB

def line_dir_pt(m, A, k1, k2):
    n = 10
    dim = A.shape[0]
    x_AB = np.zeros((dim, n))
    lam_1 = np.linspace(k1, k2, n)
    for i in range(n):
        x_AB[:, i] = (A + lam_1[i] * m).flatten()
    return x_AB

def line_intersect(n1, A1, n2, A2):
    N = np.block([n1, n2]).T
    p = np.array([[dot(n1, A1)], [dot(n2, A2)]])
    return gauss_solve(N, p)

def rotmat(theta):
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([[c, -s], [s, c]])

# ---- plotting/funcs.py (CoordGeo) ----
def label_pts(G_v, vert_labels, off=(0, 8)):
    for i, txt in enumerate(vert_labels):
        plt.annotate(txt, (G_v[0, i], G_v[1, i]), textcoords="offset points",
                     xytext=off, ha='center')

# ---------------- solution ----------------
# CBSE 30/C/3 Q14: (0,0), (2m,-4), (3,6) collinear. Find m.
# B - A = k (C - A), unknowns [m, k]:
#   2m - 3k = 0
#        6k = -4
A = np.array([[0.0], [0.0]])
C = np.array([[3.0], [6.0]])
M = np.array([[2, -3], [0, 6]])
m, k = gauss_solve(M, np.array([0, -4])).flatten()
B = np.array([[2 * m], [-4.0]])
print("m = %.6f, k = %.6f" % (m, k))
print("residual |(B-A) - k(C-A)| = %.2e" % np.linalg.norm(dir_vec(A, B) - k * dir_vec(A, C)))
print("n^T(B-A) with n = normal of AC: %.2e" % dot(norm_vec(A, C), dir_vec(A, B)))

L = line_gen(B + (B - C) * 0.2, C + (C - B) * 0.2)
plt.plot(L[0, :], L[1, :], 'b')
pts = np.block([A, B, C])
plt.plot(pts[0, :], pts[1, :], 'ro')
label_pts(pts, ['A(0,0)', 'B(-2,-4)', 'C(3,6)'], off=(14, -4))
plt.axis('equal'); plt.grid(True)
savefig('q14.png')
