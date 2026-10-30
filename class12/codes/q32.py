
import sympy as sp

a, b, k = sp.symbols('a b k', real=True)
x, y = sp.symbols('x y')

# ---------------- (a) ----------------
M = sp.Matrix([[1 + a**2 - b**2, 2*a*b, -2*b],
               [2*a*b, 1 - a**2 + b**2, 2*a],
               [2*b, -2*a, 1 - a**2 - b**2]])
s = 1 + a**2 + b**2

E1 = sp.Matrix([[1, 0, 0], [0, 1, 0], [-b, 0, 1]])
E2 = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, a, 1]])
M1 = (M*E1*E2).applyfunc(sp.expand)
print(M1)            # [[s, 0, -2b], [0, s, 2a], [b s, -a s, 1-a^2-b^2]] (expanded)

# take s out of C1 and C2, then R3 -> R3 - b R1 + a R2 is left multiplication by E3 (|E3| = 1)
N = sp.Matrix([[1, 0, -2*b],
               [0, 1, 2*a],
               [b, -a, 1 - a**2 - b**2]])
E3 = sp.Matrix([[1, 0, 0], [0, 1, 0], [-b, a, 1]])
print((E3*N).applyfunc(sp.expand))   # upper triangular, last diagonal entry is s
print(sp.simplify(M1 - sp.Matrix([[s, 0, -2*b], [0, s, 2*a], [b*s, -a*s, 1 - a**2 - b**2]])))  # zero matrix

print("|M| =", sp.factor(M.det()))
print("|M| - (1+a^2+b^2)^3 =", sp.simplify(M.det() - s**3))     # 0
print("numerical check a=2, b=3:", M.subs({a: 2, b: 3}).det(), (1 + 4 + 9)**3)   # 2744

# ---------------- (b) OR ----------------
A = sp.Matrix([1, 3]); B = sp.Matrix([0, 0]); D = sp.Matrix([k, 0])
line = sp.Matrix([[x, y, 1], [A[0], A[1], 1], [B[0], B[1], 1]]).det()
print("line AB :", sp.expand(line), "= 0")                      # 3x - y = 0

area = sp.Rational(1, 2)*sp.Matrix([[A[0], A[1], 1], [B[0], B[1], 1], [D[0], D[1], 1]]).det()
print("area =", sp.simplify(area))                              # 3k/2
print("k =", sp.solve(sp.Eq(sp.Abs(area), 3), k))               # [-2, 2]
