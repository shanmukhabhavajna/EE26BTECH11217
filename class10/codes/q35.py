# q35.py  --  CBSE Class 10 Maths (Standard) 30/C/3
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
# CBSE 30/C/3 Q35: (a) AB/PQ = AC/PR = AD/PM  =>  triangle ABC ~ triangle PQR
#                  (OR) right angle at A, 4 (BN^2 + CM^2) = 5 BC^2
# (a) numerical illustration (assumed triangle ABC, PQR built with ratio k)
A = np.array([[1.0], [1.0]]); B = np.array([[6.0], [2.0]]); C = np.array([[3.0], [7.0]])
k = 0.5
R = k * rotmat(np.deg2rad(30)); sh = np.array([[8.0], [1.0]])
P, Q, Rr = R @ A + sh, R @ B + sh, R @ C + sh
D, _, _ = tri_mid_pt(A, B, C)                 # D midpoint of BC
Mm, _, _ = tri_mid_pt(P, Q, Rr)               # M midpoint of QR
nr = np.linalg.norm
print("AB/PQ = %.4f, AC/PR = %.4f, AD/PM = %.4f" % (nr(B - A) / nr(Q - P), nr(C - A) / nr(Rr - P), nr(D - A) / nr(Mm - P)))
# construction used in the proof: E = 2D - A (ABEC is a parallelogram), S = 2M - P
E = 2 * D - A; S = 2 * Mm - P
print("BE = %.4f = AC = %.4f;  QS = %.4f = PR = %.4f" % (nr(E - B), nr(C - A), nr(S - Q), nr(Rr - P)))
print("AB/PQ = BE/QS = AE/PS = %.4f %.4f %.4f" % (nr(B - A) / nr(Q - P), nr(E - B) / nr(S - Q), nr(E - A) / nr(S - P)))
def angle(U, V):
    return np.degrees(np.arccos(dot(U, V) / (nr(U) * nr(V))))
print("angles ABC: A=%.3f B=%.3f C=%.3f" % (angle(B - A, C - A), angle(A - B, C - B), angle(A - C, B - C)))
print("angles PQR: P=%.3f Q=%.3f R=%.3f" % (angle(Q - P, Rr - P), angle(P - Q, Rr - Q), angle(P - Rr, Q - Rr)))

# (OR) right angle at A = origin, B = (b,0), C = (0,c); M, N midpoints of AB, AC
def check(b, c):
    A_ = np.zeros((2, 1)); B_ = b * e1; C_ = c * e2
    N_ = (A_ + C_) / 2; M_ = (A_ + B_) / 2
    lhs = 4 * (nr(B_ - N_)**2 + nr(C_ - M_)**2)
    rhs = 5 * nr(B_ - C_)**2
    return lhs, rhs
for b, c in [(8, 4), (3, 4), (5, 12), (2.5, 6.1)]:
    print("AB=%4.1f AC=%4.1f   4(BN^2+CM^2) = %8.4f   5BC^2 = %8.4f" % ((b, c) + check(b, c)))

fig, ax = plt.subplots(1, 2, figsize=(10, 4.2))
plt.sca(ax[0])
for X, Y in [(A, B), (B, C), (C, A), (P, Q), (Q, Rr), (Rr, P), (A, D), (P, Mm)]:
    L = line_gen(X, Y); plt.plot(L[0, :], L[1, :], 'b')
label_pts(np.block([A, B, C, D]), ['A', 'B', 'C', 'D']); label_pts(np.block([P, Q, Rr, Mm]), ['P', 'Q', 'R', 'M'])
plt.axis('equal'); plt.grid(True)
plt.sca(ax[1])
b, c = 8, 4
A_ = np.zeros((2, 1)); B_ = b * e1; C_ = c * e2; N_ = (A_ + C_) / 2; M_ = (A_ + B_) / 2
for X, Y in [(A_, B_), (B_, C_), (C_, A_), (B_, N_), (C_, M_)]:
    L = line_gen(X, Y); plt.plot(L[0, :], L[1, :], 'b')
label_pts(np.block([A_, B_, C_, M_, N_]), ['A', 'B', 'C', 'M', 'N'])
plt.axis('equal'); plt.grid(True)
savefig('q35.png')
