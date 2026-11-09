# q31.py  --  CBSE Class 12 Mathematics 65/C/3
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

# ---------------- solution ----------------
# CBSE 65/C/3 Q31: unit vector perpendicular to (a + b) and (a - b), a = i + j + k, b = i + 2j + 3k
a = col(1, 1, 1)
b = col(1, 2, 3)
u, v = a + b, a - b
# n.u = 0, n.v = 0 : set n3 = 1 and solve the 2 x 2 system for n1, n2 by Gauss elimination
A = np.array([[u[0, 0], u[1, 0]], [v[0, 0], v[1, 0]]])
rhs = -np.array([u[2, 0], v[2, 0]])
n12 = gauss_solve(A, rhs).flatten()
n = col(n12[0], n12[1], 1.0)
nu = n / norm(n)
print("a+b =", u.flatten(), " a-b =", v.flatten())
print("n =", n.flatten(), " n.u = %.2e, n.v = %.2e" % (dot(n, u), dot(n, v)))
print("unit vector = +-", nu.flatten(), " = +-(1, -2, 1)/sqrt(6) =", (col(1, -2, 1) / np.sqrt(6)).flatten())
