# CBSE 65-C-3 (Class 12) -- Q15
# y = log x, find d^2y/dx^2.   Exact: y' = 1/x, y'' = -1/x^2
# Numerical check with the forward difference formula
#   y''_n = (y_{n+2} - 2 y_{n+1} + y_n)/h^2   (centred at x_{n+1})
import numpy as np

h = 1e-3
x0 = 2.0
xn  = x0 - h                    # x_n, so that x_{n+1} = x0
y = lambda t: np.log(t)

ypp = (y(xn + 2*h) - 2*y(xn + h) + y(xn))/h**2
print("Q15: numerical y''(2) =", ypp)           # about -0.25
print("Q15: -1/x^2 at x = 2  =", -1/x0**2)
print("Q15: d2y/dx2 = -1/x^2")
