# q28.py  --  CBSE Class 10 Maths (Standard) 30/C/3
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
# CBSE 30/C/3 Q28: area of quadrilateral A(-4,-3), B(3,-1), C(0,5), D(-4,2)
A = np.array([[-4.0], [-3.0]]); B = np.array([[3.0], [-1.0]])
C = np.array([[0.0], [5.0]]);   D = np.array([[-4.0], [2.0]])
# diagonal AC splits ABCD into triangles ABC and ACD (B and D on opposite sides)
n = norm_vec(A, C)
print("n^T(B-A) = %.1f, n^T(D-A) = %.1f (opposite signs)" % (dot(n, B - A), dot(n, D - A)))
print("ar(ABC) = %.2f, ar(ACD) = %.2f" % (tri_area(A, B, C), tri_area(A, C, D)))
print("ar(ABCD) = %.2f sq. units" % (tri_area(A, B, C) + tri_area(A, C, D)))

# (OR) A(2,0), B(6,1), C(p,q), area = 12, 2p + q = 10
A2 = np.array([[2.0], [0.0]]); B2 = np.array([[6.0], [1.0]])
nn = norm_vec(A2, B2)                         # normal vector of AB; area = |n^T (C-A)|/2
sols = []
for s in (+24, -24):                          # n^T (C - A) = +-24
    N = np.block([[nn.T], [np.array([[2.0, 1.0]])]])
    rhs = np.array([dot(nn, A2) + s, 10.0])
    sols.append(gauss_solve(N, rhs))
for Cs in sols:
    print("C = (%.4f, %.4f), area = %.4f" % (Cs[0, 0], Cs[1, 0], tri_area(A2, B2, Cs)))

fig, ax = plt.subplots(1, 2, figsize=(10, 4.2))
plt.sca(ax[0])
V = np.block([A, B, C, D, A])
plt.plot(V[0, :], V[1, :], 'b'); L = line_gen(A, C); plt.plot(L[0, :], L[1, :], 'r--')
label_pts(V[:, :4], ['A', 'B', 'C', 'D']); plt.grid(True); plt.axis('equal')
plt.sca(ax[1])
for Cs, col in zip(sols, ['b', 'g']):
    V = np.block([A2, B2, Cs, A2]); plt.plot(V[0, :], V[1, :], col)
    plt.annotate('C(%.2f, %.2f)' % (Cs[0, 0], Cs[1, 0]), (Cs[0, 0], Cs[1, 0]), textcoords="offset points", xytext=(5, 6))
label_pts(np.block([A2, B2]), ['A', 'B'])
x = np.linspace(0, 8, 10); plt.plot(x, 10 - 2 * x, 'k:', label='2p+q=10')
plt.legend(); plt.grid(True); plt.axis('equal')
savefig('q28.png')
