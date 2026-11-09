# q36.py  --  CBSE Class 10 Maths (Standard) 30/C/3
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
# CBSE 30/C/3 Q36: from top of a 60 sqrt(3) m cliff, angles of depression of the
# top and bottom of a tower are 45 and 60 deg. Find the height of the tower.
H = 60 * np.sqrt(3)
C = np.array([[0.0], [H]])                    # top of cliff
O = np.zeros((2, 1))
def sight(theta):                             # direction of line of sight (depression theta)
    return np.array([[np.cos(theta)], [-np.sin(theta)]])
m60, m45 = sight(np.deg2rad(60)), sight(np.deg2rad(45))
# bottom of tower B: line of sight at 60 deg meets the ground y = 0
Bt = line_intersect(omat @ m60, C, e2, O)
# top of tower T: line of sight at 45 deg meets the tower, x = x_B
Tt = line_intersect(omat @ m45, C, e1, Bt)
h = Tt[1, 0]
print("distance of tower from cliff = %.4f m" % Bt[0, 0])
print("height of tower = %.4f m (exact 60(sqrt3-1))" % h)
print("with sqrt(3) = 1.73: %.2f m" % (60 * 1.73 - 60))

L = line_gen(C, Bt); plt.plot(L[0, :], L[1, :], 'b')
L = line_gen(C, Tt); plt.plot(L[0, :], L[1, :], 'g')
L = line_gen(O, C); plt.plot(L[0, :], L[1, :], 'k', lw=3)
L = line_gen(O, Bt); plt.plot(L[0, :], L[1, :], 'k')
L = line_gen(Bt, Tt); plt.plot(L[0, :], L[1, :], 'r', lw=3)
V = np.block([O, C, Bt, Tt]); plt.plot(V[0, :], V[1, :], 'ko', ms=3)
label_pts(V, ['F', 'C', 'B', 'T'])
plt.axis('equal'); plt.grid(True)
savefig('q36.png')
