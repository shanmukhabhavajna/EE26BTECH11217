# q30.py  --  CBSE Class 12 Mathematics 65/C/3
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

# ---- Newton-Raphson ----
def newton(f, df, x0, tol=1e-12, maxit=100):
    x = x0
    for _ in range(maxit):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# ---------------- solution ----------------
# CBSE 65/C/3 Q30: shortest distance between (x-1)/2 = (y+1)/3 = z and (x+1)/5 = (y-2)/1, z = 2
p1, d1 = col(1, -1, 0), col(2, 3, 1)
p2, d2 = col(-1, 2, 2), col(5, 1, 0)
w = p1 - p2
# minimise |w + s d1 - t d2|^2 : normal equations (solved by Gauss elimination, no cross product)
M = np.array([[dot(d1, d1), -dot(d1, d2)], [dot(d1, d2), -dot(d2, d2)]])
rhs = np.array([-dot(d1, w), -dot(d2, w)])
s, t = gauss_solve(M, rhs).flatten()
q1, q2 = p1 + s * d1, p2 + t * d2
dist = norm(q1 - q2)
print("s = %.6f, t = %.6f" % (s, t))
print("closest points:", q1.flatten(), q2.flatten())
print("shortest distance = %.6f, 9/sqrt(195) = %.6f" % (dist, 9 / np.sqrt(195)))
print("(q1-q2).d1 = %.2e, (q1-q2).d2 = %.2e" % (dot(q1 - q2, d1), dot(q1 - q2, d2)))
print("distance != 0  -> the lines do not intersect")

# (OR) plane through the line of intersection of  x + 3y + 6 = 0  and  3x - y - 4z = 0
# at unit distance from the origin:  n(l) = n1 + l n2,  c = -6,  |c|/|n(l)| = 1
n1, n2 = col(1, 3, 0), col(3, -1, -4)
g = lambda l: dot(n1 + l * n2, n1 + l * n2) - 36
dg = lambda l: 2 * dot(n1 + l * n2, n2)
for l0 in (2.0, -2.0):
    l = newton(g, dg, l0)
    n = n1 + l * n2
    print("lambda = %.6f, plane: %g x + %g y + %g z + 6 = 0, distance from origin = %.6f"
          % (l, n[0, 0], n[1, 0], n[2, 0], 6 / norm(n)))
