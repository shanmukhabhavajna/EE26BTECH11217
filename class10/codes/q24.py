# CBSE (Class 10) -- Q24: a jar has 18 marbles, red and yellow. Pr(red) = 2/3.
# Find the number of yellow marbles.
# OR: a die is thrown twice. Find Pr(at least one 5) and Pr(no 5)
import numpy as np
import matplotlib.pyplot as plt

# red = 18 * Pr(red), yellow = 18 - red
red = 18*2/3
yellow = 18 - red

# OR: all 36 outcomes, count the fives in each
f = (np.arange(1, 7) == 5).astype(int)
fives = np.add.outer(f, f)
pmf = np.bincount(fives.ravel(), minlength=3)/36

print("yellow =", yellow, " Pr(at least one 5) =", pmf[1] + pmf[2], " Pr(no 5) =", pmf[0])

fig, ax = plt.subplots(1, 2)
ax[0].bar(['red', 'yellow'], [red, yellow])
ax[0].set_ylabel('marbles')
ax[1].bar([0, 1, 2], pmf)
ax[1].set_xlabel('number of fives')
ax[1].set_ylabel('probability')
plt.savefig('../figs/q24_probability.png')
plt.show()
