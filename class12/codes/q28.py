import os
import numpy as np
import matplotlib.pyplot as plt

w = np.array([1, 2, 3])              # P(x) = k*w
k = 1/w.sum()                        # the probabilities add up to 1
p = k*w
cdf = np.cumsum(p)                   # P(X <= x)

print(k, cdf[1], cdf[2], 1 - cdf[1])           # k, P(X<2), P(X<=2), P(X>=2)

# simulation to compare with
np.random.seed(0)
N = 100000
sim = np.bincount(np.random.choice(3, N, p=p), minlength=3)/N

x = np.arange(3)
fig, ax = plt.subplots(figsize=(5, 3.5))
for pos, y, c, name in [(x - 0.06, p, 'tab:blue', 'theory'),
                        (x + 0.06, sim, 'tab:orange', 'simulation')]:
    marker, lines, base = ax.stem(pos, y)
    plt.setp(marker, color=c, label=name)
    plt.setp(lines, color=c)
    plt.setp(base, visible=False)
ax.set_xticks(x)
ax.set_xlabel('X')
ax.set_ylabel('P(X)')
ax.legend()
plt.tight_layout()

figs = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figs')
os.makedirs(figs, exist_ok=True)
plt.savefig(os.path.join(figs, 'q28_distribution.png'), dpi=150)
plt.show()
