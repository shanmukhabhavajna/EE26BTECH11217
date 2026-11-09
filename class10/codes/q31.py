# q31.py  --  CBSE Class 10 Maths (Standard) 30/C/3
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

# ---- Newton-Raphson ----
def newton(f, df, x0, tol=1e-12, maxit=100):
    x = x0
    for _ in range(maxit):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
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

# ---- conics/funcs.py (CoordGeo) ----
def circ_gen(O, r):
    n = 100
    theta = np.linspace(0, 2 * np.pi, n)
    x_circ = np.zeros((2, n))
    x_circ[0, :] = r * np.cos(theta)
    x_circ[1, :] = r * np.sin(theta)
    return x_circ + O

# ---------------- solution ----------------
# CBSE 30/C/3 Q31: circle of radius 2.5 cm, point P at 7 cm from the centre,
# construct the pair of tangents from P
r, d = 2.5, 7.0
O = np.zeros((2, 1)); P = d * e1
M = (O + P) / 2                              # step 1: midpoint of OP
# step 2: circle with diameter OP meets the given circle at the tangent points T1, T2
# T = O + r R(+-phi) u,  cos(phi) = r/d  (Newton-Raphson)
phi = newton(lambda t: np.cos(t) - r / d, lambda t: -np.sin(t), 1.0)
uvec = (P - O) / np.linalg.norm(P - O)
T1 = O + r * rotmat(phi) @ uvec
T2 = O + r * rotmat(-phi) @ uvec
print("phi = %.4f deg" % np.degrees(phi))
print("T1 =", T1.flatten(), " T2 =", T2.flatten())
print("|PT1| = %.4f, |PT2| = %.4f, sqrt(d^2-r^2) = %.4f" % (np.linalg.norm(P - T1), np.linalg.norm(P - T2), np.sqrt(d**2 - r**2)))
print("OT1.T1P = %.2e (OT1 perp PT1)" % dot(T1 - O, P - T1))
print("|T1-M| = %.4f = |OP|/2 = %.4f (T1 lies on circle with diameter OP)" % (np.linalg.norm(T1 - M), d / 2))

plt.plot(*circ_gen(O, r), 'k')
plt.plot(*circ_gen(M, d / 2), 'g--')
for T in (T1, T2):
    L = line_gen(P, T); plt.plot(L[0, :], L[1, :], 'b')
    L = line_gen(O, T); plt.plot(L[0, :], L[1, :], 'r:')
L = line_gen(O, P); plt.plot(L[0, :], L[1, :], 'k:')
V = np.block([O, P, T1, T2, M]); plt.plot(V[0, :], V[1, :], 'ko', ms=3)
label_pts(V, ['O', 'P', 'T1', 'T2', 'M'])
plt.axis('equal'); plt.grid(True)
savefig('q31.png')
