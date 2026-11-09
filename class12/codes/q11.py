# q11.py  --  CBSE Class 12 Mathematics 65/C/3
# Uses only numpy; helper functions follow matgeo / CoordGeo and are written inline.
import numpy as np

# ---- determinants by cofactor expansion (only for evaluating |A|, never to solve equations) ----
def det2(M):
    return M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]

def det3(M):
    s = 0.0
    for j in range(3):
        minor = np.delete(np.delete(M, 0, axis=0), j, axis=1)
        s += (-1) ** j * M[0, j] * det2(minor)
    return s

# ---------------- solution ----------------
# CBSE 65/C/3 Q11: A square matrix A is singular if |A| = 0.
#                  (OR) A = [[3,-5],[2,0]], B = [[1,17],[0,-10]], find |AB|
S = np.array([[1.0, 2.0], [2.0, 4.0]])
print("example of a singular matrix [[1,2],[2,4]]: |S| = %.1f" % det2(S))
A = np.array([[3.0, -5.0], [2.0, 0.0]])
B = np.array([[1.0, 17.0], [0.0, -10.0]])
AB = A @ B
print("AB =\n", AB)
print("|A| = %.1f, |B| = %.1f, |A||B| = %.1f" % (det2(A), det2(B), det2(A) * det2(B)))
print("|AB| = %.1f" % det2(AB))
