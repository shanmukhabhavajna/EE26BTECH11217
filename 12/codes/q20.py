import numpy as np
import numpy.linalg as LA

# x-axis: A = 0, direction m = e1;  point P = (a, b, c)
I = np.eye(3)
m = I[:, 0].reshape(-1, 1)
A = np.zeros((3, 1))
P = np.array([2, 3, 4]).reshape(-1, 1)

# foot of the perpendicular and distance
Q = A + (m @ m.T)/(m.T @ m) @ (P - A)
d = LA.norm(P - Q)
print("Q =", Q.T.flatten(), " d =", d, " sqrt(b^2+c^2) =", np.sqrt(P[1, 0]**2 + P[2, 0]**2))
assert np.isclose(d, 5.0)
