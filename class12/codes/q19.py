

import numpy as np

f = lambda x: np.cbrt(3 - x**3)      # real cube root, also works when 3 - x^3 < 0

x = np.linspace(-5, 5, 1001)
# cbrt blows up rounding errors near 0 (about 1e-16 becomes 1e-5), so the tolerance is loose
print(np.allclose(f(f(x)), x, atol=1e-4))    # True, so f(f(x)) = x
