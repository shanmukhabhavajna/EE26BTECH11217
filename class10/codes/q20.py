# CBSE (Class 10) -- Q20: a point on the ground is 80 m from the foot of a tower.
# The angle of elevation of the top is 30 degrees. Find the height of the tower.
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

def line_gen(P, Q):
    return P + (Q - P)*np.linspace(0, 1, 20)

theta = np.deg2rad(30)
B = np.array([[0], [0]])
A = np.array([[80], [0]])

# tan(theta) = BC/AB, so C = (0, 80 tan(theta))
C = np.array([[0], [80*np.tan(theta)]])

# angle at A from the dot product
u, v = B - A, C - A
ang = np.rad2deg(np.arccos((u.T @ v)/(LA.norm(u)*LA.norm(v))))[0, 0]

print("height =", C[1, 0], " angle A =", ang)

for X, Y in [(A, B), (B, C), (C, A)]:
    s = line_gen(X, Y)
    plt.plot(s[0], s[1], 'b')
for name, X, d in [('A', A, (1, 1)), ('B', B, (-4, -3)), ('C', C, (-4, 1))]:
    plt.plot(X[0], X[1], 'ko')
    plt.annotate(name, (X[0, 0] + d[0], X[1, 0] + d[1]))
plt.axis('equal')
plt.grid()
plt.savefig('../figs/q20_tower.png')
plt.show()
