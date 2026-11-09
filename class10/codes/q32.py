# q32.py  --  CBSE Class 10 Maths (Standard) 30/C/3
# Uses only numpy; helper functions are copied inline from matgeo / CoordGeo.
import numpy as np


# ---- trapezoidal rule ----
def trapz(y, x):
    return float(np.sum(0.5 * (y[1:] + y[:-1]) * (x[1:] - x[:-1])))

# ---------------- solution ----------------
# CBSE 30/C/3 Q32: coins A, B, C, D;  d_A = 0.7 cm, d_B = 2 d_A, then +50 % each,
# thickness 0.25 cm, pi = 22/7
pi = 22 / 7
t = 0.25
dia = np.zeros(4)
dia[0] = 0.7
dia[1] = 2 * dia[0]
dia[2] = 1.5 * dia[1]
dia[3] = 1.5 * dia[2]
rad = dia / 2
area = pi * rad**2                           # area of one face
z = np.linspace(0, t, 101)
vol = np.array([trapz(np.full_like(z, a), z) for a in area])   # V = int_0^t A dz (trapezoidal rule)

print("coin   diameter   area_face    volume")
for nm, dd, aa, vv in zip("ABCD", dia, area, vol):
    print("  %s     %.4f    %.5f     %.5f" % (nm, dd, aa, vv))
print("check A: area 0.385, volume 0.09625")
