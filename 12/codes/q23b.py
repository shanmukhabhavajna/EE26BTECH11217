from fractions import Fraction
from itertools import product

# two tosses of a die, Y = number of tosses showing a number > 5
outcomes = list(product(range(1, 7), repeat=2))
p_Y = {k: Fraction(0) for k in range(3)}
for d1, d2 in outcomes:
    k = (d1 > 5) + (d2 > 5)
    p_Y[k] += Fraction(1, len(outcomes))
print("p_Y =", {k: str(v) for k, v in p_Y.items()})
assert sum(p_Y.values()) == 1
assert [p_Y[k] for k in range(3)] == [Fraction(25, 36), Fraction(10, 36), Fraction(1, 36)]
