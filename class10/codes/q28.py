# CBSE (Class 10) -- Q28 (OR): A(2,0), B(6,1), C(p,q) form a triangle of area 12
# (positive only) and 2p + q = 10. Find p and q.
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

def line_gen(P, Q):
    return P + (Q - P)*np.linspace(0, 1, 20)

A = np.array([[2], [0]])
B = np.array([[6], [1]])

# area = (1/2) det[B-A  C-A] = (1/2)(4q - p + 2) = 12  ->  -p + 4q = 22
# 2p + q = 10
M = np.array([[-1, 4], [2, 1]])
b = np.array([[22], [10]])
C = LA.solve(M, b)

area = 0.5*LA.det(np.block([B - A, C - A]))
print("p, q =", C.ravel(), " area =", area)

for X, Y in [(A, B), (B, C), (C, A)]:
    s = line_gen(X, Y)
    plt.plot(s[0], s[1], 'b')
for name, X, d in [('A', A, (0.1, -0.4)), ('B', B, (0.1, -0.4)), ('C', C, (0.1, 0.2))]:
    plt.plot(X[0], X[1], 'ko')
    plt.annotate(name, (X[0, 0] + d[0], X[1, 0] + d[1]))
plt.axis('equal')
plt.grid()
plt.savefig('../figs/q28_triangle.png')
plt.show()
