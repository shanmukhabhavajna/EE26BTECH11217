# q9.py  --  CBSE Class 10 Maths (Standard) 30/C/3
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

# ---------------- solution ----------------
# CBSE 30/C/3 Q9: two dice, Pr(sum < 12) using pmf
pmf_die = np.ones(6) / 6                     # pmf of one die, faces 1..6
pmf_sum = np.convolve(pmf_die, pmf_die)      # pmf of S = X + Y, S = 2..12
S = np.arange(2, 13)
p = pmf_sum[S < 12].sum()
print("pmf of S:", np.round(pmf_sum * 36).astype(int), "/ 36")
print("Pr(S<12) = %.6f, 35/36 = %.6f -> option (B)" % (p, 35 / 36))

plt.stem(S, pmf_sum, basefmt=' ')
plt.stem([12], [pmf_sum[-1]], linefmt='r-', markerfmt='ro', basefmt=' ')
plt.xlabel('$s$'); plt.ylabel('$p_S(s)$'); plt.grid(True)
savefig('q9.png')
