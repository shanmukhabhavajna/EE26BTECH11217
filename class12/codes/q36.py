
import sympy as sp

x = sp.Symbol('x', positive=True)
y = x**sp.sin(x) + sp.asin(sp.sqrt(x))

# derivative by sympy
dy = sp.diff(y, x)
print("dy/dx =", dy)
