import numpy as np
# discriminant of 3 sqrt3 x^2 + 10 x + sqrt3 = 0, computed directly
v = np.array([3*np.sqrt(3), 10.0, np.sqrt(3)])       # (a, b, c)
Disc = v[1]**2 - 4*v[0]*v[2]
print("D = b^2 - 4ac =", Disc)
assert np.isclose(Disc, 64)

