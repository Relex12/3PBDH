from fractions import Fraction as frac
import matplotlib.pyplot as plt
from random import randint

from classes import *

finite=True

if not finite:
    C = EllipticCurve(a=-2, b=4)
    C.plot(50)

    P = Point(C, frac(3), frac(5))
    Q = Point(C, frac(-2), frac(0))
    R = Point(C, frac(240), frac(3718))
    R = 36*R

    plot (P)
    plot (Q)
    plot (R)

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
    plot (A, 'A')
    plot (B, 'B')
    plot (C, 'C')

else:
    C = FiniteEllipticCurve(-5, 8, 37)
    C.plot()

    P = FinitePoint(C, 5, 16)
    Q = FinitePoint(C, 10, 25)
    P.plot('P')
    Q.plot('Q')

plt.savefig("graph.png")
