# CBSE (Class 10) -- Q22: PQ || BC, PQ = 3 cm, BC = 9 cm, AC = 7.5 cm.
# Find AQ.
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

def line_gen(P, Q):
    return P + (Q - P)*np.linspace(0, 1, 20)

PQ, BC, AC = 3, 9, 7.5

# AB is not needed for the answer, A = (4.5, 6) is chosen so that AC = 7.5
B = np.array([[0], [0]])
C = np.array([[BC], [0]])
A = np.array([[BC/2], [np.sqrt(AC**2 - (BC/2)**2)]])

# triangles APQ and ABC are similar, so AQ/AC = AP/AB = PQ/BC = k
k = PQ/BC
P = A + k*(B - A)
Q = A + k*(C - A)

print("AQ =", LA.norm(Q - A), " PQ =", LA.norm(Q - P))

for X, Y in [(A, B), (B, C), (C, A), (P, Q)]:
    s = line_gen(X, Y)
    plt.plot(s[0], s[1], 'b')
for name, X, d in [('A', A, (0, 0.2)), ('B', B, (-0.4, -0.5)), ('C', C, (0.1, -0.5)),
                   ('P', P, (-0.4, 0)), ('Q', Q, (0.1, 0))]:
    plt.plot(X[0], X[1], 'ko')
    plt.annotate(name, (X[0, 0] + d[0], X[1, 0] + d[1]))
plt.axis('equal')
plt.grid()
plt.savefig('../figs/q22_triangle.png')
plt.show()
