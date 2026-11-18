import numpy as np
from fractions import Fraction
from itertools import product

# pmf of Z = X + Y for two dice: all 36 outcomes are equally likely
n = np.arange(2, 13)
pmf = {int(k): Fraction(0) for k in n}
for x, y in product(range(1, 7), repeat=2):
  pmf[x + y] += Fraction(1, 36)

# formula for the pmf
for k in n:
  k = int(k)
  expected = Fraction(k - 1, 36) if k <= 7 else Fraction(13 - k, 36)
  assert pmf[k] == expected

# cdf  F_Z(k) = Pr(Z <= k)  as a running sum of the pmf
F, run = {}, Fraction(0)
for k in n:
  run += pmf[int(k)]
  F[int(k)] = run
print("pmf (x36):", [int(36*pmf[int(k)]) for k in n])
print("cdf      :", [str(F[int(k)]) for k in n])

# closed form for 7 < k <= 12 : F(k) = 1 - (12-k)(13-k)/72
for k in range(8, 13):
  assert F[k] == 1 - Fraction((12 - k)*(13 - k), 72)

# Pr(Z < 12) = F(11)
P = F[11]
print("Pr(Z < 12) = F(11) =", P)
assert P == Fraction(35, 36)
