# q18.py  --  CBSE Class 10 Maths (Standard) 30/C/3
# Uses only numpy; helper functions are copied inline from matgeo / CoordGeo.
import numpy as np


# ---------------- solution ----------------
# CBSE 30/C/3 Q18: p = a b^3, q = a^2 b (a, b primes). Find LCM(p, q)
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

ep = np.array([1, 3])                        # exponents (of a, b) in p
eq = np.array([2, 1])                        # exponents (of a, b) in q
elcm = np.maximum(ep, eq)                    # LCM -> max of exponents
ehcf = np.minimum(ep, eq)                    # HCF -> min of exponents
print("exponent vector of LCM:", elcm, " -> a^%d b^%d" % tuple(elcm))
for a, b in [(2, 3), (3, 5), (5, 7), (11, 13)]:
    p, q = a * b**3, a**2 * b
    lcm = p * q // gcd(p, q)
    print("a=%2d b=%2d  p=%6d q=%6d  LCM=%8d  a^2 b^3=%8d  %s" % (a, b, p, q, lcm, a**2 * b**3, lcm == a**2 * b**3))
