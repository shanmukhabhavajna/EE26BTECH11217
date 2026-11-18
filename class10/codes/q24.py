# q24.py  --  CBSE Class 10 Maths (Standard) 30/C/3
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

# ---------------- solution ----------------
# CBSE 30/C/3 Q24: (a) jar of 18 marbles, Pr(red) = 2/3. Number of yellow?
#                  (OR) die thrown twice: Pr(at least one 5), Pr(no 5)
# (a) unknowns [r, y]:  r + y = 18,   3 r - 2 (r + y) = 0  ->  r - 2 y = 0
r, y = gauss_solve(np.array([[1, 1], [1, -2]]), np.array([18, 0])).flatten()
pmf_marble = np.array([r, y]) / 18           # pmf over {red, yellow}
print("red = %.1f, yellow = %.1f, pmf = %s" % (r, y, pmf_marble))

# (OR) one throw: pmf of 'no. of fives' is [5/6, 1/6]; two throws -> convolution
pmf1 = np.array([5 / 6, 1 / 6])
pmfX = np.convolve(pmf1, pmf1)               # X = number of fives, X = 0,1,2
print("pmf of X:", pmfX * 36, "/ 36")
print("(i)  Pr(X >= 1) = %.6f, 11/36 = %.6f" % (pmfX[1:].sum(), 11 / 36))
print("(ii) Pr(X = 0)  = %.6f, 25/36 = %.6f" % (pmfX[0], 25 / 36))

fig, ax = plt.subplots(1, 2, figsize=(9, 3.6))
ax[0].bar(['red', 'yellow'], pmf_marble, color=['r', 'y'])
ax[0].set_ylabel('pmf'); ax[0].set_title('marble drawn')
ax[1].stem([0, 1, 2], pmfX, basefmt=' '); ax[1].set_xticks([0, 1, 2])
ax[1].set_xlabel('number of 5s'); ax[1].set_title('two throws of a die')
for a_ in ax: a_.grid(True)
savefig('q24.png')
