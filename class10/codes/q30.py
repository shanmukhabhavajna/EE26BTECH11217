# q30.py  --  CBSE Class 10 Maths (Standard) 30/C/3
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

def param_norm(n, c):
    c = c / np.linalg.norm(n)
    n = n / np.linalg.norm(n)
    if c == 0:
        A = np.zeros((2, 1))
    elif np.array_equal(n, e1):
        A = np.array([[c, 0]]).reshape(-1, 1)
    elif np.array_equal(n, e2):
        A = np.array([[0, c]]).reshape(-1, 1)
    else:
        A = np.array([[c / n[0][0], 0]]).reshape(-1, 1)
    m = omat @ n
    return m, A

# ---------------- solution ----------------
# CBSE 30/C/3 Q30: solve x + 2y = 6, 2x - 5y = 12 graphically
#                  (OR) (ax - by) + (a + 4b) = 0, (bx + ay) + (b - 4a) = 0
n1 = np.array([[1.0], [2.0]]);  c1 = 6.0
n2 = np.array([[2.0], [-5.0]]); c2 = 12.0
X = gauss_solve(np.block([n1, n2]).T, np.array([c1, c2]))
print("(x, y) = (%.4f, %.4f)" % (X[0, 0], X[1, 0]))

# (OR)  a x - b y = -(a + 4b),  b x + a y = 4a - b   (a, b assumed)
def solve_or(a, b):
    M = np.array([[a, -b], [b, a]])
    return gauss_solve(M, np.array([-(a + 4 * b), 4 * a - b]))
for a, b in [(2, 3), (1, 1), (5, -2), (0.5, 4)]:
    s = solve_or(a, b)
    print("a=%4.1f b=%4.1f  (x, y) = (%.4f, %.4f)" % (a, b, s[0, 0], s[1, 0]))

fig, ax = plt.subplots(1, 2, figsize=(10, 4.2))
plt.sca(ax[0])
for n, c, lab in [(n1, c1, 'x+2y=6'), (n2, c2, '2x-5y=12')]:
    m, A = param_norm(n, c)
    L = line_dir_pt(m, A, -8, 8); plt.plot(L[0, :], L[1, :], label=lab)
plt.plot(X[0], X[1], 'ro'); plt.annotate('(6,0)', (6, 0), textcoords="offset points", xytext=(6, 6))
plt.xlim(-2, 10); plt.ylim(-5, 5); plt.legend(); plt.grid(True)
plt.sca(ax[1])
a, b = 2, 3
n1 = np.array([[a], [-b]]); n2 = np.array([[b], [a]])
for n, c, lab in [(n1, -(a + 4 * b), 'ax-by+(a+4b)=0'), (n2, 4 * a - b, 'bx+ay+(b-4a)=0')]:
    m, A = param_norm(n, c)
    L = line_dir_pt(m, A, -8, 8); plt.plot(L[0, :], L[1, :], label=lab)
s = solve_or(a, b)
plt.plot(s[0], s[1], 'ro'); plt.annotate('(-1,4)', (s[0, 0], s[1, 0]), textcoords="offset points", xytext=(6, 6))
plt.xlim(-8, 8); plt.ylim(-4, 10); plt.legend(); plt.grid(True)
savefig('q30.png')
