# CBSE 65-C-3 (Class 12) -- Q16
# (a) A = [4 x+2; 2x-3 x+1] is symmetric, find x
# (b) OR: A^2 = A, find (2+A)^3 - 19A
import numpy as np

# (a) A^T = A  =>  (x+2) - (2x-3) = 0, linear in x
f = lambda x: (x + 2) - (2*x - 3)
x = -f(0)/(f(1) - f(0))
A = np.array([[4, x + 2], [2*x - 3, x + 1]])
print("x =", x)                          # 5
print(" A =\n", A, "\nsymmetric:", np.allclose(A, A.T))

# (b) (2I + A)^3 = 8I + 12A + 6A^2 + A^3 = 8I + 19A  when A^2 = A
I = np.eye(2)
idem = [np.array([[1, 1], [0, 0]]),              # A^2 = A, not symmetric
        np.outer([1, 2], [1, 2])/5]              # projection matrix, A^2 = A
for M in idem:
    assert np.allclose(M @ M, M)
    R = np.linalg.matrix_power(2*I + M, 3) - 19*M
    print("Q16(b): (2+A)^3 - 19A =\n", np.round(R, 10), "\n= 8I:", np.allclose(R, 8*I))
