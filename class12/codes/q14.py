# CBSE 65-C-3 (Class 12) -- Q14
# Integrating factor of  x dy/dx - y = log x
# Standard form dy/dx + P y = Q with P = -1/x, Q = (log x)/x.
# The integrating factor mu satisfies mu' = P mu, mu(1) = 1: solve it with Euler's method
import numpy as np

P = lambda x: -1/x

h = 1e-4
x = np.arange(1, 3 + h/2, h)
mu = np.zeros_like(x)
mu[0] = 1
for n in range(len(x) - 1):
    mu[n+1] = mu[n] + h*P(x[n])*mu[n]          # Euler: y_{n+1} = y_n + h f(x_n, y_n)

err = np.max(np.abs(mu - 1/x))
print("Q14: max |mu_Euler - 1/x| =", err)       # about 1e-4
print("Q14: integrating factor = 1/x")

# check: with mu = 1/x,  (mu y)' = mu Q.  The exact solution is y = Cx - log x - 1
C0 = 0.7
y = lambda t: C0*t - np.log(t) - 1
t, d = 1.7, 1e-6
lhs = (y(t + d)/(t + d) - y(t - d)/(t - d))/(2*d)    # d/dx (y/x)
rhs = (1/t)*(np.log(t)/t)                            # mu * Q
print("Q14: (y/x)' =", lhs, " mu*Q =", rhs)
