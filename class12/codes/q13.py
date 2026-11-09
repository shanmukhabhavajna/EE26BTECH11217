# q13.py  --  CBSE Class 12 Mathematics 65/C/3
# Uses only numpy; helper functions follow matgeo / CoordGeo and are written inline.
import numpy as np


# ---------------- solution ----------------
# CBSE 65/C/3 Q13: a queen is picked from 52 cards. Pr(it is the queen of spades)?
suits = ['spades', 'hearts', 'diamonds', 'clubs']
pmf_card = np.full(52, 1 / 52)                # one card, uniform pmf
is_queen = np.zeros(52, dtype=bool)
is_qs = np.zeros(52, dtype=bool)
for i in range(52):
    rank, suit = i % 13, i // 13              # rank 11 = queen
    is_queen[i] = (rank == 11)
    is_qs[i] = (rank == 11 and suit == 0)
p_q = pmf_card[is_queen].sum()
p_qs = pmf_card[is_qs & is_queen].sum()
print("Pr(Q) = %.6f, Pr(QS and Q) = %.6f" % (p_q, p_qs))
print("Pr(QS | Q) = Pr(QS and Q)/Pr(Q) = %.6f  (1/4 = %.2f)" % (p_qs / p_q, 0.25))
