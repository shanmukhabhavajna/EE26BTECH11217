import numpy as np
from fractions import Fraction

# unit step function u(n)
def u(n):
  return 1 if n >= 0 else 0

x0, x2 = Fraction(-5, 7), Fraction(2)
d = (x2 - x0)/2                                  # x(2) = x(0) + 2d
x = lambda n: (x0 + n*d)*u(n)                    # x(n) = (x(0) + n d) u(n)

print("d =", d)
print("x(0), x(1), x(2) =", x(0), x(1), x(2))
print("a = x(1) =", x(1), "=", float(x(1)))
assert x(2) == 2 and x(1) == Fraction(9, 14)
assert x(1) - x(0) == x(2) - x(1) == d           # consecutive terms of an AP
assert x(-1) == 0                                 # the step function switches the sequence on at n = 0
