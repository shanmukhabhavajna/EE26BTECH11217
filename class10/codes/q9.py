# CBSE (Class 10) -- Q9: two dice are thrown. Find Pr(sum < 12).
# Using the z-transform: H(z) = sum p[n] z^-n, and Z{p_S} = H(z)^2
import numpy as np
import matplotlib.pyplot as plt

# pmf of one die: p[n] = 1/6 for n = 1,...,6
p = np.zeros(7)
p[1:] = 1/6

# product of z-transforms = convolution of pmfs
pS = np.convolve(p, p)              # pS[n] = Pr(S = n), n = 0,...,12

print("Pr(S<12) =", 1 - pS[12], " H(1)^2 =", p.sum()**2)

n = np.arange(len(pS))
plt.stem(n, pS)
plt.xlabel('n')
plt.ylabel('Pr(S = n)')
plt.grid()
plt.savefig('../figs/q9_dice.png')
plt.show()
