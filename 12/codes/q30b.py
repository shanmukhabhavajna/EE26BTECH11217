import numpy as np
import numpy.linalg as LA

# Gauss elimination (forward elimination only, on the augmented matrix)
def gauss_forward(Ab):
  Ab = Ab.astype(float).copy()
  rows = Ab.shape[0]
  for j in range(rows):
    for i in range(j + 1, rows):
      Ab[i, :] -= (Ab[i, j]/Ab[j, j])*Ab[j, :]
  return Ab

# planes n1^T x = -6, n2^T x = 0
Ab = np.array([[1, 3, 0, -6], [3, -1, -4, 0]])
print("echelon form:\n", gauss_forward(Ab))     # [[1 3 0 -6], [0 -10 -4 18]]
A0 = np.array([-3/5, -9/5, 0]).reshape(-1, 1)      # z = 0
m = np.array([6, -2, 5]).reshape(-1, 1)            # direction (z = 5t)
assert np.allclose(Ab[:, :3] @ A0, Ab[:, 3:])
assert np.allclose(Ab[:, :3] @ m, 0)

# u^T m = 0, u^T A = 1, ||u|| = 1 :  r = 4q + 2, p = -5/3 - 3q
M = np.array([[6, -2, 5, 0], [3, 9, 0, -5]])
print("echelon form:\n", gauss_forward(M))        
for q in np.roots([9, 9, 2]):
  u = np.array([-5/3 - 3*q, q, 4*q + 2]).reshape(-1, 1)
  print("q =", q, " u =", u.flatten(), " ||u|| =", LA.norm(u).item())
  assert np.isclose(LA.norm(u), 1)
  assert np.isclose((u.T @ m).item(), 0) and np.isclose((u.T @ A0).item(), 1)
  print("plane:", 3*u.flatten(), "x = 3")
