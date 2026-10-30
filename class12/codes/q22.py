# CBSE 65-C-3 (Class 12) -- Q22: show that 2i - j + k, i - 3j - 5k, 3i - 4j - 4k
# are the vertices of a right-angled triangle
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

A = np.array([2, -1, 1]).reshape(-1, 1)
B = np.array([1, -3, -5]).reshape(-1, 1)
C = np.array([3, -4, -4]).reshape(-1, 1)


print(f"it is right angled triangle because the dot product of ac and bc :{(A - C).T @ (B - C)}")                  # 0, so the angle at C is 90 degrees


