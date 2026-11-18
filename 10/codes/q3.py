import numpy as np
import numpy.linalg as LA

rng = np.random.default_rng(0)
for _ in range(5):
  a, b = rng.uniform(1, 5, size=2)
  O = np.zeros((2, 1))
  P = np.array([[a - b], [a + b]])
  d = np.sqrt((P - O).T @ (P - O)).item()   # d^2 = (P-O)^T (P-O)
  opts = {'A': 2*np.sqrt(a*b), 'B': np.sqrt(2*a**2 + a*b),
          'C': 2*np.sqrt(a**2 + b**2), 'D': np.sqrt(2*a**2 + 2*b**2)}
  match = [k for k, v in opts.items() if np.isclose(v, d)]
  print(f"a={a:.3f} b={b:.3f}  d={d:.4f}  matching option: {match}")
  assert match == ['D']
