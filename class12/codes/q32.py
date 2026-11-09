# q32.py  --  CBSE Class 12 Mathematics 65/C/3
# Uses only numpy; helper functions follow matgeo / CoordGeo and are written inline.
import numpy as np

# ---- vector helpers (column vectors, as in matgeo / CoordGeo) ----
def dot(u_, v_):
    return (u_.T @ v_).item()

def norm(u_):
    return np.sqrt(dot(u_, u_))

def col(*a):
    return np.array(a, dtype=float).reshape(-1, 1)

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

# ---- determinants by cofactor expansion (only for evaluating |A|, never to solve equations) ----
def det2(M):
    return M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]

def det3(M):
    s = 0.0
    for j in range(3):
        minor = np.delete(np.delete(M, 0, axis=0), j, axis=1)
        s += (-1) ** j * M[0, j] * det2(minor)
    return s

# ---------------- solution ----------------
# CBSE 65/C/3 Q32: |1+a^2-b^2, 2ab, -2b ; 2ab, 1-a^2+b^2, 2a ; 2b, -2a, 1-a^2-b^2| = (1 + a^2 + b^2)^3
def D(a, b):
    return det3(np.array([[1 + a**2 - b**2, 2 * a * b, -2 * b],
                          [2 * a * b, 1 - a**2 + b**2, 2 * a],
                          [2 * b, -2 * a, 1 - a**2 - b**2]]))
np.random.seed(3)
for _ in range(5):
    a, b = np.random.uniform(-2, 2, 2)
    print("a=%7.4f b=%7.4f  |.| = %12.6f   (1+a^2+b^2)^3 = %12.6f" % (a, b, D(a, b), (1 + a**2 + b**2)**3))

# (OR) line through A(1,3), B(0,0);  k such that area of triangle ABD, D(k, 0), is 3
A, B = col(1, 3), col(0, 0)
n = np.array([[0, 1], [-1, 0]]) @ (A - B)       # normal vector of AB
c = dot(n, B)
print("line AB: %g x + %g y = %g  (3x - y = 0)" % (n[0, 0], n[1, 0], c))
# area = 1/2 |n^T (D - B)| = 3  ->  n^T D = +-6, with D = (k, 0): Gauss elimination (1 x 1)
for sgn in (+6.0, -6.0):
    k = gauss_solve(np.array([[n[0, 0]]]), np.array([sgn]))[0, 0]
    area = 0.5 * abs(dot(n, col(k, 0) - B))
    print("k = %.6f, area = %.6f" % (k, area))
