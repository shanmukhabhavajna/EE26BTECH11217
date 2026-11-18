# q2.py  --  CBSE Class 10 Maths (Standard) 30/C/3
# Uses only numpy; helper functions are copied inline from matgeo / CoordGeo.
import numpy as np


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

# ---- unit step sequence ----
def u(n):
    return np.where(np.asarray(n) >= 0, 1.0, 0.0)

# ---------------- solution ----------------
# CBSE 30/C/3 Q2: -5/7, a, 2 are consecutive terms of an AP. Find a.
# AP as a sequence:  x(n) = (x0 + n d) u(n),  unknowns [x0, d]
#   x(0) = -5/7      ->  x0        = -5/7
#   x(2) =  2        ->  x0 + 2 d  =  2
A = np.array([[1, 0], [1, 2]])
b = np.array([-5/7, 2])
x0, d = gauss_solve(A, b).flatten()

n = np.arange(-3, 6)
x = (x0 + n * d) * u(n)
a = x0 + d                                  # x(1)
print("x0 = %.6f, d = %.6f" % (x0, d))
print("a  = %.6f  (9/14 = %.6f)" % (a, 9/14))
for lab, val in zip("ABCD", [9/7, 9/14, 19/7, 19/14]):
    print("(%s) %.6f %s" % (lab, val, "<-- answer" if np.isclose(a, val) else ""))
