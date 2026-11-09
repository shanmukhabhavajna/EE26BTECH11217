# q19.py  --  CBSE Class 10 Maths (Standard) 30/C/3
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

# ---- triangle/funcs.py (CoordGeo) ----
def tri_sides(A, B, C):
    a = np.linalg.norm(B - C)
    b = np.linalg.norm(C - A)
    c = np.linalg.norm(A - B)
    return c, a, b

def tri_vert(a, b, c):
    p = (a**2 + c**2 - b**2) / (2 * a)
    q = np.sqrt(c**2 - p**2)
    A = np.array([[p], [q]])
    B = np.array([[0.0], [0.0]])
    C = np.array([[a], [0.0]])
    return A, B, C

def tri_mid_pt(A, B, C):
    D = (B + C) / 2
    E = (C + A) / 2
    F = (A + B) / 2
    return D, E, F

def tri_area(A, B, C):
    # area = 1/2 |n^T (C-A)|, n = normal vector of AB (no cross product)
    return 0.5 * abs(dot(norm_vec(A, B), C - A))

# ---------------- solution ----------------
# CBSE 30/C/3 Q19: triangle ABC ~ triangle PQR, BC/QR = 1/3. Find ar(PRQ)/ar(ACB)
A = np.array([[1.0], [1.0]])
B = np.array([[5.0], [2.0]])
C = np.array([[3.0], [6.0]])
k = 3.0                                      # QR/BC
R = k * rotmat(np.deg2rad(25))               # similarity: scale and rotate
sh = np.array([[6.0], [-2.0]])
P, Q, Rr = R @ A + sh, R @ B + sh, R @ C + sh

c1, a1, b1 = tri_sides(A, B, C)
c2, a2, b2 = tri_sides(P, Q, Rr)
print("BC/QR = %.4f, CA/RP = %.4f, AB/PQ = %.4f" % (a1 / a2, b1 / b2, c1 / c2))
ar1, ar2 = tri_area(A, B, C), tri_area(P, Q, Rr)
print("ar(ABC) = %.4f, ar(PQR) = %.4f" % (ar1, ar2))
print("ar(PRQ)/ar(ACB) = %.4f  (= (QR/BC)^2 = %.1f)" % (ar2 / ar1, k**2))

for X, Y in [(A, B), (B, C), (C, A), (P, Q), (Q, Rr), (Rr, P)]:
    L = line_gen(X, Y); plt.plot(L[0, :], L[1, :], 'b')
V1 = np.block([A, B, C]); V2 = np.block([P, Q, Rr])
label_pts(V1, ['A', 'B', 'C']); label_pts(V2, ['P', 'Q', 'R'])
plt.axis('equal'); plt.grid(True)
savefig('q19.png')
