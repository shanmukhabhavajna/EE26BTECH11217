from fractions import Fraction
from itertools import product

# a die is thrown twice, X = number of 5s
outcomes = list(product(range(1, 7), repeat=2))
pX = [Fraction(sum(1 for o in outcomes if (o[0] == 5) + (o[1] == 5) == k), 36) for k in range(3)]
print("pX =", [str(x) for x in pX])
assert pX == [Fraction(25, 36), Fraction(10, 36), Fraction(1, 36)]

at_least_once = 1 - pX[0]
none = pX[0]
print("Pr(5 at least once) =", at_least_once, " Pr(no 5) =", none)
assert at_least_once == Fraction(11, 36) and none == Fraction(25, 36)
