from fractions import Fraction

suits = ["spades", "hearts", "diamonds", "clubs"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# pmf of X, the card drawn: all 52 cards are equally likely
p_X = {(r, s): Fraction(1, 52) for r in ranks for s in suits}
assert sum(p_X.values()) == 1

# event A: the card is a queen
A = [x for x in p_X if x[0] == "Q"]
Pr_A = sum(p_X[x] for x in A)                    # Pr(X in A)

# conditional pmf of X given X in A
p_X_given_A = {x: p_X[x]/Pr_A for x in A}

print("Pr(X in A)             =", Pr_A)          # 1/13
for x in A:
    print("p(X = Q of", x[1], "| A) =", p_X_given_A[x])
print("Pr(queen of spades | queen) =", p_X_given_A[("Q", "spades")])   # 1/4
