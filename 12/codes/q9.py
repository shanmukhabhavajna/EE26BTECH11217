import numpy as np

def trapezoid(n):
    h = (np.pi/2 - 0)/n
    theta = np.linspace(0, np.pi/2, n+1)    # nodes
    f = np.sin(theta)                       # tan(theta)cos(theta) = sin(theta)
    w = np.ones(n+1); w[[0, -1]] = 0.5      # trapezoid weights
    return h, h*(w @ f)                     # I ~ h w^T f

print("   n        h          I")
for n in [6, 100, 200, 400]:
    h, I = trapezoid(n)
    print(f"{n:4d}  {h:9.6f}  {I:.6f}")
print("exact = 1")
