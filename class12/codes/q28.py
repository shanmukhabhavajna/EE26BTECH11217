# q28.py  --  CBSE Class 12 Mathematics 65/C/3
# Uses only numpy and matplotlib; helper functions follow matgeo / CoordGeo and are written inline.
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

# ---------------- solution ----------------
# CBSE 65/C/3 Q28: P(0) = k, P(1) = 2k, P(2) = 3k.   Find k, P(X<2), P(X<=2), P(X>=2)
# sum of the pmf = 1:   [1 2 3] . [k k k]  ->  6 k = 1   (Gauss elimination on the 1x1 system)
k = gauss_solve(np.array([[1 + 2 + 3]]), np.array([1.0]))[0, 0]
w = np.array([1, 2, 3])
pmf = k * w
print("k = %.6f (1/6 = %.6f)" % (k, 1 / 6))
print("pmf =", pmf)
print("P(X<2)  = %.6f" % pmf[:2].sum())
print("P(X<=2) = %.6f" % pmf[:3].sum())
print("P(X>=2) = %.6f" % pmf[2:].sum())

plt.stem([0, 1, 2], pmf, basefmt=' ')
for i, v in enumerate(pmf):
    plt.annotate('%.3f' % v, (i, v), ha='center', textcoords="offset points", xytext=(0, 6))
plt.xticks([0, 1, 2]); plt.xlabel('$x$'); plt.ylabel('$P(x)$'); plt.grid(True)
savefig('q28.png')
