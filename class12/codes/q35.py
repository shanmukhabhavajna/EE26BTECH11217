# Q35 (OR): integral of x / ((x-1)^2 (x+2)) dx
import sympy as sp

x = sp.Symbol('x')
f = x / ((x - 1)**2 * (x + 2))

# split into partial fractions
parts = sp.apart(f)


# integrate
F = sp.integrate(f, x)
print("integral:", F)


