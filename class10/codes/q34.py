# q34.py  --  CBSE Class 10 Maths (Standard) 30/C/3
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
# CBSE 30/C/3 Q34: (a) a4 = -15, a9 = -30, find S16
#                  (OR) S14 = 1050, a4 = 40, find a20
# AP as a sequence  x(n) = (a + (n-1) d) u(n-1)
def ap(a, d, n):
    return (a + (n - 1) * d) * u(n - 1)

n = np.arange(0, 25)
# (a)  a + 3d = -15,  a + 8d = -30
a, d = gauss_solve(np.array([[1, 3], [1, 8]]), np.array([-15, -30])).flatten()
x = ap(a, d, n)
win = u(n - 1) - u(n - 17)                   # window selecting n = 1..16
S16 = np.sum(x * win)
print("(a) a = %.1f, d = %.1f, S16 = %.1f   (16/2 (2a+15d) = %.1f)" % (a, d, S16, 8 * (2 * a + 15 * d)))

# (OR)  S14 = 7 (2a + 13 d) = 1050,  a + 3d = 40
a2, d2 = gauss_solve(np.array([[2, 13], [1, 3]]), np.array([150, 40])).flatten()
x2 = ap(a2, d2, n)
S14 = np.sum(x2 * (u(n - 1) - u(n - 15)))
print("(OR) a = %.1f, d = %.1f, S14 = %.1f, a20 = %.1f" % (a2, d2, S14, x2[20]))

fig, ax = plt.subplots(1, 2, figsize=(10, 3.8))
ax[0].stem(n[1:17], x[1:17], basefmt=' '); ax[0].set_title('(a) first 16 terms, S16 = %.0f' % S16)
ax[1].stem(n[1:21], x2[1:21], basefmt=' '); ax[1].set_title('(OR) a20 = %.0f' % x2[20])
for a_ in ax: a_.set_xlabel('$n$'); a_.grid(True)
savefig('q34.png')
