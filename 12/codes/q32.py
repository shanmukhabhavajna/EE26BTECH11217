import numpy as np
import numpy.linalg as LA

A = np.array([1, 3]).reshape(-1, 1)
B = np.array([0, 0]).reshape(-1, 1)

# line AB: det [x y 1; 1 3 1; 0 0 1] = 3x - y ; check at several points of the line y = 3x
def line_det(x, y):
  return LA.det(np.array([[x, y, 1], [A[0, 0], A[1, 0], 1], [B[0, 0], B[1, 0], 1]]))

for x in [-2.0, 0.0, 1.5, 4.0]:
  assert np.isclose(line_det(x, 3*x), 0)              # points on y = 3x
  assert np.isclose(line_det(x, 5.0), 3*x - 5.0)      # det equals 3x - y
n = np.array([3, -1])
assert np.isclose(n @ A, 0).all() and np.isclose(n @ B, 0).all()   # n^T x = 0 holds at A and B
print("line AB: n^T x = 0, n =", n)

# area of triangle ABD with D = (k, 0): det [1 3 1; 0 0 1; k 0 1] = 3k
def area(k):
  M = np.array([[A[0, 0], A[1, 0], 1], [0, 0, 1], [k, 0, 1]])
  return 0.5*abs(LA.det(M))

for k in [2, -2]:
  print("k =", k, " area =", area(k))
  assert np.isclose(area(k), 3)
