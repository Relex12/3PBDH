# https://jeremykun.com/2014/02/24/elliptic-curves-as-python-objects/
# https://volya.xyz/ecc/

from math import sqrt
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

    def ecc(self, x):
        return x**3 + self.a*x + self.b

    def isSmooth(self):
        return self.discriminant != 0

    def testPoint(self, x, y):
        return y*y == x*x*x + self.a * x + self.b

    def __str__(self):
        return 'y^2 = x^3 + %Gx + %G' % (self.a, self.b)

    def __eq__(self, other):
        return (self.a, self.b) == (other.a, other.b)

    def plot(self, xsize):
        margin = 5
        ysize = sqrt(xsize**3 + self.a*xsize + self.b)
        y, x = np.ogrid[-ysize:ysize:1000j, -xsize:xsize:1000j]
        plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * self.a - self.b, [0])
        plt.grid()
        plt.xlim([-margin, xsize + margin])
        plt.ylim([-ysize, ysize])


class FiniteEllipticCurve(EllipticCurve):
    def __init__(self, a, b, p):
        super().__init__(a, b)
        self.p = p

    def ecc(self, x):
        # assert (4*self.a**3 + 27*self.b**2) % self.p!= 0   # not understood
        return (x**3 + self.a*x + self.b) % self.p

    def plot(self):
        x = np.array(range(0, self.p))
        x2 = x**2 % self.p
        y2 = self.ecc(x)
        y = [(i, *y_i) for i, y_i in enumerate([np.where(y2_i == x2)[0] for y2_i in y2]) if y_i.size > 0]   # not understood
        plt.figure(dpi=100)
        for y_p in y:
            [plt.scatter(y_p[0], i, c='b') for i in y_p[1:]]


class Point(object):
    def __init__(self, curve, x, y, label=None):
        self.curve = curve # the curve containing this point
        self.x = x
        self.y = y
        self.label= label

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
            elif self.label != None:
                plt.annotate(self.label, (self.x, self.y))


class FinitePoint(Point):
    def __init__(self, curve, x, y, label=None):
        self.curve = curve
        self.x = x
        self.y = y
        self.label= label
        
        print 
        print ((x**3 + self.curve.a * x + self.curve.b) % self.curve.p)

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
