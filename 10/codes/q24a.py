import numpy as np
from fractions import Fraction

# 18 marbles, Pr(red) = 2/3
n = 18
p = np.array([Fraction(2, 3), 1 - Fraction(2, 3)])      # (Pr(red), Pr(yellow))
counts = [n*x for x in p]
print("red, yellow =", [str(c) for c in counts])
assert counts == [12, 6]
