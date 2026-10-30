# CBSE (Class 10) -- Q31: circle of radius 2.5 cm, point P at 7 cm from the centre.
# Construct the pair of tangents from P to the circle.
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

def line_gen(P, Q):
    return P + (Q - P)*np.linspace(0, 1, 20)

def circ_gen(O, r):
    t = np.linspace(0, 2*np.pi, 100)
    return O + r*np.vstack((np.cos(t), np.sin(t)))

O = np.array([[0], [0]])
P = np.array([[7], [0]])
r = 2.5

# tangent points satisfy |x| = r and (x - O)^T (x - P) = 0,
# so x^T P = r^2 gives x1 = r^2/7
x1 = r**2/P[0, 0]
x2 = np.sqrt(r**2 - x1**2)
A = np.array([[x1], [x2]])
B = np.array([[x1], [-x2]])

print("PA =", LA.norm(P - A), " PB =", LA.norm(P - B), " OA.AP =", ((A - O).T @ (P - A))[0, 0])

M = (O + P)/2                               # circle on OP as diameter
for X, Y in [(P, A), (P, B), (O, A), (O, B)]:
    s = line_gen(X, Y)
    plt.plot(s[0], s[1], 'b')
c1 = circ_gen(O, r)
c2 = circ_gen(M, LA.norm(P - O)/2)
plt.plot(c1[0], c1[1], 'k')
plt.plot(c2[0], c2[1], 'k--')
for name, X, d in [('O', O, (-0.4, -0.4)), ('P', P, (0.1, 0.1)),
                   ('A', A, (0, 0.15)), ('B', B, (0, -0.4))]:
    plt.plot(X[0], X[1], 'ko')
    plt.annotate(name, (X[0, 0] + d[0], X[1, 0] + d[1]))
plt.axis('equal')
plt.grid()
plt.savefig('../figs/q31_tangents.png')
plt.show()
