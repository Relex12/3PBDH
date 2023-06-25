from fractions import Fraction as frac
import matplotlib.pyplot as plt
from random import randint

from classes import *


# C = EllipticCurve(a=-2, b=4)
# C.plot(50)

# P = Point(C, frac(3), frac(5))
# Q = Point(C, frac(-2), frac(0))
# R = Point(C, frac(240), frac(3718))
# R = 36*R

# plot (P)
# plot (Q)
# plot (R)

# G = Point(C, frac(3), frac(5))

# a = randint(10, 1000)
# b = randint(10, 1000)
# c = randint(10, 1000)

# A = (a*G)
# B = (b*G)
# C = (c*G)

# print (A)
# plot (A, 'A')
# print (B)
# plot (B, 'B')
# print (C)
# plot (C, 'C')

G = FiniteEllipticCurve(-5, 8, 37)
G.plot()

P = FinitePoint(G, 5, 16)

plt.savefig("graph.png")
