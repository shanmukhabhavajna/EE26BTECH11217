import numpy as np
from fractions import Fraction

# pmf vector p = k*(1, 2, 3)^T ; 1^T p = 6k = 1
w = np.array([1, 2, 3])
k = Fraction(1, int(w.sum()))
p = [k*int(v) for v in w]
print("k =", k, " p =", [str(v) for v in p])
assert sum(p) == 1

# cumulative probabilities F = L p, L lower-triangular matrix of ones
L = np.tril(np.ones((3, 3), dtype=int))
F = [sum(int(L[i, j])*p[j] for j in range(3)) for i in range(3)]
print("F =", [str(v) for v in F])

P_lt2 = F[1]                 # P(X < 2) = P(X <= 1)
P_le2 = F[2]                 # P(X <= 2)
P_ge2 = 1 - P_lt2            # P(X >= 2)
print("P(X<2) =", P_lt2, " P(X<=2) =", P_le2, " P(X>=2) =", P_ge2)
assert (P_lt2, P_le2, P_ge2) == (Fraction(1, 2), 1, Fraction(1, 2))
assert P_ge2 == p[2]
