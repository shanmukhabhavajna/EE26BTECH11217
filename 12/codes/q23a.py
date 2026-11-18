from fractions import Fraction
from itertools import permutations

# 19 tickets, two draws without replacement, X = number of even tickets
tickets = range(1, 20)
pairs = list(permutations(tickets, 2))          # all ordered draws, equally likely
p_X = {k: Fraction(0) for k in range(3)}
for t1, t2 in pairs:
    k = (t1 % 2 == 0) + (t2 % 2 == 0)
    p_X[k] += Fraction(1, len(pairs))
print("p_X =", {k: str(v) for k, v in p_X.items()})
assert sum(p_X.values()) == 1
assert [p_X[k] for k in range(3)] == [Fraction(5, 19), Fraction(10, 19), Fraction(4, 19)]
