import numpy as np

# unit step function u(n)
def u(n):
  return 1 if n >= 0 else 0

# AP: x(n) = (x(0) + n d) u(n);  x(3) = -15, x(8) = -30  (4th and 9th terms)
A = np.array([[1, 3], [1, 8]], dtype=float)
b = np.array([-15.0, -30.0])
x0, d = np.linalg.solve(A, b)
print("x(0), d =", x0, d)
x = lambda n: (x0 + n*d)*u(n)

# S_N = sum_n x(n) [u(n) - u(n - N)] = N x(0) + N(N-1)/2 d
N = 16
S = sum(x(n)*(u(n) - u(n - N)) for n in range(-5, 40))
S_formula = np.array([N, N*(N - 1)/2]) @ np.array([x0, d])
print("S_16 =", S, S_formula)
assert np.isclose(x0, -6) and np.isclose(d, -3)
assert np.isclose(S, -456) and np.isclose(S_formula, -456)
