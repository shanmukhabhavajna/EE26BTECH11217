# CBSE 65-C-3 (Class 12) -- Q18, following matgeo
# (a) a = 2i - j + 2k, b = 5i - 3j - 4k.
#     Find (projection of a on b)/(projection of b on a)
# (b) OR: a^, b^ unit vectors, c = a^ + 2 b^ and d = 5 a^ - 4 b^ are perpendicular.
#     Find the angle between a^ and b^
import numpy as np
import numpy.linalg as LA

def ang_vec(m1, m2):                           # same as ang_vec in matgeo/codes/CoordGeo/line/funcs.py
    return np.arccos((m1.T @ m2).item()/(LA.norm(m1)*LA.norm(m2)))

# (a)
a = np.array([2, -1, 2]).reshape(-1, 1)
b = np.array([5, -3, -4]).reshape(-1, 1)

proj = lambda A, B: ((A.T @ B)/(B.T @ B)).item() * B     # projection of A on B (matgeo)
Cab = proj(a, b)                                          # projection of a on b
Cba = proj(b, a)                                          # projection of b on a
print("(a): a^T b =", (a.T @ b).item())                # 5
print("(a): ratio =", LA.norm(Cab)/LA.norm(Cba))       # 0.42426
print("(a): 3/(5 sqrt2) = 3 sqrt2/10 =", 3*np.sqrt(2)/10)
print("(a): ||a||/||b|| =", LA.norm(a)/LA.norm(b))

# (b)  c^T d = 5 - 4 a^T b + 10 a^T b - 8 = 6 cos(theta) - 3 = 0
def cTd(theta):
    ah = np.array([1, 0]).reshape(-1, 1)
    bh = np.array([np.cos(theta), np.sin(theta)]).reshape(-1, 1)
    c = ah + 2*bh
    d = 5*ah - 4*bh
    return (c.T @ d).item()

lo, hi = 0.0, np.pi                           # c^T d decreases from 3 to -9
for _ in range(60):                           # bisection
    mid = (lo + hi)/2
    if cTd(mid) > 0:
        lo = mid
    else:
        hi = mid
theta = (lo + hi)/2
print("(b): theta =", theta, "rad =", np.degrees(theta), "deg")   # pi/3 = 60 deg
ah = np.array([1, 0]).reshape(-1, 1)
bh = np.array([np.cos(theta), np.sin(theta)]).reshape(-1, 1)
print("(b): ang_vec =", ang_vec(ah, bh), " pi/3 =", np.pi/3)
