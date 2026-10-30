# CBSE (Class 10) -- Q39: f(x) = 3x^4 - 9x^3 + x^2 + 15x + k is divisible by 3x^2 - 5.
# Find k and two zeroes using the quotient.
# OR: find all zeroes of x^4 - 8x^3 + 23x^2 - 28x + 12 if two of them are 2 and 3.
# Zeroes are found with the Newton-Raphson method
import numpy as np

def newton(p, x):
    dp = np.polyder(p)
    for i in range(100):
        step = np.polyval(p, x)/np.polyval(dp, x)     # x = x - f(x)/f'(x)
        x = x - step
        if abs(step) < 1e-10:
            break
    return float(round(x, 4))

# divide with k = 0, the remainder is k + 10, so k = -remainder
q, r = np.polydiv([3, -9, 1, 15, 0], [3, 0, -5])
k = -r[-1]
zeros1 = [newton(q, x0) for x0 in (0, 3)]

# OR: starting points near 1, 2 and 3
p2 = [1, -8, 23, -28, 12]
zeros2 = [newton(p2, x0) for x0 in (0, 1.5, 4)]

print("k =", k, " quotient =", q, " zeros =", zeros1, " OR zeros =", zeros2)
