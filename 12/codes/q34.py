import numpy as np

f = lambda x: x**2 + 1 + np.exp(x)

def trapezoid(n, a=1.0, b=3.0):
  h = (b - a)/n
  x = np.linspace(a, b, n+1)                # nodes x_i = a + i h
  w = np.ones(n+1); w[[0, -1]] = 0.5        # trapezoid weights
  return h, h*(w @ f(x))                    # I ~ h w^T f

I_exact = 32/3 + np.exp(3) - np.exp(1)      # [x^3/3 + x + e^x] from 1 to 3
print("   n        h          I          error")
for n in [4, 10, 100, 1000]:
  h, I = trapezoid(n)
  print(f"{n:4d}  {h:9.6f}  {I:.6f}  {I - I_exact:.6f}")
print("exact =", I_exact)

h, I = trapezoid(100)
assert abs(I - I_exact) < 1e-3
assert abs(trapezoid(1000)[1] - I_exact) < 1e-5
