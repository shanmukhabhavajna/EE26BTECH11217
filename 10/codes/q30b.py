import numpy as np

# Part (b): (ax - by) + (a + 4b) = 0, (bx + ay) + (b - 4a) = 0
# augmented matrix [M | r] and Gauss elimination by row operations
def gauss_ab(a, b):
  Mr = np.array([[a, -b, -(a + 4*b)],
                 [b,  a, -(b - 4*a)]], dtype=float)
  R1, R2 = Mr[0].copy(), Mr[1].copy()
  Mr[0] = a*R1 + b*R2          # R1 -> aR1 + bR2   (removes y)
  Mr[1] = a*R2 - b*R1          # R2 -> aR2 - bR1   (removes x)
  return Mr

for a, b in [(1, 1), (2, 3), (-1, 5), (0.5, 2)]:
  Mr = gauss_ab(a, b)
  d = a**2 + b**2
  x, y = Mr[0, 2]/Mr[0, 0], Mr[1, 2]/Mr[1, 1]
  print(f"a = {a}, b = {b}: reduced rows = {Mr[0]}, {Mr[1]}, (x, y) = ({x}, {y})")
  assert np.allclose(Mr, [[d, 0, -d], [0, d, 4*d]])
  assert np.isclose(x, -1) and np.isclose(y, 4)
