import numpy as np

# classes 20-30, ..., 80-90 and their frequencies
upper = np.array([30, 40, 50, 60, 70, 80, 90])
f = np.array([10, 8, 12, 24, 6, 25, 15])
N = f.sum()
F = np.cumsum(f)                                   # cumulative frequency F_i
print("N =", N, " cumulative frequencies =", F)

# median class: first class with F >= N/2
i = np.argmax(F >= N/2)
l, h, fm, Fprev = upper[i] - 10, 10, f[i], F[i - 1]
print("median class", l, "-", l + h, " l, h, f, F_prev =", l, h, fm, Fprev)

# Median = l + (N/2 - F_prev)/f * h
median = l + (N/2 - Fprev)/fm*h
print("median =", median)
assert N == 100 and (l, h, fm, Fprev) == (50, 10, 24, 30)
assert np.isclose(median, 58 + 1/3)
