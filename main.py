from fractions import Fraction as frac
import matplotlib.pyplot as plt
from random import randint

from classes import *

finite=True

if not finite:
    C = EllipticCurve(a=-2, b=4)
    C.plot(20)
    print (C)

    P = Point(C, frac(3), frac(5), 'P')
    Q = Point(C, frac(-2), frac(0), 'Q')
    R = Point(C, frac(240), frac(3718))
    R = 36*R

    P.plot()
    Q.plot()
    R.plot('R')

else:
    C = FiniteEllipticCurve(-5, 8, 37)
    C.plot()
    print (C)

    P = FinitePoint(C, 5, 16, 'P')
    Q = FinitePoint(C, 10, 25, 'Q')
    R = FinitePoint(C, 8, 6, 'R')
    P.plot()
    Q.plot()
    R.plot()

G = P

a = randint(10, 1000)
b = randint(10, 1000)
c = randint(10, 1000)

A = (a*G)
B = (b*G)
C = (c*G)

print (A)
print (B)
print (C)
A.plot('A')
B.plot('B')
C.plot('C')

plt.savefig("graph.png")
