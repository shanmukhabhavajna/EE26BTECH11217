# q23.py  --  CBSE Class 12 Mathematics 65/C/3
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

# ---------------- solution ----------------
# CBSE 65/C/3 Q23: 19 tickets numbered 1..19, two drawn without replacement.
#   pmf of the number of even tickets.   (OR) two tosses of a die, success = number > 5
tickets = np.arange(1, 20)
pmf = np.zeros(3)
n = 0
for i in tickets:                              # enumerate ordered pairs (i, j), j != i
    for j in tickets:
        if i != j:
            pmf[int(i % 2 == 0) + int(j % 2 == 0)] += 1
            n += 1
pmf = pmf / n
print("X = number of even tickets, pmf =", pmf, " = ", np.round(pmf * 19, 6), "/ 19")
print("check: 5/19, 10/19, 4/19 =", np.round([5 / 19, 10 / 19, 4 / 19], 6), " sum = %.6f" % pmf.sum())

# (OR)  success: 6 -> pmf of one toss [5/6, 1/6], two tosses by convolution
p1 = np.array([5 / 6, 1 / 6])
p2 = np.convolve(p1, p1)
print("(OR) pmf =", p2, " = ", np.round(p2 * 36, 6), "/ 36")

fig, ax = plt.subplots(1, 2, figsize=(9, 3.6))
ax[0].stem([0, 1, 2], pmf, basefmt=' '); ax[0].set_title('19 tickets, even numbers')
ax[1].stem([0, 1, 2], p2, basefmt=' '); ax[1].set_title('two tosses, number > 5')
for a_ in ax:
    a_.set_xticks([0, 1, 2]); a_.set_xlabel('$x$'); a_.set_ylabel('$p_X(x)$'); a_.grid(True)
savefig('q23.png')
