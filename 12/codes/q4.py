import numpy as np
from fractions import Fraction

# pmf of the number of successes of one trial: (Pr(0), Pr(1))
pA = np.array([1 - Fraction(1, 3), Fraction(1, 3)])        # A solves with probability 1/3
pB = np.array([1 - Fraction(1, 5), Fraction(1, 5)])        # B solves with probability 1/5

# X = number of persons who solve, independent trials: pmf of the sum is the convolution
pX = [Fraction(0)]*3
for i in range(2):
  for j in range(2):
    pX[i + j] += pA[i]*pB[j]
print("p_X =", [str(x) for x in pX])
assert sum(pX) == 1
assert pX == [Fraction(8, 15), Fraction(6, 15), Fraction(1, 15)]

# the question is solved if X >= 1
Pr = pX[1] + pX[2]
print("Pr(X >= 1) =", Pr)
assert Pr == Fraction(7, 15) == 1 - pX[0]
