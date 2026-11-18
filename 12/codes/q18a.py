import numpy as np
import numpy.linalg as LA

# ratio of the projection of a on b to the projection of b on a
a = np.array([2, -1, 2])
b = np.array([5, -3, -4])
proj_a_on_b = (a @ b)/LA.norm(b)
proj_b_on_a = (b @ a)/LA.norm(a)
print("ratio =", proj_a_on_b/proj_b_on_a, " 3sqrt(2)/10 =", 3*np.sqrt(2)/10)
assert np.isclose(proj_a_on_b/proj_b_on_a, 3*np.sqrt(2)/10)
