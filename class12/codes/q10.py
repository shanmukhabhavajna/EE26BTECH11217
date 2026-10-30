# CBSE 65-C-3 (Class 12) -- Q10
# roots of det [[x,0,8],[4,1,3],[2,0,x]] = 0
import numpy as np

def det(x):
    M = np.array([[x, 0, 8], [4, 1, 3], [2, 0, x]], dtype=float)
    return np.linalg.det(M)

xs = np.array([-2., 0., 1., 3.])
coef = np.polyfit(xs, [det(v) for v in xs], 2)   # det is quadratic in x
print("roots =", np.roots(coef))            # [ 4. -4.]
