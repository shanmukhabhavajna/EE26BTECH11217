# q4.py  --  CBSE Class 12 Mathematics 65/C/3
# Uses only numpy; helper functions follow matgeo / CoordGeo and are written inline.
import numpy as np


# ---------------- solution ----------------
# CBSE 65/C/3 Q4: Pr(A solves) = 1/3, Pr(B solves) = 1/5, independent. Pr(question is solved)?
pA = np.array([2 / 3, 1 / 3])                 # pmf of A: [fails, solves]
pB = np.array([4 / 5, 1 / 5])                 # pmf of B: [fails, solves]
joint = np.outer(pA, pB)                      # independence -> joint pmf is the product
print("joint pmf [[00, 01], [10, 11]] =\n", joint)
p_solved = 1 - joint[0, 0]                    # Pr(E') = 1 - Pr(E)
print("Pr(solved) = %.6f, 7/15 = %.6f" % (p_solved, 7 / 15))
for lab, v in zip("ABCD", [7 / 15, 8 / 15, 2 / 15, 14 / 15]):
    print("(%s) %.6f %s" % (lab, v, "<-- answer" if np.isclose(p_solved, v) else ""))
