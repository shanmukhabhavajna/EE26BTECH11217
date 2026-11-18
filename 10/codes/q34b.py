import numpy as np

# unit step function u(n)
def u(n):
  return 1 if n >= 0 else 0

# AP: x(n) = (x(0) + n d) u(n);  S_14 = 1050 and x(3) = 40 (4th term)
N = 14
A = np.array([[N, N*(N - 1)/2], [1, 3]])
b = np.array([1050.0, 40.0])
x0, d = np.linalg.solve(A, b)
print("det =", np.linalg.det(A), " x(0), d =", x0, d)
x = lambda n: (x0 + n*d)*u(n)
print("20th term x(19) =", x(19))
S = sum(x(n)*(u(n) - u(n - N)) for n in range(-5, 40))
assert np.isclose(x0, 10) and np.isclose(d, 10)
assert np.isclose(S, 1050) and np.isclose(x(3), 40) and np.isclose(x(19), 200)
