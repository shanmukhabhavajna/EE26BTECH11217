# CBSE (Class 10) -- Q30 (OR): solve (ax - by) + (a + 4b) = 0 and
# (bx + ay) + (b - 4a) = 0 using matrices. Check with a = 1, b = 2
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

def line_dir_pt(m, A, k1, k2):
    k = np.linspace(k1, k2, 20)
    return A + k*m

a, b = 1, 2

# [a -b; b a] x = [-(a + 4b); 4a - b]
M = np.array([[a, -b], [b, a]])
c = np.array([[-(a + 4*b)], [4*a - b]])
x = LA.solve(M, c)

print("x, y =", x.ravel())

# plot the two lines n^T x = c, direction m = (-n2, n1)
for n, ci in zip(M, c.ravel()):
    n = n.reshape(-1, 1)
    A0 = n*ci/(n.T @ n)
    m = np.array([[-n[1, 0]], [n[0, 0]]])
    s = line_dir_pt(m, A0, -5, 5)
    plt.plot(s[0], s[1])
plt.plot(x[0], x[1], 'ko')
plt.annotate('(-1, 4)', (x[0, 0] + 0.2, x[1, 0] + 0.2))
plt.axis('equal')
plt.grid()
plt.savefig('../figs/q30_lines.png')
plt.show()
