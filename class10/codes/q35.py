# CBSE (Class 10) -- Q35: sides AB, AC and median AD of triangle ABC are
# proportional to PQ, PR and median PM of triangle PQR. Show ABC ~ PQR.
# OR: BN and CM are medians of a triangle ABC right-angled at A.
# Prove 4(BN^2 + CM^2) = 5 BC^2
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

def line_gen(P, Q):
    return P + (Q - P)*np.linspace(0, 1, 20)

def draw(pairs, pts):
    for X, Y in pairs:
        s = line_gen(X, Y)
        plt.plot(s[0], s[1], 'b')
    for name, X in pts.items():
        plt.plot(X[0], X[1], 'ko')
        plt.annotate(name, (X[0, 0] + 0.1, X[1, 0] + 0.1))

# main part: PQR is ABC scaled by 1.5, medians D and M are midpoints
A = np.array([[1], [3]]); B = np.array([[0], [0]]); C = np.array([[5], [0]])
P, Q, R = 1.5*A + 8, 1.5*B + 8, 1.5*C + 8
D, M = (B + C)/2, (Q + R)/2
print(LA.norm(A - B)/LA.norm(P - Q), LA.norm(A - C)/LA.norm(P - R), LA.norm(A - D)/LA.norm(P - M))

plt.subplot(1, 2, 1)
draw([(A, B), (B, C), (C, A), (A, D), (P, Q), (Q, R), (R, P), (P, M)],
     {'A': A, 'B': B, 'C': C, 'D': D, 'P': P, 'Q': Q, 'R': R, 'M': M})
plt.axis('equal')
plt.grid()

# OR part: right angle at A, N and M are the midpoints of AC and AB
A = np.array([[0], [0]]); B = np.array([[8], [0]]); C = np.array([[0], [4]])
M, N = (A + B)/2, (A + C)/2
BN, CM, BC = LA.norm(B - N)**2, LA.norm(C - M)**2, LA.norm(B - C)**2
print("4(BN^2 + CM^2) =", 4*(BN + CM), " 5 BC^2 =", 5*BC)

plt.subplot(1, 2, 2)
draw([(A, B), (B, C), (C, A), (B, N), (C, M)], {'A': A, 'B': B, 'C': C, 'M': M, 'N': N})
plt.axis('equal')
plt.grid()
plt.savefig('../figs/q35_medians.png')
plt.show()
