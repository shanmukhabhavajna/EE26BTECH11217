# CBSE 65-C-3 (Class 12) -- Q13
# A card is picked from 52 cards. Given it is a queen, find Pr(queen of spades)
import itertools
from fractions import Fraction

ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['spades', 'hearts', 'diamonds', 'clubs']
deck = list(itertools.product(ranks, suits))          # 52 outcomes

Q  = [c for c in deck if c[0] == 'Q']                 # event: queen
QS = [c for c in deck if c == ('Q', 'spades')]        # event: queen of spades (QS is inside Q)

pQ  = Fraction(len(Q), len(deck))
pQS = Fraction(len(QS), len(deck))                    # Pr(QS and Q) = Pr(QS)
p = pQS / pQ                                          # Pr(QS|Q) = Pr(QS Q)/Pr(Q)

                       # 1/52
print("Q13: Pr(QS|Q) =", p, "=", float(p))            # 1/4
