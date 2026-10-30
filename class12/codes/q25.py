# CBSE 65-C-3 (Class 12) -- Q25: verify A(adj A) = (adj A)A = |A| I for A = [2 3; -4 -6]
import numpy as np

A = np.array([[2, 3], [-4, -6]])

adjA = np.array([[A[1, 1], -A[0, 1]],
                 [-A[1, 0], A[0, 0]]])      # swap the diagonal, negate the rest
d = A[0, 0]*A[1, 1] - A[0, 1]*A[1, 0]

print(A @ adjA, adjA @ A, d*np.eye(2), sep='\n')
print(np.array_equal(A @ adjA, d*np.eye(2)) and np.array_equal(adjA @ A, d*np.eye(2)))
