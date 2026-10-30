# CBSE (Class 10) -- Q5: tangents PA and PB from P make an angle of 80 degrees.
# Find angle AOB.
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

def line_gen(P, Q):
    return P + (Q - P)*np.linspace(0, 1, 20)

def circ_gen(O, r):
    t = np.linspace(0, 2*np.pi, 100)
    return O + r*np.vstack((np.cos(t), np.sin(t)))

O = np.array([[0], [0]])
r = 1
theta = np.deg2rad(80)                      # angle APB

# OP bisects angle APB, so OP = r/sin(theta/2)
P = np.array([[r/np.sin(theta/2)], [0]])

# angle POA = 90 - theta/2, A and B are symmetric about OP
phi = np.pi/2 - theta/2
A = r*np.array([[np.cos(phi)], [np.sin(phi)]])
B = r*np.array([[np.cos(phi)], [-np.sin(phi)]])

def angle(X, Y, Z):                         # angle XYZ in degrees
    u, v = X - Y, Z - Y
    return np.rad2deg(np.arccos((u.T @ v)/(LA.norm(u)*LA.norm(v))))[0, 0]

print("AOB =", angle(A, O, B), " APB =", angle(A, P, B),
      " OA.AP =", ((A - O).T @ (P - A))[0, 0])

for X, Y in [(O, A), (O, B), (P, A), (P, B)]:
    s = line_gen(X, Y)
    plt.plot(s[0], s[1], 'b')
c = circ_gen(O, r)
plt.plot(c[0], c[1], 'k')
for name, X, d in [('O', O, (-0.1, -0.1)), ('A', A, (0, 0.05)),
                   ('B', B, (0, -0.12)), ('P', P, (0.03, 0.03))]:
    plt.plot(X[0], X[1], 'ko')
    plt.annotate(name, (X[0, 0] + d[0], X[1, 0] + d[1]))
plt.axis('equal')
plt.grid()
plt.savefig('../figs/q5_tangents.png')
plt.show()
