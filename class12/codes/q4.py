# CBSE 65-C-3 (Class 12) -- Q4
pA, pB = 1/3, 1/5
p = 1 - (1 - pA)*(1 - pB)          # Pr(A+B) = 1 - Pr(A'B')
print("Q4: Pr(solved) =", p, "= 7/15 =", 7/15)
for opt, val in {'A': 7/15, 'B': 8/15, 'C': 2/15, 'D': 14/15}.items():
    print("Q4: option", opt, val, "<-- correct" if abs(p - val) < 1e-12 else "")
