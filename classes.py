# https://jeremykun.com/2014/02/24/elliptic-curves-as-python-objects/

from fractions import Fraction as frac
import numpy as np
import matplotlib.pyplot as plt

class EllipticCurve(object):
    def __init__(self, a, b):
        # assume we're already in the Weierstrass form
        self.a = a
        self.b = b
 
        self.discriminant = -16 * (4 * a*a*a + 27 * b * b)
        if not self.isSmooth():
            raise Exception("The curve %s is not smooth!" % self)
 
    def isSmooth(self):
        return self.discriminant != 0
 
    def testPoint(self, x, y):
        return y*y == x*x*x + self.a * x + self.b
 
    def __str__(self):
        return 'y^2 = x^3 + %Gx + %G' % (self.a, self.b)
 
    def __eq__(self, other):
        return (self.a, self.b) == (other.a, other.b)

    def plot(self, size):
        y, x = np.ogrid[-size:size:100j, -size:size:100j]
        plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * self.a - self.b, [0])
        plt.grid()
        plt.xlim([-size, size])
        plt.ylim([-size, size])

class Point(object):
    def __init__(self, curve, x, y):
        self.curve = curve # the curve containing this point
        self.x = x
        self.y = y
 
        if not curve.testPoint(x,y):
            raise Exception("The point %s is not on the given curve %s" % (self, curve))

    def __str__(self):
        x = self.x.denominator / self.x.numerator
        y = self.y.denominator / self.y.numerator
        return '(%s,%s)' % (x, y)

    def __repr__(self):
        return '(%s,%s)' % (self.x, self.y)

    def __neg__(self):
        return Point(self.curve, self.x, -self.y)

    def __add__(self, Q):
        if isinstance(Q, Ideal):
            return self
 
        x1, y1, x2, y2 = self.x, self.y, Q.x, Q.y
 
        if (x1, y1) == (x2, y2):
            if y1 == 0:
                return Ideal(self.curve)
 
            # slope of the tangent line
            m = (3 * x1 * x1 + self.curve.a) / (2 * y1)

        else:
            if x1 == x2:
                return Ideal(self.curve) # vertical line

            # Using Vieta's formula for the sum of the roots
            m = (y2 - y1) / (x2 - x1)

        x3 = m*m - x2 - x1
        y3 = m*(x3 - x1) + y1
 
        return Point(self.curve, x3, -y3)

    def __sub__(self, Q):
        return self + -Q

    def __mul__(self, n):
        if not isinstance(n, int):
            raise Exception("Can't scale a point by something which isn't an int!")
        else:
            if n < 0:
                return -self * -n
            if n == 0:
                return Ideal(self.curve)
            else:
                Q = self
                R = self if n & 1 == 1 else Ideal(self.curve)

                i = 2
                while i <= n:
                    Q = Q + Q

                    if n & i == i:
                        R = Q + R

                    i = i << 1
        return R

    def __rmul__(self, n):
        return self * n

    def __eq__(self, point):
        return (self.curve, self.x, self.y) == (point.curve, point.x, point.y)

    def plot(self, label = None):
        if not isinstance(self, Ideal):
            plt.plot(self.x, self.y, marker=".")
            if label != None:
                plt.annotate(label, (self.x, self.y))


class Ideal(Point):
    def __init__(self, curve):
        self.curve = curve
 
    def __str__(self):
        return "Ideal"

    def __add__(self, Q):
        return Q

    def __neg__(self):
        return self

    def __mul__(self, n):
        if not isinstance(n, int):
            raise Exception("Can't scale a point by something which isn't an int!")
        else:
            return self


def plot(point, label = None):
    point.plot(label)


if __name__ == "__main__":

    C = EllipticCurve(a=-2, b=4)
    C.plot(20)

    P = Point(C, frac(3), frac(5))
    Q = Point(C, frac(-2), frac(0))
    R = Point(C, frac(240), frac(3718))
    R = 36*R

    # plot (P, 'P')
    # plot (Q, 'Q')
    # plot (R, 'R')
    # plot (P+Q, 'P+Q')
    # plot (P+R, 'P+R')
    # plot (Q+R, 'Q+R')
    # plot (P+Q+R, 'P+Q+R')

    plt.savefig("graph.png")
