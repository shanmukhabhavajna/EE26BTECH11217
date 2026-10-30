# CBSE 65-C-3 (Class 12) -- Q23
# (a) 19 tickets, two drawn without replacement: distribution of the number of even tickets
# (b) OR: two tosses of a die, success = "number greater than 5"
import os
import numpy as np
import matplotlib.pyplot as plt
from math import factorial

def comb(n, k):
    return factorial(n)//(factorial(k)*factorial(n - k))

np.random.seed(0)
N = 100000

# (a) 9 even and 10 odd tickets
th_a = [comb(9, k)*comb(10, 2 - k)/comb(19, 2) for k in range(3)]
draw = np.argsort(np.random.rand(N, 19), axis=1)[:, :2] + 1   # two different tickets per trial
sim_a = np.bincount((draw % 2 == 0).sum(axis=1), minlength=3)/N

# (b) a success is a 6
th_b = [comb(2, k)*(1/6)**k*(5/6)**(2 - k) for k in range(3)]
roll = np.random.randint(1, 7, (N, 2))
sim_b = np.bincount((roll > 5).sum(axis=1), minlength=3)/N

def stems(ax, th, sim, title):
    k = np.arange(3)
    for x, y, c, name in [(k - 0.06, th, 'tab:blue', 'theory'),
                          (k + 0.06, sim, 'tab:orange', 'simulation')]:
        marker, lines, base = ax.stem(x, y)
        plt.setp(marker, color=c, label=name)
        plt.setp(lines, color=c)
        plt.setp(base, visible=False)
    ax.set_xticks(k)
    ax.set_xlabel('X')
    ax.set_ylabel('Pr(X = k)')
    ax.set_title(title)
    ax.legend(loc='upper right')

fig, axs = plt.subplots(1, 2, figsize=(9, 3.5))
stems(axs[0], th_a, sim_a, 'tickets')
stems(axs[1], th_b, sim_b, 'die')
plt.tight_layout()

figs = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figs')
os.makedirs(figs, exist_ok=True)
plt.savefig(os.path.join(figs, 'q23_distribution.png'), dpi=150)
plt.show()

print(np.round(th_a, 4), np.round(sim_a, 4))
print(np.round(th_b, 4), np.round(sim_b, 4))
